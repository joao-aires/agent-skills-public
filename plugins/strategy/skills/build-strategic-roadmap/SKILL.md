---
name: build-strategic-roadmap
description: 'Turn an accepted strategy into a bounded operating period: observable outcomes, strategic initiatives, OKRs, capacity, dependencies, cadence and decision rights. Use after the strategy is accepted; stop before the product roadmap, PRD, feature sequencing or delivery commitments.'
user-invocable: true
metadata:
  kind: activity
  domain: product
  phase: planning
  scope: generic
  invocation: both
---

# Build a strategic roadmap

Convert strategic choices into a small set of outcomes, initiatives and decision rules the organization can run without re-deriving the strategy. Stop at an accepted roadmap with its period, owners and decision rules.

Use [business strategy](../business-strategy/SKILL.md) as the logic owner. Apply [operating plan](../business-strategy/references/operating-plan.md) and record the period with the [operating plan](../business-strategy/assets/operating-plan.md) asset. Reuse the accepted [strategy brief](../business-strategy/assets/strategy-brief.md) rather than restating it.

When the affected stack, architecture or domain has installed expertise or guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## Own the request

Frame the period, the decision owner and the outcomes the strategy requires next. Establish that the strategy is accepted. If it is still contested, return to [set-strategy](../set-strategy/SKILL.md) instead of planning execution against an unresolved choice.

## Inputs

- the accepted strategy brief and its constraints;
- current performance, cohort and unit-economics evidence;
- capacity, budget, hiring lead time and external dependencies, plus assumptions still waiting for evidence and existing commitments.

## Work

1. Derive a small number of observable outcomes from the strategic choices. State who changes, the baseline and source, target and window, owner, confirming evidence and a counter-signal.
2. Build an initiative portfolio mapping each initiative to the strategic choice it serves, the assumption it tests, its outcome, cost, owner and decision point. Remove work that serves no current choice.
3. Distinguish bets from maintenance, and state what is explicitly not being done with the reason and revisit condition.
4. Check capacity honestly: people and allocation, hiring and ramp, budget, support load, management attention and the critical path. Do not plan at full utilization.
5. Use OKRs only where a bounded shared set helps, keeping key results as measurable outcomes with a baseline and date. Set cadence and decision rights: who recommends, decides, is consulted and informed for strategic, portfolio, operating and exceptional decisions.
6. State confidence by initiative, leading indicators, the reforecast rule and what would reopen a strategic choice. Hand the business outcomes and constraints to product direction without choosing product scope.

## Output

- outcomes with baselines, targets, windows and owners;
- initiative portfolio with strategic links and decision points;
- explicit exclusions and deferred work;
- total capacity and constraints, dependencies, critical path, cadence, decision rights and handoff constraints; channel and commercial requirements come from plan-go-to-market rather than being returned to it.

## Stop and hand off

Stop at the strategic roadmap. It is a pre-SDLC strategy record: the strategy pack owns its craft and the record it produces. Do not produce a product roadmap, PRD, feature sequence, release plan or delivery commitment. Product direction turns this direction into those artifacts at the start of the SDLC. Hand evidence gaps to [test-assumptions](../test-assumptions/SKILL.md), channel and commercial capacity requirements to [plan-go-to-market](../plan-go-to-market/SKILL.md), and the period-end verdict to [review-strategy](../review-strategy/SKILL.md).
