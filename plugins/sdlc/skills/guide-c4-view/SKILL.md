---
name: guide-c4-view
description: Guide to producing and reviewing C4 context, container and component views. Use for system boundaries, responsibilities, actors, directed dependencies, current versus proposed state and text equivalents.
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

# C4 view guide

Read [activity system](../activity-system/SKILL.md) for scope, the [architecture-set contract](../artifact-system/references/contracts/architecture-set.md) for authority and [software types](../artifact-system/references/software-types.md) for the component evidence.

A C4 view is a **view artifact**, not the architecture itself. It should make responsibilities and dependencies inspectable at a chosen level, without pretending to be a complete inventory.

## Reader question

Can a reader identify the system boundary, the major elements, what each owns and which dependency crosses a consequential boundary?

## When to use

- a new system or a boundary change;
- a service, client, data store or external system needs a shared map;
- a proposed target must be compared with the current system;
- a reviewer needs to see responsibility and dependency rather than a folder tree.

Do not use a C4 view as a substitute for source evidence, a sequence, a data-ownership view or a deployment plan.

## Minimum content

- level: context, container or component;
- system boundary and external actors/systems;
- named elements and the responsibility of each;
- directed dependencies and the protocol or relationship where relevant;
- trust, data or deployment boundaries that change the meaning;
- current, proposed or mixed status;
- a short text equivalent of the important relationships.

## Structure and quality

- Choose the shallowest level that answers the question.
- Keep one story per view; do not mix context and component detail.
- Label elements by responsibility, not by repository folder.
- Use arrows for dependency direction, with a legend when notation is ambiguous.
- Separate current and proposed views; never relabel a proposal as current.
- Link source, contracts, decisions or observed evidence for the claims.
- Keep a text equivalent for readers who cannot render the diagram.

## Common failures

- a box for every folder or package;
- unlabeled arrows;
- a context view that hides an external actor or trust boundary;
- a proposed target presented as implemented;
- a C4 view with no text equivalent or evidence;
- using color alone to convey status.

## Authority, home and review

- **Authority:** the architecture set owns durable current-state views; the design proposal or RFC owns proposed target views.
- **Home:** application repository `docs/architecture/`; proposed views in the ECR/RFC or a linked design record.
- **Review:** use [design review](../design/references/design-review.md) and [artifact assurance](../artifact-system/references/assurance.md).

## Specialist route

Use `system-documentation` for evidence and current-state mapping, and `visualization` (`architecture-diagramming` or `system-flow-explorer`) for rendering or exploration. The view is not evidence of implementation by itself.

## Handoff

Record the view level, revision, current/proposed status, source links and the decision it supports. Reconcile the canonical architecture set only after verified implementation.
