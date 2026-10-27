# Evaluation roadmap

This roadmap identifies improvements needed to make skill and plugin evaluations repeatable, reviewable and useful for regression decisions. It is for maintainers choosing the next investment. The priorities below are proposed; they carry no delivery dates or claim of implementation. Keep implementation tasks and progress in linked issues or PRs.

Use the [evaluation guide](evaluations.md) for the current method and evidence limits, and the [scenario catalogue](../../evals/development-workflows.json) for defined behavior and generation cases.

## Current position

The collection has a documented evaluation method, scenario definitions and recorded trials. Behavioral probes are manually prepared, dispatched and assessed. CI validates definitions and packages; it does not rerun those agent trials. Records retain useful evidence but vary in format, and some targeted probes are recorded outside the main catalogue. The collection has not received a complete behavioral rerun at its current revision.

## Priorities and completion evidence

| Priority | Intended improvement | Evidence needed to consider it delivered |
| --- | --- | --- |
| 1. Consistent cases and records | Give reusable probes stable case IDs, versioned raw fixtures and a shared result format. Link the [product/AI follow-up probes](../../evals/results/authoring-methods/editorial-probes/assessment.md) into the catalogue. Record effective guidance identity, harness/model configuration when exposed, capabilities, criteria, artifacts, interventions and evidence limits. | A validator checks case/result references and required fields. New records distinguish pass, fail, partial, blocked and not-run per criterion. Historical records retain their original uncertainty; missing facts are not reconstructed as observations. |
| 2. Repeatable execution | Provide a documented way to run a selected case against pinned guidance and fixtures in a fresh workspace/context. Keep actor inputs separate from grader criteria. Bound time, resource use, external effects and cleanup. Start with a supported execution environment before adding client adapters. | Another maintainer can invoke the same case and inspect its inputs, outputs and execution boundary without reconstructing the original conversation. Interrupted runs preserve available artifacts and an honest incomplete status. Repeatability does not require identical model output. |
| 3. Trustworthy assessment | Use executable assertions for observable properties and explicit rubrics for judgment. Separate the acting agent from assessment, add independent review where consequential, and calibrate judgments against reviewed examples. | Results cite actual artifacts or exercised outcomes. Reviewer disagreements and false positives remain visible. Application claims use runtime and persisted-state evidence; visual claims use rendered evidence. Agent self-ratings cannot establish success. |
| 4. Meaningful comparisons | Compare candidate and baseline guidance under comparable inputs, tools, permissions and model settings. Use repeated runs and unfamiliar cases where they add confidence. Record unavoidable differences. | Reports retain failures and per-case outcomes, describe variation and avoid unsupported causal or reliability claims. Latency and usage/cost include failed attempts and recovery when available; unavailable measurements stay explicit. |
| 5. Current workflow and client coverage | Prioritize affected flows and important gaps: workflow-only use, absent-specialist fallback, installed-client discovery/routing, UI journeys, persistence/authority, extension/native lifecycle and protocol/provider interoperability. Keep bounded probes and full application trials distinct. | A coverage view links each exercised claim to its guidance revision, case, environment and evidence. Defined, executed, blocked and unverified coverage remain distinguishable; a full rerun is reported only after its intended scope is exercised. |
| 6. Proportionate CI integration | Automate record/fixture validation and affordable deterministic regressions first. Add behavioral jobs only with explicit triggers, supported capabilities and execution budgets. Gate credentialed, costly and live-target checks separately. | CI reports exactly what ran and why something was skipped or blocked. Required checks cannot become successful merely because execution was unavailable. Passing probes do not authorize publication or merge. |

## Sequence and upkeep

Establish case/record conventions before building the runner around them. Develop assessment criteria alongside that work, then use repeatable runs for comparisons and broader client/application coverage. Add CI execution after its local behavior and resource boundaries are understood; existing definition and package checks continue throughout.

Keep [actor/grader separation, action scope and evidence rules](evaluations.md#run-and-grade-a-scenario) in force at every stage. Turn observed failures into general guidance or meaningful regressions, preserving acceptable alternative solutions. Retire or revise cases when supported behavior changes, with the reason retained in review history.

Update this roadmap when priorities change or completion evidence becomes available. Move delivered behavior into the evaluation guide and link its evidence, keeping this page focused on remaining outcomes rather than a release history or duplicate task tracker.
