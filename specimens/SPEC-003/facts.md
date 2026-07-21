# SPEC-003 — Fact Extraction

## Field Detail

| Field | Value |
|---|---|
| Date | June 4, 2026 |
| Time | 13:53 IST |
| AI Tool | Gemini Pro |
| Task | Search for second-hand laptop dealers in Karaikudi, Tamil Nadu |
| Data Source Used by AI | Justdial business directory |
| Outcome | Hallucinated listings — shops misclassified as laptop dealers |
| Prepared By | Sirajudeen Seethapathy, TamilOps — Solo SME Vendor, Tamil AI Data |

## What the AI Returned

Gemini Pro pulled shop names from Justdial under the category "Second Hand Laptop Dealers" in Karaikudi, including Kims Computers and Playback Computers, and presented these as verified second-hand laptop dealers.

## Verification Table

| Shop Name | Justdial Listing | Actual Business |
|---|---|---|
| Kims Computers | Second Hand Laptop Dealer | Sells only spare parts (chargers, screens) + repair services |
| Uniqon | Second Hand Laptop Dealer | Exclusively sells brand-new HP laptops and high-end assembled PCs |
| Playback Computers | Second Hand Laptop Dealer | Service shop — not a laptop reseller |

## Root Cause

Justdial allows businesses to self-tag listings with any category keyword, independent of actual inventory. Shops apply the "second-hand laptop" tag to attract footfall, then convert visitors to new-product sales. AI models that search or train on these directories inherit the mistagging as fact.

## Model's Self-Admission (as stated, not treated as validated general claim)

On being challenged with verified data, Gemini Pro acknowledged the error, named the specific shops, and confirmed the mismatch between the directory listings and each shop's actual operations.

## Classification

- **Failure Type:** Directory-Sourced Hallucination / Source Data Contamination
- **Operational Impact:** Moderate–High
- **Correction Trigger:** Required direct human/SME verification against actual shop inventory — not resolved by the AI independently
- 
