# DeepEval implementation playbook

Use this reference after the evaluation approach and acceptance are agreed. It maps the selected DeepEval release to cases, datasets, metrics and execution. Case design, evidence boundaries and program decisions remain with `ai-testing` and the selected evaluation activity; this playbook does not redefine them.

## Pin and inspect the selected release

Use one reviewed DeepEval version in the project's test or development dependency group and lock it. Record the installed version and Python requirement with the evaluation evidence.

```text
deepeval==<reviewed-version>
```

- Check the installed API before writing code; metric names, test-case parameters and tracing helpers change between releases.
- Do not upgrade DeepEval, pytest or the judge during an evaluation comparison unless the upgrade is part of the intervention.
- Verify the effective judge provider, model and credentials separately from the application's model.
- Keep the suite runnable locally without a hosted account. Confident AI is an optional integration, not a prerequisite.

The evaluation runner can be Python while the evaluated application uses another language. Do not migrate the application to run the suite.

## Represent actual cases

Keep the input scenario, expected outcome or rubric, and observed execution distinct. Populate the test case from the run being assessed, not from an ideal reconstruction.

| Evidence | DeepEval representation |
| --- | --- |
| One input and one observed output | `LLMTestCase` with at least `input` and `actual_output`. |
| Reference answer or expected result | `expected_output`, when the selected metric uses it. |
| Retrieved evidence | `retrieval_context`; keep it distinct from `context` and from what should have been available. |
| Tools actually used and expected tools | `tools_called` and `expected_tools`, when the metric requires them. |
| Multi-turn interaction | `ConversationalTestCase` with ordered `Turn(role=..., content=...)` values. |
| Rerunnable input collection | `EvaluationDataset` containing `Golden` or `ConversationalGolden`. |
| Categorical expectation | `expected_labels` for a selected classifier. |

A dataset is single-turn or multi-turn, not both. Use `Golden(input=..., expected_output=...)` for single-turn inputs and `ConversationalGolden(scenario=..., expected_outcome=...)` for conversations. Load curated cases from the project's authoritative JSON, JSONL or CSV source rather than copying them into an untracked script. `save_as()` and the matching load helpers are useful for local interchange, but the authoritative revision and provenance stay with the project.

Do not fill `actual_output`, `retrieval_context` or `tools_called` from a golden unless the application actually produced those values. A recorded output establishes the recorded run; it does not establish live behavior.

## Select metrics by the property

Choose the smallest set that observes the accepted criteria. Three to five metrics is a useful first suite; add more only when the decision needs them. Record every metric's required fields and explicit threshold instead of relying on defaults.

| Property | Candidate metrics |
| --- | --- |
| Task completion or end-to-end usefulness | `TaskCompletionMetric`, task-specific `GEval` |
| RAG grounding and retrieval | `FaithfulnessMetric`, `AnswerRelevancyMetric`, `ContextualRelevancyMetric`, `ContextualPrecisionMetric`, `ContextualRecallMetric` |
| Agent trajectory | `TaskCompletionMetric`, `StepEfficiencyMetric`, `PlanAdherenceMetric`, `PlanQualityMetric` |
| Tool selection and arguments | `ToolCorrectnessMetric`, `ArgumentCorrectnessMetric` |
| Conversation behavior | `ConversationCompletenessMetric`, `RoleAdherenceMetric`, `TurnRelevancyMetric`, `ConversationalGEval` |
| Format or prompt adherence | `JsonCorrectnessMetric`, `PromptAlignmentMetric`, or a deterministic schema check |
| Safety or policy | `BiasMetric`, `ToxicityMetric`, `PIILeakageMetric`, `MisuseMetric`, `RoleViolationMetric`, or an application policy check |

Check the installed metric's required parameters before running it. Reference-based metrics need reference fields; referenceless metrics are easier to use for online sampling but may not measure the property the acceptance needs. A `JsonCorrectnessMetric` does not replace schema validation in the application, and a safety metric does not enforce authorization.

Keep deterministic invariants outside the judge: authorization, isolation, required fields, side effects, tool permissions and recovery. A high judge score does not compensate for a failed invariant.

## Calibrate a custom rubric

Use `GEval` for a task-specific, subjective criterion that no suitable built-in metric covers. Define what the judge must distinguish and which evidence it may read.

