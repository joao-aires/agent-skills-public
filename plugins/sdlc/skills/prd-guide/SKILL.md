---
name: prd-guide
description: Guide to writing a product brief or PRD. Covers problem, audience, outcome, scope, success signal, constraints, evidence and open decisions.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: product
  phase: planning
  scope: generic
  invocation: both
  role: support
---

# PRD guide

A product brief or PRD explains why a product or change is worth doing, for whom, what outcome it promises and how success will be recognized. It is product intent, not a feature list and not an implementation plan.

## Reader questions

1. What problem are we solving, for whom, and why now?
2. What outcome or behavior should change?
3. What is in scope, and what is explicitly not?
4. How will we know it worked?
5. What constraints, dependencies and risks shape the choice?
6. Which decisions are still open, and who owns them?
7. What evidence supports the problem and the promised outcome?

## Minimum content

- problem and affected audience;
- why this matters now and what happens if we do nothing;
- desired outcome and user/business value;
- scope and non-goals;
- success signal or acceptance evidence;
- constraints, dependencies and risks;
- open decisions and owners;
- links to research, strategy, roadmap and the change record.

## Structure and quality

- Lead with the problem and evidence, not the solution.
- Describe the outcome in user or business terms; keep implementation choices out unless they are constraints.
- Make the non-goals explicit; they prevent scope creep.
- Distinguish a measured baseline from a hypothesis.
- State the smallest useful slice and what is deferred.
- Keep claims proportionate to the evidence; link the source.
- Use real user language and avoid internal jargon.
- If a solution is already accepted, say so and link the decision.

## Common failures

- a feature list with no problem or audience;
- “everyone” as the audience;
- success defined as “ship it”;
- no non-goals;
- implementation detail presented as product intent;
- unsupported market or user claims;
- open decisions hidden or assigned to “the team”;
- a brief that never links to the research or strategy it depends on.

## Review

Read the brief as a product, design and engineering partner:

- Do we agree on the problem, audience and outcome?
- Is the scope small enough to act on and clear enough to say no?
- Is the success signal observable?
- Are constraints and open decisions explicit?
- Is the evidence strong enough for the decision being requested?

## Handoff

The requirements and design reader needs the audience, outcome, scope, success signal, constraints and open decisions. Link the research and strategy rather than copying them. The brief should let the next phase start without re-litigating why the work exists.
