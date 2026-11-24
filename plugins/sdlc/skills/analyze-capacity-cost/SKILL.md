---
name: analyze-capacity-cost
description: Analyze measured capacity and cost — demand and saturation, sizing, unit economics, FinOps allocation, forecasting, optimization evidence and verification. Use for a measured review of an existing or proposed system; capacity and cost plans, targets and accepted tradeoffs belong to design-system and the requirements record.
metadata:
  kind: method
  domain: operations
  phase: cross-phase
  scope: generic
  invocation: both
user-invocable: true
---

# Analyze capacity and cost from evidence

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Capacity asks whether the system can serve observed or projected demand with acceptable latency and failure behavior. Cost asks which resources deliver that outcome and at what measured spend. Both are analysis questions here. The demand plan, sizing decision, cost tradeoff and accepted budget belong to design and the requirements record; this method supplies and tests the evidence behind them.

[Design system](../design-system/SKILL.md) owns capacity and cost planning through its [capacity planning](../design-system/references/capacity-planning.md) and [cost planning](../design-system/references/cost-planning.md) references, and owns the design tradeoff. The ECR records the accepted decision. Provider-specific cost mechanics belong to installed platform expertise selected by capability, such as `aws-platform` or `operations-platforms`; do not import another provider's procedure.

## Establish the measured question

Name the service, journey, environment, population, time window, currency and billing period. State the claim under test: a saturation point, a sizing mismatch, a unit cost, a forecast variance or the observed effect of a change. Separate observation, estimate, forecast and projection. Missing telemetry means an estimate that needs validation, not a measurement. Do not set a target, invent a budget or select a plan.

## Analyze demand and saturation

1. Establish arrivals, service time and in-flight work with clear units. Include fan-out, retries, long-running AI or audio work, and slow providers that hold concurrency while local CPU is idle.
2. Inspect tail latency, queue depth and wait, throttling, memory peaks, database and storage limits, quotas and connection pools.
3. Locate the bottleneck on the full request path. Replicas can multiply connections and exhaust a shared dependency.
4. Compare sustained, peak and degraded demand using observed or explicitly stated conditions, not an assumed target.
5. Read [capacity analysis](references/capacity.md) for mechanics, Kubernetes behavior and measurement limits.

Scaling mechanics, resource requests and limits, autoscaler behavior and platform quotas are analysis objects when they affect the observed result. Choosing the scaling strategy belongs to design.

## Analyze cost, allocation and unit economics

1. Reconcile invoices, usage exports and billing periods. State currency, exchange-rate date, taxes, credits and commitments.
2. Attribute direct cost; expose shared, idle and unallocated cost with the allocation rule and coverage.
3. Compute unit cost from completed useful work, with the population and period fixed.
4. Explain variance by volume, rate and mix, and reconcile a forecast to actual spend.
5. Read [cost analysis](references/cost.md), [FinOps analysis](references/finops.md) for allocation, forecasting, commitment and chargeback evidence, and [SaaS cost attribution](references/saas-cost-attribution.md) when the unit is a customer, tenant or tier.

Keep rate, usage and mix effects separate. A lower unit cost with a higher bill, or a flat bill under growth, is not self-explanatory. Do not add prices to this guidance; read the actual invoice, contract and provider documentation.

## Test optimization and sizing claims

For each claim, state the cost or capacity driver, baseline period, comparison, expected direction and the observation that would falsify it. Normalize for demand and separate projected from verified. A higher limit, a cheaper line item or a completed configuration change is not a verified outcome.

| Claim | Evidence needed |
| --- | --- |
| Saturation point | Measured arrival rate, service time, queue behavior and the limiting dependency or quota |
| Sizing or headroom | Observed usage distribution compared with provisioned capacity, requests and limits |
| Unit cost | Reconciled spend and a meter for the same population and period |
| Forecast | Drivers, stated range and confidence, reconciled against actual |
| Optimization | Comparable periods with demand normalized and the effect observed at the target |
| Commitment | Coverage, utilization, expiry and the terms that govern exchange or refund |
| Chargeback | Approved allocation rules, reconciled close and a dispute record |

## Record and hand off

Use the ECR or design record for a planning decision and its evidence. Use [Run operations review](../run-operations-review/SKILL.md) for a recurring measured review, and keep original ages and findings rather than resetting them. Tie each finding to an owner and the decision it can trigger.

Hand implementation changes to the relevant activity. Route provider-specific cost mechanics by capability, and measurement-quality questions to [observability](../design-system/references/observability-and-monitoring.md). Do not claim production savings or capacity from a local estimate alone.