```python
from deepeval.metrics import GEval
from deepeval.test_case import SingleTurnParams

correctness = GEval(
    name="Correctness",
    evaluation_steps=[
        "Compare the factual claims in the actual output with the expected output.",
        "Penalize a contradiction or a material omission.",
        "Do not penalize a different wording that preserves the accepted meaning.",
    ],
    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    threshold=0.8,
)
```

- Provide `criteria` or `evaluation_steps`, not both. Supplying criteria alone lets the judge generate steps on each run, which increases variability; inspect the generated steps, then freeze explicit steps when the rubric is agreed.
- Include only parameters the rubric actually uses. An unused reference field can distort the judgment or fail when the dataset lacks it.
- Use `rubric` score bands when the judge clusters in the middle, and `strict_mode` only when the accepted decision is truly binary.
- Calibrate against human-labeled good, borderline and unacceptable outputs. Inspect the judge's reasons and disagreements; an aggregate agreement number alone is not calibration.
- Record the judge model, version and prompt/steps. Recalibrate after changing the judge, rubric or evaluation parameters.
- Check for shortcuts: leaked expected answers, a format the output can satisfy without doing the task, or a judge that rewards length or confidence.

Use `ConversationalGEval` for criteria that span a conversation. It judges the whole conversation, not one turn at a time.

## Run with the supported route

Use `evaluate()` for a script or batch run. It accepts a list of test cases or an `EvaluationDataset`, metrics and optional configuration for concurrency, errors, caching and local result storage.

```python
from deepeval import evaluate
from deepeval.evaluate import DisplayConfig

evaluate(
    test_cases=dataset.test_cases,
    metrics=[correctness],
    display_config=DisplayConfig(results_folder="./evals/results"),
    identifier="support-prompt-v3",
)
```

Use `assert_test()` inside a pytest-style suite for per-case failures and CI gating. With tracing, `assert_test(golden=golden, metrics=[...])` can build the case from the observed trace; without tracing, build an `LLMTestCase` or `ConversationalTestCase` and pass it explicitly.

```python
import pytest
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset, Golden
from deepeval.test_case import LLMTestCase

dataset = EvaluationDataset(
    goldens=[Golden(input="...", expected_output="...")]
)

@pytest.mark.parametrize("golden", dataset.goldens)
def test_support_agent(golden: Golden):
    result = run_agent(golden.input)
    assert_test(
        test_case=LLMTestCase(
            input=golden.input,
            actual_output=result,
            expected_output=golden.expected_output,
        ),
        metrics=[correctness],
    )
```

Run the suite with the DeepEval runner, not bare pytest:

```text
deepeval test run tests/evals/test_support_agent.py
```

`deepeval test run` applies the runner, result reporting and supported flags. Ordinary pytest collection can execute a test file without establishing that the DeepEval run completed as intended.

Useful runner flags, verified against the installed release:

| Need | Flag |
| --- | --- |
| Parallel processes | `-n <count>` or the release's equivalent |
| Repeat each case for variance | `-r <count>` |
| Reuse cached metric results | `-c` |
| Continue after metric errors | `-i` |
| Skip metrics with missing test-case parameters | `-s` |
| Name the run | `-id "<name>"` |
| Show only failing cases | `-d failing` |

Flags change what the result means. `-i` and `-s` can leave a criterion unexecuted; keep those cases visible and do not count them as passes. Caching is useful for iteration, but a cached result must be keyed to the same case and metric configuration and should not be presented as a fresh run.

## Add tracing only where it answers a question

Local tracing needs no account. Instrument the application path with `@observe` and set the observed values with `update_current_trace()` and `update_current_span()`.

- A trace carries the end-to-end input/output and the ordered span tree. Trajectory metrics need that tree.
- A span carries the component-level case for a retriever, tool, model call or agent step. Attach component metrics only where diagnosis needs them.
- Set `input`, `output`, `retrieval_context`, `tools_called`, `expected_output`, `tags` and `metadata` from the actual execution, not from a fixture.
- Preserve an existing tracing owner and avoid duplicate instrumentation. DeepEval tracing is an evaluation path; it is not a replacement for the project's production observability.
- Short-lived jobs that export hosted traces need a bounded flush; local-only runs do not establish that a remote destination received them.

Do not add tracing merely to run a black-box metric. Use it when the decision needs trajectory evidence or component diagnosis.

## Keep results local by default

A local run can produce console output, per-case scores and reasons, and a persisted test-run artifact.

