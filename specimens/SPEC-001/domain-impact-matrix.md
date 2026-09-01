# SPEC-001 — Domain Impact Matrix

| Domain | Failure Scenario | Consequence Severity | Detection Likelihood | Mitigation Priority |
|--------|-----------------|---------------------|---------------------|---------------------|
| Academic research | Incorrect historical attribution | High | Medium | High |
| Cultural preservation | Misrepresentation of classical texts | High | Low | Critical |
| Educational content | Wrong author/date taught to students | High | Medium | High |
| AI training data | Unsupported claims enter fine-tuning corpus | Critical | Low | Critical |
| Journalism | Unverified AI output published as fact | High | Medium | High |
| Social media | Fabricated "test results" spread virally | Moderate | Low | Medium |

## Key Insight

The most dangerous failure in SPEC-001 is not the reasoning error (Finding A) but the **unsupported generated claims** (Finding B). The model fabricated a test against "three frontier AI models" and an incorrect historical date. These claims are easy to believe, hard to verify, and likely to propagate. A reasoning error is local. A fabricated claim is a virus.
