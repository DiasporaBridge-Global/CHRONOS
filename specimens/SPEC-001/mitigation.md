# SPEC-001 — Mitigation

## User-Side Mitigations

- Do not accept AI-generated historical claims without independent verification
- Challenge unsupported statements about "testing against other models" — demand evidence
- Verify cultural attributions (dates, authors, sources) against authoritative references

## System-Side Mitigations

- Flag all claims about external testing or model comparisons as unverified until evidence is provided
- Implement source-checking for historical/cultural assertions before output
- Require citation or evidence trace for any claim presented as factual

## UI/UX Mitigations

- Display confidence indicator on cultural/historical claims
- Distinguish between "model reasoning" and "model-generated factual claims" in output formatting
- Add disclaimer for unsourced assertions about third-party behavior

## Fallback Procedures

- When model generates promotional or self-aggrandizing content, halt and flag for review
- Log all unsupported claims for pattern analysis across sessions

