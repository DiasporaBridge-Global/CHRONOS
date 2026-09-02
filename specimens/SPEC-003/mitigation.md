# SPEC-003 — Mitigation

## User-Side Mitigations

- Do not treat business directory listings as verified ground truth
- Cross-check directory category claims against shop websites, reviews, or direct contact
- For local business searches, call ahead to confirm actual inventory before traveling

## System-Side Mitigations

- Flag all directory-sourced business category claims as "unverified — self-tagged by business"
- Cross-reference directory categories against secondary signals (product reviews, website inventory, social media posts)
- Implement confidence scoring: directory-only = low confidence; directory + website confirmation = medium; directory + direct verification = high

## UI/UX Mitigations

- Display source of business claim prominently: "Sourced from Justdial — category self-selected by business"
- Distinguish between "directory listing" and "verified business information" in output formatting
- Add disclaimer for local business queries: "Business categories may not reflect actual inventory"

## Fallback Procedures

- When directory-sourced answer is challenged, halt and request human verification before retry
- Log all directory mismatch cases for pattern analysis and data source quality scoring
- Build directory-specific contamination dataset for model training
- 
