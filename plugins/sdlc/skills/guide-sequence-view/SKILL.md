---
name: guide-sequence-view
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

Read [activity system](../activity-system/SKILL.md) for scope, the [architecture-set contract](../artifact-system/references/contracts/architecture-set.md) for durable views and [software types](../artifact-system/references/software-types.md) for the affected components.

A sequence view is a **view artifact** that answers “what happens, in what order, and who owns each step.” It is not a substitute for a contract, a state model or failure analysis.

## Reader question

Can a reviewer follow a consequential operation from trigger to observable result, including the branches and failures that change the outcome?

## When to use

- request, event, job or tool-call ordering matters;
- synchronous versus asynchronous completion is unclear;
- retry, timeout, cancellation or partial failure changes behavior;
- several components or external systems participate;
- a seam between frontend, backend or AI needs a shared explanation.

Do not use a sequence view for a static dependency map; use a C4 view.

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
- Use participant names that match the accepted components.
- Label the message intent, not only the transport.
- Show the branch that changes the decision, not every internal call.
- Separate current and proposed behavior.
- Link the contract, source, decision or test evidence.
- Do not imply delivery or production behavior from a diagram alone.

## Common failures

- a happy-path-only sequence;
- participants that do not exist in the system;
- unordered arrows or ambiguous async work;
- hiding retry/idempotency/duplicate effects;
- mixing current and proposed behavior;
- treating a sequence as proof that an integration works.

## Authority, home and review

- **Authority:** architecture set for current behavior; design proposal/RFC for proposed behavior.
- **Home:** `docs/architecture/runtime/` or the ECR/RFC design record.
- **Review:** use [design review](../design/references/design-review.md) and [artifact assurance](../artifact-system/references/assurance.md).

## Specialist route

Use `system-documentation` for evidence, `system-design` for state, ownership and failure decisions, and `visualization` for rendering. Use backend or integration expertise when the sequence depends on a real protocol.

## Handoff

Record the scenario, participants, revision, current/proposed status and the failure path shown. Reconcile canonical runtime views after verified implementation.
