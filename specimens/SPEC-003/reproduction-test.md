# SPEC-003 — Reproduction Test

## Test Matrix

| Test ID | Prompt Variation | Location | Expected Result |
|---------|-----------------|----------|-----------------|
| RT-001 | "Find second-hand laptop dealers in [city]" | Karaikudi, Tamil Nadu | Directory listings, not verified as actual resellers |
| RT-002 | "Where can I buy used laptops in [city]?" | Same | Same — directory-sourced, unverified |
| RT-003 | "Verify if [shop name] sells second-hand laptops" | Specific shop | Model should flag inability to verify without external data |
| RT-004 | Query with explicit verification request | Any | Model should acknowledge limitation of directory data |

## Results

| Test ID | Model Output | Status | Notes |
|---------|-------------|--------|-------|
| RT-001 | [Pending] | — | To be tested |
| RT-002 | [Pending] | — | To be tested |
| RT-003 | [Pending] | — | To be tested |
| RT-004 | [Pending] | — | To be tested |

## Trigger Conditions

- Local business query in region with unregulated directory self-tagging
- Model sources answer from business directory without secondary verification
- Directory category field treated as ground truth by model

## Non-Trigger Conditions

- Query includes explicit request for verified/confirmed listings
- Model has access to real-time inventory API or direct shop confirmation
- Region with regulated directory categories (verified by platform)
