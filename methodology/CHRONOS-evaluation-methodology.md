# CHRONOS Evaluation Methodology

**Document status:** Methodology overview for the four-specimen closed archive  
**Version:** 1.0  
**Project:** CHRONOS — TamilOps  
**Project Owner:** Sirajudeen Seethapathy

---

## 1. Purpose

CHRONOS is an evidence-led framework for examining, documenting, classifying, and communicating observable failures and reliability weaknesses in AI systems.

It is designed to move beyond an isolated statement that an AI system was "wrong". A CHRONOS evaluation records the conditions under which behaviour occurred, preserves the available evidence, separates directly observed facts from interpretation, checks claims against an appropriate reference, and reports limitations alongside conclusions.

The repository is a research and methodology archive. Its four existing specimens demonstrate selected applications of this approach; they do not establish universal failure rates or prove that every AI system exhibits the same behaviour.

## 2. What CHRONOS examines

The four archived specimens illustrate these evaluation areas:

| Evaluation area | What is examined | Archived example |
|---|---|---|
| Multilingual and contextual reasoning | Whether the system reaches a supported answer when linguistic, cultural, or contextual reasoning is required | SPEC-001 |
| Temporal consistency and correction | Whether dates and related facts remain consistent, including during correction | SPEC-002 |
| Source reliability and factual verification | Whether retrieved directory information is independently checked before being presented as verified | SPEC-003 |
| Workflow and state management | Whether the system recognises a change in platform or workflow state and avoids unnecessary duplication | SPEC-004 |

These are demonstrated areas, not an exhaustive list of all possible CHRONOS evaluation domains.

## 3. Evaluation lifecycle

A professional CHRONOS evaluation should document the following stages. The depth of each stage depends on the agreed scope, access to the system, available evidence, and the risk of the use case.

### Stage 1 — Define the evaluation

Record the evaluation objective, question, intended use, system under examination, relevant users or stakeholders, scope boundaries, and exclusions.

State what behaviour would count as success, failure, partial success, or an inconclusive result before interpreting the outcome wherever practicable.

### Stage 2 — Record the test environment

Record, where available:

- AI provider and product;
- model name and exact version or the fact that it is unconfirmed;
- interface, platform, and access method;
- evaluation date, time, and timezone;
- relevant settings, tools, files, and external sources;
- prompt and conversation context needed to understand the test.

Do not imply that an unobserved setting or model version is known. Mark unavailable information as unknown.

### Stage 3 — Establish test conditions

Preserve the prompt, task, inputs, expected behaviour, reference information, and any relevant preconditions.

Identify the source used as ground truth and why it is appropriate. Where a reliable reference cannot be established, state that limitation and do not present the disputed point as independently verified.

### Stage 4 — Execute and preserve

Run the evaluation within the defined scope. Preserve original screenshots, logs, traces, outputs, and relevant source documents.

Record deviations, user interventions, retries, corrections, and any changes to the test conditions. Do not silently omit failed attempts or inconvenient outputs.

### Stage 5 — Extract facts

Create a structured account of what the evidence directly shows. Keep this layer descriptive: record what was said or done, in sequence, with references to the source evidence.

Do not place causal explanations, inferred intent, or broader generalisations in the fact-extraction layer.

### Stage 6 — Analyse and classify

Compare the extracted facts with the stated objective, expected behaviour, and reference information.

Identify the observed failure mechanism and assign a taxonomy classification where an existing code is applicable. Distinguish:
- direct observations;
- independently verified facts;
- evaluator interpretations;
- hypotheses about causes;
- unresolved questions.

A model's explanation or admission is evidence of what the model said; it is not, by itself, proof that the explanation is correct.

### Stage 7 — Verify and challenge the finding

Use independent reference checks where possible. Consider plausible alternative explanations and identify evidence that could weaken the proposed interpretation.

Where appropriate and feasible, attempt a controlled reproduction or counter-test. Record the exact conditions and outcomes. A single successful reproduction does not establish a universal rate; a failed reproduction does not automatically invalidate the original preserved observation.

If reproduction was not attempted, was not possible, or was inconclusive, say so explicitly.

### Stage 8 — Assess impact and limitations

Describe the observed impact in the tested context. Separate that impact from potential consequences in other contexts.

Severity must be justified by stated criteria and evidence. Do not label a hypothetical consequence as an observed harm. Record limitations such as incomplete context, unknown model version, limited trials, unavailable logs, or reliance on a single source.

### Stage 9 — Report

Produce a report that allows a reader to trace each material conclusion to extracted facts and then to original evidence.

Include the objective, environment, test conditions, sequence, findings, classification, verification, impact, alternative explanations, limitations, and practical recommendations where supported.

## 4. Evidence architecture and traceability

CHRONOS uses a three-layer evidence model:

