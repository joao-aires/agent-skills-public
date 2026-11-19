# Attribute SaaS cost to customers, tenants and tiers

Use this reference when the cost question is commercial: which customer, tenant or plan consumes the spend, whether a tier covers its cost, or what gross margin the service actually earns. It extends [cost analysis](cost.md) with a per-unit model and [FinOps analysis](finops.md) with the allocation and governance evidence a subscription business needs. It does not set prices, revenue recognition or contract terms; finance and product own those.

## Define the unit before allocating

"Cost per customer" is ambiguous until the population is fixed.

| Unit | Use | Trap |
| --- | --- | --- |
| Billing account | Invoice reconciliation and collections | One account may contain several tenants or brands |
| Tenant | Infrastructure isolation, shared cost and noisy-neighbor analysis | A tenant is not always a paying customer |
| Workspace or project | Product-level attribution inside a tenant | Users can create many, inflating counts and support cost |
| Seat | Per-user license and support comparison | Invited, inactive and service accounts distort the count |
| Active customer | Unit economics and trend reporting | Definition of active changes margin without changing cost |
| Plan or tier | Margin by offer | Grandfathered and custom contracts do not fit the public tier |
| Completed unit of work | Usage-based products | Retries and failed jobs inflate consumption |

Fix the unit, the period and whether the population is contracted or active. State which costs are direct, which are allocated, and which are excluded. A margin figure without that scope is not comparable with another period or team.

## Separate cost of revenue from operating expense

Cost of goods sold, or cost of revenue, is the cost of delivering the service to customers in the period. Operating expense covers running the business that sells and supports it. The boundary is an accounting decision, but the engineering inputs are concrete:

| Cost | Usually cost of revenue | Usually operating expense | Decision needed |
| --- | --- | --- | --- |
| Production compute, database, storage, egress | Yes, for serving customers | No | Shared with internal environments? |
| Third-party APIs charged per request, token or message | Yes, when consumed by the product | No | Prototype and internal use excluded? |
| CDN, queue, observability for the production path | Yes, the serving share | The internal and development share | Allocation key for shared telemetry |
| Payment processing and billing fees | Yes | No | Treated as a percentage of revenue |
| Customer support tools and staff | The direct support share | Sales, marketing, R&D, G&A | Time attribution or ticket-volume key |
| Licenses resold or bundled | Yes, at cost | No | Distinguish resale from internal tooling |
| Idle capacity and commitments | The serving share | Unused capacity may be a period cost | Who owns stranded commitments |

Write the boundary down once and apply it consistently. Moving a cost between the two categories changes gross margin without changing the bill, so a boundary change is a reporting event that needs a restated comparison. Do not allocate everything: a cost with no plausible causal driver belongs in a pool with an explicit rule, not in a made-up per-customer figure.

## Build the cost-to-serve model

Work from the bill inward, then reconcile outward:

1. Start with the reconciled provider and vendor invoices for the period.
2. Tag or map each line to a service, environment and owner. Keep unallocated spend visible.
3. Split production from non-production; only the production share enters cost of revenue.
4. Attribute direct costs where a resource, meter or invoice line identifies the tenant.
5. Allocate shared platform costs with an agreed driver.
6. Add people and vendor costs that the product consumes, using the approved rate or actual invoice.
7. Reconcile the attributed total back to the finance view and explain the residual.

Direct attribution is strongest when the product already meters usage per tenant: requests, storage, compute time, messages, tokens, seats or jobs. Where metering is absent, usage proxies such as database size, row counts or request logs impose assumptions and need a confidence label.

## Choose allocation keys with their failure modes

| Method | Use when | Failure mode |
| --- | --- | --- |
| Direct assignment | The resource is dedicated or the invoice line names the tenant | Dedicated resources hide shared dependency cost |
| Usage-proportional | A meter exists and tracks the cost driver | The meter measures activity, not resource consumption |
| Seat or headcount | Per-user licenses, support and fixed tooling | Inactive seats and shared accounts distort the split |
| Revenue-weighted | Shared sales or success capacity | Allocates cost by price, not by work performed |
| Equal split | Only a small, genuinely uniform shared service | Punishes small tenants and hides large consumers |
| Hybrid | Most real systems: direct where possible, driver-based pools otherwise | Complexity without a documented rule becomes unfalsifiable |

Prefer the driver closest to the cost's causal mechanism. If two drivers are equally defensible, choose the one the affected owners can influence and understand. Revisit a key when the product changes shape; a storage-based key fails when the product becomes compute-heavy.

Treat these as shared pools with named rules: control plane, observability, CI/CD, identity, networking, support, security tooling, commitment discounts and vendor minimums. Allocate idle capacity and unused commitments deliberately. Spreading them evenly hides the tenant or tier that caused them; assigning all of it to the largest customer overstates that customer's cost.

