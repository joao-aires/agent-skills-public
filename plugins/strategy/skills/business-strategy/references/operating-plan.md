# Operating Plan

## Purpose

An operating plan turns strategic choices into a bounded set of outcomes, initiatives, capacity and decision rules the organization can actually run. It is not a calendar of activity and not a restatement of the strategy brief.

Use it after the strategy is chosen. Use [go-to-market](go-to-market.md) for the commercial motion, [experiments and PMF](experiments-and-pmf.md) for the test ladder, and [strategy review and pivot](strategy-review-and-pivot.md) for the review that reopens the plan.

## From strategy to outcomes

Each strategic choice should produce a small number of observable outcomes. Prefer outcome statements over deliverable lists.

```text
Outcome:   reachable mid-market teams adopt the review workflow and keep using it
Deliverable: ship the review queue
```

The deliverable can be completed while the outcome fails. Plan for the outcome.

### Outcome shape

An outcome states:

- **who** changes or benefits;
- **what** observable result occurs;
- **baseline** and source;
- **target** and window;
- **owner**;
- **evidence** that would confirm it;
- **counter-signal** that would reveal harm or displacement.

Without a baseline, a target is a wish. Without a window, a result can be claimed at any time.

### Objectives and key results

Use OKRs when the team benefits from a shared, bounded set. Keep them honest:

- objectives are qualitative and directional;
- key results are measurable outcomes, not tasks;
- each key result has a baseline, target and date;
- two to four objectives are usually enough for a quarter;
- do not assign key results to work that has no owner;
- do not use OKRs to relabel a delivery backlog.

A key result that can only be achieved by shipping a feature is a milestone, not a result. State the behavioral or economic change it should produce.

## Initiative portfolio

Map every initiative to the strategic choice it serves and the assumption it tests.

| Initiative | Strategic choice | Assumption | Outcome | Cost | Owner | Confidence | Decision point |
|---|---|---|---|---|---|---|---|

Portfolio rules:

- **Every initiative earns its place.** If it serves no current choice and tests no assumption, it is drift.
- **Separate bets from maintenance.** Maintenance protects the existing business and still needs capacity.
- **Prefer the few initiatives that change the decision.** A portfolio of twenty small items rarely produces strategic learning.
- **Name what is not being done.** Deferred and rejected initiatives, with the reason, prevent quiet re-entry.
- **Protect the constraint.** Fund the binding capability — distribution, delivery, compliance — not only the visible product work.
- **Sequence by dependency.** Some initiatives create the evidence or capability another requires.

A useful portfolio test:

> If all initiatives succeed, which strategic assumption becomes true, and would that change the company's position?

If the answer is unclear, the portfolio is activity rather than strategy.

## Capacity and dependencies

Plans fail on capacity more often than on intent.

Establish:

- **People** — who is available, at what allocation, with which skills.
- **Hiring** — lead time, ramp time and the risk of hiring into an unproven motion.
- **Budget** — committed and discretionary spend, with the approval path.
- **External dependencies** — partners, vendors, certifications, platform reviews, legal.
- **Critical path** — the sequence that determines the earliest possible outcome.
- **Support load** — the operational cost of each new customer or market.
- **Management attention** — the scarcest and most commonly overbooked resource.

Do not plan at 100% utilization. Leave room for incidents, sales cycles and learning.

Check the plan against the financial model: headcount and programs must match the burn and revenue assumptions in [financial scenario modeling](financial-scenario-modeling.md). A plan that requires impossible hiring speed is a wish with a spreadsheet.

## Operating cadence

Separate cadences by purpose.

| Cadence | Purpose | Output |
|---|---|---|
| Weekly | Execution, blockers, capacity conflicts | Adjusted commitments and owners |
| Monthly | Metrics, cohort movement, spend, risks | Corrective actions within the plan |
| Quarterly | Strategy and portfolio review | Continue, rebalance or reopen choices |
| Event-driven | Tripwire, incident, competitor move, funding change | A decision within a stated window |

Rules:

- The weekly meeting does not re-decide strategy; the quarterly review does not manage tasks.
- Each cadence has a named owner, a fixed input and a decision output.
- Metrics are defined once and reused; do not let each forum invent its own.
- Decisions that change a strategic choice go to the decision log, not only to meeting notes.
- Cancel forums that no longer produce decisions.

## Decision rights

Ambiguity about who decides is a common cause of slow strategy.

For each material decision, state:

- **who recommends**;
- **who decides**;
- **who must be consulted**;
- **who must be informed**;
- **what evidence the decision requires**;
- **the time frame** in which it must be made.

Keep the number of deciders small. Distinguish:

- **strategic decisions** — customer, market, model, major capital;
- **portfolio decisions** — which initiatives are funded;
- **operating decisions** — execution trade-offs within an accepted plan;
- **exceptional decisions** — incidents, legal, security, pricing exceptions.

An operating plan that requires the founder or CEO for every decision does not scale; one that delegates strategic choices produces incoherence.

## Confidence and forecasting

Avoid false precision in plans.

- Use ranges for uncertain outcomes, with the assumptions that produce them.
- Label confidence as high, medium or low per initiative, not for the plan as a whole.
- Distinguish committed outcomes from stretch outcomes.
- State the leading indicator that would show an initiative is off track before the lagging result arrives.
- Reforecast on a fixed cadence, not whenever a number is inconvenient.
- Keep the original forecast visible so learning can be distinguished from revision.

A confidence number is only useful if it changes a decision — funding, sequencing or a test. Otherwise it is decoration.

## Handoff to product direction

The operating plan sets business outcomes; product direction decides which problems, slices and measures deliver them.

The handoff should state:

- the outcomes the product must influence;
- the accepted strategic constraints — customer, segment, model, channel;
- the assumptions product work is expected to test;
- the capacity and dependencies already committed;
- the decisions product may make without returning;
- the evidence that would reopen a strategic choice.

Do not turn the operating plan into a feature roadmap. Do not let product planning silently change the strategy by redefining the target customer or the success measure.

Use installed `product-direction` expertise for the product decision itself. Product evidence returns to this plan as a change in confidence or a reason to reopen the relevant strategic question.

## Failure modes

- Plans built from deliverables rather than outcomes.
- OKRs that restate the roadmap.
- Every initiative marked priority one.
- Capacity estimated from headcount without ramp, support or management load.
- Dependencies discovered during execution rather than planned.
- A cadence that reviews everything and decides nothing.
- Decision rights implicit until a conflict appears.
- Forecasts revised silently.
- A product roadmap that replaces the operating plan.
- No named owner for a critical outcome.

## Output

End with:

- the outcomes, baselines and targets for the period;
- the initiative portfolio with strategic links and decision points;
- capacity, dependencies and the critical path;
- the operating cadence and decision rights;
- confidence, leading indicators and reforecast rules;
- the handoff to product direction;
- what is explicitly not being done.

The useful result is a plan a team can execute without re-deriving the strategy in every meeting.

Starting structure: [`assets/operating-plan.md`](../assets/operating-plan.md). Adapt or omit sections; do not fill it with invented evidence.
