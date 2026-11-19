# Strategy Review and Pivot

## Purpose

A strategy review asks whether the current choices still deserve their cost. It is not a status meeting, a budget exercise or an opportunity to relitigate every preference.

Use it on a cadence and when evidence changes. Use [strategy stress testing](strategy-stress-testing.md) for adversarial failure analysis, [experiments and PMF](experiments-and-pmf.md) for the evidence behind results, and [operating plan](operating-plan.md) for the execution cadence this review governs.

## Review cadence

| Review | Frequency | Question | Output |
|---|---|---|---|
| Execution check | Weekly | Are the committed outcomes on track, and what is blocked? | Adjustments within the plan |
| Performance review | Monthly | Are leading and lagging indicators moving as expected? | Corrective actions, test changes |
| Strategy review | Quarterly, or at a major funding or market event | Do the choices still hold given the evidence? | Continue, narrow, park, pivot or kill |
| Assumption review | Event-driven | Has a critical assumption been falsified? | Reopen only the affected analysis |

Rules:

- Put the strategy review on the calendar before it is needed; ad hoc reviews happen only in a crisis.
- Separate the performance conversation from the strategy conversation. Mixing them produces either operational excuses or premature pivots.
- Give the review a decision owner and a quorum that can actually change the strategy.
- Circulate evidence in advance; do not spend the meeting presenting status.
- End with a recorded decision, even if the decision is to continue unchanged.

## Inputs

Bring:

- the current strategy brief and the choices it records;
- the assumption and evidence state;
- actual outcomes against the last plan, including failures;
- unit economics and cash position;
- competitive and market changes;
- customer and product evidence gathered since the last review.

Do not bring only the metrics that improved. A review that cannot see failure cannot decide.

## Tripwires

A tripwire converts a belief into a monitored signal.

| Assumption | Signal | Threshold | Window | Decision reopened |
|---|---|---|---|---|
| The beachhead buys at the assumed price | Win rate and discount depth |  |  | Pricing, segment, value proposition |
| The channel reaches the segment | Qualified pipeline per channel |  |  | Motion, partner, market |
| Retention reflects value | Cohort flattening by segment |  |  | Product, onboarding, ICP |
| Unit economics survive growth | CAC payback, gross margin |  |  | Pricing, packaging, motion |
| Incumbents will not bundle | Product launches, pricing, partnerships |  |  | Wedge, positioning, durability |
| The required capability is available | Hiring, build progress, vendor terms |  |  | Sequencing, mode, feasibility |
| Capital lasts to the next milestone | Burn, runway, fundraising progress |  |  | Scope, round size, plan |

Guidance:

- A tripwire needs a threshold, a window and a decision. Without all three it is a dashboard.
- Prefer leading indicators. Revenue confirms too late to change course cheaply.
- Assign an owner and a review date.
- Distinguish a **tripwire** (a signal to investigate) from a **kill criterion** (a result that ends the bet). Not every tripwire should stop the strategy.
- Review the tripwire set when the strategy changes; stale triggers create noise.
- Record when a tripwire fires but the thesis is reaffirmed, and why. That is evidence too.

## Steelman, then attack

A review that only attacks produces defensiveness; one that only defends produces drift. Do both, in order.

### 1. Steelman

State the strongest version of the current strategy:

- why it is the best available choice given the constraints;
- what would have to be true for it to succeed;
- what the team has learned that strengthens it;
- which competitor or alternative it is beating, and how.

If the team cannot state the strongest case, it does not understand the strategy well enough to review it.

### 2. Attack

Then attempt to break it. Use the failure mechanisms in [strategy stress testing](strategy-stress-testing.md), and add:

- Which assumption has the weakest evidence relative to its importance?
- What did we expect that did not happen, and what is the least flattering explanation?
- What would a well-informed skeptic say is being avoided?
- Which customer or deal are we explaining away?
- What would we do if we started today with no sunk cost?
- Which competitor response would make the wedge uneconomic?
- What are we learning that we did not want to learn?

### 3. Pre-mortem

Assume the strategy failed badly in the review horizon. Reconstruct why. Convert the most plausible failure paths into tests, mitigations or tripwires.

Pre-mortems work best when participants write independently before discussion; group discussion otherwise converges on the first confident voice.

## Deciding

Use a small set of explicit verdicts.

### Continue

The thesis holds, evidence supports the critical assumptions, and the plan is the right use of the next period. Continue does not require new analysis; it requires a reason.

### Narrow

The strategy works for a subset but not the target. Reduce scope — segment, use case, geography, channel — and state what is being dropped and why. Narrowing is a choice, not a failure of ambition.

### Park

The premise may become true later, and the cost of keeping the option alive is low. Stop investment, preserve the asset or relationship, and state the signal that would reopen it.

### Pivot

A core assumption has failed and evidence points to a materially different formulation. State:

- which assumption failed;
- what is retained — capability, customers, data, distribution;
- what changes — customer, problem, solution, channel or model;
- the new thesis and its first test;
- the cost of the change and what it forecloses.

A pivot that retains the same customer, problem, channel and model but changes the message is a repositioning, not a pivot.

### Kill

The bet no longer justifies its cost under realistic assumptions. Stop, release the resources, and record what was learned. Killing a strategy is a legitimate outcome of a well-run review; keeping a dead strategy alive is the expensive failure.

Do not average verdicts. A strategy can be worth continuing in one segment and killing in another; split the decision rather than compromising.

## Decision log

Record material review outcomes in `decision-log.md` when persistent state exists. Capture:

```text
Decision:
Date and review horizon:
Verdict: continue / narrow / park / pivot / kill
Evidence that drove the change:
Assumptions affected:
What is retained and what is released:
Options considered and why rejected:
Opportunity cost:
New thesis, if any:
Next tests and owners:
What would reopen this decision:
Status: proposed / accepted
```

Keep proposed recommendations distinct from accepted decisions. A review that produces a recommendation the decision owner has not accepted has not changed the strategy.

## Facilitation

- Assign a **red team** role to someone who is not the strategy's author.
- Ask participants to submit the strongest counter-case before the meeting.
- Protect dissent: record the strongest argument against the chosen verdict even when it loses.
- Separate the person from the thesis; the goal is a better decision, not a verdict on the team.
- Watch for status effects: senior agreement can suppress evidence.
- Give the decision owner the evidence and the options, not a forced consensus.
- Timebox the review. An open-ended strategy debate becomes an identity conflict.

## Failure modes

- Review as status reporting.
- Metrics chosen to show progress rather than to test the thesis.
- Moving the target after the result.
- Sunk cost presented as commitment.
- Strategy churn — a new direction every quarter without evidence.
- No verdict, only discussion.
- A pivot that changes the narrative but not the behavior.
- Killing a viable narrow segment because the broad thesis failed.
- Continuing a dead strategy because a large customer or a public commitment exists.
- Decision recorded but never reflected in the plan, pricing or product.

## Output

End with:

- the verdict and its evidence;
- the assumptions confirmed, weakened or falsified;
- what changes in the strategy brief, plan and economics;
- what is retained, stopped or parked;
- the next tests, owners and dates;
- the next review date and the tripwires that would advance it;
- the decision-log entry and its status.

The useful result is a strategy that is current, owned and still falsifiable.

Starting structure: [`assets/strategy-review.md`](../assets/strategy-review.md). Adapt or omit sections; do not fill it with invented evidence.
