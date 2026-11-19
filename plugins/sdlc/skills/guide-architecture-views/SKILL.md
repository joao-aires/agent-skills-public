---
name: guide-architecture-views
description: Guide to producing and reviewing C4 and sequence views. Use for system boundaries, actors, responsibilities, directed dependencies, current versus proposed state, request ordering, synchronous versus asynchronous work, failure, retry, recovery and text equivalents.
user-invocable: true
metadata:
  kind: guide
  origin: local
  pack: sdlc
  domain: visualization
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Architecture view guide

Architecture views make selected parts of a system inspectable. Choose the view from the question: a C4 view explains structure, responsibility and dependency; a sequence view explains ordering, concurrency and failure. Neither is the architecture itself, and neither is proof that the implementation or runtime behavior exists.

## Choose the view

| Question | View |
| --- | --- |
| What is inside the boundary, who uses it, what are the major elements and what crosses a trust, data or deployment boundary? | C4 context, container or component view |
| What happens in what order, which work is synchronous or asynchronous, and what changes on rejection, timeout, retry, cancellation or partial failure? | Sequence view |

A C4 view is not a substitute for a sequence, data-ownership view, deployment plan or source evidence. A sequence view is not a static dependency map.

## Reader questions

1. What starts or bounds the behavior being explained?
2. Which actors, participants or elements matter, and what does each own?
3. Which dependencies or messages cross a boundary that changes the meaning?
4. What happens in what order, or which element depends on which?
5. Which branches change the decision: denial, timeout, retry, cancellation or partial failure?
6. Is this the current system or a proposed target?
7. Can I understand the important relationships from the text if the diagram does not render?

## Minimum content

### C4 view

- the level: context, container or component;
- the system boundary and external actors/systems;
- named elements and the responsibility of each;
- directed dependencies, with the protocol or relationship where relevant;
- trust, data or deployment boundaries that change the meaning;
- current, proposed or mixed status;
- a short text equivalent of the important relationships.

### Sequence view

- trigger and actor;
- participants and the responsibility of each;
- ordered calls, events or state changes;
- synchronous, asynchronous and fire-and-forget distinctions;
- success, rejection, timeout, retry and recovery branches that matter;
- the observable result and where completion becomes authoritative;
- a short text equivalent for the main path and one failure path.

## Structure and quality

- Choose the shallowest view or smallest scenario that answers the question.
- Keep one story per view; do not mix context and component detail.
- Name elements and participants by responsibility, not repository folder.
- Use arrows for dependency direction or message order, with a legend when notation is ambiguous.
- Label message intent, not only transport.
- Show the branch that changes the decision, not every internal call.
- Separate current and proposed behavior; never relabel a proposal as current.
- Link source, contracts, decisions, tests or observed evidence for the claims.
- Keep a usable text equivalent for readers who cannot render the diagram.
- Do not imply delivery, production behavior or a successful integration from a diagram alone.

## Common failures

- a box for every folder or package;
- unlabeled arrows or ambiguous asynchronous work;
- a context view that hides an external actor or trust boundary;
- a happy-path-only sequence;
- participants that do not exist in the system;
- hiding retry, idempotency, duplicate effects or partial failure;
- mixing current and proposed behavior;
- a proposed target presented as implemented;
- no text equivalent or evidence;
- using color alone to convey status;
- showing every internal call and losing the question.

## Review

Read the view as someone who must change or operate the system:

- Can you identify the boundary, elements or participants that matter?
- Does each have a clear responsibility?
- Are the important dependencies or messages labeled, directed and ordered correctly?
- Does the sequence show the failure path that changes behavior?
- Is synchronous versus asynchronous work explicit?
- Are current and proposed states unmistakable?
- Is the view supported by source, contract, test or decision evidence?
- Is there a usable text equivalent?

## Handoff

Record the view type, level or scenario, revision or date, current/proposed status, source links and the decision it supports. The implementer or operator should know which parts are proposed and which are already true. Reconcile canonical runtime documentation after verified implementation.
