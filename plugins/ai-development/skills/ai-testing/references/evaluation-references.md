# Evaluation evidence

Keep datasets, expected outcomes and deterministic evaluators runnable in the application without a hosted service. Identify code/model/prompt/tool, dataset and evaluator revisions. Retain per-case failures, denominators, sample size, variability and relevant latency/usage boundaries. A dashboard is a view of evidence, not its source of authority.

Calibrate subjective grading against accepted human examples. Keep authorization, schema, side-effect and failure invariants deterministic even when a model judge rates quality highly. Observed execution signals explain what ran and how it failed; they cannot establish answer usefulness on their own. Use available observability methods for signal contracts and selected technical guidance for SDK/backend setup.

## Evaluate the relevant levels

Derive levels from the architecture and the user's outcome; a simple bounded feature may need only a few. Keep acceptance at each boundary explicit and select technical evaluators only for the accepted implementation.

| Level | Question and evidence | Limit |
| --- | --- | --- |
| Deterministic unit/component | Do schemas, policies, parsers, tool effects, isolation and failure handling satisfy invariants? Use fixtures and exact service-state assertions. | No claim about live model quality |
| Model/retrieval component | Does a prompt, retriever, ranking step or generator meet the intended task and grounding criteria on representative cases? | A strong component can still fail in the composed system |
| Protocol/runtime integration | Can actual compatible peers discover, exchange events, resume state and execute authorized actions correctly? | Self-defined schemas and replay fixtures do not establish interoperability |
| Agent trajectory | Does the sequence of decisions/tools/handoffs reach the right outcome within allowed authority and budgets, including recovery? | Exact tool order is only an invariant when the task requires it |
| Conversation or multimodal interaction | Does the system preserve context, follow corrections, ask useful questions and handle modality/turn-taking constraints? | A simulated user or uploaded recording does not establish live participant or real-time experience |
| End-to-end product journey | Can a user complete the accepted task through the real interface with correct persisted state, access control and understandable failures? | A final answer, trace or aggregate metric alone is insufficient |
| Operating/online quality | Do privacy-approved samples, feedback and incidents reveal drift or regressions after release? | Sampled telemetry is not complete coverage or a substitute for held-out release evidence |

Use cheap deterministic checks routinely. Run bounded quality experiments when behavior changes, broader held-out comparisons for consequential model/prompt/retrieval/tool changes, and appropriately sampled online evaluation when authorized. Avoid requiring every expensive layer on every commit. Keep simulated, offline-recorded, live-provider and production evidence labelled separately.

Score outcome correctness/usefulness separately from safety, authority, grounding, latency and cost. Choose exact assertions, reference/semantic measures, domain-specific checks, calibrated model judges or human assessment according to the property. Do not turn optional tool order, wording or a preferred implementation into the expected answer. Confidence/sample size, case-level failures and important user slices matter alongside averages; rare consequential failures may need explicit acceptance gates.

Technical evaluation frameworks implement this model; they do not define the product's acceptance or replace deterministic service/protocol tests. Seek available implementation expertise for the selected evaluation library. Operational instrumentation supplies execution evidence and context for failures; scoring usefulness is a separate activity even when one platform supports both.

## Speech evaluation

Select representative languages/dialects, recording devices/conditions, noise, silence and domain vocabulary from the actual product. For Portuguese, include the intended Portuguese variants rather than assuming one dialect represents all speakers. Assess recognition errors and preservation of consequential terms; use word error rate when suitable alongside task usefulness. A fixture transcript cannot establish live quality. Uploaded-audio success cannot establish streaming latency, turn-taking or interruption.

## Define and run a useful evaluation

Select a small representative case set from the product task: normal inputs, ambiguity, malformed input, provider failure and relevant adversarial cases. Define acceptance thresholds before comparing candidates. Use agreed criteria; if quality targets are not specified, state provisional targets and uncertainty rather than silently inventing a product commitment.

Separate two kinds of evidence:

- **Deterministic application checks:** fixtures for contracts, authorization, invalid output, retries, limits and failure presentation. Run these routinely in CI; mocks prove application handling, not model quality.
- **Live quality evaluations:** explicit calls with representative inputs, recording model/prompt version, quality results, latency, usage/cost where available and sample size. Keep credentials/data and execution within the authorized scope. Inspect errors rather than inferring quality from a few attractive examples.

For speech, evaluate the product's languages/dialects, recording conditions and important domain terms. Match the method to the capability: uploaded-file transcription and streaming/interruption require different evidence. Use the speech measures above when relevant.

## Close the evaluation loop

Keep representative inputs, expected outcomes/rubrics, dataset revision and deterministic evaluators under application version control. Separate development examples from held-out regression cases where useful; do not tune only to the examples used to build the feature. Derive cases from accepted product behavior, include meaningful failure/adversarial conditions and preserve privacy when promoting observed failures into fixtures. No external dataset service or record format is required.

After meaningful AI changes run deterministic handling checks, then authorized live quality comparisons when relevant. Record code/model/prompt/tool configuration and dataset/evaluator versions, sample size, per-case failures, latency and usage alongside quality. Repeat stochastic cases sufficiently for the decision and report variability; one favorable generation or aggregate score cannot hide failed authority/task constraints. Calibrate model judges against accepted human examples, include human review for unresolved subjective judgments and keep deterministic invariants outside the judge. Do not silently change expected outputs, thresholds or rubrics to pass. Mocks establish application behavior only.

Keep evaluation runnable without a dashboard. Instrument logical task and tool outcomes where useful, protect sensitive data and use available matching technical guidance for SDK/observability integration. Missing provider access leaves live quality unverified.
