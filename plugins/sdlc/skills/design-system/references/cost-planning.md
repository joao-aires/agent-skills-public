# Cost planning in design

Cost planning makes the cost consequence of a design explicit before it is built: which resource or provider dominates, what is paid continuously, what follows demand, how a unit of value is priced and how hard the choice is to leave. It reasons in structure and relative difference, not in prices. Measured spend, commitments and savings belong to the capacity and cost method; provider fee tables and service mechanics belong to provider guidance.

Read [cost](cost.md) for the compact design lens, [capacity planning](capacity-planning.md) for the demand and reliability capacity that drives variable cost, and [analyze-capacity-cost](../../analyze-capacity-cost/SKILL.md) when the question needs the actual bill or a verified change.

## Name the cost driver

A design that cannot name its cost driver cannot be assessed. Choose from the resources the journey actually consumes:

- requests, compute time, concurrency or provisioned replicas;
- storage growth, retained objects, log and trace volume, backups and snapshots;
- network egress, cross-region or cross-zone traffic, CDN delivery;
- model tokens, audio minutes, inference calls or third-party API usage;
- per-seat, per-tenant or per-environment isolation;
- licenses, support plans and committed capacity.

State the unit the cost follows: per journey, per tenant, per active user, per thousand events, per stored gigabyte-month. Then identify the component that dominates that unit. A cost claim that lists many small line items usually hides the one that decides the design.

## Separate fixed, variable and stepwise

- **Fixed.** Standing infrastructure, idle replicas, control planes, environments and commitments are paid regardless of traffic.
- **Variable.** Usage-based components follow demand and can dominate at scale even when the architecture looks cheap at low volume.
- **Stepwise.** Quota tiers, shard counts, node pools, license bands and reserved capacity move in jumps. A step can make a small growth event disproportionately expensive.

Distinguish these before comparing options. An option with low fixed cost and high variable cost is not cheaper than its opposite; they fail differently at different demand levels.

## Reason about unit economics

Unit economics connects the design to value:

- cost per completed journey, per tenant or per unit of work;
- the marginal cost of the next unit versus the average;
- gross margin or budget headroom where the organization uses them;
- how the unit cost changes with scale, cache hit rate, batch size or model choice;
- which shared cost cannot be attributed to a unit.

Use the organization's accepted unit and finance definitions; do not invent a margin, a price or a chargeback model. If the unit is a customer or plan, the cost-attribution method for SaaS products may apply. The design states the driver and the direction of the tradeoff; finance and product own the commercial decision.

## Design attribution

Attribution is decided in the design, not reconstructed from a bill later:

- choose the key: tenant, journey, team, environment, feature or cost center;
- state which resources can carry that key through tags, labels, account structure or request context;
- name the shared cost that cannot be attributed and who owns it;
- avoid high-cardinality attribution that makes telemetry or billing unmanageable;
- decide whether the purpose is showback, chargeback, budget alerting or engineering feedback — each needs different fidelity.

An attribution key that cannot survive a provider boundary or a shared cluster is an assumption, not a design. Mark it.

## Budgets and tradeoffs

When an accepted budget exists, use it as a constraint. When it does not, return the budget question with the cost range and the options rather than choosing one inside the design.

Make the tradeoff visible:

- reliability headroom, replication and recovery site against standing cost;
- latency targets against provisioned capacity, caching or provider choice;
- isolation and residency against shared-resource efficiency;
- observability retention, audit evidence and backup depth against storage cost;
- build versus buy, and single-provider leverage against exit cost.

A relative comparison is enough for a design decision: one option adds a continuously running replica, another accepts a longer recovery time. Do not put prices, discount schedules or provider fee tables in the design; they date quickly and belong to current first-party provider documentation and the actual contract.

## Exit cost

Every provider or platform commitment has a cost to leave. Record:

- data gravity and the effort to export, transform and verify it;
- proprietary formats, APIs and runtime features the design depends on;
- egress, migration traffic and parallel-running cost during a move;
- contract term, commitment and notice period;
- the operational and engineering effort of switching;
- the condition that would trigger reconsideration.

A reversible choice can tolerate less certainty about cost; an irreversible one needs a bounded commitment and a named review point.

## Evidence and handoff

The cost plan is ready when it states:

- the cost driver and the unit it follows, with the dominant component;
- the fixed, variable and stepwise split;
- the attribution key, what can carry it and what shared cost remains;
- the accepted budget or the returned budget decision;
- the reliability, performance and compliance cost included in the choice;
- the exit cost and the assumption that would reverse the decision;
- whether the claim is measured, estimated or assumed.

Connect every cost claim to the outcome it supports. A cheaper design that fails the journey has not saved money. Use measured usage and a defensible rate, or label the estimate as provisional. Route the measured bill, commitments, avoidable spend and production savings to the [capacity and cost method](../../analyze-capacity-cost/SKILL.md); route concrete provider service mechanics to provider guidance. Do not claim production savings from a local estimate or a list price.
