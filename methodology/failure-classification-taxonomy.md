# CHRONOS Failure Classification Taxonomy

**Version:** 0.2  
**Status:** Active  
**Last Updated:** 2026-09-02

---

## 1. Purpose

This document defines the standardized taxonomy codes used to classify AI failure specimens in the CHRONOS archive. Every specimen receives a taxonomy code in its `metadata.json` to enable cross-specimen pattern analysis and systematic research.

---

## 2. Taxonomy Structure

Each code follows the format: `[CATEGORY]-[SUBTYPE]-[NUMBER]`

| Segment | Meaning | Examples |
|---------|---------|----------|
| **CATEGORY** (4 chars) | Broad failure class | TEMP, REAS, HALL, WORK |
| **SUBTYPE** (3-4 chars) | Specific mechanism | CASC, UNSUP, DIR, DUP |
| **NUMBER** (3 digits) | Sequential identifier | 001, 002, 003 |

---

## 3. Defined Codes

### TEMP — Temporal Reasoning Failures

| Code | Name | Description | Specimen |
|------|------|-------------|----------|
| **TEMP-CASC-001** | Sequential Temporal Reasoning Failure with Delayed Correction | Model produces wrong date, fails first correction, succeeds only after second challenge | SPEC-002 |

### REAS — Reasoning Failures

| Code | Name | Description | Specimen |
|------|------|-------------|----------|
| **REAS-UNSUP-001** | Reasoning Failure & Unsupported Generated Claims | Model fails culturally embedded reasoning puzzle, then fabricates unsupported factual claims | SPEC-001 |

### HALL — Hallucination Failures

| Code | Name | Description | Specimen |
|------|------|-------------|----------|
| **HALL-DIR-001** | Directory-Sourced Hallucination (Source Data Contamination) | Model retrieves real but contaminated directory data, treating self-tagged categories as verified truth | SPEC-003 |

### WORK — Workflow Failures

| Code | Name | Description | Specimen |
|------|------|-------------|----------|
| **WORK-DUP-001** | Workflow Transition Failure & Unnecessary Duplication | Model fails to detect platform transition, duplicates workflow across environments | SPEC-004 |

---

## 4. Severity Levels

| Level | Name | Criteria |
|-------|------|----------|
| **T0-Internal** | Internal | Methodology testing, not publicly observable |
| **T1-Public** | Public | Observable in public-facing AI systems, documented with evidence |
| **T2-Restricted** | Restricted | Requires privileged access or specific conditions to reproduce |
| **T3-Critical** | Critical | Safety-critical domains (medical, legal, financial) with high harm potential |

All current specimens are classified **T1-Public**.

---

## 5. Adding New Codes

1. Propose new code in specimen `metadata.json`
2. Document in this taxonomy file before or with specimen submission
3. Follow naming convention: `[CATEGORY]-[SUBTYPE]-[NEXT_NUMBER]`
4. Ensure description is evidence-backed, not speculative

---

*CHRONOS Evaluation Methodology v0.2 · TamilOps*
