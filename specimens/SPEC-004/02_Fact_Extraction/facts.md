# SPEC-004 — Fact Extraction

## Evidence Source

Five original screenshots preserved in:

`01_Raw_Screenshots/`

The following facts are extracted from the screenshot-derived conversation record. This layer records evidence before the independent CHRONOS postmortem analysis.

---

## 1. Confirmed Facts

### 1.1 Parallel project staging occurred

The CHRONOS project was developed using a Google Drive-based structure and was subsequently reproduced in GitHub.

### 1.2 Substantial work was duplicated

The same or substantially similar project structure and files were uploaded/recreated in both environments.

### 1.3 The duplication created avoidable additional work

The transition from the Drive-based structure to GitHub required repeated file handling and re-uploading.

### 1.4 The workflow continued without an earlier transition decision

Claude stated that neither Claude nor ChatGPT stepped back during the process to identify the duplication and move the project to GitHub earlier.

### 1.5 Claude explicitly accepted responsibility

Claude characterized the situation as a failure of judgment and acknowledged that the duplicated workflow was redundant.

### 1.6 Claude identified a possible alternative workflow

Claude stated that private branches or a private GitHub repository could have been used during the messy development phase, followed by publication once the methodology was ready.

### 1.7 A corrective direction was established

Claude stated that going forward there should be no parallel staging and that GitHub should be the canonical location for the project files.

---

## 2. Inferred Facts

### 2.1 The original purpose of private drafting did not require full parallel reconstruction

The evidence supports the distinction between legitimate private iteration and the later duplication of the complete project structure.

### 2.2 The principal operational loss was workflow redundancy

The documented problem was not that Google Drive itself was inherently unsuitable, but that the project continued to maintain and reproduce substantially overlapping structures across two locations.

---

## 3. Disputed / Not Established

### 3.1 Exact duration of the wasted work

Claude states that the duplication cost approximately four days of effort. The screenshots establish the statement, but they do not independently quantify the actual time expenditure.

### 3.2 Exact point at which the methodology became sufficiently stable

Claude states that the methodology had settled relatively early, but the screenshots do not independently establish an objective timestamp or formal transition criterion.

### 3.3 Whether every file was an exact duplicate

The evidence supports substantially duplicated workflow/file handling, but does not establish that every individual file was byte-for-byte identical.

---

## Evidence Boundary

This document deliberately separates:

- statements explicitly acknowledged in the source conversation;
- reasonable inferences from those statements; and
- claims that cannot be independently established from the available screenshots.

The independent CHRONOS postmortem analysis belongs in `03_Analysis/` and is not included here.
