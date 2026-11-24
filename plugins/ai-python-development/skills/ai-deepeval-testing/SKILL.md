---
name: ai-deepeval-testing
description: Implement Python AI evaluation suites with DeepEval for model, retrieval, agent trajectory, conversation and end-to-end quality. Use when DeepEval is selected or being evaluated; preserve existing evaluation tools and do not introduce model calls, hosted reporting or synthetic generation without scope.
user-invocable: false
metadata:
  kind: method
  domain: ai
  phase: cross-phase
  scope: stack-specific
  invocation: both
  stack: Python, DeepEval, pytest
---

# Implement Python AI evaluations with DeepEval

Use the accepted task, quality criteria and evaluation approach. This skill owns the selected DeepEval integration in Python, not the acceptance criteria, the evaluation method or the delivery decision; those stay with the evaluation activity and the project. The runner can be Python while the evaluated application uses another language.

## Reading path

| Need | Read |
| --- | --- |
| Decide what to evaluate and what the evidence means | `ai-testing` when installed |
| Run evaluation as a program with acceptance, gates and reporting | `ai-evaluation` when installed |
| Map the evaluation decision to cases, datasets, metrics and execution | [DeepEval playbook](references/deepeval-playbook.md) |
| Wire the suite into CI and preserve result evidence | [CI and reporting](references/ci-and-reporting.md) |
| Verify application behavior and persisted outcomes | `test` when installed |
| Understand traces and execution signals | `design-system` observability guidance when available; project telemetry tooling |

## Select DeepEval or keep what exists

DeepEval is an optional runner the project selects. Choose it when the project is Python, needs model-judged quality over recorded inputs and outputs, and has no accepted evaluation route already. Keep an accepted harness unless comparison or migration is requested; a bounded deterministic check does not need a judge framework.

Skip it when deterministic assertions settle the claim, when the judge's data, credentials or budget are not authorized, or for a protocol-only service that needs compatibility checks. A missing judge leaves that quality boundary unverified, not passing.

## Pin and verify the installed release

Lock one reviewed version in the established test or development dependency group and record it with the evidence. Check imports, parameters and flags against the installed package and the release's documentation before writing code; published examples do not establish installed compatibility. Do not upgrade DeepEval, pytest, the judge model or the application model during a comparison unless the upgrade is the intervention.

Configure the evaluated application and the judge separately. Most metrics call a judge even when the application output was recorded.

## Map the decision to a representation

| The decision needs | Representation |
| --- | --- |
| Quality of one request/response or one component call | Single-turn case |
| Behavior across turns | Conversation case |
| A rerunnable, sliceable, versioned input set | Dataset |

Choose the interaction being evaluated, then populate the case from that actual execution. At application level it may be the user's request and final response; at component level, the input and output of that component. Keep one consistent case scope so the metric judges the behavior the test intends. A dataset holds one kind of case, not both.

## Choose metrics by property, keep invariants outside

Name the property before the metric: task completion and usefulness, retrieval grounding, tool or trajectory correctness, conversation outcome, format or prompt adherence, safety and policy. Cover the accepted criteria with the smallest set that observes them; a few focused metrics usually beat a broad panel.

Prefer a built-in metric whose documented requirements match the evidence collected. Use a custom rubric such as `GEval` only for a subjective criterion no built-in covers, and only with explicit evaluation steps, a named calibration basis and a recorded threshold. Inspect each metric's required fields against the installed release; a metric missing its inputs proves nothing.

Keep deterministic invariants outside the judge: authorization, isolation, required fields, schema, side effects, tool permissions and recovery are exact application assertions. A high score never compensates for a failed invariant, and a format or safety metric does not enforce the corresponding application rule.

## Execute locally, keep hosted services opt-in

Run and inspect results locally without an account or upload. Confident AI reporting, hosted datasets, traces and online evaluation are separate selected integrations with account, retention, region and data-sharing decisions; do not log in or upload cases merely to run or read a local suite.

- Bound providers, concurrency, retries, timeouts and total cases through project configuration; record usage or cost where measured and label estimates.
- Redact private content at source and in retained failure artifacts.
- Synthetic generation and conversation simulation are optional credentialed paths. Use them for a real coverage gap, review the generated cases, and keep them distinguishable from observed or curated ones.

Repair a failing candidate, not the criterion: do not weaken expected outcomes, thresholds or rubric wording to make a run green.

## CI and evidence boundary

Use the DeepEval runner, not bare pytest collection, for a committed suite, and verify exit status and result completeness. Skipped, errored, missing-parameter and flaky cases are not passes. Keep per-case evidence and the exact application, prompt, model, judge, dataset and metric revisions.

Separate fast deterministic tests from credentialed quality jobs, and run live jobs only in trusted contexts with authorized data and secrets. Read [CI and reporting](references/ci-and-reporting.md) for gate levels, invocation, artifacts and triage.

A passing metric establishes the evaluated cases and configuration. It does not establish a product journey, persisted user outcomes, protocol compatibility or production quality; report the executed levels and remaining gaps.

## Sources and fit

This is original integration guidance based on DeepEval's evaluation, metrics and CI documentation. Read the [evaluation introduction](https://deepeval.com/docs/evaluation-introduction) and [metrics](https://deepeval.com/docs/metrics-introduction) for the installed release's API. The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) were reviewed as references; their mandatory intake, synthetic-generation, hosted-service preference and fixed iteration defaults are not adopted. Exact API names, parameters and flags must be checked against the installed release.
