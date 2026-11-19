---
name: guide-state-machine
description: Guide to producing and reviewing state machines. Use for states, triggers, guards, terminal states, denied transitions, invariants and concurrent or retried behavior.
user-invocable: true
metadata:
  kind: guide
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# State machine guide

A state machine explains which conditions an entity or workflow can be in, what may change them and what must never happen. It is not a UI flow, a list of calls or an implementation detail.

## Reader questions

1. Which states exist, and what does each mean?
2. What is the initial, terminal or blocked state?
3. What event moves the system between states?
4. What guard or condition must hold?
5. Which transitions are denied, and why?
6. What invariant must hold in each state?
7. What happens on retry, duplicate event, concurrency or partial completion?
8. Can I understand the main and denied paths from the text?

## When to use

- an entity or workflow has meaningful states and transitions;
- retries, cancellation, expiry, approval or partial completion matter;
- illegal transitions must be prevented or made explicit;
- several actors or components can change the same state;
- implementation needs a shared model before code.

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
- treating the diagram as proof that the implementation enforces it;
- a model nobody can map back to the code or data.

## Review

Read the model as an implementer and a tester:

- Can you tell which transitions are allowed and which are denied?
- Are guards and invariants explicit?
- Does the model cover retry, duplicate and concurrent events?
- Does it agree with the sequence and data behavior?
- Is there a text equivalent?
- Can tests be derived from the model?

## Handoff

Record the model, revision, current/proposed status and the invariants implementation must enforce. The implementer should know what must never happen and how illegal transitions are rejected. Verify enforcement in code and tests before claiming the model is implemented.
