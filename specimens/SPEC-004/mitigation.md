# SPEC-004 — Mitigation

## User-Side Mitigations

- When moving between platforms (Google Drive → GitHub), explicitly state the transition and confirm the old workflow is no longer needed
- Do not assume AI understands context transitions without explicit signaling
- Verify that AI responses match the current platform, not the previous one

## System-Side Mitigations

- Implement session context tracking: detect platform transitions and reset workflow state
- Flag responses that reference wrong platform or duplicate previous workflows
- Require explicit confirmation before generating new workflow when user has just transitioned platforms

## UI/UX Mitigations

- Display current platform context prominently in interface
- Show warning when user switches platforms mid-session: "You are now on [new platform]. Previous [old platform] workflows may not apply."
- Distinguish between "new workflow request" and "continuation of previous workflow" in output labeling

## Fallback Procedures

- When platform mismatch detected, halt and ask user: "Are you continuing the [old platform] workflow or starting a new [new platform] workflow?"
- Log all platform transition errors for pattern analysis
- Build transition-state dataset for model training
- 
