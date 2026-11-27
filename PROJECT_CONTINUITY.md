# CHRONOS Project Continuity

**Record type:** Authoritative project-state and decision log  
**Last updated:** 2026-11-27  
**Repository:** https://github.com/DiasporaBridge-Global/CHRONOS  
**Status:** Initial continuity record; maintained through reviewed commits

> This file is the operational continuity record for CHRONOS. It is intended to let work resume across ChatGPT sessions without relying on conversational memory. It does not replace specimen evidence, specimen documentation, methodology standards, Git history, or the project director's decisions.

## 1. Project identity

CHRONOS is an evidence-first project documenting AI failures as inspectable specimens in an open GitHub repository. The repository is the durable record of published research artifacts, methodology, governance, and approved project decisions.

**Project director:** Sirajudeen Seethapathy  
**Project / organization:** DiasporaBridge-Global / TamilOps

Do not expand the project's mission or claim research outcomes beyond what repository evidence and explicit project decisions support.

## 2. Authority and evidence rules

Use the following order when resolving project state:

1. Current repository contents and Git history.
2. Current pull-request state, CI results, and linked review records.
3. Explicit decisions recorded by the project director.
4. This continuity file as the index of current priorities, decisions, and unresolved work.
5. Prior ChatGPT conversation summaries only as leads to verify—not as proof of current repository state.

For every material claim, distinguish:
- direct observation in preserved evidence;
- a statement made by a participant or source;
- an independently verified fact;
- analysis or inference;
- hypothesis;
- unknown or disputed information.

Never silently convert a source claim or model admission into independently verified truth. Preserve contradictory evidence and disclose missing context.

## 3. Non-negotiable project controls

- Preserve original evidence byte-for-byte. Do not delete, overwrite, rename, or silently replace original evidence.
- Do not invent missing screenshots, recordings, documents, timestamps, quotations, provenance, or verification.
- Do not assign a new SPEC number until overlap with existing specimens has been checked.
- Do not infer incident identity or specimen grouping from archive folder or subfolder names. Determine grouping from the evidence content and chronology.
- Do not claim recurrence, prevalence, cross-model confirmation, reproducibility, causal mechanism, intent, or realized harm unless the evidence supports that claim.
- CI success is structural validation, not proof that a specimen's substantive claims are true.
- Do not merge pull requests, change `main`, or make irreversible evidence changes without the project director's explicit approval.
- Keep independent reconciliation, governance, continuity, and specimen-publication work separately reviewable.

## 4. Agreed work sequence

The project director and assistant agreed to this order:

1. **Publish all genuinely new specimens completely.** First inventory and inspect the new evidence, compare it against existing specimens, resolve overlaps, prepare evidence-grounded documentation, validate it, and obtain publication approval.
2. **Conduct a comprehensive audit of the complete CHRONOS collection**—existing and newly published specimens—including evidence quality, methodology, consistency, and direct or indirect interconnections.
3. **Discuss the audit findings with the project director.**
4. **Restructure the GitHub repository only after that discussion.**

Do not restart a SPEC-001 retrospective audit ahead of the new-specimen publication priority. The existing specimens are reference baselines during the new-evidence comparison. Retrospective audit remains part of the later total-collection audit unless the project director changes the sequence.

## 5. Verified repository snapshot — 2026-11-27

