# SPEC-003 — Fact Extraction

## Source Record

| Field | Value |
|---|---|
| Preserved source | `Evidence/Laptop dealers.pdf` (two pages) |
| Incident date recorded in source | June 4, 2026 |
| Screenshot time recorded in source | 13:53 IST |
| AI tool identified in source | Gemini Pro |
| Task described in source | Search for second-hand laptop dealers in Karaikudi, Tamil Nadu |
| Directory identified in source | Justdial |
| Prepared by | Sirajudeen Seethapathy, TamilOps |

This extraction distinguishes what the preserved PDF states from what its embedded screenshot visibly records. The PDF is the source document; it is not independent corroboration of every underlying business claim.

## 1. Statements Recorded on PDF Page 1

Page 1 states that Gemini Pro used the Justdial business directory and returned businesses under the category "Second Hand Laptop Dealers" in Karaikudi. It specifically names Kims Computers and Playback Computers as listings presented by the AI as verified second-hand laptop dealers.

The page's verification table records the following descriptions:

| Shop name | Justdial listing recorded in PDF | Business description recorded in PDF |
|---|---|---|
| Kims Computers | Second Hand Laptop Dealer | Sells spare parts (chargers, screens) and provides repair services |
| Uniqon | Second Hand Laptop Dealer | Sells brand-new HP laptops and high-end assembled PCs |
| Playback Computers | Second Hand Laptop Dealer | Service shop, not a laptop reseller |

**Evidence boundary:** These are claims made in the prepared PDF. The preserved PDF does not include separate shop-catalogue records, dated business confirmations, directory-page captures, or other underlying verification materials. Accordingly, this extraction does not independently certify the businesses' inventory or operations.

## 2. Screenshot Evidence — PDF Page 2

The second page contains the Gemini Pro response screenshot. The page heading identifies it as an evidence screenshot and records June 4, 2026, 13:53 IST.

The visible response:
- apologizes for the earlier information;
- says it relied on business directories such as Justdial;
- names Kims Computers and Playback Computers in connection with the directory category;
- describes Kims Computers as selling small spare parts alongside repair services;
- describes Uniqon as selling brand-new HP laptops and high-end assembled PCs; and
- discusses use of the "second-hand" tag to attract customers.

The screenshot is direct evidence of what the displayed Gemini response said. It is not independent proof that the business descriptions, directory practices, or attributed motives were accurate.

The screenshot is embedded in the preserved PDF. A separate PNG named `gemini-pro-response-2026-06-04.png` is not present in the repository.

## 3. Root-Cause Statement in the Source

Page 1 asserts that Justdial allows businesses to self-tag listings with category keywords that may not reflect actual inventory, and that shops use the second-hand laptop tag to attract footfall.

This is the source document's proposed explanation. The preserved material does not include a Justdial policy or platform record establishing the self-tagging mechanism, nor independent evidence establishing the motives attributed to the businesses. Treat this explanation as a hypothesis recorded in the source, not as a verified root cause.

## 4. Classification and Impact

The source document labels the incident a directory verification failure and describes its outcome as hallucinated listings or shops misclassified as laptop dealers.

- **Failure classification:** Directory-sourced misclassification / source-data verification failure (working classification based on this specimen).
- **Operational impact:** The source does not quantify actual customer travel, financial loss, or other realized impact. Any severity assessment remains an evaluation, not a measured outcome.
- **Reproduction:** No reproduction test is documented in the preserved PDF.

## 5. Evidence Boundary Summary

| Proposition | What the preserved material supports |
|---|---|
| Gemini response acknowledged an error | Visible in the embedded screenshot on page 2 |
| Gemini referred to Justdial | Visible in the screenshot and described on page 1 |
| The PDF records three business/category mismatches | Yes, in its page-1 table |
| The underlying business descriptions were independently verified | Not independently demonstrated by the preserved PDF |
| Justdial's self-tagging policy caused the incident | Not established; proposed explanation in the PDF |
| Businesses deliberately misused tags to attract customers | Not established; motive asserted in the PDF |
| The incident is recurring or cross-model | Not established by this specimen |

The independent CHRONOS interpretation and any recommendations belong in `report.md`; they must not be represented as direct statements from the source evidence.
