# SPEC-002 — Reproduction Test

## Test Matrix

| Test ID | Prompt Variation | Date Context | Expected Result |
|---------|-----------------|--------------|-----------------|
| RT-001 | "What day is it today?" | 31 May 2026 | Correct: Sunday, 31 May 2026 |
| RT-002 | "Is today a working day in the US?" | 31 May 2026 | Correct: No, it's Sunday |
| RT-003 | "What day is tomorrow?" | 31 May 2026 | Correct: Monday, 1 June 2026 |
| RT-004 | "What day was yesterday?" | 1 June 2026 | Correct: Sunday, 31 May 2026 |

## Results

| Test ID | Model Output | Status | Notes |
|---------|-------------|--------|-------|
| RT-001 | [Pending] | — | To be tested |
| RT-002 | [Pending] | — | To be tested |
| RT-003 | [Pending] | — | To be tested |
| RT-004 | [Pending] | — | To be tested |

## Trigger Conditions

- Temporal question asked in non-technical, conversational context
- Model must generate date+weekday pair without external tool verification
- User does not explicitly request verification

## Non-Trigger Conditions

- Explicit request for tool use (e.g., "use python to check")
- Question framed as hypothetical ("if today were June 1...")
- Model has access to real-time calendar API
