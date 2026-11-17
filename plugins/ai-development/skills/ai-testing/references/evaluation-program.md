# Evaluation program mechanics

Use this reference when evaluation must support a decision across changes, releases or operating conditions, rather than one bounded check. It covers the mechanics that keep cases, graders and results comparable. The evaluation method itself lives in [AI testing](../SKILL.md) and the program-level decisions and authority live in `ai-evaluation`.

## Keep a decision and claim register

Record these fields for each evaluation program. A short table in the change record is enough; a separate document is optional.

| Field | What to record |
| --- | --- |
| Decision | Who will act, what action, by when, and what result would change the action. |
| Claim | Candidate, criteria, population/slices and revision the evidence will describe. |
| Comparison | Baseline, alternative or threshold, and whether the claim is observational or causal. |
| Acceptance | Must-pass criteria, aggregate thresholds, minimum slice sizes and uncertainty policy. |
| Evidence | Dataset, grader, judge, execution mode and target revision. |
| Authority | Who may accept the result, spend budget, use data or expose samples. |

Write the claim before running the comparison. If the available evidence cannot support it, narrow the claim or report the gap. Do not let a broader product or safety claim inherit a narrow component result.

## Version datasets and holdouts

An evaluation dataset is an asset with an identity, not an incidental file.

- Record the authoritative source, revision or content hash, owner, license/permission and collection date.
- Keep stable case IDs. Preserve the input, expected outcome or rubric, slice labels and provenance separately from the actual execution result.
- Treat a material edit to an input, expected outcome, rubric or slice as a new dataset revision. Do not silently change acceptance while repairing behavior.
- Keep development cases and held-out cases distinguishable. Record which cases were inspected while changing the candidate.
- Restrict holdout access to the people or jobs that need it. Do not use holdout results to select prompts, thresholds, features or grader wording.
- Rotate or refresh a saturated holdout deliberately. A holdout repeatedly used for decisions becomes a development set in practice.
- Keep a regression set of accepted failures and important prior behavior. Grow it from observed failures, but review each promotion for correctness and privacy.
- Check for duplication, leaked answers, stale expected values and contamination from public benchmarks or the candidate's training data.

Local files, a database or a hosted dataset service can all hold the dataset. The service is not the authority; the recorded revision and provenance are. Keep the dataset and deterministic evaluators usable without a hosted account.

## Select slices deliberately

Define slices before seeing results. Useful slice dimensions include user segment, data source, task intent, risk or severity, language/dialect, modality, tenant, input length, tool path and journey step.

- Choose slices that could change the decision or reveal a failure hidden by the aggregate.
- Keep a rare but consequential slice even when its sample is small; report the small denominator instead of pooling it away.
- Balance positive and negative cases within a behavior. Include cases where the system should act and where it should not.
- Avoid slicing so finely that every result becomes noise. Use the decision to decide how much disaggregation is useful.
- Report slice denominators and missing cases. A slice with no executed cases is unverified, not passing.

## Calibrate graders and judges

Prefer deterministic checks for anything the application can decide: schema validity, authorization, required fields, tool arguments, persisted effects, exact classifications.

For a model judge:

1. Write the criteria and, where possible, explicit evaluation steps or score bands.
2. Build a calibration set of accepted human judgments covering good, borderline and unacceptable results.
3. Compare judge decisions with those judgments, including per-class disagreement rather than only overall agreement.
4. Inspect the cases where they disagree and refine the rubric, examples or judge.
5. Record the judge model, version, prompt, parameters and calibration revision.
6. Repeat calibration after changing the judge or rubric.

Check for position, verbosity, style and reference-answer bias. Give the judge a legitimate way to abstain when evidence is insufficient. Make the task resistant to shortcuts: do not leave the expected answer in the prompt, do not grade only a format the candidate can satisfy without doing the work, and randomize details that should not affect the result.

A judge measures the property its rubric describes. It does not establish that the application enforced authorization, stored the right record or interoperated with a peer. Keep those as separate checks.

## Plan repetitions and variance

Identify the stochastic sources: model sampling, retrieval, tool/provider behavior, judge sampling, environment and concurrent work.

- Repeat each stochastic case enough times to support the decision, and report the distribution or pass rate rather than one favorable run.
- Prefer paired or interleaved candidate/baseline runs on the same inputs to reduce drift from time, cache, queue or provider changes.
- Separate infrastructure errors from quality failures. A timeout or judge parse error is not a low-quality answer.
- Do not tune a threshold to a single run's noise. State the minimum detectable difference or the uncertainty that the sample can support.
- Use confidence intervals or a clear range when reporting estimates. With small samples, describe the result as a signal or a defect, not a reliability rate.

## Define denominators and missingness

Choose the denominator from the promised outcome before computing a percentage.

| Question | Denominator |
| --- | --- |
| How often does the system produce an acceptable result? | All evaluated attempts, including failed and errored attempts, when the user experiences those attempts. |
| How often does an accepted response meet quality criteria? | Accepted responses, reported separately from acceptance rate. |
| How often does the task complete within budget? | Task intents attempted, including retries and abandoned work. |
| What does a successful task cost? | Accepted task completions, with total cost and failed-attempt cost shown alongside. |

