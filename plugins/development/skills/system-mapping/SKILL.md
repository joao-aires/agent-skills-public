---
name: system-mapping
description: Discover and document an application's services, dependencies, deployment
  topology and user/request/data journeys from repository, documentation and runtime
  evidence for setup, feature analysis or recurring architecture updates.
metadata:
  scope: generic
  invocation: both
  version: '1.0'
  role: support
user-invocable: false
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
6. Draw Mermaid context/container and sequence/dataflow views at the depth needed. Do not force components into microservices or create unsupported acronym expansions.
7. Reconcile conflicting docs/code/live evidence with dates and explicit unresolved decisions. Absence from sampled traces does not prove no dependency.

## Output

Choose the output for the requested scope. A bounded feature can use the compact trace and affected evidence gaps above. A system-wide baseline needs a service/component catalog, dependency edges, topology, representative journeys and ownership/evidence gaps; choose diagrams and tables that make those relationships understandable. A recurring review can return the affected changes and remaining gaps without recreating the baseline.

- Keep volatile live replicas/tags/tuning in timestamped observations rather than static architectural truth.
- Omit secrets and personal data from generated docs.

Validate references and diagram participant names against the evidence; mark inferred/proposed edges with explicit labels. Hand journey definitions to reliability expertise, incident scope to incident investigation expertise, and procedure gaps to operating-procedure expertise when appropriate; the model remains useful without those installed.

For an explicitly requested interactive HTML walkthrough, hand the evidence to interactive system explanation expertise when available. Static maps and inventories do not require its JSON contract or renderer.
