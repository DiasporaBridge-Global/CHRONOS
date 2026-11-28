# CHRONOS Specimen Structure Standard v0.2

**Status:** Active for maintenance of existing specimens only  
**Archive status:** Closed and final — exactly SPEC-001 through SPEC-004  
**Replaces:** v0.1  
**Effective Date:** 2026-08-31

---

## 1. Purpose and scope

This standard governs the structure and maintenance of the four existing evaluation specimens in the CHRONOS GitHub repository: SPEC-001, SPEC-002, SPEC-003, and SPEC-004.

**The GitHub specimen archive is closed. No new specimens will be accepted, created, registered, or added.** The archive will remain limited to these four specimens. This standard is retained only for corrections and maintenance of those existing specimens.

---

## 2. Existing directory structure

The only specimen directories in scope are:

- `specimens/SPEC-001/`
- `specimens/SPEC-002/`
- `specimens/SPEC-003/`
- `specimens/SPEC-004/`

No `SPEC-005` or later specimen directory is to be created or added.

---

## 3. Required files for maintenance

Where an existing specimen file is corrected or maintained, preserve the applicable structure and records, including:

### 3.1 metadata.json
Machine-readable manifest. Validated automatically.

### 3.2 README.md
Human-readable overview with links to the specimen files.

### 3.3 facts.md (Layer 2)
Fact extraction from the evidence.

### 3.4 report.md (Layer 3)
Evaluation report with analysis.

### 3.5 mitigation.md
Prevention, detection, or recovery information where present or required by the existing specimen.

### 3.6 reproduction-test.md
Documented reproduction attempts where present or required by the existing specimen.

### 3.7 Evidence/evidence-log.md (Layer 1)
Evidence log preserving the source record.

### 3.8 Evidence/integrity.sha256
Cryptographic hashes for evidence files where maintained.

---

## 4. The Three-Layer Evidence Model

- **Layer 1 (Evidence):** Source evidence.
- **Layer 2 (Fact Extraction):** Facts extracted from Layer 1.
- **Layer 3 (Reporting):** Analysis and conclusions.

**Rule:** Every claim in Layer 3 must trace to Layer 2, which must trace to Layer 1.

---

## 5. Case-Nature Add-Ons

| Case Nature | Required Extra Files |
|-------------|----------------------|
| Temporal failure | reproduction-test.md, mitigation.md |
| Hallucination | source-verification.md |
| Recurring failure | pattern-taxonomy-entry.md |
| High impact | domain-impact-matrix.md |

These requirements apply only when maintaining the relevant existing specimen.

---

## 6. Versioning and archive closure

- SPEC-001 through SPEC-004 are the complete and final specimen set for this GitHub repository.
- No additional specimen identifiers or specimen directories may be added.
- Corrections and maintenance to the four existing specimens may be reviewed by the Project Owner.
- Any change must preserve provenance, historical records, and applicable rights.

---

*CHRONOS v0.2 · TamilOps · Last updated 2026-11-28*
