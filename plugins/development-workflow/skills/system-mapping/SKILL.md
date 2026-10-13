---
name: system-mapping
description: "Discover and document an application's services, dependencies, deployment topology and user/request/data journeys from repository, documentation and runtime evidence for setup, feature analysis or recurring architecture updates."
metadata:
  scope: generic
  invocation: both
  version: "1.0"
---

# System mapping

Produce a small navigable evidence model that other work can use. Record uncertainty instead of making architecture look more complete than the sources permit.

## Scope and modes

Discover the requested product/feature, repositories, documents and target output. Begin with the narrow relevant paths; expand when a dependency requires it. Accept any architecture: monolith, browser, VM, container, serverless, batch or managed service.

- **Interactive:** resolve ambiguous scope and critical user tasks after inspecting available evidence.
- **Setup/feature:** map the existing/proposed boundaries and trace the affected journey, including migrations and new dependencies. Separate proposed design from observed implementation.
- **Recurring review:** compare a supplied base revision and current sources, refresh impacted nodes/flows, retain stable IDs/provenance, and report contradictions or missing owners without inventing answers.

Consult [references/mapping-guide.md](references/mapping-guide.md) for deeper implementation details when needed.

## Discovery

1. Inventory source entry points, routes, commands, consumers, jobs and visible UI capabilities. Use contracts and handlers, not repository naming alone.
2. Inspect clients, configuration references, queue/topic bindings, datastore access and dependency contracts. Classify runtime edges separately from build/package dependencies.
3. Derive hosting/target topology from actual infrastructure and delivery definitions. Resolve rendered overrides where relevant; use live state as a cross-check, not an assumption that desired state is deployed.
4. Identify ownership, operational docs and signal identities. Record evidence source/revision/time for each node and edge.
5. Model representative critical journeys from user intent to outcome. Include client-only work, external systems, caches, failures, retries, async completion and optional/degraded paths.
6. Draw Mermaid context/container and sequence/dataflow views at the depth needed. Do not force components into microservices or create unsupported acronym expansions.
7. Reconcile conflicting docs/code/live evidence with dates and explicit unresolved decisions. Absence from sampled traces does not prove no dependency.

## Output

Deliver a service/component catalog, dependency edge table, topology map, user-journey sequences, ownership/evidence gaps and navigation. Keep volatile live replicas/tags/tuning in timestamped observations rather than static architectural truth. Omit secrets and personal data from generated docs.

Validate references and diagram participant names against the evidence; mark inferred/proposed edges with explicit labels. Hand journey definitions to `reliability-design`, incident scope to `incident-response`, and procedure gaps to `runbook-engineering` when appropriate; the model remains useful without those installed.

For an explicitly requested interactive HTML walkthrough, hand the evidence to `system-flow-explorer` in `visual-communication` when available. Static maps and inventories do not require its JSON contract or renderer.
