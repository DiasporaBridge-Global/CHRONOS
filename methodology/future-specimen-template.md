# Future Specimen Template — SPEC-XXX

Copy this structure for a new specimen. Replace every placeholder. Do not mark `governance_status` as `standard-v1` until the review gates are complete.

```text
specimens/SPEC-XXX/
├── README.md
├── metadata.json
├── Evidence/
│   ├── [original evidence files, unchanged]
│   ├── evidence-log.md
│   └── integrity.sha256
├── facts.md
├── report.md
├── mitigation.md
├── reproduction-test.md
└── domain-impact-matrix.md   [when applicable]
```

## metadata.json governance additions

Keep all existing schema-required fields and add:

```json
{
  "governance_status": "draft",
  "evidence_provenance": {
    "captured_by": "name or unknown",
    "capture_method": "method or unknown",
    "capture_timezone": "timezone or unknown",
    "source_platform": "platform or unknown",
    "limitations": ["known evidence limitations"]
  },
  "review": {
    "evidence_review": "pending",
    "fact_review": "pending",
    "analysis_review": "pending",
    "reproduction_status": "not-tested",
    "publication_decision": "not-approved"
  }
}
```

Allowed governance status values: `draft`, `legacy-review`, `standard-v1`. Use `standard-v1` only after all applicable review requirements are complete.

## README.md
- Specimen ID and title
- One-paragraph evidence-bounded summary
- Model/provider/version (unknown if not recorded)
- Incident date and environment
- Failure classification and taxonomy code
- Links to evidence log, facts, report, mitigation and reproduction record
- Current review/publication status

## Evidence/evidence-log.md
List each original artifact, its original filename, type, source/collector, capture time and timezone (or unknown), relevant page/frame/time range, description and limitations. Distinguish original evidence from derived/transcribed material.

## Evidence/integrity.sha256
Use standard SHA-256 format: 64 hexadecimal characters, two spaces, then specimen-root-relative path. Include each preserved evidence asset; do not include the manifest itself.

## facts.md
For each material fact, include:
- Fact ID
- Exact observation or attributed source statement
- Evidence path and locator
- Attribution class: direct-observation, source-reported, independently-verified, inference, hypothesis, or unknown/disputed
- Confidence/limitations, where applicable

Do not include causal interpretation in this layer.

## report.md
Include: question/objective; context and environment; observed sequence; findings linked to Fact IDs; analysis and alternative explanations; failure classification; impact rationale; limitations; reproduction status; conclusion and recommendations.

## mitigation.md
State prevention, detection and recovery recommendations. Label recommendations as CHRONOS proposals, not as observed facts.

## reproduction-test.md
Record protocol, model/version, prompt/setup, number of attempts, dates, outputs, pass/fail criteria and limitations. If not tested, state that plainly and explain what would be required.

## domain-impact-matrix.md
Use when the specimen makes domain or harm claims. Separate plausible exposure from observed harm and measured impact.
