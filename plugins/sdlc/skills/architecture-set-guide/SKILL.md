---
name: architecture-set-guide
description: Guide to writing an architecture document set. Covers context, containers, components, runtime, data, interfaces, deployment, qualities, decisions and evidence.
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

# Architecture set guide

An architecture set is the coherent group of documents that explain the implemented system: its boundary, major elements, runtime behavior, data, interfaces, deployment and consequential decisions. It is system knowledge, not a proposal.

## Reader questions

1. What is the system boundary, and what is outside it?
2. What are the major containers or components, and what does each own?
3. How does a critical operation move through authority, validation, state and an external effect?
4. Where is data owned, stored, cached or projected?
5. How is the system deployed, and what differs between environments?
6. Which interfaces and contracts do consumers depend on?
7. Which quality attributes and failure paths matter?
8. Which decisions constrain the design, and where are they recorded?
9. What is implemented now, what is proposed, and what is unknown?

## Minimum content

- scope, status and revision;
- context and external actors;
- containers/components and responsibilities;
- critical runtime or sequence views;
- data ownership, lifecycle and consistency;
- important interfaces and contracts;
- deployment and environment differences;
- quality, failure and recovery;
- decisions and links to ADRs;
- evidence, gaps and open questions.

## Structure and quality

- Choose the smallest set that answers the reader's questions; not every system needs every document.
- Link the views from a docs index and from related decisions.
- Keep current and proposed views distinct; only verified implementation updates the current set.
- Give each view a short text equivalent of the important relationships.
- Use a consistent notation and define unfamiliar elements.
- Link source, contracts, tests, runtime observations or decisions for claims.
- Record uncertainty instead of making the architecture look complete.
- Reconcile the set when boundaries, interfaces or deployment change.

## Common failures

- a folder tree masquerading as architecture;
- diagrams with no text equivalent or evidence;
- a proposed target presented as current;
- every possible view created for a small system;
- interfaces or data ownership omitted;
- deployment described from configuration without observed state;
- decisions buried in prose instead of linked ADRs;
- stale views after a boundary change.

## Review

Read the set as a new contributor and an operator:

- Can you locate the responsible component for a behavior?
- Can you explain a critical journey and its failure path?
- Do you know where data is owned and which interfaces are contractual?
- Is current versus proposed clear?
- Are the decisions and evidence reachable?

## Handoff

The design, implementation and operations reader needs the current and proposed views, component responsibilities, interfaces, data ownership, deployment, decisions and evidence. Link the views rather than copying them into a change record.
