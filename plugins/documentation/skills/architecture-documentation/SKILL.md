---
name: architecture-documentation
description: Explain and maintain a software system's architecture through structural
  views, runtime and lifecycle scenarios, interface analysis, deployment boundaries
  and evidence. Use for architecture documentation, system breakdowns and technical
  architecture reviews; preserve current versus target design and existing project scope.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

Read [composition guidance](../../COMPOSITION.md) and apply [documentation-writing](../documentation-writing/SKILL.md) for authoring quality.

# Explain architecture through useful views

Make the system's structure, behaviour and consequences understandable from evidence. Topic mentions, technology lists and diagrams alone are insufficient. Work within the requested documentation/design scope; findings do not authorize refactoring or deploying a system.

## Establish the baseline and questions

Read the product/quality requirements, accepted decisions, existing documentation and relevant code/configuration. Identify whether the view describes implemented code, a configured topology, an accepted design or a proposal. Mark uncertainty instead of inferring deployment or control effectiveness from configuration.

For a whole-system review, use arc42 as a coverage check: drivers/constraints, context, strategy, building blocks, runtime, deployment, cross-cutting concepts, decisions, quality scenarios, risks/debt and vocabulary. Link existing authorities rather than copying requirements, schemas and runbooks or imposing twelve new files. For a bounded change, maintain the affected views only.

## Model structure and responsibilities

Use C4 context and containers for the baseline, then selected component views where detail resolves ambiguity or risk. A container is an application/data store, not necessarily a Docker container. A component view zooms into one container; a code diagram is rarely needed for routine architectural explanation.

For each meaningful building block, explain responsibility, interface, dependencies, state/ownership and code location. Describe the actual decomposition, including mixed legacy handlers, coupling and incomplete abstractions. Do not present a desired service layer as implemented or turn in-process libraries into imaginary services.

Each diagram declares type/scope/status and uses understandable element types, responsibilities, technologies and directed relationships. Label communication protocols and optional boundaries; add a legend where notation needs one. Explain what readers should infer and what the view does not establish. Keep a text equivalent for important relationships.

## Explain runtime, lifecycle and data boundaries

Choose representative architectural scenarios: important user work, critical external interfaces, startup/release and failure/recovery. Use sequences for interaction/ordering, state diagrams for lifecycle and data-flow views for information movement. Do not create a diagram per endpoint.

Trace actor/context through authorization, validation, transaction, persistence, events and user-visible outcome. Include stale version, revoked authority, retry, partial batch and post-commit acknowledgement failure when relevant. Distinguish draft, intent and actual record; distinguish successful transport/model output from committed business state. Map participants to the structural views and source code.

Explain who owns local drafts, session/cache state, persistent records and generated projections; document lifetime, freshness, reconciliation and scaling consequences. Use the canonical physical schema for database facts; a conceptual domain diagram is complementary, not a replacement.

## Analyse interfaces, not just list endpoints

For important interface families, cover resource identity, operations/lifecycle, actor/tenant scope, request/response schemas, validation, side effects, errors, concurrency, idempotency, pagination, time/units, events and compatibility. Use specific contracts/examples for critical workflows and link generated reference for exhaustive syntax.

Inspect the generated OpenAPI or equivalent contract against code: declared responses/media types/errors may omit runtime behaviour. Streaming requires event ordering, correlation, completion/error and replay/cancellation semantics beyond an HTTP success code. Tool interfaces require capability/authority analysis; an automatically generated database/API tool is not automatically safe to expose.

Separate existing conventions from recommended changes. HTTP/OpenAPI and relevant standards inform assessment without forcing global renames, generic CRUD, a new error format or an unapproved architecture. Identify consumers and migration implications before proposing compatibility changes.

## Connect deployment, qualities and decisions

Show deployment separately from software containers. Declare environment, nodes/processes, storage, networks/trust boundaries, release/migration jobs and optional support systems. Distinguish shipped configuration, locally exercised setup and provisioned/verified hosted topology.

Connect requirements to design mechanisms and verification. Explain tradeoffs and operational consequences: security/privacy, availability, recovery, observability, performance/cost, process-local state and scaling. Link ADRs and service definitions; unknown rationale or unapproved SLOs remain open facts.

## Validate and maintain

Check source mappings, exact interfaces/examples, cross-view names and current/target consistency. Parse/render diagrams with the project's available tooling; inspect readability as well as syntax. Generated schemas and link checks cannot prove architectural truth, full authorization or provider behaviour.

Test reader questions: can a contributor trace a critical operation, identify authority/state/commit boundaries, explain a failure/retry and locate its evidence? Use proportionate checks; independent evaluation only when authorized. Route actionable gaps into existing identified work or record an explicit disposition, without creating a competing hidden backlog.

Update affected structural, runtime, lifecycle, interface and deployment views when their boundaries change. Preserve the existing diagram format and document ownership. Optional visual-rendering skills can help presentation when requested/available; this coverage guidance does not require an HTML diagram app, a modelling platform or a fixed folder tree.

## Standards

[C4 diagrams](https://c4model.com/diagrams) and [notation](https://c4model.com/diagrams/notation) inform structural views; [arc42](https://docs.arc42.org/home/) informs coverage; [OpenAPI](https://spec.openapis.org/oas/latest.html) informs HTTP reference. Apply their concepts proportionately to the project rather than claim complete conformance from a checklist.