| Layer | Role | What belongs here |
|---|---|---|
| Layer 1 — Source evidence | Preserve the original record | Screenshots, logs, traces, source documents and integrity records |
| Layer 2 — Fact extraction | Describe what the source evidence establishes | Structured facts, sequence, timestamps and evidence references |
| Layer 3 — Analysis and reporting | Interpret and communicate findings | Classification, analysis, impact, limitations and conclusions |

**Traceability rule:** material claims in the report must link to facts; those facts must link to identifiable source evidence.

The [Evidence Handling Protocol](evidence-handling-protocol.md) defines preservation, evidence logs, integrity checks, and cross-layer references. The [Specimen Structure Standard](specimen-structure-standard.md) defines the structure used when maintaining the four archived specimens.

## 5. Reproducibility and measurement

CHRONOS distinguishes an evidence-backed observation from a repeatable result.

For each evaluation, report the number of trials actually conducted, the number of observed outcomes in each relevant category, and the conditions held constant or changed. If only one interaction was examined, identify it as a single observed session; do not imply statistical reliability.

For repeated trials, document at minimum:

- the test prompt or procedure and any permitted variations;
- the model and environment identifiers available;
- the number of attempts;
- the outcome of each attempt;
- whether the same failure mechanism recurred;
- any human intervention, correction, or external tool use;
- deviations and missing observations.

Use descriptive measures appropriate to the test, such as observed occurrence count, correction attempts required, task completion outcome, or agreement with a specified reference. Define the denominator and counting rule whenever reporting a rate.

Do not combine unlike tasks, models, environments, or test conditions into a single score without a justified and documented method. Do not present a severity label as a statistical confidence measure. Where the sample is small or non-random, state that results are descriptive and cannot support population-wide failure-rate claims.

A reproduction record should distinguish:
1. exact or near-exact reproduction;
2. partial reproduction;
3. non-reproduction under the attempted conditions;
4. not attempted or not feasible.

These labels describe the reproduction attempt, not the truth or falsity of the original evidence.

## 6. Classification and severity

The [Failure Classification Taxonomy](failure-classification-taxonomy.md) provides the codes currently used by the four archived specimens.

Classification describes the observed failure category. Severity describes the potential or observed significance under stated criteria. They are not interchangeable.

For every severity judgement, identify the tested context, evidence supporting the judgement, and whether the impact was observed or hypothetical. Where the current taxonomy's severity levels are used, explain the basis for the selected level and note any uncertainty.

## 7. Expected evaluation outputs

A scoped CHRONOS evaluation may produce the following outputs, depending on the engagement and available evidence:

- evaluation scope and test objective;
- system and environment record;
- test procedure and preserved interaction evidence;
- evidence inventory and integrity information, where applicable;
- structured fact extraction;
- failure analysis and taxonomy classification;
- verification and reproduction results;
- impact assessment, limitations, and uncertainty;
- final report with traceable findings;
- practical mitigation or monitoring recommendations where supported.

The precise deliverables must be agreed before an evaluation begins. CHRONOS does not claim certification, regulatory approval, or a universal benchmark score through this repository.

## 8. Professional value

The intended value of CHRONOS is a disciplined, reviewable account of how an AI system behaved under defined conditions—not simply a collection of screenshots or a list of errors.

For AI developers, product teams, and organisations, this approach can help:
- identify failure mechanisms that ordinary demonstrations may not expose;
- understand whether an output was unsupported, incorrectly sourced, inconsistent, or operationally disruptive;
- inspect the evidence and reasoning behind an evaluation conclusion;
- distinguish a one-off observation from a repeated result;
- prioritise further testing, safeguards, or workflow changes.

The four public specimens are examples of the method in use. They are not a claim that all service capabilities have already been validated across every model, domain, or risk category.

## 9. Limitations and integrity principles

CHRONOS findings are bounded by the evidence and conditions recorded in each evaluation. Model versions may be unavailable; interfaces may change; results may vary across sessions; and access to internal system state may be limited.

CHRONOS therefore commits to:
- preserve original evidence and disclose relevant gaps;
- distinguish fact, inference, hypothesis, and recommendation;
- avoid claims broader than the tested conditions support;
- disclose failed, partial, and inconclusive reproduction attempts;
- identify third-party material and respect its rights;
- report limitations and alternative explanations.

## 10. Relationship to the four-specimen archive

The GitHub specimen archive is closed and final at exactly SPEC-001, SPEC-002, SPEC-003, and SPEC-004. This methodology document explains and connects the framework demonstrated by those four records. It does not authorise or propose additional specimens.

Corrections and maintenance to the four existing specimens and improvements to methodology or repository documentation may be considered under the repository's contribution and ownership policies.

---

*CHRONOS Evaluation Methodology v1.0 · TamilOps*
