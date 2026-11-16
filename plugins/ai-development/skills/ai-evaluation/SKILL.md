---
name: ai-evaluation
description: Plan, run and report a program-level AI evaluation for a change, release or product claim. Use for acceptance criteria, dataset and slice governance, grader choice and calibration, baselines, experiments, CI gates, production sampling, regression and red-team coverage, and the evidence behind a go/no-go recommendation.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: technical
  domain: ai
  phase: cross-phase
  scope: generic
  invocation: both
  role: task
---

# Evaluate AI behavior as a program

Use this activity when a decision needs evaluation evidence across several cases, changes or operating conditions, rather than one bounded check. It owns the evaluation program: the decision and claim, acceptance, dataset and slice governance, graders, baseline and experiment, gates, production sampling, reporting and authority.

It composes [AI testing](../ai-testing/SKILL.md) for what to evaluate and what the evidence means, `ai-deepeval-testing` when that Python implementation is selected, `test` for application verification, `observability` for execution signals and `release` for the delivery decision. This skill does not own the evaluation method, the selected runner or the deployment.

| Field | This activity |
| --- | --- |
| Intent | Support a named decision with evaluation evidence that is proportionate to its consequence. |
| Output | An evaluation plan or result: claim, criteria, dataset/slices, graders, baseline, comparison, gate evidence and remaining limits. |
| Stopping point | Evaluation plan/results and a decision recommendation. Not merge, deployment, publication or live mutation. |
| Authority | Run evaluations only with authorized data, providers, credentials and budget. The decision owner accepts the result; `release` owns delivery. |

## Frame the decision and claim

Identify who will act on the result, what changes if they do, and what a wrong answer would cost. A go/no-go recommendation, a model or prompt choice, a safety claim and a monitoring decision need different evidence.

State the claim as a bounded sentence: candidate, criteria, population and revision. For example, "candidate prompt P2 meets the accepted grounding and task-completion criteria on the held-out support slices at revision R." Distinguish:

- a component claim from a product-journey claim;
- an offline comparison from operating evidence;
- an observed difference from a causal explanation.

Use the narrowest claim that still supports the decision. Widen it only with evidence that covers the wider population or boundary. If the request uses causal language such as "improved" or "safer," design a comparison that can separate the intervention from other changes; otherwise report an observation.

## Agree acceptance and evidence authority

Derive criteria from the promised task and consequential failure modes, not from an available metric. Separate deterministic invariants from uncertain quality:

| Property | Acceptance |
| --- | --- |
| Authorization, isolation, schema, persisted side effects, required fields | Exact application assertions, independent of a model judge. |
| Grounding, completeness, ambiguity handling, refusal, usefulness | Task-specific criteria and a suitable measure or calibrated grader. |
| Subjective quality that remains contested | Named human reviewer or accepted rubric. |

Set thresholds, must-pass criteria, slice minimums and the comparison baseline before seeing candidate results. Label provisional targets and their uncertainty rather than inventing a product commitment. An aggregate score cannot compensate for a failed authority, safety or factual criterion.

Record who may accept a result, and on what evidence. A fluent grader explanation, a green dashboard or the evaluating agent's self-rating is not acceptance. Unresolved subjective questions remain with the decision owner.

## Govern datasets, slices and holdouts

Treat the evaluation dataset as a versioned asset with provenance, permission and an owner. Keep inputs, expected outcomes or rubrics, and actual execution results distinct. Give cases stable identities so a failure can be traced across runs.

- Select cases from the promised task and observed failures, including normal, ambiguous, missing or conflicting evidence, malformed input, provider/tool failure and relevant adversarial conditions.
- Define meaningful slices before running: user or data population, risk, language, modality, tenant, input length or journey. Include rare consequential slices that an average would hide.
- Keep development cases separate from held-out cases used to judge generalization. Limit holdout access and do not tune prompts, thresholds or graders against it.
- Balance positive and negative cases. A one-sided set rewards a shortcut such as always escalating, always refusing or always using a tool.
- Use authorized production samples with a stated sampling frame and privacy boundary. Review synthetic or simulated cases for task fit before treating them as evidence.

Read [evaluation program mechanics](../ai-testing/references/evaluation-program.md) for dataset versioning, slice selection, denominator and evidence-level detail.

## Choose and calibrate graders

Choose the cheapest grader that can observe the property:

1. Deterministic assertions for facts, format, authority and persisted effects.
2. Reference-based or semantic measures when several outputs can satisfy the task.
3. A model judge for a defined rubric that cannot be reduced to a deterministic check.
4. Human review where the judgment remains subjective or consequential disagreement persists.

For a model judge, write the criteria, evaluation steps or score bands it must apply. Calibrate it against accepted human assessments that include borderline and unacceptable results, then inspect disagreements rather than relying on an aggregate agreement number. Record the judge model, prompt, parameters and revision; recalibrate after a judge change. Check that the judge cannot be satisfied by a shortcut, leaked answer or superficial format.

