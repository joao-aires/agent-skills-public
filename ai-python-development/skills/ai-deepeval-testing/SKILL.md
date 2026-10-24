---
name: ai-deepeval-testing
description: Implement Python AI evaluation suites with DeepEval for model, retrieval, agent trajectory, conversation and end-to-end quality. Use when DeepEval is selected or being evaluated; preserve existing evaluation tools and do not introduce model calls, hosted reporting or synthetic generation without scope.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: Python, DeepEval, pytest
  role: support
---

# Implement Python AI evaluations with DeepEval

Use the accepted task, architecture and quality criteria. Seek available expertise in conceptual AI evaluation for case design and evidence boundaries; retain deterministic correctness, authority and meaningful quality evidence when that specialist is absent. This skill implements an evaluation approach in Python, not the product's acceptance policy or all application testing. The evaluation runner can be Python while the application uses another language; do not migrate the application to run a suite.

## Choose a compatible, bounded integration

Inspect the project's Python/dependency constraints, existing tests, datasets, metrics, model/judge settings and CI. Use a locked compatible DeepEval version in the established test/development dependency group. Preserve an accepted alternative unless comparing or migrating is requested. Consult the [DeepEval evaluation guide](https://deepeval.com/docs/evaluation-introduction) for the selected release's API; documented examples do not establish installed compatibility.

Map the accepted evaluation levels to supported DeepEval APIs. Use output cases for bounded inference, component/trajectory APIs where internal execution matters and conversation cases for supported multi-turn evaluation. Instrument only the relevant path with the existing tracing owner. A protocol-only service may need compatibility checks without DeepEval.

## Map actual artifacts to test cases

Keep input scenarios/goldens, expected outcomes/rubrics and test results distinct.

| Evidence or input | Compatible DeepEval representation |
| --- | --- |
| Single-turn input/output | `LLMTestCase` |
| Supported multi-turn evaluation | `ConversationalTestCase` |
| Rerunnable input collection | `EvaluationDataset` and `Golden` where appropriate |

Choose the interaction being evaluated, then collect its actual inputs and results. At application level, this may be the user's request and final response; at a component level, it is the input and output of that component. Keep the case at a consistent scope so the metric is judging the behavior intended by the test.

Supply the fields the chosen metric needs from the real run. Distinguish evidence that should have been available from evidence the retriever actually returned, and expected tool behavior from the tools actually used. Otherwise a grounded-answer score or tool score can be based on a reconstructed ideal rather than the execution being assessed. Match the field requirements to the installed API and metric documentation. Invented outputs establish only a fixture.

Adapt curated cases and held-out regressions to the selected dataset API without replacing the authoritative case source. Synthetic generation and conversation simulation are optional, credentialed execution paths; preserve agreed scope and review generated goldens before using them as acceptance evidence.

Select metrics for the property: task correctness/usefulness, retrieval/grounding, appropriate tools/trajectory or conversation outcomes. Use a custom rubric such as `GEval` only with explicit evaluation parameters and calibrated judgments. Inspect the metric's required fields, judge/provider, threshold and failure behavior against [metric documentation](https://deepeval.com/docs/metrics-introduction). A safety or business-authority invariant stays an exact application assertion, outside the judge.

## Control execution and data movement

Configure the evaluated application model and evaluation judge separately.

- Many metrics and synthetic/simulation paths make model calls even when the application's output was recorded; inspect defaults before running.
- Set agreed providers, limits, concurrency, timeouts/retries and credentials through the project's configuration.
- Missing access leaves that quality boundary unverified, not passing.

Keep local results reproducible without requiring a hosted dashboard. Confident AI reporting, hosted datasets/traces and online evaluation are separate selected integrations with account, retention, region and data-sharing decisions. Check the library's reporting/storage configuration and active credentials before execution; do not log in or upload cases merely to run a local suite. Redact private inputs at source and in failure artifacts.

## Wire meaningful checks into CI

Use DeepEval's supported `evaluate()` route for evaluation scripts or `assert_test()` with `deepeval test run <existing-eval-path>` for a committed pytest-style evaluation suite. Follow the [CI guide](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) for the installed version; do not treat ordinary pytest collection as proof that the DeepEval run completed.

Separate fast deterministic tests from credentialed quality jobs.

- Define when each suite runs, its limits and required gates, and preserve exact application/prompt/model/judge/dataset/metric revisions.
- Run live jobs only in trusted contexts with authorized data and secrets.
- Keep per-case failures, reasons, denominators, variability and latency/usage evidence.
- Verify exit status and result completeness; skipped/error/flaky results must remain visible and cannot silently bypass a required criterion.

After a change, run the relevant deterministic suite and authorized quality comparison. Inspect representative failures and make scoped repairs without weakening criteria, thresholds or holdouts to pass. Report fixture versus live evidence, executed levels and remaining gaps. Instrumentation and a passing metric do not establish protocol interoperability, persisted user outcomes or production quality.

## Sources and fit

This is original integration guidance based on DeepEval's evaluation, metrics and CI documentation. The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) were reviewed as references; their mandatory intake, synthetic-generation, hosted-service preference and fixed iteration defaults are not adopted. Check current primary API guidance when implementing a project integration.
