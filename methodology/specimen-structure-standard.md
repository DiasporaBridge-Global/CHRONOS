# CHRONOS Specimen Structure Standard v0.2

**Status:** Active  
**Replaces:** v0.1  
**Effective Date:** 2026-08-31

---

## 1. Purpose

Defines the mandatory structure for every evaluation specimen in the CHRONOS repository.

---

## 2. Directory Structure

Every specimen lives under `specimens/SPEC-XXX/`:

---

## 3. Required Files

### 3.1 metadata.json
Machine-readable manifest. Validated automatically.

### 3.2 README.md
Human-readable overview with links to all files.

### 3.3 facts.md (Layer 2)
Rigid fact extraction. No interpretation.

### 3.4 report.md (Layer 3)
Full evaluation report with analysis.

### 3.5 mitigation.md
How to prevent, detect, or recover from this failure.

### 3.6 reproduction-test.md
Documented attempts to reproduce the failure.

### 3.7 Evidence/evidence-log.md (Layer 1)
Immutable observation log. Zero interpretation.

### 3.8 Evidence/integrity.sha256
Cryptographic hashes for all evidence files.

---

## 4. The Three-Layer Evidence Model

- **Layer 1 (Immutable):** Raw evidence. Zero interpretation.
- **Layer 2 (Fact Extraction):** Rigid extraction from Layer 1.
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

---

## 6. Versioning

- New specimens (from 2026-08-31) must comply at submission.
- Old specimens (SPEC-001 to SPEC-004) must be retrofitted by 2026-09-15.

---

*CHRONOS v0.2 · TamilOps · Last updated 2026-08-31*