Keep skipped, missing-parameter, errored and flaky cases visible. Either include them in the denominator with their status or report them separately and explain why they are excluded. "Passed 8 of 8 executed" is not the same as "passed 8 of 10 selected".

## Set thresholds and gates

Set thresholds before the comparison. A threshold can be an absolute target, a maximum acceptable regression, a must-pass case set or a slice-specific floor.

- Separate must-pass criteria from aggregate targets. A high average cannot excuse a failed authority, safety or factual case.
- Allow for measurement noise. A small difference between candidates may be sampling or judge variance; state whether the sample can distinguish it.
- Label provisional targets and their uncertainty. Do not invent a product commitment because a metric has a default threshold.
- Define which suites gate a change, which are advisory and which run periodically. Keep cheap deterministic checks routine.
- Define behavior when access, credentials, data or a judge is unavailable: the affected boundary is unverified, not waived.
- Record the threshold revision when acceptance changes for a real product reason.

## Separate development and held-out evidence

Use development cases to inspect behavior and iterate. Use held-out cases to assess whether the change generalizes beyond the material used to build it.

- Report development and held-out results separately.
- Do not select a candidate, prompt or threshold on held-out results and then present the same results as an unbiased estimate.
- If a holdout is exposed during debugging, record the exposure and refresh or qualify the evidence.
- Keep a capability suite that can still show improvement and a regression suite that should remain stable. A capability case that saturates can graduate to regression coverage, but a 100% suite no longer measures improvement.
- Read transcripts and case-level outputs. A score without inspection can hide a broken task, an unfair grader or a valid alternative solution.

## Sample production with a stated frame

Production sampling provides operating evidence for the observed population. It is not complete coverage.

- Define the sampling frame, rate, time window and stratification. Record changes in traffic or sampling that limit comparison with earlier periods.
- Obtain the required privacy, retention, access and deletion approval before collecting content. Prefer metadata or redacted samples when they answer the question.
- Use user feedback and corrections as candidate signals, not as representative labels. People who complain differ from those who do not.
- Compare slices with an identifiable baseline and separate application, model/provider, corpus and environment changes.
- Promote observed failures into reviewed, privacy-preserving regression cases. Remove unnecessary personal data while retaining the behavior that failed.
- Keep online scores, offline held-out results and user feedback distinguishable in reports, including their population and uncertainty.

## Cover failure and red-team behavior

Derive adversarial coverage from the accepted threat model and the product's authority. Cover at least the relevant categories: ambiguous or missing evidence, conflicting instructions, malformed input, prompt injection through retrieved content or tool results, data exfiltration, unauthorized tool use, unsafe side effects, harmful or disallowed content, refusal and over-refusal, and multi-turn attempts to erode a boundary.

- Test both the behavior that should occur and the behavior that should not. A set containing only attacks rewards a system that blocks everything.
- Define severity and an acceptable response for each category. "The model said something bad" is not a complete finding; record the action, affected authority and reproducibility.
- Run adversarial work in a sandbox with bounded credentials, network and side effects. Do not cause the harm being tested or touch real users and data.
- Record coverage and gaps by category. A fixed attack list or commercial red-team service can help, but neither establishes coverage of the accepted threat model.
- Keep safety and authority invariants as deterministic application checks where possible. A judge can assess tone or refusal quality; it cannot grant permission or prove that a tool call was authorized.

## Run an eval-driven development loop

1. Observe a failure or a gap in a representative case.
2. Classify it before changing the system: dataset, expected outcome, grader, harness, application, model/provider or environment.
3. Add or refine a case that captures the behavior without copying private content.
4. Make one scoped change to the candidate.
5. Rerun the affected suite and the relevant held-out comparison.
6. Inspect case-level results and transcripts; keep the change only if it improves the intended behavior without an unacceptable regression.
7. Promote the useful case into regression coverage and record the evidence.

Do not optimize against the test set until the score rises. That measures the test, not the product. Change the dataset only when the task or accepted behavior changed, and record why.

## State the evidence level

| Evidence level | What it can support | What it cannot |
| --- | --- | --- |
| Smoke or spot check | The path runs and produces inspectable output. | Quality, reliability or generalization. |
| Bounded development experiment | A defect or a promising change on selected cases. | A population estimate or release claim. |
| Held-out comparison | The candidate meets criteria on the evaluated population and conditions. | Operating performance or unexamined slices. |
| Repeated held-out comparison | A more stable estimate with stated variability. | Causation without a suitable design. |
| Authorized production sampling | Observed operating behavior for the sampled population. | Complete coverage or a substitute for held-out release evidence. |

Report the level with the result. A component score, a simulated user, a recorded output and a live journey are different evidence, even when they use the same metric.

## Sources and fit

This reference is original synthesis informed by:

- OpenAI, [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): task-specific datasets, human-calibrated graders, continuous evaluation and anti-patterns such as generic metrics and vibe-based assessment.
- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): capability versus regression suites, balanced cases, grader design, transcript review, environment isolation and saturation.
- Anthropic, [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests): task-specific edge cases and automated grading.

Adapt the mechanics to the project's accepted acceptance criteria and authority. These sources do not define a required tool, dataset service or release gate.