Use one grader for one property. A judge may assess answer quality; it does not establish authorization, persistence or protocol compatibility. When a deterministic check and a judge disagree, investigate the boundary before choosing the convenient result.

## Establish the baseline, experiment and comparison

Record the evaluated application, model/provider, prompt, retrieval/context, tool and runtime configuration, together with dataset, grader and judge revisions. Compare candidates on the same relevant inputs and execution conditions.

- Repeat stochastic cases enough for the decision and report variability, not only a best run.
- Change one material intervention at a time where possible. Use paired or interleaved runs, and record confounders that cannot be controlled.
- Inspect case-level failures and important slices alongside the aggregate.
- Include latency and usage/cost with the denominator that matches the promised outcome. Include failed and retried attempts when accounting for cost or end-to-end time.
- Pre-register the comparison and stopping rule. Do not stop early because the current result is favorable, and do not turn a small sample into a reliability claim.

## Run CI gates, sample production and cover failure

Choose when each evidence level runs instead of requiring every expensive suite on every change:

| Level | Typical use | Limit |
| --- | --- | --- |
| Deterministic checks | Every change and pull request | No claim about model quality. |
| Bounded quality experiment | Prompt, model, retrieval or tool change | Narrow cases and configuration. |
| Broad held-out comparison | Consequential release or provider change | Only the evaluated population and conditions. |
| Authorized production sampling | Operating feedback, drift and new failures | Sampled and biased by traffic; not complete coverage. |

Define which suites gate delivery, which are advisory, their time and cost budget, and what happens when credentials, judges or data are unavailable. Missing access leaves the boundary unverified, not passing.

Production sampling needs an accepted purpose, privacy review, retention and deletion rules. Compare slices with an identifiable baseline, account for changed traffic and sampling, and promote useful failures into privacy-preserving regression cases. Operating scores describe the observed population; they do not replace held-out release evidence.

Cover failure and adversarial behavior deliberately: ambiguity, missing or conflicting evidence, invalid input, provider/tool failure, prompt injection, data exfiltration, authority bypass, unsafe tool use, harmful content, refusal and over-refusal. Test both "should" and "should not" behavior, assign severity and an acceptable response, and run adversarial work in a bounded environment that cannot cause the harm being tested. A red-team tool or fixed attack list is optional; coverage of the accepted threat model is not.

## Diagnose, report and decide

Inspect representative failures and transcripts before interpreting scores. Classify the likely cause: dataset or expected outcome, grader or judge, harness or environment, application behavior, model/provider behavior or missing evidence. Repair the cause, rerun the affected checks and preserve the useful case as a regression.

Keep an eval-driven loop: observe a failure, add a representative case, make a scoped change, compare against the baseline and check held-out behavior. Do not weaken criteria, thresholds, holdouts or grader prompts to make a candidate pass.

Report at least:

- the decision and the claim the evidence supports;
- candidate, baseline and configuration revisions;
- dataset, slice, grader and judge revisions;
- commands or scenarios, target and environment;
- case counts, denominators, pass/fail results, slice results and variability;
- failed, skipped, errored or unavailable checks;
- latency and usage/cost where they affected acceptance;
- unresolved limits and the recommended next action.

Use the existing ECR verification and release section, or the project's verification record, and link the evaluation evidence. Do not create a new artifact type or copy a dashboard into a second source of truth.

A completed evaluation supports a decision; it does not authorize merge, deployment, publication or live mutation. State a recommendation as go, conditional or no-go with its evidence, then hand the delivery decision to `release` within the established authority.

## Composition

| Need | Use |
| --- | --- |
| What to evaluate, case and grader design, evidence boundaries | [`ai-testing`](../ai-testing/SKILL.md) |
| Program mechanics: dataset versions, slices, variance, denominators, gates, evidence levels | [Evaluation program](../ai-testing/references/evaluation-program.md) |
| Selected Python/DeepEval implementation | `ai-deepeval-testing` when installed and chosen |
| Application, contract, persistence and journey verification | `test` when available |
| Traces, signals and execution diagnosis | `observability` when available |
| Delivery readiness, promotion and recovery | `release` when available |
| Evidence record and artifact homes | The project's ECR/verification record and artifact conventions |

Stop when the plan or result and its limits are reported. If the request continues into deployment, merge or external publication, treat that as a separate authorized activity rather than extending this one.

## Sources and fit

This activity is original guidance informed by:

- OpenAI, [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): eval-driven development, task-specific data, human calibration, continuous evaluation and common anti-patterns.
- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): capability and regression suites, balanced cases, grader design, transcript review, saturation and environment isolation.

Those sources supply general evaluation practice. They do not define this repository's artifact model, acceptance authority or delivery process, and no text is copied.
