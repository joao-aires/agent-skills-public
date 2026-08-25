# Strategy Stress Testing

## Purpose

Before recommending a strategy, attempt to break it.

Stress testing is not a generic risk list. It should identify failure mechanisms that would cause a different decision.

## 1. Pre-mortem

Assume the strategy failed badly three years from now.

Ask:

- What happened?
- Which assumption was wrong?
- What did competitors do?
- Why did customers not adopt or expand?
- Where did economics fail?
- What did the team underestimate?

Rank failure modes by likelihood × impact.

## 2. Incumbent response

Model the strongest rational reaction:

- copy feature
- bundle for free / low incremental cost
- acquire competitor
- cut price
- block distribution or API access
- create a standard
- use installed base to cross-sell

Then ask whether the company still has a path to win.

## 3. Customer non-adoption

Test the case where customers agree the problem exists but still do not buy.

Possible reasons:

- no budget owner
- low urgency
- behavior change
- trust
- procurement
- implementation burden
- value accrues to user but cost is paid by another function

## 4. Distribution failure

Ask:

- What if CAC is 3× expected?
- What if the preferred channel does not convert?
- What if community adoption does not produce enterprise leads?
- What if sales cycles are twice as long?

A good product with no efficient route to market is not a good strategy.

## 5. Economic stress

Run downside assumptions for:

- price
- gross margin
- churn
- expansion
- variable compute/API cost
- support burden
- sales productivity

Identify the variable that most threatens viability.

## 6. Dependency stress

Test major dependencies:

- one model/platform/provider
- one distribution channel
- one customer
- regulation
- a key integration
- founder-specific expertise

Ask what happens if the dependency changes terms or disappears.

## 7. Commoditization stress

Assume core technology becomes dramatically cheaper and easier to reproduce.

What remains differentiated?

If the answer is "our implementation is better," the long-term thesis may be weak.

## 8. Future-state stress

Use the future scenarios to test whether the company is solving an invariant customer need or a temporary artifact of today's stack.

## 9. Strategy coherence

Check that the pieces reinforce each other:

- wedge matches target customer
- positioning matches differentiated capability
- distribution reaches that customer
- pricing matches value and buyer
- expansion follows naturally from adoption
- moat grows from product usage
- economics support GTM

A collection of individually attractive choices can still be incoherent.

## 10. Falsifiability

For every critical belief ask:

> What observable result would make us stop, pivot, or choose a different strategy?

Avoid tripwires that can always be explained away.

## Verdict

Conclude with one of:

- **Proceed** — risks are acceptable and critical assumptions have reasonable evidence
- **Proceed with tests** — thesis is attractive but one or more high-impact uncertainties must be tested before scaling
- **Pivot thesis** — evidence supports a materially different formulation
- **Do not pursue now** — expected value is poor under realistic assumptions

State what evidence would change the verdict.