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

Separate deterministic invariants from uncertain model quality. Authorization, resource isolation, schema validity, side effects and recovery need application assertions even when a model judge gives an answer a high score. Define useful quality criteria for the task, including grounding, ambiguity, refusal and relevant safety constraints. State provisional thresholds and their uncertainty when acceptance is unresolved; do not invent product commitments.

Read [evaluation methods](references/evaluation-references.md) when choosing levels, cases or graders. Assess model/retrieval components, protocol/runtime integration, agent trajectories, conversations, multimodal interaction and complete user journeys where the architecture needs them. Use actual compatible peers and persistent service state for integration and outcome claims. A component score, simulated user or recorded output establishes a narrower boundary than a live end-to-end interaction.

## Build representative cases and suitable measures

Derive cases from accepted behavior, meaningful user/data slices and privacy-reviewed observed failures. Cover normal tasks, ambiguity, missing/conflicting evidence, invalid input, provider/tool failure and relevant adversarial conditions. Keep inputs, expected outcomes/rubrics and actual results distinct. Preserve versioned datasets and useful held-out regressions; synthetic generation is an optional source requiring review, not a replacement for task evidence.

Choose exact assertions, reference-based or semantic measures, domain-specific metrics, calibrated model judges and human assessment according to the property. Separate retrieval quality from answer usefulness and task outcome from optional implementation details such as tool order. Calibrate subjective judges against accepted human examples, preserve disagreement and use human review where the decision remains subjective. Keep expected results, thresholds and rubrics stable while repairing behavior.

Record the evaluated application/model/prompt/context/tool configuration and dataset/evaluator revisions. Compare candidates on the same relevant inputs and execution conditions. Retain denominators, case-level failures, important slice results, sample size and appropriate variability; repeat stochastic cases enough for the decision. An average must not hide failed authority or consequential task criteria. Include latency and usage/cost when they affect acceptance, with unavailable or estimated values labelled.

## Implement and run proportionate checks

Seek available expertise for the selected evaluator, test drivers and runtime; without it, use project evidence and primary documentation while retaining the same criteria. A Python evaluator can test a non-Python application. No SDK, hosted dataset service, dashboard or particular record format is required by this method.

Keep cheap deterministic checks routinely runnable. Use bounded quality experiments during behavior changes, broader held-out comparisons for consequential model/prompt/retrieval/tool changes and authorized online sampling for operating feedback. Define when each level runs and which conditions gate delivery rather than requiring every expensive suite on every commit. Protect credentials, evaluation inputs and resulting artifacts in trusted execution contexts.

Report execution failures, skips, missing access and incomplete cases explicitly. Recorded application outputs may still require live judge calls; fixtures, simulated users, live providers and production samples have different permissions and evidence. Do not turn an unavailable judge or unexecuted suite into a pass. A passing evaluation does not replace protocol compatibility, accessibility, authorization or persisted journey checks.

## Close the learning loop

Inspect failures against the agreed criteria and make scoped changes, then rerun affected checks without tuning only to development examples. Turn useful observed failures into privacy-preserving regression cases. Operational telemetry can explain execution and identify candidate cases; scoring usefulness remains a separate activity even when the same platform supports both.

Return the evaluation approach, versioned cases/measures, actual results and unresolved limits at the requested scope. Update the existing verification/decision record as behavior or accepted criteria change. Quality evidence supports a release decision; it does not independently grant permission to deploy or make external changes.
