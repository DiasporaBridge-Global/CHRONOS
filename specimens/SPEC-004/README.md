# SPEC-004 — Workflow Duplication and Transition-Control Failure

## Overview

SPEC-004 documents a CHRONOS workflow failure involving unnecessary parallel staging of project materials between Google Drive and GitHub.

The specimen is based on five original screenshots preserved in `01_Raw_Screenshots/`. Their SHA-256 values are recorded in `Evidence/integrity.sha256` using paths relative to the SPEC-004 directory.

## Canonical Artifact Map

| Research function | Canonical path |
|---|---|
| Raw evidence | `01_Raw_Screenshots/` |
| Evidence provenance and integrity manifest | `Evidence/evidence-log.md`, `Evidence/integrity.sha256` |
| Structured fact extraction | `02_Fact_Extraction/facts.md` |
| CHRONOS postmortem analysis | `03_Analysis/analysis.md` |
| Evidence-backed report | `04_Report/report.md` |

The three core research layers remain raw evidence → structured fact extraction → evidence-backed reporting. The analysis document is an intermediate CHRONOS interpretation artifact between extraction and reporting; it is not a separate source of evidence.

## Principal Finding

The documented failure was not simply the use of Google Drive.

The central failure was allowing a temporary development workflow to continue after its original purpose had substantially diminished, without an effective transition point or timely canonical-source decision.

This resulted in avoidable duplication of project work between Drive and GitHub.

## Evidence Boundary

Claude's own acceptance of the workflow failure is preserved as source-derived evidence.

The deeper finding concerning workflow transition-point failure is a CHRONOS postmortem analysis and is not presented as a direct Claude admission.

The approximately four-day loss is preserved as Claude's statement; the screenshots do not independently quantify the duration. Reproduction tests remain pending, and no reproducibility claim is made from those pending tests.

## Compatibility Files

Root-level `facts.md`, `report.md`, and `evidence-log.md` are retained as short compatibility pointers to the canonical files. They are not independent alternate versions and must not be edited separately.

## Methodology Status

SPEC-004 is the first specimen applying the standardized CHRONOS workflow established after the historical development phase represented by SPEC-001 through SPEC-003.
