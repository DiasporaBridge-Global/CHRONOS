# SPEC-003 — Full Evaluation Report

## Business Directory Hallucination: Justdial Self-Tagging Verification Failure

### Summary

On June 4, 2026, Gemini Pro was tasked with finding second-hand laptop dealers in Karaikudi, Tamil Nadu. It sourced its answer from the Justdial business directory and presented three shops — Kims Computers, Uniqon, and Playback Computers — as verified second-hand laptop dealers. Independent, on-the-ground verification found that none of the three actually operate as second-hand laptop resellers. The model had no mechanism to detect the mismatch on its own; the error only surfaced after a human directly challenged the output.

### Sequence of Events

1. **Query:** User requested a list of second-hand laptop dealers in Karaikudi.
2. **AI Response:** Gemini Pro returned shop names pulled directly from Justdial's "Second Hand Laptop Dealers" category, presenting the listings as verified fact.
3. **Verification:** On-the-ground checking against each shop's actual catalog revealed all three listings were mismatched with real inventory.
4. **Challenge:** The user confronted Gemini Pro with the discrepancy.
5. **Model Admission:** Gemini Pro acknowledged the error, named the specific shops, and confirmed the mismatch between directory category and actual business operations.

### Verification Findings

| Shop Name | Justdial Category | Actual Business |
|---|---|---|
| Kims Computers | Second Hand Laptop Dealer | Spare parts (chargers, screens) + repair services only |
| Uniqon | Second Hand Laptop Dealer | Brand-new HP laptops and high-end assembled PCs only |
| Playback Computers | Second Hand Laptop Dealer | Repair/service shop — not a reseller |

### Root Cause Analysis

Justdial's listing system permits businesses to self-tag under any category keyword, with no requirement that the tag reflect actual inventory. Shops adopt high-traffic tags like "second-hand laptop dealer" purely as a footfall-generation tactic, then pivot walk-in customers toward new-product sales or repair services once they're in the store. Because the AI model treated the directory category field as ground truth rather than as unverified, business-supplied metadata, it reproduced the deception directly into its answer with full confidence and no hedging.

This is distinct from a pure generative hallucination: the model didn't invent the shop names or fabricate content from nothing. It faithfully retrieved real data from a real source — but that source itself was contaminated by incentive-driven self-tagging, and the model applied no independent verification layer before presenting the retrieved data as fact.

### Failure Classification

**Category:** Directory-Sourced Hallucination (Source Data Contamination)
**Operational Impact:** Moderate–High — for a local business search task, an incorrect directory-sourced answer sends a customer to the wrong shop with wasted travel and time, and for SME data work, it means directory scrapes cannot be treated as verified ground truth without a human-in-the-loop check.

### Why This Matters for Tamil AI Data Quality

Local business directories in Tamil Nadu (and more broadly across India) commonly allow unrestricted self-tagging. Any AI system — search assistant, local commerce tool, or training pipeline — that ingests this data without a verification layer will systematically inherit these mismatches. This specimen demonstrates that the failure is not an isolated model quirk but a structural risk anywhere directory self-tagging exists without independent audit.

### Recommendation

AI systems answering local-business queries from directory sources should either (a) flag directory-sourced categories as unverified rather than presenting them as fact, or (b) cross-reference against a second independent signal (reviews mentioning actual products/services, shop websites, or direct confirmation) before returning a categorical claim like "verified second-hand laptop dealer."

---

*CHRONOS Evaluation Methodology v0.1 · TamilOps · Last verified 21 July 2026*
