# Analyze cost and unit cost

Use this reference when the question is which resources drive measured spend, what a unit of work costs, or whether a claimed saving was observed. The cost plan, accepted budget and commitment purchase belong to design, finance and the decision record; this reference covers evidence and interpretation.

## Reconcile the bill

Identify the environment, provider, region, currency, billing period and application or team ownership.

- Use current invoices, price sheets and usage exports where available. Separate estimates from billed amounts and allocated cost from cash savings.
- Keep exchange-rate date, taxes, discounts and credit assumptions explicit. Do not reuse a stale rate or mix currencies in one series.
- Keep currency consistent within a comparison; do not add prices to this guidance.

Trace the bill to the work the application performs and the capacity kept available for it. Include compute, databases, storage and backup retention, network egress, load balancers, logs and telemetry, build artifacts, CI minutes and third-party or AI usage. Keep shared system cost and idle capacity visible, and state how shared amounts are allocated so an apparent saving does not merely move to another owner.

Track total spend alongside a useful unit such as cost per active user, completed job or served request. Use completed useful work as the denominator where retries or failures consume real resources. Separate a lower unit cost from a lower bill: growth, fixed commitments and unused reserved capacity can make the two diverge.

## Attribute spend

Start from the provider hierarchy already in use: billing account, subscription or project, folder or organizational unit, environment and service. Then use tags or cost categories for owner, service, environment and cost center.

- Check whether the provider requires cost-allocation tags to be activated, and whether activation applies to historical reports.
- Treat grouping constructs such as cost categories as reporting conveniences; they do not repair missing source labels.
- Model container cost from requests, usage and node pricing; the provider does not bill per pod. Namespace and label allocation carries assumptions that belong with the result.
- Keep unallocated spend visible with an owner and a remediation path. Silent distribution hides waste.
- Report allocation coverage with every attributed figure: the share mapped to an owner and the share resting on estimated keys.
- Version allocation rules and restate prior periods when a rule change would otherwise look like a cost change.

Read [FinOps analysis](finops.md) for shared-cost rules, forecast reconciliation and commitment evidence. For multi-provider or SaaS consolidation, read the provider mechanics in the current first-party documentation and normalize dimensions deliberately; a normalized dataset is not a cost-management product.

## Compute unit cost

Define the unit before computing it.

- Name the population and period: active customers, contracted tenants, completed orders, successful jobs or served requests.
- Use completed useful work as the denominator where retries, failures or abandoned jobs consume resources.
- Separate direct cost from fully loaded cost, and state which shared pools are included.
- Report the trend against total spend. Falling unit cost with a rising bill can still be a good outcome; rising unit cost can be masked by growth.
- Watch step functions: fixed commitments, minimums and support tiers do not scale smoothly with the unit.

Publish the method with the number so a later reader can tell which part is billed and which is modelled. Read [SaaS cost attribution](saas-cost-attribution.md) when the unit is a customer, tenant, plan or tier and margin is part of the question.

## Analyze forecast and variance

A forecast states what will be spent under explicit assumptions. The decision that adopts a budget belongs to planning and finance.

- Build from demand drivers and rates: active tenants, requests, jobs, storage growth, egress, seats, token volume, then rate and product mix.
- Separate volume, rate and mix effects when explaining variance. A flat bill under growing usage is a rate or mix story, not proof of efficiency.
- Express a range with the assumptions that move it and the confidence level. A point estimate implies precision the evidence rarely supports.
- Carry known step changes: new customers, migrations, contract expiries, seasonal peaks and commitment amortization.
- Reconcile the forecast to actual each period, explain the largest variances by driver and change the model deliberately. Do not rebase history silently.

A budget or anomaly alert is a comparison input. Report the threshold, the observed breach and the decision it requires; do not treat an alert as an automatic shutdown of production work.

## Analyze commitments

Rate optimization trades flexibility for price. Analyze it against stable demand and the actual contract, not a published discount.

| Question | Evidence |
| --- | --- |
| What is covered? | Commitment coverage by service, family, region and account |
| Is it used? | Utilization against the covered usage, with headroom |
| When does it end? | Expiry calendar and the decision date |
| What is the break-even? | Expected usage, term, upfront payment and cost of unused commitment |
| Who owns the risk? | Central purchase with allocated benefit, or team-level ownership |
| What happens on change? | Permitted exchanges, refunds, scope changes and provider terms, verified at the time |

Track coverage and utilization together. High coverage with low utilization is stranded cost; low coverage with stable usage is a missed opportunity. Amortize commitment benefits to consumers so reported cost reflects the rate they actually caused. Purchase, exchange and refund decisions belong to cost planning and finance; verify current terms before stating an expected effect.

Interruptible and spot capacity belongs to the capacity decision first: a workload that cannot tolerate interruption should not appear in a savings claim alone.

## Test optimization claims

Prioritize measured waste before structural change: idle resources, oversized allocations, unnecessary data movement or retention and expensive hot paths.

| Lever | Evidence needed |
| --- | --- |
| Kubernetes requests and capacity | Representative usage, node packing and scheduling constraints; establish whether released capacity reduces billable nodes |
| Managed database or storage sizing | Backup needs, restore coverage and resilience preserved |
| Interruptible or spot capacity | Demonstrated tolerance for interruption |
| Commitments or reservations | Stable demand and a break-even analysis against current terms |
| Scaling to zero | Acceptable startup latency and supported infrastructure |
| AI model, token and audio volume | Quality requirement, caching or batching effect, retry limits and rate controls |

For each item state the cost driver, expected savings range, evidence, risk, recovery path and effort. Apply changes only within the authorized scope and through the project's configuration and delivery flow. Compare comparable billing and usage periods, normalize for demand, and distinguish projected savings from verified reductions.

## State the limits of the analysis

- Tags and labels may be incomplete, delayed or inconsistent across providers; coverage below the whole bill leaves a residual.
- Invoice granularity may stop at the account or subscription; splitting below that is modelled.
- Usage meters measure product events, not necessarily the resource that drives the bill.
- Shared-cost keys are judgment calls; a different defensible key produces a different answer.
- Small denominators make percentage changes misleading; report absolute values and the population.
- Free tiers and provider credits are account-dependent experiments, not a production cost guarantee.

Attach the method and a confidence level to every published figure, and reconcile attributed totals to the finance view with the residual shown. Hand the cost plan and accepted budget to [cost planning](../../design-system/references/cost-planning.md), recurring review to [Run operations review](../../run-operations-review/SKILL.md), and signal retention or cardinality questions to [observability](../../design-system/references/observability-and-monitoring.md). Cost changes must retain agreed reliability and recovery constraints.
