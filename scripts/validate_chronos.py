#!/usr/bin/env python3
"""Validate CHRONOS specimen structure and governance declarations.

Legacy specimens receive structural/path checks. Specimens declaring
governance_status=standard-v1 receive the additional provenance, review,
and evidence-integrity checks. This script does not assess research truth
or replace human publication review.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "specimens"
SCHEMA_PATH = SPECIMENS / "metadata-schema.json"
REQUIRED = [
    "README.md", "facts.md", "report.md", "mitigation.md",
    "reproduction-test.md", "Evidence/evidence-log.md",
    "Evidence/integrity.sha256",
]
SHA_LINE = re.compile(r"^([0-9a-fA-F]{64})  (.+)$")


def safe_file(spec_dir: Path, relative: str, errors: list, label: str) -> Path | None:
    candidate = (spec_dir / relative).resolve()
    try:
        candidate.relative_to(spec_dir.resolve())
    except ValueError:
        errors.append(f"{label}: path escapes specimen directory: {relative}")
        return None
    if not candidate.is_file():
        errors.append(f"{label}: referenced file missing: {relative}")
        return None
    return candidate


def safe_evidence_file(spec_dir: Path, relative: str, errors: list, label: str) -> Path | None:
    """Resolve evidence paths, including known legacy folder layouts.

    The declared path is always attempted first. Fallbacks are limited to
    the two historical evidence directories used by the archive.
    """
    resolved = safe_file(spec_dir, relative, [], label)
    if resolved is not None:
        return resolved
    name = Path(relative).name
    for legacy_dir in ("Evidence", "01_Raw_Screenshots"):
        candidate = (spec_dir / legacy_dir / name).resolve()
        try:
            candidate.relative_to(spec_dir.resolve())
        except ValueError:
            continue
        if candidate.is_file():
            print(f"LEGACY PATH RESOLVED: {label}: {relative} -> {candidate.relative_to(spec_dir.resolve())}")
            return candidate
    errors.append(f"{label}: evidence file missing after legacy path resolution: {relative}")
    return None


def validate_manifest(spec_dir: Path, errors: list, strict: bool) -> None:
    manifest = spec_dir / "Evidence/integrity.sha256"
    if not manifest.is_file():
        return
    listed = set()
    for number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        match = SHA_LINE.match(raw)
        if not match:
            errors.append(f"{spec_dir.name}: malformed SHA-256 manifest line {number}")
            continue
        expected, relative = match.groups()
        target = safe_file(spec_dir, relative, errors, spec_dir.name)
        if target is None:
            continue
        listed.add(relative)
        if strict:
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            if actual.lower() != expected.lower():
                errors.append(f"{spec_dir.name}: SHA-256 mismatch: {relative}")
    if strict:
        evidence_dir = spec_dir / "Evidence"
        for asset in evidence_dir.rglob("*"):
            if not asset.is_file() or asset.name in {"evidence-log.md", "integrity.sha256"}:
                continue
            relative = asset.relative_to(spec_dir).as_posix()
            if relative not in listed:
                errors.append(f"{spec_dir.name}: evidence asset absent from integrity manifest: {relative}")


def main() -> int:
    errors = []
    if not SCHEMA_PATH.is_file():
        print("ERROR: specimens/metadata-schema.json is missing")
        return 1
    try:
        import jsonschema
    except ImportError:
        print("ERROR: install jsonschema before validation")
        return 1

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    for spec_dir in sorted(SPECIMENS.glob("SPEC-*")):
        if not spec_dir.is_dir():
            continue
        label = spec_dir.name
        metadata_path = spec_dir / "metadata.json"
        if not metadata_path.is_file():
            errors.append(f"{label}: metadata.json missing")
            continue
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            jsonschema.validate(instance=metadata, schema=schema)
        except Exception as exc:
            errors.append(f"{label}: metadata/schema validation failed: {exc}")
            continue

        for required in REQUIRED:
            if not (spec_dir / required).is_file():
                errors.append(f"{label}: required file missing: {required}")

        layers = metadata.get("layers", {})
        strict = metadata.get("governance_status") == "standard-v1"
        # Legacy metadata uses inconsistent evidence path conventions. Do not
        # fail historical specimens on path normalization; record them for
        # retrospective review. New standard-v1 specimens are checked strictly.
        if strict:
            for relative in layers.get("layer_1_evidence", []):
                safe_evidence_file(spec_dir, relative, errors, label)
        else:
            print(f"LEGACY evidence references deferred to specimen audit: {label}")
        for key in ("layer_2_facts", "layer_3_report"):
            relative = layers.get(key)
            if relative:
                safe_file(spec_dir, relative, errors, label)

        if strict:
            provenance = metadata.get("evidence_provenance", {})
            required_provenance = (
                "captured_by", "capture_method", "capture_timezone",
                "source_platform", "limitations",
            )
            for key in required_provenance:
                if key not in provenance or provenance[key] in ("", None):
                    errors.append(f"{label}: standard-v1 missing evidence_provenance.{key}")
            review = metadata.get("review", {})
            for key in (
                "evidence_review", "fact_review", "analysis_review",
                "reproduction_status", "publication_decision",
            ):
                if not review.get(key):
                    errors.append(f"{label}: standard-v1 missing review.{key}")
            if review.get("publication_decision") not in {"approved", "approved-with-limitations"}:
                errors.append(f"{label}: standard-v1 is not publication-approved")
            if review.get("evidence_review") != "passed" or review.get("fact_review") != "passed" or review.get("analysis_review") != "passed":
                errors.append(f"{label}: standard-v1 review gates are incomplete")
        validate_manifest(spec_dir, errors, strict)
        print(f"{'STRICT' if strict else 'LEGACY'} checked: {label}")

    if errors:
        print("\nCHRONOS VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nCHRONOS STRUCTURAL VALIDATION PASSED")
    print("Note: structural validation is not substantive evidence review or publication approval.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
