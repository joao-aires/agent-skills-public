---
name: sequence-view-guide
description: Guide to producing and reviewing sequence views. Use for participant responsibilities, request ordering, synchronous versus asynchronous work, branches, failure, retry and recovery.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: visualization
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Sequence view guide

A sequence view explains what happens, in what order, and who owns each step. It is useful when ordering, concurrency or failure changes the outcome, and misleading when the reader only needs a static dependency map.

## Reader questions

1. What starts the operation?
2. Which participants are involved, and what does each own?
3. What happens in what order?
4. Which work is synchronous, asynchronous or fire-and-forget?
5. What changes on rejection, timeout, retry, cancellation or partial failure?
6. Where does completion become authoritative?
7. Can I understand the main path and one failure path from the text?

## When to use

- request, event, job or tool-call ordering matters;
- synchronous versus asynchronous completion is unclear;
- retry, timeout, cancellation or partial failure changes behavior;
- several components or external systems participate;
- a boundary between UI, service, data or AI needs a shared explanation.

Do not use a sequence view for a static dependency map; use a C4 or component view.

## Minimum content

- trigger and actor;
- participants and the responsibility of each;
- ordered calls, events or state changes;
- synchronous, asynchronous and fire-and-forget distinctions;
- success, rejection, timeout, retry and recovery branches that matter;
- the observable result and where completion becomes authoritative;
- a short text equivalent for the main path and one failure path.

## Structure and quality

- Keep one operation or scenario per view.
- Use participant names that match the real components.
- Label message intent, not only the transport.
- Show the branch that changes the decision, not every internal call.
- Separate current and proposed behavior.
- Link the contract, source, decision or test evidence.
- Do not imply delivery or production behavior from a diagram alone.

## Common failures

- a happy-path-only sequence;
- participants that do not exist in the system;
- unordered arrows or ambiguous async work;
- hiding retry, idempotency or duplicate effects;
- mixing current and proposed behavior;
- treating a sequence as proof that an integration works;
- showing every internal call and losing the question.

## Review

Read the sequence as an implementer or operator:

- Can you follow the operation from trigger to observable result?
- Are the participants and their responsibilities clear?
- Does the view show the failure path that changes behavior?
- Is synchronous versus asynchronous work explicit?
- Is the current/proposed status clear?
- Is the evidence or source linked?

## Handoff

Record the scenario, participants, revision, current/proposed status and the failure path shown. The implementer should know what must happen, in what order, and what happens when a step fails. Reconcile canonical runtime documentation after verified implementation.
