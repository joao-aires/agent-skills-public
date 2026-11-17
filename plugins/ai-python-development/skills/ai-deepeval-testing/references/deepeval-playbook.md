# DeepEval implementation playbook

Use this reference after the evaluation approach and acceptance are agreed. It maps the decision to a DeepEval representation and names the boundaries that survive release changes. Case design, evidence levels and program authority stay with `ai-testing` and the evaluation activity.

## Decide from the evidence, not the API

| What the decision needs | Representation | Check first |
| --- | --- | --- |
| Quality of one request/response, or one component call | Single-turn case | You have the actual output, not a fixture |
| Quality inside retrieval, tool use or a model call | Component case attached to the observed span | The span carries the input and output actually used |
| Agent or workflow behavior over steps | Trajectory case from a completed trace | The trace is end-to-end and ordered |
| Behavior across turns | Conversation case with ordered turns | Roles and turn order match the interaction |
| Comparison across many inputs, slices or revisions | Dataset of goldens or records | Provenance, revision and case IDs are recorded |
| Categorical expectation | Labels on the case for a selected classifier | The classes are the ones acceptance uses |

If a field can only be filled from the expected answer, you have a fixture, not evidence. A recorded output establishes the recorded run, not live behavior.

## Minimum stable vocabulary

| Name | Role | Verify before use |
| --- | --- | --- |
| `LLMTestCase` | One interaction: input, observed output, optional expected output, retrieval context and tools | Field names and required fields |
| `ConversationalTestCase` | Ordered turns for multi-turn evaluation | Turn type, roles and ordering |
| `EvaluationDataset`, `Golden` | Versioned, rerunnable input collection | Single-turn versus multi-turn shape; load and save helpers |
| Metric classes | Measure one property against a threshold | Required parameters, judge, default threshold, reference dependence |
| `GEval` | Custom rubric over selected case fields | Parameter names, `criteria` versus `evaluation_steps`, score bands |

These names are stable enough to reason with; their parameters, imports and defaults are not. Check the installed release's documentation before writing the call, and record the version with the result.

## One example, for the decision it clarifies

The common mistake is asserting on a case assembled from goldens. Build the case from the run, then gate it through the DeepEval runner:

```python
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase

@pytest.mark.parametrize("case", load_accepted_cases())
def test_support_answer(case):
    result = run_agent(case.input)
    assert_test(
        test_case=LLMTestCase(
            input=case.input,
            actual_output=result.output,
            expected_output=case.expected_output,
        ),
        metrics=[rubric],
    )
```

Run it with `deepeval test run <path>`, not bare pytest. Field names, decorators and metric signatures may differ in the installed release.

## Keep data fidelity

- Hold the input scenario, the expected outcome or rubric, and the observed execution apart. Fill case fields from the execution being assessed.
- Keep retrieved evidence distinct from what should have been available, and tools called distinct from tools expected.
- Load curated cases from the project's authoritative source. Local export and load helpers are interchange, not the dataset authority.
- Size the suite from the decision and observed coverage. A fixed golden count or iteration count is not an acceptance rule.
- Treat generated or simulated cases as reviewed input: check task fit, correctness, duplication and privacy, and label them as synthetic.

## Calibrate the grader

- Give the judge explicit evaluation steps or score bands rather than criteria it expands differently on each run.
- Include only the fields the rubric reads; an unused reference can distort or fail the judgment.
- Use score bands when the judge clusters mid-range, and strict binary scoring only when the accepted decision is binary.
- Calibrate against human-labeled good, borderline and unacceptable outputs, and inspect disagreements rather than an aggregate agreement figure.
- Record judge model, version, prompt and rubric revision; recalibrate after any of them changes.
- Check for shortcuts: a leaked expected answer, a format that can be satisfied without doing the task, or rewards for length and confidence.

## Bound cost and privacy

- Assume a judge call per metric per case, including recorded outputs; generation, simulation and tracing add more.
- Set the judge and the application model independently, and bound concurrency, retries, timeouts and cases per run.
- Treat rate limits, provider errors and judge parse failures as execution failures, not quality results.
- Keep results local by default; hosted reporting is a separate integration with account, retention, region and data-sharing decisions.
- Redact inputs, retrieved content and failure artifacts before retention or upload.

## Look up the exact surface

| Need | Authoritative page |
| --- | --- |
| Evaluation flow and runner | [Evaluation introduction](https://deepeval.com/docs/evaluation-introduction) |
| Case fields | [Test cases](https://deepeval.com/docs/evaluation-test-cases) |
| Datasets and goldens | [Datasets](https://deepeval.com/docs/evaluation-datasets) |
| Metric names and parameters | [Metrics](https://deepeval.com/docs/metrics-introduction) |
| Custom rubric | [G-Eval](https://deepeval.com/docs/metrics-llm-evals) |
| Tracing for trajectory evidence | [LLM tracing](https://deepeval.com/docs/evaluation-llm-tracing) |
| Runner flags and reporting | [Flags and configs](https://deepeval.com/docs/evaluation-flags-and-configs), [CI/CD](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd), [local storage](https://deepeval.com/docs/evaluation-local-backend-storage) |

For gates, artifacts and failure triage, read [CI and reporting](ci-and-reporting.md).

## Sources and fit

This playbook is original integration guidance informed by DeepEval's test-case, dataset, metric, tracing and CI documentation, and by the official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills), reviewed as a reference. Their mandatory intake, synthetic-generation preference, hosted-service preference and fixed iteration defaults are not adopted. Concepts here are stable; exact API names, parameters and flags must be checked against the installed release.
