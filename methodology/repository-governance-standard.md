# CHRONOS Repository Governance Standard

**Version:** 1.0  
**Status:** Proposed for review  
**Applies to:** SPEC-001 onward, all future specimens, methodology and repository changes

## 1. Purpose and authority

This standard defines the minimum research, evidence, publication and maintenance controls for the CHRONOS repository. It supplements the evidence-handling protocol, failure-classification taxonomy and specimen-structure standard. If two documents conflict, preserve original evidence and follow the more conservative evidence rule until the conflict is resolved and documented.

No specimen is made publication-ready merely by passing automated checks. CI verifies structural and mechanical requirements; human review remains responsible for substantive accuracy, context, ethics and publication approval.

## 2. Evidence and claim categories

Every material statement in a specimen must be distinguishable as one of:

- **Direct observation:** visible or audible in a preserved original artifact.
- **Source-reported statement:** stated by a participant, model, document or third party; attribution must be explicit.
- **Independently verified fact:** checked against an identified independent source or reproducible method; record source and verification date.
- **Inference / analysis:** interpretation derived from identified observations; explain the reasoning and alternatives.
- **Hypothesis:** a proposed explanation not established by the available evidence.
- **Unknown / disputed:** unavailable, incomplete, conflicting or unresolved information.

Never upgrade a source-reported statement into an independently verified fact merely by repeating it in facts or report files. Model self-admission is evidence of what the model said, not proof that its explanation is true.

## 3. Three-layer research chain

1. **Layer 1 — Evidence:** original, preserved artifacts and a factual evidence log. No analytical rewriting of source content.
2. **Layer 2 — Fact extraction:** attributed observations and source-reported statements, each traceable to a Layer 1 artifact and location (page, timestamp, screenshot, line, event or equivalent).
3. **Layer 3 — Analysis and report:** interpretation, classification, causal hypotheses, impact assessment, limitations and recommendations. Each material factual premise traces to Layer 2 and ultimately Layer 1.

An analysis file may be used as an intermediate working artifact, but it is not an additional evidence layer. It must not be cited as primary evidence.

## 4. Minimum specimen record

Every specimen must include:
- `metadata.json` and a human-readable `README.md`;
- preserved Layer 1 evidence and `Evidence/evidence-log.md`;
- `Evidence/integrity.sha256` for preserved evidence files;
- `facts.md`, `report.md`, `mitigation.md`, and `reproduction-test.md`;
- `domain-impact-matrix.md` when impact assessment is relevant or claimed;
- any additional source-verification or analysis artifact required by its case type.

Paths in metadata and manifests are relative to the specimen directory. Evidence logs and integrity manifests are documentation/control files, not raw evidence assets. Do not list them as raw evidence unless the specimen specifically studies those files.

## 5. Evidence preservation and provenance

- Preserve originals byte-for-byte. Never overwrite, crop, recompress, rename or delete original evidence as part of a correction.
- If a derivative, transcription, redaction or extracted image is needed, create a clearly named derivative and document its relationship to the original.
- Record original filename, artifact type, capture/creation time and timezone (or state unknown), collector/source, platform/device when known, model/version when known, and limitations.
- For PDFs and other compound artifacts, record relevant page numbers and whether embedded images, tables or attachments were inspected.
- Hash each preserved evidence asset with SHA-256. Paths must resolve from the specimen root. Recompute hashes after any authorized evidence addition; do not silently update a hash to conceal a changed original.
- Missing referenced files must be reported as missing, not recreated or inferred.

## 6. Fact extraction and traceability

Facts must preserve the source's meaning and uncertainty. Distinguish:
- what the model said or did;
- what the user or another participant said;
- what an external source stated;
- what CHRONOS independently verified; and
- what remains unknown.

Cite each material fact to a specific evidence file and locator. If exact locators cannot be established, identify the limitation. Contradictory evidence must be retained and described, not silently reconciled.

## 7. Analysis, classification and impact

Reports must include the evaluation question, context/environment, observed sequence, evidence-backed findings, alternative explanations, limitations, classification, impact rationale, conclusion and recommendations where applicable.

- Separate observed failure from inferred mechanism and proposed root cause.
- Do not infer model intent, training causes, source contamination, systematic prevalence or business/user motives without supporting evidence.
- Use taxonomy codes defined in the central taxonomy. Propose new codes through a reviewed taxonomy change.
- Explain severity and impact; do not present qualitative estimates as measured outcomes.
- Distinguish a single observed incident from recurrence, cross-model confirmation or reproducibility.
- Record reproduction attempts, including unsuccessful or inconclusive attempts. Never imply a test was run when it was not.

## 8. Specimen lifecycle and publication gate

Each specimen moves through: **Draft → Evidence checked → Fact extraction checked → Analysis reviewed → Reproduction status recorded → CI passed → Human publication approval → Published**.

A CI pass is necessary but not sufficient. A reviewer must verify evidence integrity, attribution, traceability, limitations, ethics, privacy/safety, metadata, taxonomy and publication approval. A specimen with unresolved gaps may be published only if those gaps are explicit and the publication decision accepts them; otherwise it remains draft.

## 9. Retrospective specimens

SPEC-001 through SPEC-004 predate this standard and may contain legacy structure or incomplete provenance. They must be audited individually. Do not rewrite historical evidence to fit the new template. Record each specimen's migration status and gaps; make only evidence-supported documentation corrections. Keep original evidence and historical claims traceable.

## 10. Future specimens

All new specimens must use the current template and set `governance_status` to `standard-v1` only after required provenance, traceability and review fields are complete. A specimen must not claim compliance solely because its files exist or its metadata parses.

## 11. Ownership, attribution and permitted derivatives

Every specimen README and future-specimen template must display the exact project attribution imprint:

> Original Evidence Owner: Sirajudeen Seethapathy | Project CHRONOS — TamilOps

This imprint records the project's declared evidence-collection provenance and curatorial attribution. It must not be interpreted as transferring ownership of third-party, platform, user, or model-generated content to CHRONOS. Known third-party rights must be identified separately.

Raw evidence remains immutable: do not watermark or alter primary screenshots, recordings, exports, or documents. Put the imprint in the specimen's documentation and provenance record. Any visual watermark belongs only on a clearly identified derivative, with the original preserved and separately hashed.

The detailed policy and current licence/platform limitations are documented in [Evidence Ownership and Attribution Policy](evidence-ownership-and-attribution-policy.md). This governance requirement does not itself override the current repository licence or GitHub's public-repository terms.

## 12. Change control

Changes to this standard, schema, templates, taxonomy or validator require a reviewed pull request. Existing published specimens are not silently rewritten by a policy update. Record version, effective date and migration impact. Protect `main`; use branches and pull requests for review.
