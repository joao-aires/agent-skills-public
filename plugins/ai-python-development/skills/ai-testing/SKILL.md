---
name: ai-testing
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

Choose a simple output-based evaluation for a bounded task. Use component or trajectory evaluation when a multi-step agent needs diagnostic evidence; instrument only the relevant path and coordinate the existing tracing owner. Use conversation cases for multi-turn behavior. A protocol-only service may need deterministic compatibility checks without a judge or model evaluation.

## Map actual artifacts to test cases

Keep input scenarios/goldens, expected outcomes/rubrics and test results distinct. Use `LLMTestCase` for single-turn input/output evidence and `ConversationalTestCase` for supported multi-turn evaluation. `EvaluationDataset` and `Golden` can organize rerunnable inputs. Populate cases from the actual application run, including relevant retrieved context and tool evidence supported by the installed API; invented outputs establish only a fixture.

Retain curated task cases, held-out regressions and privacy-reviewed failure examples in the project's existing format. Synthetic generation and conversation simulation are optional, require their own execution/data authorization, and need human/domain review before becoming acceptance evidence. Do not default to a fixed dataset size or repeated paid generation loop.

Select metrics for the property: task correctness/usefulness, retrieval/grounding, appropriate tools/trajectory or conversation outcomes. Use a custom rubric such as `GEval` only with explicit evaluation parameters and calibrated judgments. Inspect the metric's required fields, judge/provider, threshold and failure behavior against [metric documentation](https://deepeval.com/docs/metrics-introduction). A safety or business-authority invariant stays an exact application assertion, outside the judge.

## Control execution and data movement

Configure the evaluated application model and evaluation judge separately. Many metrics and synthetic/simulation paths make model calls even when the application's output was recorded; inspect defaults before running. Set agreed providers, limits, concurrency, timeouts/retries and credentials through the project's configuration. Missing access leaves that quality boundary unverified, not passing.

Keep local results reproducible without requiring a hosted dashboard. Confident AI reporting, hosted datasets/traces and online evaluation are separate selected integrations with account, retention, region and data-sharing decisions. Check the library's reporting/storage configuration and active credentials before execution; do not log in or upload cases merely to run a local suite. Redact private inputs at source and in failure artifacts.

## Wire meaningful checks into CI

Use DeepEval's supported `evaluate()` route for evaluation scripts or `assert_test()` with `deepeval test run <existing-eval-path>` for a committed pytest-style evaluation suite. Follow the [CI guide](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) for the installed version; do not treat ordinary pytest collection as proof that the DeepEval run completed.

Separate fast deterministic tests from credentialed quality jobs. Define when each suite runs, its limits and required gates, and preserve exact application/prompt/model/judge/dataset/metric revisions. Run live jobs only in trusted contexts with authorized data and secrets. Keep per-case failures, reasons, denominators, variability and latency/usage evidence. Verify exit status and result completeness; skipped/error/flaky results must remain visible and cannot silently bypass a required criterion.

After a change, run the relevant deterministic suite and authorized quality comparison. Inspect representative failures and make scoped repairs without weakening criteria, thresholds or holdouts to pass. Report fixture versus live evidence, executed levels and remaining gaps. Instrumentation and a passing metric do not establish protocol interoperability, persisted user outcomes or production quality.

## Sources and fit

This is original integration guidance based on DeepEval's evaluation, metrics and CI documentation. The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) were reviewed as references; their mandatory intake, synthetic-generation, hosted-service preference and fixed iteration defaults are not adopted. Check current primary API guidance when implementing a project integration.
