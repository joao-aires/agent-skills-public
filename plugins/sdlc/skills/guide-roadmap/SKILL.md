---
name: guide-roadmap
description: Guide to writing and reviewing a strategic or product roadmap. Covers outcomes and evidence, Now/Next/Later horizons, confidence, dependencies, capacity, sequencing, explicit deferrals, status, review cadence and common failures.
user-invocable: true
metadata:
  kind: guide
  origin: local
  pack: sdlc
  domain: product
  phase: planning
  scope: generic
  invocation: both
  role: support
---

# Roadmap guide

A **roadmap** coordinates several changes toward outcomes. It explains what direction the work serves, why the sequence is what it is, and what is committed, proposed, exploratory or deliberately deferred. It is not a feature list, a backlog, a release note or a change record.

A **product roadmap** expresses product direction for a product, segment or journey: the outcomes users or the business should see, and the sequence of product changes that pursue them. The product-direction decision belongs to the Plan activity and its owners. A strategic roadmap is a pre-SDLC strategy record owned by the strategy pack and does not use this guide.

This guide owns the artifact craft — structure, evidence, confidence, sequencing and review. It does not choose the strategy, accept a priority or authorize delivery.

## Reader questions

A reader who was not in the planning conversation must be able to answer:

1. What outcomes are we pursuing, for whom, and what evidence or assumption supports each?
2. What is in the current horizon, and what is explicitly not yet?
3. In what order, and why does that order matter?
4. What must be true before an item can start?
5. What is committed, proposed, exploratory or deferred?
6. How confident are we, and what would change the answer?
7. Who owns each outcome or decision, and what capacity is assumed?
8. Which briefs, change records or issues carry the work?
9. When will the roadmap be reviewed, and what triggers an earlier revisit?

## Minimum content

- scope: product, portfolio or business area, audience and time horizon;
- outcomes in user, business or system terms, each with evidence or a labelled assumption;
- the Now, Next and Later horizon with the reason for each item's placement;
- commitment status per item: committed, proposed, exploratory or deferred;
- confidence per outcome and the evidence or unknown that drives it;
- dependencies, prerequisites and external commitments that gate the sequence;
- capacity and constraints assumed for the current horizon;
- sequencing rationale: risk, learning, dependency, capacity or commitment;
- explicit not-yet and deferred work, with the reason and revisit trigger;
- owners for outcomes, decisions and coordination points;
- links to the briefs, change records, issues and decisions that carry the work;
- roadmap status, revision and review cadence.

## Horizons and commitment are different axes

Now/Next/Later answers *when we intend to look at it*. Commitment answers *how firmly it is decided*.

| Horizon | Typical content | What it must not imply |
| --- | --- | --- |
| **Now** | Work in progress or next in line, with named capacity and prerequisites | That every item will finish on a date |
| **Next** | Proposed outcomes being shaped, with dependencies and open decisions | That the order is locked or funded |
| **Later** | Exploratory or candidate direction, deliberately unscheduled | A promise, estimate or delivery commitment |

Use commitment labels independently:

- **Committed** — accepted, resourced and scheduled; the horizon does not define it.
- **Proposed** — a recommended direction awaiting a decision or capacity.
- **Exploratory** — a question or option being investigated, not a plan.
- **Deferred / not yet** — intentionally excluded now, with a reason and a trigger to reconsider.

A four-column table or per-item label is enough. Do not use dates to create false precision; a date is a commitment only when the owner and capacity behind it are real. "Later" is not a synonym for "we forgot"; every deferred item states why it is not now.

## Structure and quality

- Start with the outcome and the evidence, not the feature name. A feature entry earns its place by the outcome it serves.
- Name the audience or segment for each product outcome. "Users" is not an audience.
- Separate observed evidence from assumption and conviction. State confidence per outcome, not once for the whole document.
- Explain why the order matters. Dependencies, risk reduction, learning value, capacity and prior commitments are legitimate reasons; alphabetical order is not.
- Make prerequisites concrete: an accepted decision, a dependency shipped, a hire, a budget, a migration, a partner or a measured baseline.
- Show the capacity and constraint that make Now plausible. A roadmap that ignores capacity is a wish list.
- Keep the smallest useful sequence. Prefer a few outcomes with clear boundaries over a long inventory.
- Mark explicitly deferred work and its revisit trigger; silence is not a decision.
- Link the authoritative brief, change record or issue for each item. The roadmap sequences and summarizes; it does not duplicate the change record.
- Keep current, proposed and historical views distinct. Say at which revision the roadmap is current.
- When a commitment slips, record the change and the reason. Do not rewrite history so the earlier commitment disappears.
- Use one roadmap per product or programme at the established home. A second copy is not a competing authority.

## Status, evidence and review cadence

Document maturity is **draft**, **accepted** or **superseded** and applies to the roadmap as a whole. Committed, proposed and exploratory are per-item commitment labels; do not reuse them as document status.

Evidence for a roadmap item is outcome evidence or a decision, not a shipped feature. A committed item can cite accepted direction, capacity and prerequisites; it cannot claim implementation or a released result. Link release notes or change records for that claim.

Set a review cadence that matches the planning rhythm — for example a frequent check of Now, a periodic review of Next, and a longer review of Later. Record the cadence and the event triggers: new evidence, lost capacity, a changed dependency, a missed commitment or a decision that invalidates an outcome. Review the sequence against actual progress; a roadmap that is never revised is either perfect or ignored.

## Common failures

- a feature list with no outcomes, audience or evidence;
- every item marked Now or committed, leaving no honest uncertainty;
- dates presented as commitments without owner, capacity or prerequisites;
- no dependencies, so the sequence is arbitrary;
- no capacity or constraint, so the plan cannot be resourced;
- deferred work that is silently dropped instead of labelled and explained;
- confidence stated once for the whole document, or not at all;
- a strategic direction document masquerading as a product roadmap, or the reverse;
- a roadmap used as authorization to implement or release;
- a missed commitment erased from the current revision;
- no owners or decision points, so nothing can be unblocked;
- no links to the change records that carry the work;
- a stale roadmap with no review cadence or revisit trigger;
- several competing copies of the same roadmap.

## Review

Read the roadmap as a product, delivery and engineering partner:

- Can we state the outcomes and the evidence behind them without reading a feature list?
- Is the Now/Next/Later placement honest about commitment and confidence?
- Does the order follow from dependencies, risk, learning or capacity?
- Is the capacity assumption visible and plausible?
- Is what we are deliberately not doing as clear as what we are doing?
- Can each item be traced to an owner and a change record?
- Is the roadmap's status, revision and review cadence current?
- Does the roadmap claim a decision or delivery result it does not own?

## Handoff

The delivery, product and requirements readers need the outcomes, the sequence and its rationale, prerequisites, commitment status, owners, deferrals and links to the carrying change records. Planning consumes the roadmap as direction and sequencing; change records and issues own scope, acceptance and delivery. A roadmap item does not authorize implementation, and a release record does not update the roadmap by itself.

When new evidence or a changed constraint invalidates an outcome or its order, revise the roadmap and reopen the affected decision rather than running an outdated sequence.
