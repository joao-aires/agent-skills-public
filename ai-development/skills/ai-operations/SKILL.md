---
name: ai-operations
description: Define and improve AI operating behavior across task observability, quality monitoring, latency/cost, provider limits, drift, rollout and recovery. Use for AI production readiness, operational diagnosis or learning from live behavior independently of a language, telemetry SDK or monitoring backend.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Operate AI capabilities against user outcomes

Use the accepted task, architecture, authority and operating constraints. This method owns AI-specific operational decisions and evidence, not SDK initialization, a monitoring vendor or all incident/deployment procedures. Reuse established service operations and seek relevant reliability, capacity, security or delivery expertise when available; absence does not remove responsibility for the affected outcome. Planning an operating change does not authorize live mutation or data export.

## Define meaningful operating signals

Begin at the user task and follow the work needed to finish it. Record enough to tell whether the request was admitted, the model responded, a tool acted, and the intended result was completed. These events can disagree: a provider response may be valid while the task fails, and a timeout may occur after a tool effect has already committed.

Use that separation to choose operating signals. Measure delays where they arise, preserve the identity of unfinished work, and distinguish execution failure from a quality judgment about a completed result. This makes it possible to diagnose a regression without treating every poor answer as a provider outage.

- Relate success/failure, latency and freshness to the actual user journey.
- Define useful denominators, time windows and candidate or approved targets; do not promise an SLO or quality threshold without acceptance.
- For interactive work, distinguish first useful output, full completion and interruption/cancellation behavior.

Make the deployed application, model/provider, prompt, tool/skill, retrieval/corpus and protocol configuration revisions identifiable. Correlate request/task, model, retrieval, tool and delegated work through supported execution context; retain gaps for opaque remote peers rather than inventing a complete trajectory. Choose signal detail and sampling for the decisions they support, including the risk of missing rare consequential failures.

## Control resource, provider and recovery behavior

Account for quotas, rate limits, concurrency, context/token budgets and end-to-end cost, including retries, judges, retrieval and delegated work. Separate estimates from measured usage and use relevant operating/capacity expertise for resource planning. Provider success or nominal per-call price cannot establish useful task throughput or total cost.

Read [performance and resource decisions](references/performance-and-resources.md) when investigating latency, selecting an optimization or budgeting a multi-call task. Locate the constraint before choosing smaller outputs, different reasoning, caching or concurrency. Their benefit depends on the workload, quality requirements and actual service capabilities.

Bound retries and work duration; handle overload, cancellation, partial effects and resumable state.

- Keep idempotency and business state authoritative outside the model.
- Choose fallbacks against accepted quality, licensing, data handling and authority constraints; silently switching providers/models or replaying side effects can change the product contract.
- Use degradation or a controlled error when a safe accepted fallback is unavailable.

For incidents, supply the affected task/configuration revision, known effects, scope and diagnostic evidence to the existing response process. Seek appropriate incident, security and recovery expertise rather than duplicating those procedures. Containment or rollback stays within established authorization and must preserve auditability and known committed effects.

## Observe without exposing task content

Prefer operational metadata over raw prompts, completions, documents, tool arguments/results, recordings or internal reasoning.

- Content capture needs an accepted purpose, appropriate access, redaction, sampling, retention and deletion.
- Protect data before recording/export, and make collection limits or missing signals visible.
- Avoid unbounded metric dimensions and sensitive identifiers where aggregated signals suffice.

Seek implementation expertise matching the actual runtime and selected telemetry/backend. Preserve instrumentation ownership and existing destinations; prevent duplicate signals, incompatible conventions and disruptive overhead. An AI observability platform may combine traces, experiments and scoring, but installing it is not required for these outcomes and does not establish data-use authorization.

## Learn from quality and behavior changes

Use privacy-approved samples, user corrections and incidents to detect changes in usefulness, grounding, retrieval freshness, refusals, tool behavior, latency or cost.

1. Compare meaningful user/data slices with identifiable baselines, accounting for sampling bias and changed traffic.
2. Investigate whether the regression comes from application/configuration, model/provider, corpus, tool or environment changes before choosing a repair.
3. Use available evaluation expertise to assess quality and promote useful failures into representative regression cases.

Traces describe what ran; they do not alone establish correctness or usefulness. Keep online scores, offline held-out evaluation and actual user feedback distinguishable, including their population, uncertainty and permissions.


## Release and recover reproducibly

Version and promote the compatible application/model/prompt/retrieval/tool configuration with the relevant evidence. Define readiness, staged exposure where useful, rollback/roll-forward conditions and state/data compatibility through the project's delivery process. External provider behavior can change without an application deployment; retain a way to identify the effective configuration and respond to material change.

Verify the affected user outcome and real received/queryable signals at the authorized target. Check telemetry loss/overhead and failure isolation when material. Configuration or SDK startup does not establish collection, and sampled observations do not establish complete coverage.

Report actual operating evidence, known blind spots and next actions; keep runbooks and recovery assumptions current.
