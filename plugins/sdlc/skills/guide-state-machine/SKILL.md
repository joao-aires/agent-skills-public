---
name: guide-state-machine
description: Guide to producing and reviewing state machines. Use for states, triggers, guards, terminal states, denied transitions, invariants and concurrent or retried behavior.
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

# State machine guide

Read [activity system](../activity-system/SKILL.md) for scope, the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for authority and [software types](../artifact-system/references/software-types.md) for the component evidence.

A state machine is a **view artifact** of a behavior model. It is not a UI flow, a sequence of calls or an implementation detail. It answers what states exist, what may change them and what must never happen.

## Reader question

Can a reviewer tell which states are valid, what moves between them, what is denied, and how concurrent or repeated events affect the result?

## When to use

- an entity or workflow has meaningful states and transitions;
- retries, cancellation, expiry, approval or partial completion matter;
- illegal transitions must be prevented or made explicit;
- several components or actors can change the same state;
- the design needs a shared model before code.

Do not use a state machine for a simple one-way flow or a static dependency map.

## Minimum content

- state names and meaning;
- initial, terminal and blocked states;
- triggers and guards for each transition;
- denied or invalid transitions that matter;
- invariants that must hold in each state;
- concurrency, retry and duplicate-event behavior;
- the observable event or result for each transition;
- a text equivalent for the main and denied paths.

## Structure and quality

- Name states as conditions, not actions.
- Name transitions as events, not implementation methods.
- Keep guards explicit; “it depends” is not a state.
- Show the states that change the decision; do not draw every internal flag.
- Separate current and proposed models.
- Link the owning code, contract or decision.
- Keep the model consistent with the sequence and data views.

## Common failures

- states that are really booleans or fields;
- a trigger with no guard or owner;
- no terminal or denied state;
- an arrow that hides a retry or duplicate event;
- a state machine that contradicts the sequence view;
- treating the diagram as proof that the implementation enforces it.

## Authority, home and review

- **Authority:** the design proposal/ECR decision; the implementation and tests own actual enforcement.
- **Home:** design record, architecture set or the affected module's documentation.
- **Review:** use [design review](../design/references/design-review.md) and [artifact assurance](../artifact-system/references/assurance.md).

## Specialist route

Use `system-design` for state ownership and consistency, backend or domain modeling for the rules, and `interface-design` only when the state model changes the user's visible path. The model does not replace tests for illegal transitions.

## Handoff

Record the model, revision, current/proposed status and the invariants that implementation must enforce. Verify the enforcement in code and tests before claiming the state model is implemented.
