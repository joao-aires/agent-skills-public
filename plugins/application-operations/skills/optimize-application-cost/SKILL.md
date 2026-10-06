---
name: optimize-application-cost
description: Estimate or improve application infrastructure and service cost, including Kubernetes, managed databases, storage, networking and AI providers. Apply to cost tradeoffs, budget reviews or architecture choices using regional pricing, measured usage and reliability constraints.
---

# Optimize application cost

## Attribute the real bill

Identify the environment, provider, region, currency, billing period and application/team ownership. Use current invoices, price sheets and usage where available; separate estimates from billed amounts and allocated cost from cash savings. Use EUR and relevant European regions for this user's estimates unless the project specifies otherwise. Keep exchange-rate date, taxes/discount assumptions and commitments explicit; do not invent price conversions or reuse stale rates.

Include compute, databases, storage/backup retention, network egress and load balancers, logs/telemetry, build artifacts, CI minutes and third-party/AI usage. Shared cluster/system costs and idle capacity should remain visible. Track a useful unit such as cost per active user, completed job or request alongside total spend; lower unit cost can still produce a larger bill with growth.

## Optimize against constraints

Read capacity, recovery, latency and privacy requirements before proposing savings. Prioritize unused resources, oversized allocations, unnecessary data movement/retention and expensive hot paths. For Kubernetes, compare requests and actual usage over representative periods, then check node packing, scheduling constraints and whether released capacity will reduce billable nodes. Reducing pod requests alone does not guarantee a lower bill.

Include managed database/storage sizing and backup needs; do not cut restore coverage or resilience to make a chart look better. Consider interruptible/spot capacity only for workloads that tolerate interruption. Commitments/reservations need stable demand and a break-even assessment; do not buy them merely because a published discount looks attractive. Scaling to zero needs acceptable startup latency and supported infrastructure.

For AI, examine model choice, token/audio volume, caching, batching, retry limits and rate controls against the actual quality requirements. Free tiers are account/model-dependent experiments, not a production cost guarantee. Keep budgets, growth scenarios and reasonable anomaly signals proportionate; a small application need not acquire a full FinOps platform.

## Use provider expertise selectively

Use bundled `aks-cost-optimization` only for Azure AKS. Read this skill first: validate upstream sizing ratios and example defaults against representative usage, memory peaks, availability and current documentation; do not apply them mechanically. Preserve project change/approval boundaries and verify platform commands before use.

For other platforms, research current first-party guidance, prices and regional limits rather than adapting Azure commands:

- [AWS EKS cost practices](https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt.html), plus the actual EC2/RDS/storage pricing and discounts.
- [GKE cost practices](https://cloud.google.com/kubernetes-engine/docs/best-practices/cost-optimization), accounting for the chosen mode and service billing.
- [AKS autoscaler guidance](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler), plus current Azure pricing and the selected node/service offerings.

Use the relevant service's documentation for non-Kubernetes hosts, databases and external providers. No new cloud account, MCP server or paid cost tool is required by this bundle.

## Verify the benefit

For each proposed change, state the cost driver, expected savings range, evidence, risk, recovery path and effort. Apply changes within the authorized scope through the project's configuration/CI/CD flow. Compare comparable billing/usage periods and normalize for demand; distinguish projected savings from verified reductions. Update assumptions and decisions after material traffic or architecture changes.
