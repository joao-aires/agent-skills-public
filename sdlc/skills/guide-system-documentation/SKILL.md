---
name: guide-system-documentation
description: Guide to discovering, tracing, creating and reviewing the current-system architecture set. Covers evidence, boundaries, responsibilities, runtime behavior, interfaces, deployment, current versus proposed state and document quality.
user-invocable: true
metadata:
  kind: guide
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
---

# System documentation guide

This guide covers both halves of current-system documentation: discovering and tracing what the system actually does, and shaping that evidence into the architecture set a reader can use. It is system knowledge, not a proposal.

The architecture-set contract owns the set, its required content and its maintenance; the activity system owns discovery scope and stopping point when discovery is requested as an activity. For view craft, use [guide-architecture-views](../guide-architecture-views/SKILL.md) rather than reproducing their guidance here.

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

## Scope and modes

Discover the requested product or feature, repositories, documents and target output. Begin with the narrow relevant paths and expand when a dependency requires it. Accept any architecture: monolith, browser, VM, container, serverless, batch or managed service.

- **Interactive:** resolve ambiguous scope and critical user tasks after inspecting available evidence.
- **Setup or feature:** map existing and proposed boundaries and trace the affected journey, including migrations and new dependencies. Separate proposed design from observed implementation.
- **Recurring review:** compare a supplied base revision and current sources, refresh impacted nodes and flows, retain stable IDs and provenance, and report contradictions or missing owners without inventing answers.

Discovery supports design, implementation and operations. Durable current-state documentation is the architecture set described below; a bounded feature can return only the affected trace and evidence gaps.

Consult [references/mapping-guide.md](references/mapping-guide.md) for the evidence model, view examples and practical discovery workflow.

## Discover the current system

1. Inventory source entry points, routes, commands, consumers, jobs and visible UI capabilities. Use contracts and handlers, not repository naming alone. Record each component's software type (frontend, backend, AI or library/CLI) and platform or domain constraints as notes, not separate types; record the software type as a note.
2. Inspect clients, configuration references, queue or topic bindings, datastore access and dependency contracts. Classify runtime edges separately from build or package dependencies.
3. Derive hosting and target topology from actual infrastructure and delivery definitions. Resolve rendered overrides where relevant; use live state as a cross-check, not as an assumption that desired state is deployed.
4. Identify ownership, operational documentation and signal identities. Record the evidence source, revision and time for each node and edge.
5. Model representative critical journeys from user intent to outcome. Include client-only work, external systems, caches, failures, retries, asynchronous completion and optional or degraded paths.
6. Inspect the canonical context, container and critical sequence or dataflow views at a known application revision. Create or update **implemented-state** diagrams in the application's established documentation when missing or changed, and keep **proposed target** diagrams in the change ECR or RFC until reconciliation. Use editable Mermaid or the existing notation at an appropriate depth.
7. Reconcile conflicting documentation, code and live evidence with dates and explicit unresolved decisions. Absence from sampled traces does not prove that no dependency exists.

Keep the evidence beside the relationship it supports. A package import shows a code dependency; a configured client and its call site can show a runtime dependency; deployment configuration shows intended hosting. These support different claims. Record uncertainty instead of making the architecture look more complete than the sources permit.

## Trace a feature before changing it

For bounded feature work, begin with a comparable behavior or the entry point being changed. Follow its actual calls and transformations through permission checks, domain logic, stored changes and the result seen by its consumer. Locate the tests and configuration that exercise that path. Expand the investigation when a dependency or conflicting source changes your understanding; a folder tour alone does not establish how the feature works.

Keep a compact trace with navigable code references:

- where the behavior starts;
- which components own its decisions and effects;
- what existing pattern can be reused;
- what remains uncertain.

Distinguish current behavior from a proposed extension. Pass the trace into design so the proposal can name integration points and explain departures from existing patterns. Read the critical source yourself when relying on another actor's exploration; a summary is a guide to evidence, not a replacement for it.

## Keep current and proposed explicit

- **Current** means implemented and evidenced at a linked revision.
- **Proposed** means a target view in an ECR or RFC, not yet implemented.
- **Mixed** means part of the view is current and part is proposed; label the parts.

Do not update the canonical current view to match a proposal. Reconcile it after implementation and link the decision that authorized the change. A diagram does not establish architectural truth by itself; compare it with source, contracts and observed behavior.

## Shape of the set

The contract owns which documents the set contains and what each must answer. Choose the smallest set that answers the reader's questions; not every system needs every document. A small application may need only a context view, a container view and a runtime sequence for its critical journey.

