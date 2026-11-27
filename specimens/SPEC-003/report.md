# SPEC-003 — Full Evaluation Report

## Business Directory Hallucination: Justdial Listing Verification Failure

### 1. Summary

The preserved two-page source PDF records a June 4, 2026 incident in which Gemini Pro was asked to find second-hand laptop dealers in Karaikudi, Tamil Nadu. The PDF says the model used the Justdial business directory and presented businesses listed under the category "Second Hand Laptop Dealers" as verified dealers.

The PDF's page-1 table records mismatches between that directory category and the businesses' described operations. Page 2 contains a screenshot of a Gemini Pro response acknowledging an error and discussing its reliance on directory information.

This specimen supports a documented case of directory-category information being repeated as a categorical business claim without adequate verification being demonstrated in the preserved record. The underlying business descriptions and the proposed explanation for the directory mismatch are claims in the prepared PDF; the preserved archive does not include the underlying business records needed to independently validate them.

### 2. Evidence Reviewed

The primary preserved artifact is `Evidence/Laptop dealers.pdf`.

- **Page 1** records the task, identifies Justdial as the data source, lists three business/category mismatches, and states a proposed root cause.
- **Page 2** contains the Gemini Pro response screenshot, labelled as captured on June 4, 2026 at 13:53 IST.
- The screenshot is embedded in the PDF. No separate PNG is present in the repository.

The page-2 screenshot visibly shows Gemini apologizing, referring to its reliance on business directories such as Justdial, naming Kims Computers and Playback Computers, and describing business/category mismatches. It is evidence of the displayed model response, not independent verification of the businesses' actual operations.

### 3. Source-Recorded Findings

The PDF's verification table records:

| Shop name | Directory category recorded in PDF | Business description recorded in PDF |
|---|---|---|
| Kims Computers | Second Hand Laptop Dealer | Spare parts (chargers, screens) and repair services |
| Uniqon | Second Hand Laptop Dealer | Brand-new HP laptops and high-end assembled PCs |
| Playback Computers | Second Hand Laptop Dealer | Service shop, not a laptop reseller |

These descriptions are attributed to the source PDF. No separate shop catalogues, dated confirmations, directory captures, or other underlying verification records are included in the preserved evidence reviewed for this report. The report therefore does not present the descriptions as independently re-established facts.

### 4. Model Response and Failure Analysis

The page-2 screenshot records Gemini acknowledging that it had relied on directory information and apologizing for the resulting error. The screenshot also shows the model discussing the mismatch between the category and the businesses it names.

The failure evidenced here is not simply that a business name was invented. The source record describes the model returning real business names under a directory category and presenting the category as a verified description of the businesses. The evidence supports examining the model's treatment of directory metadata as an unverified source signal.

The preserved material does not establish the model's internal retrieval process, whether it independently consulted any other source, or the exact wording of the original user query and initial answer beyond the summary in the PDF.

### 5. Root-Cause Assessment

The source PDF proposes that Justdial permits businesses to self-tag with categories that may not match their inventory, and that businesses use the second-hand laptop category to attract footfall.

That explanation is **not independently established** by the preserved evidence. No Justdial policy, listing-history record, business-owner statement, or other independent material is included to demonstrate the platform's tagging rules or the motives attributed to the businesses.

The defensible finding is narrower: the source record describes a mismatch between a directory category and the businesses' reported operations, and the embedded Gemini response acknowledges reliance on directory information. The precise cause of the mismatch remains unverified.

### 6. Failure Classification and Impact

**Working category:** Directory-sourced business misclassification / source-data verification failure.

**Operational impact:** The source PDF assigns a "Moderate–High" assessment. The preserved evidence does not quantify actual customer journeys, time lost, financial loss, or other realized harm. The rating should therefore be understood as an assessment in the source record, not a measured impact.

**Reproducibility:** No reproduction test is documented in the preserved PDF. This specimen does not establish repeatability, recurrence, or cross-model behaviour.

### 7. Relevance to Tamil Local-Business Data Quality

This case raises a practical data-quality concern: a directory category may not, by itself, establish that a business currently provides the listed product or service. An AI system that repeats such a category as a verified business fact can pass an unverified classification to the user.

The specimen documents one reported incident. It does not establish the prevalence of this problem across Justdial, Tamil Nadu, India, other directories, or AI systems generally. Broader prevalence claims require additional independently documented specimens or external verification.

### 8. Recommendations

For local-business answers based on directory data:

1. Identify directory categories as directory-supplied information, not independent confirmation of current inventory or services.
2. Avoid describing a business as a verified provider unless an independent, relevant verification signal supports that description.
3. Where confirmation is unavailable, state the uncertainty and recommend direct confirmation with the business.
4. Preserve the source used, the time of retrieval, and any independent corroboration so that later reviewers can distinguish model output from verified business facts.

These are CHRONOS recommendations derived from the evidence boundary and failure analysis. They are not presented as statements made by Gemini.

### 9. Conclusion

The preserved PDF documents a Gemini Pro response that acknowledged reliance on Justdial directory information after a reported mismatch between listed categories and business operations. The screenshot on page 2 is present within the PDF and is direct evidence of the displayed response.

The specimen supports a focused finding about presenting directory-category information as verified business information without demonstrated independent checking. It does not, by itself, prove deliberate business mis-tagging, Justdial's precise tagging policy, systemic prevalence, actual quantified harm, or reproducibility.

---

*CHRONOS Evaluation Methodology v0.2 · TamilOps · Evidence-boundary review: 27 November 2026*
