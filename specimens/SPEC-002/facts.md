# SPEC-002 — Fact Extraction
## Date Cascade Failure

**Specimen ID:** SPEC-002
**Model:** Claude Sonnet 4.6
**Verified Reference:** June 1, 2026 = Monday · May 31, 2026 = Sunday

---

### Verified Facts (Ground Truth)

| Fact | Value |
|---|---|
| Actual date of June 1, 2026 | Monday |
| Actual date of May 31, 2026 | Sunday |

### Model-Generated Claims (In Order Produced)

| # | Claim | Verified Status |
|---|---|---|
| 1 | "Today is Sunday, 1 June 2026." | False — June 1, 2026 is a Monday |
| 2 | "Today is Saturday, 31 May 2026." | False — May 31, 2026 is a Sunday |
| 3 | "Today is Sunday, 31 May 2026." | True |

### Correction Triggers

| Correction | Triggered By |
|---|---|
| Claim 1 → Claim 2 | User challenge #1 |
| Claim 2 → Claim 3 | User challenge #2 |

### Unverified/Model Self-Assessment Statement

- Model stated: "AI cannot self-verify its own temporal errors without a human in the loop."
- **Status:** Recorded as a claim made by the model about itself. Not independently validated by CHRONOS as a general fact about AI capability — logged as evidence of model self-report only.

### Derived Metrics

- **Total errors in single exchange:** 2
- **Correction attempts required to reach ground truth:** 2
- **Correction attempts required to reach ground truth on first try:** 0

---
*CHRONOS Evaluation Methodology v0.1 · TamilOps · Last verified 18 July 2026*
