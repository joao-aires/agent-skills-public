---
name: optimize-application-cost
description: Estimate or improve application infrastructure and service cost, including
  Kubernetes, managed databases, storage, networking and AI providers. Apply to cost
  tradeoffs, budget reviews or architecture choices using regional pricing, measured
  usage and reliability constraints.
metadata:
  scope: generic
  invocation: both
  role: task
---

# Optimize application cost

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

## Attribute the real bill

Identify the environment, provider, region, currency, billing period and application/team ownership.

- Use current invoices, price sheets and usage where available; separate estimates from billed amounts and allocated cost from cash savings.
- Use EUR and relevant European regions for this user's estimates unless the project specifies otherwise.
- Keep exchange-rate date, taxes/discount assumptions and commitments explicit; do not invent price conversions or reuse stale rates.

Trace the bill to the work the application performs and the capacity kept available for it. Include compute, databases, storage/backup retention, network egress and load balancers, logs/telemetry, build artifacts, CI minutes and third-party/AI usage. Keep shared system costs and idle capacity visible, and state how shared amounts are allocated so apparent savings do not merely move to another owner.

Track total spend alongside a useful unit such as cost per active user, completed job or request. Use completed useful work as the denominator when retries or failed operations can consume significant resources. Separate a more efficient unit cost from a reduction in the bill: growth, fixed commitments and unused reserved capacity can make those outcomes differ.

## Optimize against constraints

Read capacity, recovery, latency and privacy requirements before proposing savings.

Prioritize unused resources, oversized allocations, unnecessary data movement/retention and expensive hot paths. Compare relevant levers against their constraints:

| Lever | Constraint or evidence needed |
| --- | --- |
| Kubernetes requests/capacity | Compare representative actual usage, node packing and scheduling constraints. Establish whether released capacity reduces billable nodes; lower pod requests alone do not prove savings. |
| Managed database/storage sizing | Preserve backup needs, restore coverage and resilience. |
| Interruptible/spot capacity | The workload tolerates interruption. |
| Commitments/reservations | Stable demand and a break-even assessment; a published discount alone is insufficient. |
| Scaling to zero | Acceptable startup latency and supported infrastructure. |

For AI, examine model choice, token/audio volume, caching, batching, retry limits and rate controls against the actual quality requirements. Free tiers are account/model-dependent experiments, not a production cost guarantee. Keep budgets, growth scenarios and reasonable anomaly signals proportionate; a small application need not acquire a full FinOps platform.

## Use provider expertise selectively

Seek available AKS cost-optimization expertise only for Azure AKS. Read this skill first: validate upstream sizing ratios and example defaults against representative usage, memory peaks, availability and current documentation; do not apply them mechanically. Preserve project change/approval boundaries and verify platform commands before use.

For other platforms, research current first-party guidance, prices and regional limits rather than adapting Azure commands:

- [AWS EKS cost practices](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt.html), plus the actual EC2/RDS/storage pricing and discounts.
- [GKE cost practices](https://cloud.google.com/kubernetes-engine/docs/best-practices/cost-optimization), accounting for the chosen mode and service billing.
- [AKS autoscaler guidance](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler), plus current Azure pricing and the selected node/service offerings.

Use the relevant service's documentation for non-Kubernetes hosts, databases and external providers. No new cloud account, MCP server or paid cost tool is required by this bundle.

## Verify the benefit

For each proposed change, state the cost driver, expected savings range, evidence, risk, recovery path and effort. Apply changes within the authorized scope through the project's configuration/CI/CD flow. Compare comparable billing/usage periods and normalize for demand; distinguish projected savings from verified reductions. Update assumptions and decisions after material traffic or architecture changes.

For recurring evidence reviews use `operational-housekeeping`; for signal retention/cardinality use `observability-operations`. Cost changes must retain agreed reliability and recovery constraints.
