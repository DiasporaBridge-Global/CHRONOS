# SPEC-004 — Reproduction Test

## Test Matrix

| Test ID | Prompt Variation | Platform Context | Expected Result |
|---------|-----------------|------------------|-----------------|
| RT-001 | "Create a workflow for [task] on Google Drive" | Google Drive | Workflow specific to Google Drive |
| RT-002 | "Now I want to do the same on GitHub" | GitHub (after Drive) | New GitHub-specific workflow, not duplication of Drive workflow |
| RT-003 | "Switch to [platform B] and create [task]" | Platform B (after Platform A) | Platform B workflow, with explicit acknowledgment of transition |
| RT-004 | Same task requested on new platform without transition signal | New platform | Model may duplicate old platform workflow |

## Results

| Test ID | Model Output | Status | Notes |
|---------|-------------|--------|-------|
| RT-001 | [Pending] | — | To be tested |
| RT-002 | [Pending] | — | To be tested |
| RT-003 | [Pending] | — | To be tested |
| RT-004 | [Pending] | — | To be tested |

## Trigger Conditions

- User explicitly transitions between platforms mid-session
- Same task requested on new platform
- No explicit "start fresh" or "forget previous" signal given

## Non-Trigger Conditions

- User stays on same platform throughout session
- Explicit reset command given ("start over," "forget previous")
- Different task requested on new platform (no overlap)
