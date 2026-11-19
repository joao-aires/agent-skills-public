# Observability and monitoring in design

Observability is a design property: the system must emit enough trustworthy, well-identified signals for its owners to tell whether the accepted outcome happened, where it failed and what work remains unfinished. This reference decides the signal and outcome model, the measurement points and the pipeline boundary. It does not implement instrumentation, own an incident response or run the recurring telemetry review.

Read [reliability](reliability.md) for outcome targets, SLIs and error budgets, [maintainability](maintainability.md) for diagnosability as an operating property, and [security](security.md) for data exposure across trust boundaries.

## Start from the outcome

Choose the question first, then the signal:

- Which user or machine outcome must be observable — a completed journey, a delivered event, a reconciled job, a rendered result?
- Which failures would look identical from outside if no signal existed?
- Which stage or dependency would an operator need to distinguish during those failures?
- What must remain true when telemetry itself is degraded?

Separate three levels that are often conflated:

| Level | Meaning | Example |
| --- | --- | --- |
| Outcome | The user or consumer got the promised result | Order confirmed and visible to the customer |
| Technical handling | The service processed the request or event as intended | Accepted, validated, committed, enqueued |
| Infrastructure diagnosis | The platform and dependency state that explains behavior | CPU saturation, connection-pool exhaustion, provider timeout |

A green infrastructure signal is not a green outcome. A correctly rejected invalid request is good technical handling but not a completed journey.

## SLIs and measurement points

An SLI describes what matters independent of a tool; its implementation says how it is observed. Requirements and the [ECR](../../artifact-system/references/contracts/ecr.md) own targets and acceptable error budgets. Read [journey to SLO](journey-to-slo.md) for derivation, arithmetic and worked examples.

For each indicator, decide:

- **Population.** Which eligible work enters the denominator, including work that started and never finished.
- **Measurement point.** Where the signal is observed: real client, edge or gateway, service, dependency, queue and worker, or reconciled durable state.
- **Timer and completion.** When the clock starts, when it stops, and what happens at a deadline or after a cancellation.
- **Units and identity.** What one event means, which service, environment, version and journey it belongs to, and how duplicates are counted.
- **Coverage.** Which users, clients, regions and paths are represented, and which are missing.
- **Missing-data rule.** What an absent series, zero traffic or failed pipeline means. It is unknown, not healthy.

A measurement point near the user is faithful but incomplete; a server counter is precise but blind to requests that never arrive. State the blind spot rather than implying full coverage. Do not average ratios with unequal traffic, and do not multiply component availability to claim journey availability without justified dependence and correlation assumptions.

## Instrumentation points

Name where the signal is produced, not which SDK to call:

- the request or message admission boundary, with identity and population attributes;
- state transitions and the completion point, including denial, timeout and cancellation;
- worker and queue stages, including retry, dead-letter and reconciliation;
- external dependency calls, with outcome, duration class and the provider's own failure;
- authorization and tenancy denials, distinguishable from broken behavior;
- configuration, version and environment identity at every emitted signal.

Keep correlation context across synchronous and asynchronous boundaries. Use bounded attributes: identifiers for traces and diagnostic records, bounded dimensions for metrics. Do not put request IDs, user IDs, URLs or exception text into metric labels.

Instrumentation implementation — libraries, exporters, collector configuration and schema tests — belongs to the implementing activity for the selected stack. This reference decides the contract it must satisfy.

## Telemetry pipeline boundaries

Define who owns each stage of the path from application to query:

| Stage | Design decides | Owner |
| --- | --- | --- |
| Emission | Which signal, at which stage, with which identity and meaning | Application or service owner |
| Collection and processing | Where buffering, sampling, redaction and translation happen; which pipeline owns each signal | Platform or observability implementation |
| Storage and query | Retention, access, sampling differences and query population | Platform and backend owner |
| Use | Which question, dashboard, alert or review the signal serves | Reliability, incident response or operations review |

Rules that keep the boundary honest:

- Keep application instrumentation separate from backend routing, credentials and storage configuration.
- A collector can redact defensively, but sensitive data must not be captured at source. Collector masking is secondary.
- Telemetry failure must not break the user journey; bound buffers and retries, expose drops and define degraded behavior.
- Do not run competing SDKs or exporters that duplicate spans or create ambiguous populations.
- Client and edge telemetry needs a controlled ingestion boundary, rate limits and source redaction; never ship privileged backend credentials or sensitive payloads to a client.

## Retention, privacy and cost

Telemetry is data with a lifecycle:

- classify it: personal data, secrets, financial payloads, sensitive query strings, model input and output;
- decide retention by purpose — debugging, SLO evidence, audit, security investigation, product analysis;
- state where sampling reduces fidelity and where it biases the population;
- decide access scope and deletion behavior for each store;
- connect volume to cost: cardinality, traces, logs, retention and cross-region copies are cost drivers, not free byproducts.

Read [cost planning](cost-planning.md) for the cost driver and attribution; read [contextual attributes](contextual-attributes.md) when residency or contractual retention applies. Apply the accepted data-classification and privacy requirements rather than inventing a retention period.

## Verify that signals are meaningful

A declared signal is not a working one. Plan evidence that can contradict it:

- exercise a representative success and a controlled failure through the actual path;
- check span relationships and context propagation across request, worker and dependency boundaries;
- assert the emitted telemetry at an inspectable export or test boundary;
- confirm receipt and query in the selected backend when available;
- check that absence, sampling and pipeline failure produce an honest unknown, not a green result;
- verify that a query gives the same population and units that the SLI claims.

Separate locally instrumented, exported and backend-verified states. A dashboard that renders is not evidence that the signal is complete, and a schema test does not prove the production pipeline.

## Boundaries and handoff

- **SLO targets and error budgets** come from requirements and [reliability](reliability.md); this reference does not invent a target.
- **Incident response and runbooks** own detection, escalation, mitigation and recovery procedure; use [run-incident-response](../../run-incident-response/SKILL.md) and [runbook guide](../../guide-runbook/SKILL.md).
- **Recurring telemetry hygiene** — missing fields, drift, redaction regressions, pipeline cost — belongs to [recurring operations review](../../run-operations-review/SKILL.md).
- **Instrumentation and pipeline implementation** belong to the implementing activity for the accepted stack.

Return the outcome model, the SLI and measurement points, the instrumentation contract, the pipeline boundary, the retention and privacy decisions, and the verification plan. Mark what is designed, implemented and verified separately. An optional implementation reference for declarative monitoring exists in [Terraform monitoring](terraform-monitoring.md); current provider validation is still required.
