# CHRONOS Specimen Lifecycle and Review Gates

**Version:** 1.0  
**Status:** Proposed for review

## Lifecycle

| Stage | Required work | Exit condition |
|---|---|---|
| Draft | Define evaluation question, scope and model/environment details | Scope is explicit |
| Evidence checked | Preserve originals, log provenance, inspect relevant pages/frames and hash assets | Evidence inventory reconciles with repository |
| Fact extraction checked | Attribute every observation and source statement; add evidence locators | Material facts trace to Layer 1 |
| Analysis reviewed | Separate findings, inferences, hypotheses, alternatives and unknowns | No unsupported causal or prevalence claims |
| Reproduction status recorded | Record protocol, attempts, conditions, outputs and limitations; or state not tested | Reproducibility status is explicit |
| CI passed | Run schema, path, structure and integrity checks | Required automated checks pass |
| Human publication approval | Review accuracy, privacy, safety, permissions, attribution and claims | Named reviewer records decision |
| Published | Merge through approved repository review process | Main branch reflects approved version |

## Review checklist

### Evidence
- [ ] Original files preserved without alteration.
- [ ] Evidence log lists every evidence asset and its provenance.
- [ ] Compound evidence (PDF, video, archive) inspected at relevant locations.
- [ ] SHA-256 manifest matches the preserved evidence.
- [ ] Missing artifacts and incomplete context are explicitly disclosed.

### Facts and traceability
- [ ] Model output, user statements, external-source statements and CHRONOS verification are distinguished.
- [ ] Material facts cite an evidence path and locator.
- [ ] Quotations are exact and attributed.
- [ ] Uncertain or disputed items remain labelled as such.

### Analysis
- [ ] Observations are separated from inferences and hypotheses.
- [ ] Alternative explanations and limitations are considered.
- [ ] Root cause is not asserted beyond evidence.
- [ ] Classification and severity follow the taxonomy.
- [ ] Impact claims explain their basis and distinguish estimates from measurements.
- [ ] Recurrence, cross-model testing and reproduction are not overstated.

### Publication
- [ ] Metadata and README agree with canonical files.
- [ ] Privacy, sensitive information, copyright and publication permissions reviewed.
- [ ] No credentials, personal secrets or unnecessary personal data exposed.
- [ ] CI passed on the exact commit proposed for publication.
- [ ] Human reviewer and decision are recorded.

## Review outcomes

- **Approve:** all required controls satisfied.
- **Approve with disclosed limitations:** remaining gaps are explicit and publication is justified.
- **Return for revision:** correctable gaps remain.
- **Hold:** evidence, permission, privacy, safety or integrity issue prevents publication.

CI success never substitutes for this human review.