A typical set includes:

- a context view: system boundary, actors, external systems and responsibilities;
- a container view: applications, data stores, protocols, responsibilities and trust boundaries;
- selected component views where internal responsibility or coupling needs explanation;
- critical runtime or sequence views: authority, validation, state, external effect, failure and recovery;
- data and ownership: canonical stores, lifecycle, consistency and migration boundaries;
- interface views: important consumer contracts, errors, idempotency and compatibility;
- deployment: environments, nodes or processes, storage, networks, release jobs and trust boundaries;
- quality and failure: relevant scenarios, observability, recovery and open gaps;
- links to accepted decisions and a glossary.

Each view declares its type, scope and status. Use understandable element types, responsibilities, technologies and directed relationships. Label protocols and optional boundaries, add a legend where notation needs one, and keep a text equivalent for important relationships.

## Minimum content

- scope, status and revision;
- context and external actors;
- containers or components and their responsibilities;
- critical runtime or sequence views;
- data ownership, lifecycle and consistency;
- important interfaces and contracts;
- deployment and environment differences;
- quality, failure and recovery;
- decisions and links to ADRs;
- evidence, gaps and open questions.

## Create or update the set

- Start from a reader question and choose the shallowest view that answers it. One story per view; do not mix context and component detail.
- Name elements by responsibility, not by repository folder. Give each a clear boundary and label directed dependencies and the protocol or relationship where relevant.
- Analyse important interfaces rather than listing endpoints: resource identity, operations and lifecycle, actor or tenant scope, request and response schemas, validation, side effects, errors, concurrency, idempotency, pagination, time and units, events and compatibility. Inspect generated contracts against code; a declared response or media type may omit runtime behavior.
- Connect requirements to design mechanisms and verification. Explain tradeoffs and operational consequences: security and privacy, availability, recovery, observability, performance and cost, process-local state and scaling. Link ADRs and service definitions; unknown rationale or unapproved SLOs remain open facts.
- Link source, contracts, tests, runtime observations or decisions for claims. Record uncertainty instead of making the architecture look complete.
- Reconcile the set when boundaries, interfaces or deployment change. Update the affected views and dependent journeys rather than recreating the baseline.
- Keep volatile live replicas, tags and tuning in timestamped observations rather than static architectural truth. Omit secrets and personal data.

## Structure and quality

- Choose the smallest set that answers the reader's questions.
- Link the views from a docs index and from related decisions.
- Keep current and proposed views distinct; only verified implementation updates the current set.
- Give each view a short text equivalent of the important relationships.
- Use a consistent notation and define unfamiliar elements.
- Link source, contracts, tests, runtime observations or decisions for claims.
- Record uncertainty instead of making the architecture look complete.
- Reconcile the set when boundaries, interfaces or deployment change.

Validate references and diagram participant names against the evidence; mark inferred or proposed edges with explicit labels. Do not force components into microservices or create unsupported acronym expansions. Hand journey definitions to reliability expertise, incident scope to incident investigation expertise, and procedure gaps to operating-procedure expertise when appropriate; the model remains useful without those installed.

## Review

Read the set as a new contributor and an operator:

- Can you locate the responsible component for a behavior?
- Can you trace a critical operation, identify authority and commit boundaries, and explain a failure or retry?
- Do you know where data is owned and which interfaces are contractual?
- Is current versus proposed clear?
- Are the decisions and evidence reachable?
- Can you understand the important relationships from the text if the diagram does not render?

Check source mappings, exact interfaces, cross-view names and current or target consistency. Parse and render diagrams with the project's available tooling; inspect readability as well as syntax. Generated schemas and link checks cannot prove architectural truth, full authorization or provider behavior.

## Common failures

- a folder tree masquerading as architecture;
- a repository name catalogue with no journeys or responsibilities;
- diagrams with no text equivalent or evidence;
- a proposed target presented as current;
- every possible view created for a small system;
- interfaces or data ownership omitted;
- deployment described from configuration without observed state;
- decisions buried in prose instead of linked ADRs;
- stale views after a boundary change;
- unlabeled arrows, unsupported acronym expansions or components forced into an assumed architecture.

## Handoff

The design, implementation and operations reader needs the current and proposed views, component responsibilities, interfaces, data ownership, deployment, decisions and evidence. Link the views rather than copying them into a change record. When the work is a bounded trace, hand over the starting point, owning components, reusable pattern and remaining uncertainty.
