---
name: test-assumptions
description: 'Design and interpret experiments that buy a specific decision: tie each test to an assumption, precommit the bar, grade the evidence and choose persevere, narrow, repackage, pivot, park or stop. Use when a live thesis needs behavioural evidence; use validate-idea for premise triage.'
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

# Test assumptions

Buy information that can change a named decision. A test is justified when the result could alter a choice and the cost is lower than the cost of being wrong.

Use [business strategy](../business-strategy/SKILL.md) as the logic owner. Apply [experiments and PMF](../business-strategy/references/experiments-and-pmf.md) and [research protocol](../business-strategy/references/research-protocol.md); record a test with the [validation plan](../business-strategy/assets/validation-plan.md) or [bet record](../business-strategy/assets/bet-record.md).

This activity starts after a premise survives triage. [validate-idea](../validate-idea/SKILL.md) challenges the premise and runs nothing; this activity designs, runs and interprets the evidence.

## Own the request

State the binding assumption, the decision it informs, the evidence grade the decision requires and the authority to contact people, change a funnel or run a pilot. Do not start a test whose outcome cannot change anything.

## Inputs

- current thesis, assumption ledger and confidence levels;
- existing behavioural evidence and its limits, plus access to participants, instrumentation, product changes or commercial terms, the budget, window and decision owner.

## Work

1. Choose the lowest rung that can produce a decision-grade answer: existing evidence, behavioural interview, artifact, manual delivery, priced commitment, live experiment or scaling test.
2. Specify the test before running it: hypothesis, eligibility, treatment and control, primary metric and definition, baseline and source, observation window, confounds, cost and owner.
3. Precommit pass, partial and fail thresholds derived from the decision — an economic, strategic, comparative or learning bar. Record any later change to the bar and why.
4. Run only the work the request authorizes; contacting users, adding tracking, changing live prices or shipping a pilot each need explicit scope. Interpret with the correct grade and read retention and PMF by cohort and segment, checking definition, mix, survivorship, seasonality and expansion.
5. Recommend persevere, narrow, repackage, park or stop for these assumptions. A pivot changes the strategy: propose it and hand it to [set-strategy](../set-strategy/SKILL.md) rather than deciding it here. State which assumption failed, what is retained and the next cheapest test, then persist the result, grade, limits and recommendation in the existing strategy state and decision log.

## Output

- test specification and precommitted bars;
- result with population, method, grade and limits;
- interpretation against the bar, including failed and partial results;
- decision, what would reopen it, and the updated assumption ledger and state.

## Stop and hand off

Stop at the evidence-based decision for these assumptions. Do not rewrite the whole strategy from one test or scale acquisition before retention is understood. Hand a changed thesis to [set-strategy](../set-strategy/SKILL.md), a scheduled verdict to [review-strategy](../review-strategy/SKILL.md), and the next period's commitments to [build-strategic-roadmap](../build-strategic-roadmap/SKILL.md).
