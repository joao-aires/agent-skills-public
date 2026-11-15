---
name: guide-design-proposal
description: Guide to writing a design proposal. Covers the decision, constraints, affected components, materially different options, linked artifacts, tradeoffs, seam and recommendation.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Design proposal guide

A design proposal records a consequential design choice before implementation: the question, the constraints, the options, the evidence used to judge them, the tradeoffs and the recommendation. It is not an implementation plan and not a substitute for the design specification or architecture views.

## Reader questions

1. What decision is being made, and what constraints bound it?
2. Which components are affected, and which are not?
3. Which materially different options were considered?
4. What artifact lets me judge each option: design specification, C4, sequence, state machine, compatibility matrix?
5. What does each option optimize, sacrifice and do under failure or denial?
6. What has been decided at the interface between components?
7. Which option is recommended, who decides, and when should the decision be revisited?

## Minimum content

- decision, outcome and constraints;
- current state or greenfield;
- affected components and what is not affected;
- at least three materially different options for a consequential choice;
- linked design artifacts that let a reviewer judge each option;
- tradeoffs and failure behavior;
- interface or seam decisions when more than one component is involved;
- recommendation, decision owner, status and revisit trigger;
- evidence and open questions.

## Structure and quality

- State the decision first; the history follows.
- Make options differ in responsibility, behavior, ownership or failure, not in color or wording.
- Use comparable fidelity across options.
- Link the design specification, C4, sequence or state model rather than describing it twice.
- Explain what each option makes easier and harder.
- Record the rejected alternatives and the reason.
- Decide the seam once, not in each section.
- Keep the proposal open long enough to be challenged, then record the accepted decision.

## Common failures

- three cosmetic variants presented as options;
- a recommendation with no alternatives;
- no linked artifact to judge the options;
- hiding failure, migration or operational cost;
- duplicating the seam in each component section;
- an accepted design with no owner;
- a proposal that claims implementation.

## Review

Read the proposal as a reviewer and implementer:

- Is the decision and its constraints clear?
- Are the options real and comparably represented?
- Are the tradeoffs and failure behavior honest?
- Is the seam decided once?
- Is the recommendation owned and revisitable?
- Is the accepted design distinguishable from a proposal?

## Handoff

The implementer needs the decision, affected components, rejected alternatives, linked design artifacts, seam and what may start or must wait. A design proposal can be accepted while implementation is blocked; say so.
