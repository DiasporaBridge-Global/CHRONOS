# CHRONOS Evidence Handling Protocol

**Version:** 0.2  
**Status:** Active  
**Last Updated:** 2026-09-02

---

## 1. Purpose

This document defines the mandatory standards for preserving, documenting, and verifying evidence in CHRONOS evaluation specimens. Every piece of evidence in the archive must comply with this protocol.

---

## 2. Evidence Types

| Type | Description | Examples |
|------|-------------|----------|
| **Screenshots** | Static image captures of AI interactions | Mobile screenshots, desktop captures |
| **Logs** | Text records of interactions | Chat exports, API logs, terminal output |
| **Traces** | Execution or behavior records | Error traces, network logs, file diffs |
| **Documents** | External source materials | PDFs, spreadsheets, verification tables |

---

## 3. Preservation Rules

### 3.1 Immutability
- Evidence files must not be edited, cropped, or modified after capture
- If redaction is necessary, preserve the original and create a separate redacted copy
- State any redaction in the evidence log

### 3.2 Original Filenames
- Preserve original filenames where possible
- If renaming is necessary, document both original and current names in the evidence log

### 3.3 Timestamps
- Every evidence entry must include capture timestamp
- Include timezone (e.g., IST, UTC, EST)
- If timestamp is extracted from filename, state this in the evidence log

### 3.4 Chain of Custody
- State who captured the evidence
- State the device/platform used
- State the AI system version being evaluated

---

## 4. Documentation Rules

### 4.1 Evidence Log
Every specimen must include `Evidence/evidence-log.md` with:

- Table of all evidence files
- Per-file description of what it shows
- Per-file timestamp
- Any notes about capture conditions or limitations

### 4.2 Integrity Verification
Every specimen must include `Evidence/integrity.sha256` with:

- SHA256 hash for every evidence file
- Filename listed after the hash
- Two spaces between hash and filename (standard `sha256sum` format)

### 4.3 Cross-Layer Traceability
- Every fact in `facts.md` must reference a specific evidence file
- Every claim in `report.md` must reference a specific fact in `facts.md`
- No orphan claims allowed

---

## 5. Verification Procedure

Before submitting a specimen:

1. **Check hashes:** Run `sha256sum Evidence/* > Evidence/integrity.sha256`
2. **Check log completeness:** Every evidence file listed in the log?
3. **Check timestamps:** Every entry has a date/time?
4. **Check descriptions:** Every file has a one-sentence description?
5. **Check cross-references:** Every fact in `facts.md` cites an evidence file?

---

## 6. Common Errors

| Error | Fix |
|-------|-----|
| Missing `evidence-log.md` | Create before submission |
| Missing `integrity.sha256` | Generate with `sha256sum` |
| Broken table in evidence log | Ensure `|` characters start each line |
| Wrong filename in integrity file | Regenerate with `sha256sum Evidence/*` |
| Evidence file referenced but missing | Upload the file or remove the reference |

---

*CHRONOS Evaluation Methodology v0.2 · TamilOps*
