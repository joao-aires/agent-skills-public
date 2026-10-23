# Evaluation evidence

Use this reference when choosing evaluation levels, cases or graders. Begin with the property the application needs to demonstrate and select evidence that can actually observe it. Keep datasets, expected outcomes and deterministic evaluators runnable in the application without a hosted service; a dashboard can help inspect results without becoming their source of authority.

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

Choose a level to answer a question. Component evaluation helps locate a weakness; the product journey checks whether the composed system serves the user. Protocol evidence establishes exchange with compatible peers; it does not establish that a generated answer is useful. Keep those interpretations in the result so a strong score at one level is not used to conceal a gap at another.

## Make acceptance specific enough to judge

Describe the successful outcome in terms of the task. Identify consequential factual requirements, permitted uncertainty, grounding, failure/refusal behavior and actions the system may take. Separate these properties so a fluent or relevant answer cannot compensate for an unauthorized effect or a materially false claim.

Choose exact assertions for application facts and invariants. Use reference-based or semantic measures when several expressions can satisfy the same result. For a subjective rubric, describe the distinctions the grader needs to make and which evidence it may use. Calibrate a model judge against accepted human assessments, including borderline results and failures, and inspect disagreements before treating its scores as a gate. Keep unresolved subjective acceptance with human review.

Give rare consequential failures explicit acceptance conditions when an average would hide them. Keep representative inputs, expected outcomes/rubrics, dataset revisions and deterministic evaluators under application version control.

Set thresholds before comparing candidates. Where quality targets are not settled, state provisional targets and their uncertainty rather than inventing a product commitment. Do not silently change expected outcomes, rubrics or thresholds while repairing a failed result.

## Build cases that discriminate useful behavior

Select representative user tasks and data slices, then include the variation that could change the result: ambiguity, missing or conflicting evidence, malformed input, provider/tool failure and relevant adversarial conditions. Preserve the inputs separately from expected outcomes and actual execution results. Keep enough context to understand why a case matters, without collecting unnecessary personal data.

Use development cases to inspect and improve the behavior. Retain held-out cases to assess whether the change generalizes beyond the material used to build it. Review synthetic cases for task fit and correctness before using them as evidence. Promote useful observed failures into privacy-preserving regressions, retaining the principle they test rather than copying private content.

## Run a comparison the decision can support

Identify the application, model, prompt, retrieval/context and tool configuration, along with dataset and evaluator revisions. Compare candidates on the same relevant inputs and conditions. Inspect case-level failures and important slices alongside the aggregate so a gain on common easy tasks does not hide a consequential regression.

Retain denominators, sample size and variability. Repeat stochastic cases enough to support the decision; one favorable generation does not establish reliability. Include measured latency and usage/cost where they affect acceptance, labelling estimates and missing values. Inspect execution failures and skipped cases before interpreting quality scores.

Define a useful outcome before calculating efficiency. Include failed and recovery attempts in the resource accounting; reporting latency only for accepted responses can conceal a candidate that fails more often. Keep per-attempt measurements alongside job-level completion and quality. A prompt, model, reasoning setting and response format changed together cannot establish which one caused an improvement or failure. Use paired or interleaved runs where useful, record relevant queue/cache conditions and keep the conclusions proportional to the sample.

Choose measures that expose the task's tradeoffs. Abstaining on every case can appear safe while serving nobody; a fluent response can appear helpful while inventing evidence. Assess the relevant coverage, correctness and usefulness separately, allowing multiple acceptable results when the task permits them. Exact grouping, extraction or retrieval measures belong to the application's evaluation rather than becoming requirements for unrelated AI features.

Keep execution modes explicit:

- Deterministic fixtures establish how the application handles supplied outcomes, failures and authority conditions. Run cheap checks routinely in CI.
- Recorded outputs establish the behavior of the recorded application run. Scoring them can still require live judge calls.
- Live provider comparisons establish quality under the evaluated configuration and inputs, within the authorized data, credential and cost scope.
- Authorized production samples provide operating evidence for their observed population. Sampling and traffic changes limit comparisons with offline results.

Run bounded quality experiments during behavior changes and broader held-out comparisons for consequential model/prompt/retrieval/tool changes. Avoid requiring every expensive level on every commit. Missing provider or judge access leaves the relevant quality boundary unverified.

## Speech evaluation

Select representative languages/dialects, recording devices/conditions, noise, silence and domain vocabulary from the actual product. For Portuguese, include the intended Portuguese variants rather than assuming one dialect represents all speakers. Assess recognition errors and preservation of consequential terms; use word error rate when suitable alongside task usefulness.

Match the observation to the interaction being promised. A fixture transcript cannot establish live recognition quality. Uploaded-audio success cannot establish streaming latency, turn-taking or interruption; those need the actual media/client/provider path and meaningful user-task observations.

## Close the evaluation loop

Classify failures by the part of the system that could explain them before selecting a repair. Compare the changed candidate against the accepted criteria and held-out cases, retaining useful regression evidence. Technical frameworks implement this method; they do not define the product's acceptance or replace deterministic service, protocol, accessibility and persistence checks.

Use execution signals to understand what ran, how it failed and which configuration was active. Use separate evaluation evidence to judge whether the result was correct and useful. Keep their identities linked where helpful without introducing a hosted dataset or observability service as a dependency of domain logic.
