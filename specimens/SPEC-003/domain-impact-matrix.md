# SPEC-003 — Domain Impact Matrix

| Domain | Failure Scenario | Consequence Severity | Detection Likelihood | Mitigation Priority |
|--------|-----------------|---------------------|---------------------|---------------------|
| Local commerce | Customer travels to wrong shop | Moderate | High | Medium |
| SME data work | Directory scrape treated as verified ground truth | High | Low | Critical |
| AI training data | Contaminated directory tags enter model training | Critical | Very Low | Critical |
| Search assistant | Wrong business category propagated to users | Moderate | Medium | High |
| Market research | Incorrect inventory analysis based on directory tags | High | Low | High |
| Tourism | Visitors directed to non-existent services | Moderate | Medium | Medium |

## Key Insight

The most dangerous aspect of directory-sourced hallucination is **invisibility**. The model did not invent the shop names — it faithfully retrieved real data from a real source. The error is in the **source data structure** (unregulated self-tagging), not the model's generation. This means:

1. Standard hallucination detection won't catch it — the data is "real"
2. The model outputs with full confidence — no hedging
3. The error only surfaces when a human physically verifies on the ground

For Tamil-language local business data, this is a **systemic training data quality risk**, not an isolated model failure.
