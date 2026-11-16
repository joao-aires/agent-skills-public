# DeepEval in CI and reporting

Use this reference after the evaluation run is designed. It covers the pipeline boundary, result evidence and reporting. Metric choice and acceptance remain in the [DeepEval playbook](deepeval-playbook.md) and the evaluation program.

## Separate the gates

| Gate | Runs | Required evidence |
| --- | --- | --- |
| Application tests | Every change | Schemas, authorization, persisted effects, contracts and recovery. |
| Smoke evaluation | Relevant changes or nightly | The suite executes against the selected configuration and produces inspectable results. |
| Held-out quality gate | Consequential model, prompt, retrieval or tool changes | Accepted thresholds, slices, case-level failures, variability and cost. |
| Production sampling | Authorized operating window | Privacy-approved observations with population and sampling limits. |

Define which gate blocks delivery and which is advisory. A smoke run does not establish quality, and a quality score does not replace application verification.

## Run in a trusted context

- Run live evaluations in a trusted branch, protected job or controlled environment, not on untrusted pull-request code with production secrets.
- Use least-privilege credentials for the application and the judge; keep keys, dataset access and reporting tokens out of logs and artifacts.
- Pin Python, dependencies, the DeepEval version and the runner image, record the effective revisions, and bound network access to the providers the run needs.
- Do not log in or upload cases unless hosted reporting is an explicitly accepted integration. A local run needs no account.
- Redact inputs, outputs and artifacts before upload; a test-run file can contain prompts, retrieved content and personal data.

## Invoke the runner and confirm completion

```text
deepeval test run <eval-path> --identifier "<run-id>"
```

- `deepeval test run` applies the evaluation runner; bare `pytest` can collect and execute the same file while bypassing that behavior. Never cite ordinary pytest collection as a completed DeepEval run.
- Do not append `|| true`, ignore the exit status or make the step non-blocking unless the gate is explicitly advisory.
- Any flag that changes coverage, error handling, caching or repetitions belongs in the command and in the recorded result. Keep such flags out of durable guidance; check the installed release's [flags and configs](https://deepeval.com/docs/evaluation-flags-and-configs).
- Use `evaluate()` for a script or batch step only when its exit behavior is checked and its results are persisted. A printed table is not a gate.
- Set a timeout and budget proportional to the dataset and judge. A run that times out or terminates early is incomplete, not passed.

## Preserve per-case evidence

Keep a machine-readable result plus a short human report. The artifact should retain:

- run identifier, timestamp, command, code revision and environment;
- application, model/provider, prompt, retrieval, tool, judge and DeepEval revisions;
- dataset revision or hash, slice labels and case IDs;
- metric names, parameters, thresholds and judge configuration;
- per-case score, pass/fail, reason and trace or artifact reference;
- execution status: passed, failed, skipped, missing parameters, errored, flaky;
- denominators and totals, including cases that did not execute;
- latency and usage/cost where measured, with estimates labelled.

Do not report only an average, only passing cases or only a dashboard headline. Skipped, errored and flaky cases stay visible and never count as passes.

## Keep artifacts local and archivable

Write results to a path the job can archive, not to an ephemeral home directory, using the installed release's local output route. See [local result storage](https://deepeval.com/docs/evaluation-local-backend-storage) for exact paths and options.

- Treat the artifact as potentially sensitive, set retention and access, and keep the raw result with a reproducibly derived summary linked to it.
- Do not commit transient run artifacts unless the project already treats them as evidence; link the CI artifact or a stable report instead.
- If hosted reporting is selected, still retain a local or exportable result so the evidence does not depend solely on the service.

## Triage before retrying

| Result | Likely action |
| --- | --- |
| Application assertion fails | Repair the application or fixture; rerun the affected test. |
| Score below threshold | Inspect the case, output, reference and rubric before changing code. |
| Missing test-case parameter | Fix case construction or choose a metric the evidence supports. |
| Judge or provider error | Check credentials, limits, model availability and retry bounds. |
| Skipped or ignored case | Restore required coverage; a skip is not a pass. |
| Flaky case | Investigate variance or shared state; quarantine with an owner and review condition. |

Repair the cause at the smallest boundary. Do not lower thresholds or rewrite expected outcomes to make a candidate pass. Preserve the original failure and the rerun outcome.

## Report the decision

State the claim, the baseline and candidate configurations, and the executed dataset, slices and denominators. Show case-level failures and counts before aggregate scores, then variability, latency and cost. List skipped, errored, flaky and unavailable checks, and say what the evidence does not establish. Use the project's existing verification record and link the suite, dataset revision, CI run and artifact rather than creating a parallel report.

A component score supports a component claim only. It does not establish a product journey, persisted outcomes or operating quality.

## Sources and fit

This reference is original integration guidance informed by DeepEval's [CI/CD unit testing](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd), [flags and configs](https://deepeval.com/docs/evaluation-flags-and-configs) and [local result storage](https://deepeval.com/docs/evaluation-local-backend-storage) documentation. It requires neither a hosted reporting service nor a particular CI provider. Verify commands, flags and paths against the installed release.
