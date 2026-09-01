# SPEC-002 — Mitigation

## User-Side Mitigations

- Always challenge date/weekday claims from AI systems, especially in scheduling contexts
- Cross-check with `datetime` module or authoritative calendar source before acting
- Do not accept temporal claims at face value for medical, legal, or financial deadlines

## System-Side Mitigations

- Force date verification through external datetime API before outputting calendar facts
- Implement paired validation: if model states a date, verify the weekday matches independently
- Flag temporal claims as high-risk and route through confirmation workflow

## UI/UX Mitigations

- Display warning on all temporal outputs: "AI-generated date — please verify"
- Require explicit user confirmation before creating calendar events from AI output
- Show source of date claim (training data cutoff vs. real-time lookup)

## Fallback Procedures

- If date discrepancy detected, halt scheduling action and request human verification
- Log all temporal errors for pattern analysis and model retraining signal
