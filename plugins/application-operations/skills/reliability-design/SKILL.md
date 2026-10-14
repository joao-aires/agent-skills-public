---
name: reliability-design
description: Analyze user journeys and system dependencies to define, implement, and
  review SLIs, SLOs, error budgets, dashboards and actionable monitoring for new systems,
  features or recurring reliability reviews.
metadata:
  scope: generic
  invocation: both
  version: '1.0'
  role: task
---

# Reliability design

Start with a user outcome, derive a measurable contract, then implement the monitoring. Do not start with whatever metric is easiest to query and call it journey reliability.

## Inputs and execution mode

Discover the target, architecture, relevant feature/critical journeys, current telemetry, existing objectives, owners and operational policy. Use code, docs, rendered configuration and live evidence when available. Work with partial sources but label coverage and semantic decisions still needed.

- **Interactive:** analyze evidence before asking; ask targeted questions about users, acceptable outcomes, latency and budget decisions. Explain alternatives with diagrams and examples.
- **Setup/feature implementation:** produce a journey contract and implement its instrumentation/resource definitions, tests and documentation in the target stack. Keep changes compatible with existing consumers.
- **Recurring review:** compare changed flows and incidents with current contracts, identify uncovered outcomes and telemetry drift, update evidence-backed definitions within assigned policy, and prepare bounded patches. Do not automatically relax targets or suppress pages to make compliance improve.

## Derivation workflow

1. Identify the users (human or machine), intent/start boundary, observable completion, failure/cancellation/rejection branches, deadline, and important segments.
2. Draw an evidenced architecture and Mermaid sequence. Include browser/client code, cached paths, external providers, retries, async work, and dependencies required for the outcome. Use `system-mapping` if discovery is needed, or perform the relevant mapping directly.
3. Classify request-driven, storage and processing stages. Choose a small set of dimensions: availability, latency, quality, freshness, coverage, correctness or durability.
4. Write an **SLI specification** in outcome terms. Separate technical handling from conversion/business acceptance and infrastructure diagnostics.
5. Define the **implementation contract**: valid event population, good-event subset, observation point, timer, units, deduplication, retries, terminal/deadline attribution, tags, queries and missing-data behavior.
6. Compare possible observation strategies by user-experience fidelity, coverage, cost, latency and collection reliability. Name blind spots, consent/sampling bias and requests that never reach instrumentation.
7. Choose targets/windows from user needs and measured defensibility. Label initial hypotheses and aspirational targets. Document owner agreement and an error-budget decision policy; targets are product decisions, not arbitrary agent defaults.
8. Define symptom alerts and useful predictive risk alerts. Determine responder/action/runbook, scope, routing, no-data policy, timing and recovery. Prefer multiwindow burn rates where appropriate; validate low-traffic and extreme-target behavior.
9. Implement metric/monitor/SLO/dashboard definitions using the target's tools. Add missing instrumentation with `observability-operations` or directly. Keep SLO populations consistent with their indicators; label intentionally different operational proxies.
10. Validate with fixtures, historical incidents/quiet periods and live signal samples. Soak new pages silently when local practice permits, with a review date. Confirm notification and runbook reachability before marking operational.

## Optional deeper references

- [Journey to SLO](references/journey-to-slo.md): theory, diagrams, worked examples, arithmetic, contract template and acceptance cases.
- [Terraform monitoring](references/terraform-monitoring.md): optional Datadog implementation architecture and lessons; current provider validation is still required.

## Invariants

Good events are a subset of valid events from the same population/window. Sum event counts before division for an event SLI; do not average unequal-traffic ratios. Do not multiply endpoint availability to claim journey availability without justified dependency and correlation assumptions.

Started-but-never-finished work needs deadline/coverage accounting; success among terminal events alone hides stuck work. Correctly rejecting invalid input may be a good technical outcome but is not completed purchase or rendered content. An absent series, zero traffic, or failing telemetry pipeline is not a green SLI.

## Completion evidence

Deliver journey diagrams, SLI/SLO contracts, implementation changes, coverage gaps, alert rationale, validation results and outstanding owner decisions. Track specification agreed, implemented, signal verified and alert operational separately. Recurring reports retain stable finding IDs and previous dispositions and can legitimately conclude no change is needed.
