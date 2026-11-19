---
name: review-strategy
description: Re-test an existing strategy against new evidence and decide continue, narrow, park, pivot or kill. Use for scheduled strategy reviews, fired tripwires and red-team challenges; produce a recorded verdict, not a status meeting.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: product
  domain: product
  phase: cross-phase
  scope: generic
  invocation: both
  role: task
---

# Review strategy

Ask whether the current choices still deserve their cost. A review is not a status report, a budget exercise or an occasion to relitigate preferences.

Use [business strategy](../business-strategy/SKILL.md) as the logic owner. Apply [strategy review and pivot](../business-strategy/references/strategy-review-and-pivot.md) and [strategy stress testing](../business-strategy/references/strategy-stress-testing.md); record the session with the [strategy review](../business-strategy/assets/strategy-review.md) asset and the outcome in the [decision log](../business-strategy/assets/decision-log-template.md).

## Own the request

Set the review's scope and decision owner: a scheduled quarterly review, a fired tripwire or a specific assumption challenge. Name the horizon and the quorum that can actually change the strategy.

## Inputs

- the current strategy brief and decision history;
- assumption and evidence state, including failed and partial tests;
- actual outcomes against the last plan, plus unit economics, cash, runway, and competitive, market, regulatory and product changes since the last review. Circulate this evidence in advance, including what did not work: a review that cannot see failure cannot decide.

## Work

1. Check each tripwire against its signal, threshold, window and the decision it reopens. Distinguish a signal to investigate from a kill criterion.
2. Steelman the strategy first: why it is the best available choice, what must be true, what has been learned and which alternative it beats. Then attack it: weakest critical assumption, least flattering explanation for a miss, what is being explained away, the strongest incumbent response and what you would do starting today without sunk cost.
3. Run a pre-mortem in the review horizon and convert plausible failure paths into tests, mitigations or new tripwires. Use a red-team role and independent written input so seniority does not suppress dissent.
4. Decide one verdict per coherent unit: continue, narrow, park, pivot or kill. Do not average; split the decision when one segment works and another does not.
5. State what is retained and released, which assumptions changed, the new thesis and its first test, and the opportunity cost. Record the verdict and any proposed thesis change with status proposed; [set-strategy](../set-strategy/SKILL.md) accepts it.

## Output

- verdict and the evidence behind it;
- assumptions confirmed, weakened or falsified;
- tripwire results and any changed thresholds;
- what changes in the brief, model, plan and economics, plus what is retained, stopped or parked;
- next tests, owners, dates, next review trigger and decision-log status.

## Stop and hand off

Stop at the recorded verdict. Do not turn the review into task replanning or a new strategy document. Hand a changed thesis to [set-strategy](../set-strategy/SKILL.md), new evidence needs to [test-assumptions](../test-assumptions/SKILL.md), model and pricing implications to [design-business-model](../design-business-model/SKILL.md) and [model-finances](../model-finances/SKILL.md), commercial execution to [plan-go-to-market](../plan-go-to-market/SKILL.md), and the next period's commitments to [build-strategic-roadmap](../build-strategic-roadmap/SKILL.md).
