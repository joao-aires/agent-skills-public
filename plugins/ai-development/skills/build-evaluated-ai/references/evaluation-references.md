# Evaluation evidence

Keep datasets, expected outcomes and deterministic evaluators runnable in the application without a hosted service. Identify code/model/prompt/tool, dataset and evaluator revisions. Retain per-case failures, denominators, sample size, variability and relevant latency/usage boundaries. A dashboard is a view of evidence, not its source of authority.

Calibrate subjective grading against accepted human examples. Keep authorization, schema, side-effect and failure invariants deterministic even when a model judge rates quality highly. Observed execution signals explain what ran and how it failed; they cannot establish answer usefulness on their own. Use available observability methods for signal contracts and selected technical guidance for SDK/backend setup.

## Speech evaluation

Select representative languages/dialects, recording devices/conditions, noise, silence and domain vocabulary from the actual product. For Portuguese, include the intended Portuguese variants rather than assuming one dialect represents all speakers. Assess recognition errors and preservation of consequential terms; use word error rate when suitable alongside task usefulness. A fixture transcript cannot establish live quality. Uploaded-audio success cannot establish streaming latency, turn-taking or interruption.
