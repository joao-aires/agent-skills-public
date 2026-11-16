# DeepEval in CI and reporting

Use this reference after the evaluation run is designed. It covers the pipeline boundary, result evidence and reporting. Metric choice and acceptance remain in the [DeepEval playbook](deepeval-playbook.md) and the evaluation program.

## Separate the gates

Keep fast deterministic tests separate from credentialed quality jobs.

| Gate | Runs | Required evidence |
| --- | --- | --- |
| Application tests | Every change | Schemas, authorization, persisted effects, contracts and recovery. |
| Smoke evaluation | Relevant changes or nightly | The suite executes against the selected configuration and produces inspectable results. |
| Held-out quality gate | Consequential model, prompt, retrieval or tool changes | Accepted thresholds, slices, case-level failures, variability and cost. |
| Production sampling | Authorized operating window | Privacy-approved observations with population and sampling limits. |

Define which gate blocks delivery and which is advisory. A smoke run does not establish quality, and a quality score does not replace application verification.

## Run in a trusted context

Quality jobs may call paid providers and read evaluation data.

- Run live evaluations in a trusted branch, protected job or controlled environment, not on untrusted pull-request code with production secrets.
- Use least-privilege credentials for the application and judge. Keep provider keys, dataset access and hosted-reporting tokens out of logs and artifacts.
- Pin Python, dependencies, the DeepEval version and the container or runner image. Record the effective revisions.
- Bound network access to the providers and destinations the run needs.
- Do not use `deepeval login` in CI unless hosted reporting is an explicitly accepted integration. A local run needs no account.
- Redact inputs, outputs and failure artifacts before uploading them. Test-run files can contain prompts, retrieved content and personal data.

## Invoke the evaluation runner

Use the DeepEval runner for a committed suite:

```text
deepeval test run tests/evals/test_support_agent.py --identifier "$CI_RUN_ID"
```

- Do not treat `pytest tests/evals` as equivalent. It can collect and run the file while bypassing the DeepEval runner's evaluation behavior.
- Do not append `|| true`, ignore the exit status or mark the step non-blocking unless the gate is explicitly advisory.
- Keep `-i`, `-s`, `-c` and `-r` explicit in the command and in the result. They change coverage, freshness or variance.
- Use `evaluate()` for a batch or script step only when its exit behavior is checked and its results are persisted. Printing a table is not a gate.
- Set a timeout and budget proportional to the dataset and judge. A run that times out is incomplete, not passed.

## Preserve per-case evidence

Keep a machine-readable result and a short human report. The machine-readable artifact should retain:

- run identifier, timestamp, command, code revision and environment;
- application, model/provider, prompt, retrieval, tool, judge and DeepEval revisions;
- dataset revision or hash, slice labels and case IDs;
- metric names, parameters, thresholds and judge configuration;
- per-case score, pass/fail, reason and trace or artifact reference;
- execution status: passed, failed, skipped, missing parameters, errored or flaky;
- denominators and totals, including cases that did not execute;
- latency and usage/cost where measured, with estimates labelled.

Do not report only an average, only passing cases or only the dashboard's headline number. Keep failed and skipped cases inspectable.

## Persist local artifacts

Use the installed release's supported local output:

```python
from deepeval.evaluate import DisplayConfig

evaluate(
    test_cases=test_cases,
    metrics=metrics,
    display_config=DisplayConfig(results_folder="./evals/results"),
)
```

For the pytest runner, `DEEPEVAL_RESULTS_FOLDER` persists test runs in supported releases. A local SQLite store may be available; check the installed version.

- Write results to a path that the CI job can archive, not to an ephemeral home directory.
- Set retention and access on the artifact. Treat it as potentially sensitive.
- Keep the raw result plus a derived summary; derive the summary reproducibly and link it to the raw file.
- Do not commit transient run artifacts unless the project already treats them as evidence. Link the CI artifact or a stable report instead.
- If hosted reporting is selected, still retain a local or exportable result so the evidence is not solely dependent on the service.

## Report the comparison

A useful report answers the decision, not just the score.

1. State the claim and the decision it supports.
2. Identify the baseline and candidate configurations.
3. Report the executed dataset, slices and denominators.
4. Show pass/fail counts and case-level failures before aggregate scores.
5. Include variability across repetitions and the judge's uncertainty or disagreement where relevant.
6. Include latency and cost with failed and retried attempts.
7. List skipped, errored, flaky and unavailable checks.
8. State what the evidence does not establish and the recommended next action.

Use the project's ECR verification section or an existing verification record. Link the suite, dataset revision, CI run and result artifact; do not create a parallel report with different numbers.

## Diagnose before retrying

Treat these as different failures:

| Result | Likely action |
| --- | --- |
| Application assertion fails | Repair the application or the fixture; rerun the affected test. |
| Metric score below threshold | Inspect the case, rubric, reference and actual output before changing code. |
| Missing test-case parameter | Fix the case construction or choose a metric that matches the available evidence. |
| Judge/provider error | Check credentials, rate limits, model availability and retry bounds. |
| Skipped or ignored case | Restore required coverage; do not count the skip as a pass. |
| Flaky case | Investigate variance or shared state; quarantine with an owner and review condition if necessary. |
| Timeout or partial run | Reduce scope or concurrency within budget; do not report a partial run as complete. |

Rerun only the affected cases when that is sufficient, then run the required broader comparison before the decision. Preserve the original failure and the rerun outcome.

## Sources and fit

This reference is original integration guidance informed by DeepEval's [CI/CD unit testing](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd), [flags and configs](https://deepeval.com/docs/evaluation-flags-and-configs) and [local result storage](https://deepeval.com/docs/evaluation-local-backend-storage) documentation. It does not require a hosted reporting service or a particular CI provider.