## Attribute licenses, seats and usage

Subscription vendors price in several ways, and the invoice rarely matches the product tier:

- **Seat licenses** create a fixed cost per named user or admin. Track purchased, assigned and active seats; true-ups and minimum commitments make the unit cost step, not slope.
- **Usage-based services** charge per request, message, token, minute or GB. The product's meter and the vendor's meter may disagree because of retries, batching, caching or rounding.
- **Tiered volume** changes the marginal rate at thresholds. A tenant crossing a tier can change total cost without changing behavior.
- **Platform or minimum fees** are fixed regardless of consumption. Allocate them as a pool unless a contract names the tenant.
- **Bundled or resold licenses** may already be in the customer price. Counting them again as infrastructure cost double counts the same spend.

Keep a contract and seat inventory with renewal dates, minimums, overage rules and the owner. Reconcile consumed units to vendor invoices before using them in margin analysis. Do not infer current vendor terms from a public pricing page; read the contract and the current invoice. Where a vendor changes its pricing model, restate the affected periods or mark the series as discontinuous.

## Compute gross margin by tier

Gross margin is revenue minus cost of revenue, usually expressed as a percentage of revenue for the same period and scope. Make these choices explicit:

- **Period alignment.** Infrastructure cost, vendor invoices and recognized revenue may close on different calendars. Use the finance close where available; otherwise state the approximation.
- **Currency.** Convert at the approved rate and date; do not mix currencies in one series.
- **Discounts and credits.** Apply invoiced discounts and credits consistently. A commitment discount is a cost reduction, not revenue.
- **Fixed versus variable cost.** Early tiers often carry a disproportionate share of fixed platform cost; show both contribution margin and fully loaded margin.
- **One-off costs.** Migration, onboarding and remediation distort a single period; separate them from recurring cost to serve.
- **Population changes.** Churn and new logos change the denominator; compare cohort and total figures.

| View | Question it answers | Watch |
| --- | --- | --- |
| Contribution margin | Does this tier cover its variable cost? | Excludes shared fixed cost by design |
| Fully loaded gross margin | Does the tier cover its allocated delivery cost? | Depends on allocation keys |
| Cohort margin | How does margin evolve as a customer matures? | Small cohorts swing wildly |
| Margin by tenant | Which accounts are structurally unprofitable? | Custom terms and one-offs distort |

A tier that looks healthy in aggregate can contain a few tenants consuming most of the shared pool. Report the distribution, not only the average, and identify concentration before drawing conclusions.

## Respect the data-quality limits

Per-customer attribution is usually the least reliable number in a cost review. State the limits with the result:

- Tags and labels are incomplete, delayed or inconsistent across providers; coverage below the whole bill leaves a residual.
- Invoice granularity may stop at the account or subscription; splitting below that is modelled.
- Usage meters measure product events, not necessarily the resource that drives the bill.
- Shared cost keys are judgment calls; a different defensible key produces a different margin.
- Revenue recognition, discounts, credits and tax timing can make a period's margin incomparable.
- Seat counts, trials, free tiers and internal accounts can dominate a small customer base.
- Small denominators make percentage changes misleading; report absolute values and the population.

Attach a confidence level and the allocation method to every published figure. Reconcile the attributed total to the finance view and show the unexplained residual. If the residual or the estimated share is material, report a range or decline the per-tenant claim rather than presenting a precise number.

| Evidence | Claim supported |
| --- | --- |
| Reconciled invoice and usage export | Spend and consumption are measured |
| Tenant meter or dedicated resource | That tenant's direct cost is observed |
| Documented allocation key and coverage | Shared cost is attributed under stated assumptions |
| Contract and seat inventory | License cost and commitments are known |
| Closed-period revenue and cost | Margin is computed for an aligned period |
| Sensitivity across two keys | The conclusion survives a reasonable alternative |

## Hand off and keep current

Use [cost analysis](cost.md) for reduction levers, [FinOps analysis](finops.md) for allocation governance, commitments and chargeback evidence, and [design-system](../../design-system/SKILL.md) when the question is the plan or accepted budget rather than what the measured cost is. Product and finance own tier design, price, discounting and revenue recognition. Update the model when the product's cost drivers, vendor contracts or plan structure change; an attribution model that is not maintained quietly becomes fiction.

Sources: [FinOps unit economics](https://www.finops.org/framework/capabilities/unit-economics/), [licensing and SaaS](https://www.finops.org/framework/capabilities/licensing-saas/), [invoicing and chargeback](https://www.finops.org/framework/capabilities/invoicing-chargeback/) and [FOCUS](https://focus.finops.org/) define the practice vocabulary and normalized cost fields. Checked 2026-11-16. They do not define this project's prices, contract terms or accounting policy.
