# CHRONOS Changelog

All notable changes to the CHRONOS Evaluation Methodology and repository structure.

---

## [0.2] — 2026-08-31

### Added
- Specimen Structure Standard v0.2 — mandatory directory structure, file naming, and content standards
- `metadata-schema.json` — machine-readable validation schema for all specimen manifests
- `mitigation.md` — required per specimen: prevention, detection, and recovery guidance
- `reproduction-test.md` — required per specimen: documented test matrix for failure reproduction
- `domain-impact-matrix.md` — required per specimen: stakes by real-world domain
- `Evidence/integrity.sha256` — cryptographic hashes for all evidence files
- `.github/workflows/ci.yml` — automated validation of specimens against schema
- `CITATION.cff` — academic citation metadata
- `LICENSE` — CC-BY-SA 4.0
- `CONTRIBUTING.md` — submission standards for external contributors

### Changed
- `README.md` — rewritten with specimen table, badges, and professional structure
- Provenance section — "Lab/Lead Architect" changed to "Project/Founder" for accuracy
- All specimens (SPEC-001 to SPEC-004) retrofitted to v0.2 standard

### Fixed
- SPEC-003: `evidence-lod.md` renamed to `evidence-log.md` (typo)
- SPEC-004: `facts.md` and `report.md` moved to root level for v0.2 compliance
- SPEC-004: `Evidence/evidence-log.md` created for Layer 1 compliance

---

## [0.1] — 2026-07-18

### Added
- Initial repository structure
- Three-Layer Evidence Model (Layer 1: Immutable, Layer 2: Fact Extraction, Layer 3: Reporting)
- First 4 evaluation specimens: SPEC-001, SPEC-002, SPEC-003, SPEC-004
- `index.html` — project landing page
- `chronos-banner.png` — repository asset

---

*CHRONOS Evaluation Methodology · TamilOps*