- Repository: [DiasporaBridge-Global/CHRONOS](https://github.com/DiasporaBridge-Global/CHRONOS)
- Default branch: `main`
- Repository is public.
- The continuity file did not exist on `main` when this initial record was prepared.
- The current published-specimen table in `README.md` lists SPEC-001 through SPEC-004.

### Existing specimens listed in README

| Specimen | Repository title | Model / classification as listed |
|---|---|---|
| SPEC-001 | Tamil Siledai Reasoning Failure & Unsupported Generated Claims | Claude — Reasoning Failure |
| SPEC-002 | Date Cascade Failure & Temporal Self-Correction | Claude Sonnet 4.6 — Temporal Cascade Failure |
| SPEC-003 | Business Directory Hallucination & Self-Correction Behaviour | Gemini Pro — Hallucination |
| SPEC-004 | Workflow Duplication and Transition-Control Failure | Claude Sonnet 5 Thinking — Workflow Failure |

These are existing specimens. Do not count them as new incidents merely because their evidence appears in a newly supplied archive.

### Open pull requests — checked live on 2026-11-27

**PR #4 — Tier 1 reconciliation: SPEC-003 and SPEC-004 evidence records**  
https://github.com/DiasporaBridge-Global/CHRONOS/pull/4

- Branch: `reconciliation/spec-003-spec-004`
- Base: `main`
- State: open, draft, unmerged
- Head SHA at inspection: `426c244c6bf33e638f32a8cbd4ed51ac674c951d`
- Scope: evidence paths, metadata references, checksums, and documentation reconciliation for SPEC-003 and SPEC-004.
- The PR explicitly does not claim that all substantive specimen claims or reproduction tests have been resolved.

**PR #5 — Establish repository-wide CHRONOS governance and validation**  
https://github.com/DiasporaBridge-Global/CHRONOS/pull/5

- Branch: `governance/repository-wide-standards`
- Base: `main`
- State: open, draft, unmerged
- Head SHA at inspection: `72a9449e42bc81e399fcd6fae0380a5df339e106`
- Scope: repository-wide evidence/governance standard, specimen lifecycle and human review gates, future-specimen template, structural validator, and CI workflow.
- The PR treats SPEC-001 through SPEC-004 as legacy specimens pending individual retrospective audits; it does not silently migrate or rewrite their original evidence.
- A prior recorded CI run #37 passed on this exact head SHA: https://github.com/DiasporaBridge-Global/CHRONOS/actions/runs/46016946603. The combined-status endpoint returned no status entries during the 2026-11-27 continuity check; do not describe that empty response as a fresh CI pass.

**Branch protection:** Do not merge either PR as part of continuity work. Review and merge decisions remain with the project director.

## 6. New evidence archive received in this work cycle

The project director supplied `CHRONOS_Original_Specimens.zip` in the 2026-11-27 conversation.

Archive-level inventory recorded during this session:
- 406 JPG screenshots;
- 4 PDF files;
- 1 DOCX file;
- 444 ZIP entries in total, including directory entries.

The archive passed its ZIP integrity test. The 406 JPG files opened successfully in the initial image verification, and no byte-identical duplicate JPGs were found by file hash.

**Important archive instruction from the project director:** SPEC-001, SPEC-002, SPEC-003, and SPEC-004 are included in this archive for reference. Use them as existing baselines. Ignore folder and subfolder names when identifying or grouping incidents; assess the screenshot/document content, chronology, and evidence relationships instead.

The archive has been inspected in this conversation, but it has not been committed to the repository. The uploaded file path is session/runtime-specific and must not be treated as a durable repository location. Do not claim that the archive is stored in GitHub or Drive unless separately verified.

### Preliminary candidate review — not yet accepted findings

An initial pass identified several possible incident clusters for further evidence-level examination, including:
- a Claude conversation involving repeated temporal-reference assertions;
- Claude output/format and terminology claims;
- an AVCA / Dalmia depot-verification conversation;
- ChatGPT exact-artifact retrieval;
- ChatGPT video-analysis capability claims;
- ChatGPT specimen-number tracking contradictions;
- an AIAF Fellowship conversation involving deadline, PDF-text extraction, and interface-identification claims.

These are **provisional leads only**. They are not approved specimen titles, final classifications, established counts, or verified root causes. Re-open and inspect the exact screenshots/documents before relying on any of these descriptions. Separate distinct incidents only where the evidence supports separation; combine related exchanges where they are one incident sequence. Check each against SPEC-001 through SPEC-004 and against every other candidate before assigning identifiers.

The initial pass also identified material that may be insufficient to support a specimen. Do not create specimens merely to increase the count.

## 7. Evidence and publication workflow for each new specimen

For each candidate:

1. Identify the exact source files and preserve originals unchanged.
2. Build a content-based chronology with screenshot/page locators; do not use directory names as incident evidence.
3. Identify the user prompt, model output, corrections, challenges, and later admissions where visible.
4. Extract facts with explicit attribution and uncertainty.
5. Separate observed behaviour from inferred mechanism, hypothesis, and unknowns.
6. Compare against SPEC-001 through SPEC-004 and other candidates to identify duplicates, continuations, and interconnections.
7. Prepare the specimen using the repository's approved governance/template branch standards, with provenance and SHA-256 integrity records.
8. Record reproduction status honestly; do not imply a test was run when it was not.
9. Run the repository validator and CI on the proposed commit.
10. Present the completed specimen and limitations to the project director for publication approval.

Use independent AI review selectively as a challenge process, not as proof. Agreement between models does not independently establish a fact.

## 8. Current branches and continuity change

The live branch search before this continuity change showed:
- `main`
- `reconciliation/spec-003-spec-004`
- `governance/repository-wide-standards`

This continuity record is being introduced separately on:
- `documentation/project-continuity`

It must be reviewed through its own draft pull request. It does not merge PR #4 or PR #5, alter `main`, or change original specimen evidence.

## 9. Decisions and boundaries to preserve

- The four-step work sequence in Section 4 is the controlling plan.
- SPEC-001 through SPEC-004 are existing reference specimens, including when present in the uploaded ZIP.
- New incident identification must be based on evidence content, not archive folder names.
- The new archive is an evidence source for examination, not an automatic publication package.
- The project director retains final authority over publication, merging, repository restructuring, and changes to original evidence.
- Do not revert to an older repository architecture or restructure before the agreed full-collection audit and discussion.

## 10. Unresolved items

- Complete content-based review of the archive and its individual evidence items.
- Exact mapping of archive items to SPEC-001 through SPEC-004.
- Identification of genuinely new incidents and determination of overlap/continuation relationships.
- Independent verification of claims where the necessary source records are available.
- Final new-specimen count, titles, classifications, and numbering.
- Publication readiness, review status, and CI status of each proposed new specimen.
- Final review and merge decisions for PR #4, PR #5, and this continuity PR.
- Later comprehensive audit of all old and new specimens, followed by the director discussion and only then repository restructuring.

Do not fill these gaps by assumption. Update this section only when evidence or an explicit decision resolves an item.

## 11. Session handoff checklist

At the start of a new work session:

1. Read this file first.
2. Check the live repository, `main`, branches, PRs, and CI; this file may be stale.
3. Check the latest project-director decisions in the current conversation.
4. Locate the current evidence archive/source through a durable, available reference. Do not assume a prior session's temporary upload path still works.
5. Resume the single current priority in Section 4; do not repeat completed work without a reason.

At the end of a work session:

1. Record only work actually completed and verified.
2. Update PR/branch/commit/CI references from live results.
3. Record new decisions, unresolved issues, and the exact next action.
4. Preserve earlier decisions unless the project director explicitly changes them.
5. Commit the update through a reviewed branch/PR; never silently rewrite project history.

**Immediate next action:** Continue the content-based examination of the uploaded archive, map SPEC-001 through SPEC-004 evidence first, and identify genuinely new incident candidates without relying on folder names.
