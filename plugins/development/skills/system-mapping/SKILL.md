---
name: system-mapping
description: >-
  Discover and document an application's current architecture: services,
  dependencies, deployment topology, journeys, C4/sequence views and interfaces from
  repository, documentation and runtime evidence. Use for setup, feature analysis,
  architecture documentation and recurring architecture updates.
metadata:
  scope: generic
  invocation: both
  version: '1.0'
  role: support
user-invocable: true
---

# System mapping

Explain how the application actually carries work from an entry point to a result. Start with a relevant user action, request, job or command and follow the code, configuration and stored data involved. The map should let another contributor find the responsible component and understand why it depends on another one.

Keep the evidence beside the relationship it supports. A package import shows a code dependency; a configured client and its call site can show a runtime dependency; deployment configuration shows intended hosting. These support different claims. Record uncertainty instead of making architecture look more complete than the sources permit.

## Scope and modes

Discover the requested product/feature, repositories, documents and target output. Begin with the narrow relevant paths; expand when a dependency requires it. Accept any architecture: monolith, browser, VM, container, serverless, batch or managed service.

- **Interactive:** resolve ambiguous scope and critical user tasks after inspecting available evidence.
- **Setup/feature:** map the existing/proposed boundaries and trace the affected journey, including migrations and new dependencies. Separate proposed design from observed implementation.
- **Recurring review:** compare a supplied base revision and current sources, refresh impacted nodes/flows, retain stable IDs/provenance, and report contradictions or missing owners without inventing answers.

Consult [references/mapping-guide.md](references/mapping-guide.md) for deeper implementation details when needed.

## Trace a feature before changing it

For bounded feature work, begin with a comparable behavior or the entry point being changed. Follow its actual calls and transformations through permission checks, domain logic, stored changes and the result seen by its consumer. Locate the tests and configuration that exercise that path. Expand the investigation when a dependency or conflicting source changes your understanding; a folder tour alone does not establish how the feature works.

Keep a compact trace with navigable code references:

- where the behavior starts;
- which components own its decisions and effects;
- what existing pattern can be reused;
- what remains uncertain.

Distinguish the current behavior from a proposed extension. Pass the trace into design so the proposal can name integration points and explain departures from existing patterns. Read the critical source yourself when relying on another actor's exploration; a summary is a guide to evidence, not a replacement for it.

## Discovery

1. Inventory source entry points, routes, commands, consumers, jobs and visible UI capabilities. Use contracts and handlers, not repository naming alone.
2. Inspect clients, configuration references, queue/topic bindings, datastore access and dependency contracts. Classify runtime edges separately from build/package dependencies.
3. Derive hosting/target topology from actual infrastructure and delivery definitions. Resolve rendered overrides where relevant; use live state as a cross-check, not an assumption that desired state is deployed.
4. Identify ownership, operational docs and signal identities. Record evidence source/revision/time for each node and edge.
5. Model representative critical journeys from user intent to outcome. Include client-only work, external systems, caches, failures, retries, async completion and optional/degraded paths.
6. Inspect the canonical existing context/container and critical sequence/dataflow views at a known app revision. Create/update **implemented-state** diagrams in the app's established docs when missing or changed, and keep **proposed target** diagrams in the change ECR/RFC until reconciliation. Use editable Mermaid or existing notation at appropriate depth. Do not force components into microservices or create unsupported acronym expansions.
7. Reconcile conflicting docs/code/live evidence with dates and explicit unresolved decisions. Absence from sampled traces does not prove no dependency.

## Output

Choose the output for the requested scope. A bounded feature can use the compact trace and affected evidence gaps above. A system-wide baseline needs a service/component catalog, dependency edges, topology, representative journeys and ownership/evidence gaps; choose diagrams and tables that make those relationships understandable. A recurring review can return the affected changes and remaining gaps without recreating the baseline.

- Keep volatile live replicas/tags/tuning in timestamped observations rather than static architectural truth.
- Omit secrets and personal data from generated docs.

Validate references and diagram participant names against the evidence; mark inferred/proposed edges with explicit labels. Hand journey definitions to reliability expertise, incident scope to incident investigation expertise, and procedure gaps to operating-procedure expertise when appropriate; the model remains useful without those installed.

## Document the architecture set

When the output is durable architecture documentation, maintain the coherent set defined by the [architecture-set contract](../artifact-system/references/contracts/architecture-set.md). The set usually includes:

- a context view: system boundary, actors, external systems and responsibilities;
- a container view: applications, data stores, protocols, responsibilities and trust boundaries;
- selected component views where internal responsibility or coupling needs explanation;
- critical runtime/sequence views: authority, validation, state, external effect, failure and recovery;
- data and ownership: canonical stores, lifecycle, consistency and migration boundaries;
- interface views: important consumer contracts, errors, idempotency and compatibility;
- deployment: environments, nodes/processes, storage, networks, release jobs and trust boundaries;
- quality/failure: relevant scenarios, observability, recovery and open gaps;
- links to accepted decisions and a glossary.

Each diagram declares its type, scope and status. Use understandable element types, responsibilities, technologies and directed relationships. Label protocols and optional boundaries; add a legend where notation needs one. Explain what the reader should infer and what the view does not establish. Keep a text equivalent for important relationships.

Keep **current** and **proposed** explicit. Current means implemented and evidenced at a linked revision; proposed means a target view in an ECR or RFC. Do not update the canonical current view to match a proposal. Reconcile it after implementation and link the decision that authorized the change.

Analyse important interfaces rather than listing endpoints: resource identity, operations/lifecycle, actor/tenant scope, request/response schemas, validation, side effects, errors, concurrency, idempotency, pagination, time/units, events and compatibility. Inspect generated contracts against code; a declared response or media type may omit runtime behavior.

Connect requirements to design mechanisms and verification. Explain tradeoffs and operational consequences: security/privacy, availability, recovery, observability, performance/cost, process-local state and scaling. Link ADRs and service definitions; unknown rationale or unapproved SLOs remain open facts.

Check source mappings, exact interfaces, cross-view names and current/target consistency. Parse and render diagrams with the project's available tooling; inspect readability as well as syntax. Generated schemas and link checks cannot prove architectural truth, full authorization or provider behavior.

Test reader questions: can a contributor trace a critical operation, identify authority/state/commit boundaries, explain a failure/retry and locate the evidence? Use proportionate checks. For an explicitly requested interactive HTML walkthrough, hand the evidence to interactive system explanation expertise when available; static maps and inventories do not require its JSON contract or renderer.
