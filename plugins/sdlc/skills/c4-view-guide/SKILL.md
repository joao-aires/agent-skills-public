---
name: c4-view-guide
description: Guide to producing and reviewing C4 context, container and component views. Use for system boundaries, actors, responsibilities, directed dependencies, current versus proposed state and text equivalents.
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

A C4 view is a map of a software system at a chosen level of detail. It answers who uses the system, what the major elements are, what each owns and which dependency crosses a boundary that matters.

A C4 view is not the architecture itself. It is a view that makes part of the architecture inspectable, and it is only as trustworthy as the evidence behind it.

## Reader questions

1. What is inside the system boundary, and what is outside it?
2. Who are the actors and external systems?
3. What are the major elements, and what does each own?
4. Which dependencies cross a trust, data or deployment boundary?
5. Is this the current system or a proposed target?
6. Can I understand the important relationships from the text if the diagram does not render?

## When to use

- a new system or a boundary change;
- a service, client, data store or external system needs a shared map;
- a proposed target must be compared with the current system;
- a reviewer needs responsibility and dependency rather than a folder tree.

Do not use a C4 view as a substitute for a sequence, a data-ownership view, a deployment plan or source evidence.

## Minimum content

- the level: context, container or component;
- the system boundary and external actors/systems;
- named elements and the responsibility of each;
- directed dependencies, with the protocol or relationship where relevant;
- trust, data or deployment boundaries that change the meaning;
- current, proposed or mixed status;
- a short text equivalent of the important relationships.

## Structure and quality

- Choose the shallowest level that answers the question.
- Keep one story per view; do not mix context and component detail.
- Label elements by responsibility, not by repository folder.
- Use arrows for dependency direction and include a legend when notation is ambiguous.
- Separate current and proposed views; never relabel a proposal as current.
- Link source, contracts, decisions or observed evidence for the claims.
- Keep a text equivalent for readers who cannot render the diagram.

## Common failures

- a box for every folder or package;
- unlabeled arrows;
- a context view that hides an external actor or trust boundary;
- a proposed target presented as implemented;
- a C4 view with no text equivalent or evidence;
- using color alone to convey status;
- a view that is technically neat but does not answer the reader's question.

## Review

Read the view as someone who must change the system:

- Can you identify the boundary and the elements that matter?
- Does each element have a clear responsibility?
- Are the important dependencies labeled and directed correctly?
- Are current and proposed states unmistakable?
- Is the diagram supported by source, contract or decision evidence?
- Is there a usable text equivalent?

## Handoff

Record the view level, the revision or date, the current/proposed status, the source links and the decision it supports. The implementer or operator should know which parts are proposed and which are already true. Do not claim implementation from a diagram alone.