- `DisplayConfig(results_folder=...)` or `DEEPEVAL_RESULTS_FOLDER` writes structured test-run files; the installed release may also support a local SQLite store.
- Keep the run identifier, hyperparameters, case IDs, metric configuration, scores, reasons, thresholds and failures with the artifact. Use the release's hyperparameter logging route for the application, prompt and judge revisions when the runner has no direct `evaluate()` call.
- Sanitize inputs and failure artifacts before uploading or retaining them. A test-run file can contain prompts, outputs and retrieved content.
- `deepeval view` and hosted dashboards require a selected Confident AI integration. Do not log in or upload cases merely to inspect a local result.
- If hosted reporting is selected, record the account, region, retention and data-sharing decision. Hosted reporting does not change the local acceptance criteria.

## Account for cost and limits

Most quality metrics call a judge model even when the application output was recorded. Synthetic generation, conversation simulation, tracing export and component metrics add further calls.

- Set the application model and judge separately; do not assume the evaluation judge is the application model.
- Bound concurrency, retries, timeouts and total cases per run. Rate limits and provider errors are execution failures, not quality results.
- Record measured usage or cost where the provider and installed release expose it. Label estimates and missing values.
- Include failed, skipped and retried attempts when reporting end-to-end cost or latency.
- Compare candidates with the same judge, limits and cache policy; a judge or concurrency change can move scores without changing the application.

## Handle flaky, errored and skipped results

Keep the status of every case. A metric exception, missing field, judge parse error, timeout and application failure are different events.

- Use `flaky=True` only for a known, documented nondeterministic criterion, and keep the flaky result visible. A flaky failure is not a pass and should not silently satisfy a required gate.
- Use `-i` or `-s` to keep a run operable while diagnosing, not to make a release gate green.
- Rerun the affected cases after repairing the cause. Preserve the original failure and the rerun result.
- Quarantine a flaky case with an owner, reason, replacement evidence and a review condition. Do not weaken the threshold to hide it.
- Verify the runner's exit status, the number of executed cases and the result completeness. A process that exits zero after skipping the required suite has not established the claim.

## Treat synthetic data as a reviewed input

`Synthesizer` and `ConversationSimulator` are optional, credentialed paths. They can generate single-turn goldens, augment existing goldens or produce conversation turns.

- Use them when there is a real gap in coverage, not as a default replacement for task evidence.
- Review generated inputs, expected outcomes and personas for task fit, correctness, duplication and privacy before using them.
- Keep synthetic cases distinguishable from observed or expert-curated cases in the dataset and report.
- Do not adopt a fixed golden count or iteration count as an acceptance rule. Size the suite from the decision and the observed coverage.

## Triage failures by cause

Read the case, the metric reason and the trace before changing the application.

| Symptom | Check first |
| --- | --- |
| Metric reports missing parameters | Test-case fields versus the metric's requirements; `-s` may be hiding the gap. |
| Judge error or invalid structured output | Judge model, prompt, rate limit, provider status and installed release. |
| Low score with a plausible answer | Rubric, evaluation steps, reference field, judge calibration and task ambiguity. |
| Trace or trajectory metric unavailable | Instrumentation path, observed spans, trace completion and installed API. |
| Same score despite a code change | Cache, case content, metric configuration or a candidate that did not change. |
| Different results across runs | Stochastic sampling, judge variance, concurrency, provider drift or shared state. |

Repair the cause at the smallest boundary. Do not change the expected outcome, threshold or rubric merely because a candidate failed. Preserve useful failures as regression cases with private content removed.

For CI wiring, artifacts, secrets and result reporting, read [CI and reporting](ci-and-reporting.md).

## Sources and fit

This playbook is original integration guidance informed by:

- DeepEval, [Evaluation introduction](https://deepeval.com/docs/evaluation-introduction), [test cases](https://deepeval.com/docs/evaluation-test-cases), [datasets](https://deepeval.com/docs/evaluation-datasets) and [metrics](https://deepeval.com/docs/metrics-introduction).
- DeepEval, [G-Eval](https://deepeval.com/docs/metrics-llm-evals) and [LLM tracing](https://deepeval.com/docs/evaluation-llm-tracing).
- DeepEval, [flags and configs](https://deepeval.com/docs/evaluation-flags-and-configs), [CI/CD unit testing](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) and [local result storage](https://deepeval.com/docs/evaluation-local-backend-storage).
- The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills), reviewed as a reference. Their mandatory intake, synthetic-generation preference, hosted-service preference and fixed iteration defaults are not adopted.

Check the selected release's primary documentation when implementing; these notes describe stable concepts, not a guaranteed API surface.
