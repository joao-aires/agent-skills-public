---
name: capacity-and-cost
description: Plan capacity and improve application cost from measured demand and spend evidence. Use for concurrency, scaling, saturation, resource sizing, infrastructure or provider cost tradeoffs, budget reviews and architecture changes.
metadata:
  kind: activity
  origin: local
  scope: generic
  invocation: both
  role: task
  phase: maintenance
  pack: sdlc
  domain: operations
---

# Capacity and cost

Treat capacity and cost as two views of the same operating decision. Capacity asks whether the system can serve the accepted demand with acceptable latency and failure behavior. Cost asks whether the resources and providers delivering that outcome are proportionate to its value.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

## Establish the decision

Identify the service, critical journeys, demand or spend question, target environment and accepted constraints. Separate measured demand and billing evidence from hypotheses. Do not optimize a cost line or a scaling number without connecting it to the user outcome it supports.

- **Capacity design:** establish the demand model, saturation points, concurrency and failure behavior, then choose a coherent scaling path.
- **Cost review:** attribute the actual bill, identify avoidable spend, and evaluate changes against reliability, performance, security and contractual constraints.
- **Recurring review:** compare current demand/spend with prior decisions, retain stable findings and prepare bounded changes.

## Work the evidence

1. Establish the user or system outcome, current demand, growth assumption and acceptable degradation.
2. Measure the actual resource, provider or journey signals. State units, populations, time windows and missing data.
3. Compare options on capacity headroom, latency, reliability, cost, operational burden and reversibility.
4. Choose a bounded change or decision; record the assumption and the condition that would reverse it.
5. Verify the intended effect at the real target where authorized. A cheaper bill or a higher limit is not proof of a reliable outcome.

## References

- [Capacity planning](references/capacity.md): demand, concurrency, scaling and Kubernetes mechanics.
- [Cost optimization](references/cost.md): bill attribution, provider tradeoffs and verification.

## Record and hand off

Use the ECR, a decision record or the operations review for the accepted decision and evidence. Keep capacity/cost reviews distinct from routine dependency updates. Hand off an implementation change to the relevant activity; do not claim production savings or capacity from a local estimate alone.
