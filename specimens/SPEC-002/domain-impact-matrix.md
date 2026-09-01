# SPEC-002 — Domain Impact Matrix

| Domain | Failure Scenario | Consequence Severity | Detection Likelihood | Mitigation Priority |
|--------|-----------------|---------------------|---------------------|---------------------|
| Medical scheduling | Wrong appointment date | Critical | Medium | High |
| Medication timing | Wrong dosage day | Critical | Low | Critical |
| Legal filing | Missed statutory deadline | Critical | Low | Critical |
| Payroll/HR | Wrong pay period calculation | High | High | Medium |
| Recruitment | Wrong interview date | Moderate | High | Low |
| Financial trading | Wrong settlement date | High | Medium | High |
| Insurance claims | Wrong policy effective date | High | Low | High |

## Key Insight

Detection likelihood is **inversely correlated** with consequence severity in most domains. The highest-stakes errors (medication timing, legal deadlines) are also the least likely to be caught before harm occurs. This makes temporal cascade failures a **silent killer** in AI-assisted workflows.
