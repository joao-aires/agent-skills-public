---
name: ai-evaluation
description: >-
  Design and run the mechanics of a program-level AI evaluation: acceptance criteria,
  dataset and slice governance, grader choice and calibration, baselines, experiments,
  CI gates, production sampling, regression and red-team coverage. Use inside testing,
  design or release when an AI change, release or product claim needs evaluation evidence.
  It supplies the mechanics; the activity owns the decision and stopping point.
user-invocable: true
metadata:
  kind: method
  domain: ai
  phase: cross-phase
  scope: generic
  invocation: both
---

# AI evaluation mechanics

Use this method when a claim needs evidence across several cases, changes or operating conditions rather than one bounded check. It supplies the program mechanics; the activity that composes it owns the decision, output and stopping point.

The mechanics cover the claim, acceptance, dataset and slice governance, graders, baseline and experiment, gates, production sampling, reporting and authority. It composes [AI testing](../ai-testing/SKILL.md) for what to evaluate and what the evidence means, installed evaluation-framework guidance for the selected implementation, application verification guidance when installed, installed observability guidance for execution signals, and the project's delivery authority. It does not own the evaluation method, the selected runner or the deployment.

## Where it is used

| Phase | What this method supplies |
| --- | --- |
| Testing | The program behind acceptance or completion evidence for AI behavior |
| Design | A comparable baseline and experiment for a model, prompt or architecture choice |
| Release | The evidence and limits behind a readiness claim |

## Composition

Read [AI testing](../ai-testing/SKILL.md) for the method that decides what to evaluate and what each evidence level proves. This method owns the program mechanics; the activity keeps the decision and stopping point.

## Frame the decision and claim

Identify who will act on the result, what changes if they do, and what a wrong answer would cost. A go/no-go recommendation, a model or prompt choice, a safety claim and a monitoring decision need different evidence.

State the claim as a bounded sentence: candidate, criteria, population and revision. For example, "candidate prompt P2 meets the accepted grounding and task-completion criteria on the held-out support slices at revision R." Distinguish:

- a component claim from a product-journey claim;
- an offline comparison from operating evidence;
- an observed difference from a causal explanation.

Use the narrowest claim that still supports the decision. Widen it only with evidence that covers the wider population or boundary. If the request uses causal language such as "improved" or "safer," design a comparison that can separate the intervention from other changes. Otherwise report an observation.

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

For a model judge, write the criteria, evaluation steps or score bands it must apply. Calibrate it against accepted human assessments that include borderline and unacceptable results, then inspect disagreements rather than relying on an aggregate agreement number. Record the judge model, prompt, parameters and revision. Recalibrate after a judge change. Check that the judge cannot be satisfied by a shortcut, leaked answer or superficial format.

Use one grader for one property. A judge may assess answer quality. It does not establish authorization, persistence or protocol compatibility. When a deterministic check and a judge disagree, investigate the boundary before choosing the convenient result.

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

Production sampling needs an accepted purpose, privacy review, retention and deletion rules. Compare slices with an identifiable baseline, account for changed traffic and sampling, and promote useful failures into privacy-preserving regression cases. Operating scores describe the observed population. They do not replace held-out release evidence.

Cover failure and adversarial behavior deliberately: ambiguity, missing or conflicting evidence, invalid input, provider/tool failure, prompt injection, data exfiltration, authority bypass, unsafe tool use, harmful content, refusal and over-refusal. Test both "should" and "should not" behavior, assign severity and an acceptable response, and run adversarial work in a bounded environment that cannot cause the harm being tested. A red-team tool or fixed attack list is optional. Coverage of the accepted threat model is not.

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

A completed evaluation supports a decision. It does not authorize merge, deployment, publication or live mutation. State a recommendation as go, conditional or no-go with its evidence, then hand the delivery decision to the established delivery authority, within the established authority.

## Composition

| Need | Use |
| --- | --- |
| What to evaluate, case and grader design, evidence boundaries | [`ai-testing`](../ai-testing/SKILL.md) |
| Program mechanics: dataset versions, slices, variance, denominators, gates, evidence levels | [Evaluation program](../ai-testing/references/evaluation-program.md) |
| Selected Python/DeepEval implementation | Installed guidance for the chosen evaluation framework |
| Application, contract, persistence and journey verification | Verification guidance for the affected surfaces |
| Traces, signals and execution diagnosis | Installed observability guidance; project telemetry tooling |
| Delivery readiness, promotion and recovery | Installed delivery and release guidance |
| Evidence record and artifact homes | The project's ECR/verification record and artifact conventions |

Return the plan or result and its limits to the activity that composed it. Deployment, merge and external publication remain separate authorized actions.

## Sources and fit

This method is original guidance informed by:

- OpenAI, [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): eval-driven development, task-specific data, human calibration, continuous evaluation and common anti-patterns.
- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): capability and regression suites, balanced cases, grader design, transcript review, saturation and environment isolation.

Those sources supply general evaluation practice. They do not define this repository's artifact model, acceptance authority or delivery process, and no text is copied.
