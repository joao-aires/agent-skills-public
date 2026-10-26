---
name: ai-testing
description: Design and assess AI testing and evaluation across components, retrieval, agent trajectories, conversations, protocols and product journeys. Use for quality criteria, datasets, graders, regression gates and evaluation evidence independently of an implementation library or application language.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Test AI behavior at the relevant boundaries

Start from the accepted user task, architecture and consequential failure modes. This method owns what to evaluate and what the evidence means; it does not select an evaluation SDK, require a model for a protocol-only service or authorize live calls and data publication. Reuse sufficient existing criteria and tests rather than restarting evaluation design for every change.

## Define acceptance and evidence levels

| Property | Acceptance method |
| --- | --- |
| Deterministic invariants | Assert authorization, resource isolation, schema validity, side effects and recovery in the application, even when a model judge scores the answer highly. |
| Uncertain model quality | Define task-specific criteria for grounding, ambiguity, refusal and relevant safety constraints; choose suitable measures and graders. |

State provisional thresholds and uncertainty when acceptance is unresolved; do not invent product commitments.

Read [evaluation methods](references/evaluation-references.md) when choosing levels, cases or graders. Assess model/retrieval components, protocol/runtime integration, agent trajectories, conversations, multimodal interaction and complete user journeys where the architecture needs them. Use actual compatible peers and persistent service state for integration and outcome claims. A component score, simulated user or recorded output establishes a narrower boundary than a live end-to-end interaction.

## Build representative cases and suitable measures

### Select cases

Derive cases from the task the application promises to perform. Include inputs on which different implementations could make consequentially different choices, and specify what would make each result useful or unacceptable. A case should reveal something about the capability; a large collection of interchangeable easy prompts can give a high score while leaving the difficult behavior unexamined.

Use meaningful user/data slices and privacy-reviewed observed failures to identify variation. Keep cases used while developing the behavior separate from held-out cases used to assess whether the improvement generalizes.

- Cover normal tasks, ambiguity, missing/conflicting evidence, invalid input, provider/tool failure and relevant adversarial conditions.
- Keep inputs, expected outcomes/rubrics and actual results distinct.
- Preserve versioned datasets and useful held-out regressions; synthetic generation is an optional source requiring review, not a replacement for task evidence.

### Select measures

Choose a measure that can observe the property in question:

| Property | Suitable assessment |
| --- | --- |
| A fact the application can determine, such as allowed access or a required field | Exact assertions. |
| An answer that admits several valid wordings | Reference-based or semantic measures appropriate to the task. |
| A task with an established quality definition | Its domain-specific metrics. |
| Usefulness or taste that a grader cannot yet assess reliably | Human assessment. |

When using a model judge, define the criteria it should apply and compare its judgments with accepted human assessments, including borderline and unacceptable results. Inspect disagreement before relying on an aggregate score. A fluent explanation from a judge is not evidence that its decision is calibrated.

- Separate retrieval quality from answer usefulness and task outcome from optional implementation details such as tool order.
- Calibrate subjective judges against accepted human examples, preserve disagreement and use human review where the decision remains subjective.
- Keep expected results, thresholds and rubrics stable while repairing behavior.

### Compare candidates

Record the evaluated application/model/prompt/context/tool configuration and dataset/evaluator revisions.

- Compare candidates on the same relevant inputs and execution conditions.
- Retain denominators, case-level failures, important slice results, sample size and appropriate variability; repeat stochastic cases enough for the decision.
- An average must not hide failed authority or consequential task criteria.
- Include latency and usage/cost when they affect acceptance, with unavailable or estimated values labelled.

Choose the comparison's denominator from the promised outcome. Include failed attempts and recovery when accounting for time and resources; an optimization must retain accepted quality and behavior.

Change candidates under comparable conditions and separate interventions enough to support the conclusion. Record confounding factors when they cannot be controlled. A few runs can reveal a defect or justify another experiment without establishing a reliability rate or causal explanation.

## Implement and run proportionate checks

Seek available expertise for the selected evaluator, test drivers and runtime; without it, use project evidence and primary documentation while retaining the same criteria. A Python evaluator can test a non-Python application. No SDK, hosted dataset service, dashboard or particular record format is required by this method.

Keep cheap deterministic checks routinely runnable.

- Use bounded quality experiments during behavior changes, broader held-out comparisons for consequential model/prompt/retrieval/tool changes and authorized online sampling for operating feedback.
- Define when each level runs and which conditions gate delivery rather than requiring every expensive suite on every commit.
- Protect credentials, evaluation inputs and resulting artifacts in trusted execution contexts.

Report execution failures, skips, missing access and incomplete cases explicitly. Recorded application outputs may still require live judge calls; fixtures, simulated users, live providers and production samples have different permissions and evidence. Do not turn an unavailable judge or unexecuted suite into a pass. A passing evaluation does not replace protocol compatibility, accessibility, authorization or persisted journey checks.

## Close the learning loop

Inspect failures against the agreed criteria and make scoped changes, then rerun affected checks without tuning only to development examples. Turn useful observed failures into privacy-preserving regression cases. Operational telemetry can explain execution and identify candidate cases; scoring usefulness remains a separate activity even when the same platform supports both.

Return the evaluation approach, versioned cases/measures, actual results and unresolved limits at the requested scope. Update the existing verification/decision record as behavior or accepted criteria change. Quality evidence supports a release decision; it does not independently grant permission to deploy or make external changes.
