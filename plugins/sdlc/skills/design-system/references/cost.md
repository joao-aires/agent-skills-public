# Cost in design

Cost is a design consequence, not only an optimization task after launch. The architecture chooses which resources exist, how much they are used per unit of work, what is paid for continuously and how hard it is to leave a provider. This reference connects those choices to the methods that measure and improve them; it does not contain prices, discount schedules or optimization tactics.

Capacity and cost are two views of one decision: whether the resources delivering the accepted outcome are proportionate to its value. Read [Analyze capacity and cost](../../analyze-capacity-cost/SKILL.md) for demand, sizing, attribution and verified savings, and [cost planning](cost-planning.md) for the design-time cost model.

## What design decides

- **The cost driver.** Identify what scales with the journey: requests, compute time, storage growth, egress, model tokens, seats, per-tenant isolation, retained logs or backups. A design that cannot name its driver cannot be assessed for cost.
- **Fixed against variable.** Standing infrastructure, idle capacity, replicas and commitments are paid regardless of traffic; usage-based components follow it. Distinguish them before comparing options.
- **Attribution key.** Decide which tenant, journey, team or environment a cost can be assigned to, and which shared cost cannot. Attribution is a design and tagging decision, not a billing report invented later.
- **The price of the other attributes.** Headroom, replication, multi-region recovery, observability retention, encryption and isolation each add standing cost. State the reliability, performance and compliance benefit that justifies it.
- **Exit cost.** Provider-specific services, data gravity, egress, proprietary formats and contractual commitments determine how reversible the choice is. Record the switching cost and the condition that would trigger it.

## Route the question

| Question | Where it is owned |
| --- | --- |
| Demand model, saturation, scaling and recovery-site capacity | [Analyze capacity and cost](../../analyze-capacity-cost/SKILL.md) and [capacity planning](../../analyze-capacity-cost/references/capacity.md) |
| Bill attribution, avoidable spend, commitments and provider tradeoffs | [Cost optimization](../../analyze-capacity-cost/references/cost.md) |
| Unit economics, showback, chargeback and margin | FinOps framework and unit-economics capability; use the organisation's finance and product owners |
| The cost of a specific provider service or configuration | Current first-party provider documentation and the actual contract |
| The cost consequence of a reliability or continuity strategy | [Reliability](reliability.md) and [disaster recovery](reliability-disaster-recovery.md) |
| The cost consequence of performance headroom | [Performance](performance.md) |

FinOps vocabulary — allocation, forecasting, budgeting, rate optimization, unit economics — is useful for naming the question. The organization's actual billing data, commitment terms and finance decisions remain the authority.

## Design obligations

- Connect every cost claim to the user outcome it supports. A cheaper design that fails the journey has not saved money.
- Use measured usage and a defensible rate, or label an estimate as provisional. Do not invent prices, discounts or forecast growth.
- Account for shared, idle and untagged cost rather than attributing only the easy line items.
- State the assumption that would reverse the choice — demand growth, provider price change, commitment expiry, data volume — and the review point.
- Keep the exit path proportionate. A reversible choice can tolerate less certainty about cost; an irreversible one needs a bounded commitment.
- When the acceptable budget is unknown, return it as a decision with the cost range and the options, rather than selecting a budget inside the design.

A design recommendation can state a relative cost difference between options — one option adds a continuously running replica, another trades recovery time for standing cost — without naming a currency figure. The measured bill and the accepted budget belong to the analyze-capacity-cost decision and its evidence.

## Evidence questions

- What is the cost per journey, tenant or unit of work, and which component dominates it?
- Which part is fixed, which follows demand, and what happens to cost at the accepted peak?
- Which shared cost is not attributable, and who owns it?
- What does the accepted reliability, performance and security posture add, and is that visible in the choice?
- What is the switching or exit cost, and when would it be reconsidered?
- Is the cost claim based on measured usage or explicitly labelled as an estimate?

Do not claim production savings from a local estimate, a list price or a configuration change that has not been measured at the target.
