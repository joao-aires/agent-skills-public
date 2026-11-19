# Backend development plugin: service behavior and interface contracts before implementation

The `backend-development` plugin carries framework-independent backend reasoning: what a service promises, how it preserves state under concurrency and failure, which structural pattern fits, and what each published contract may change.

It does not select a framework, datastore, broker or hosting model, and it does not replace the project's architecture decision, data design or implementation conventions.

## Purpose

Use this package when a backend change needs a decision that survives implementation: a new operation, a changed durable effect, a different integration style or an unreviewed public schema. It composes with the design activity that owns architecture boundaries, the artifact system that owns the design record and the selected stack package that owns the code.

## Conceptual model

Six methods answer different questions. The order is a dependency order, not a required process.

| Question | Owner |
| --- | --- |
| What does the operation mean, who may perform it, what becomes durable, when is it complete? | [backend-design](skills/backend-design/SKILL.md) |
| Which structural pattern fits these forces, at what cost, and how would we migrate? | [architecture-patterns](skills/architecture-patterns/SKILL.md) |
| What does the HTTP surface promise request by request? | [rest-api-design](skills/rest-api-design/SKILL.md) |
| What does the GraphQL schema promise operation by operation? | [graphql-design](skills/graphql-design/SKILL.md) |
| What do published events mean, and how do consumers survive them? | [event-driven-design](skills/event-driven-design/SKILL.md) |
| What guarantee holds across process, network or region boundaries? | [distributed-systems](skills/distributed-systems/SKILL.md) |

Behavior is decided once in `backend-design`. Each interface method publishes that behavior in its own medium. `distributed-systems` constrains the guarantee; `architecture-patterns` changes structure without changing semantics.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [backend-design](skills/backend-design/SKILL.md) | method | Operation meaning, authority, operation-level invariants, durable effects, idempotency, completion and consumer-visible compatibility | A contract and its verification needs | Framework mechanics or architecture boundaries |
| [architecture-patterns](skills/architecture-patterns/SKILL.md) | method | Pattern candidates, fit check, cost comparison, migration path | A selected pattern with migration reasoning | Service behavior, event contracts, cross-service guarantees |
| [rest-api-design](skills/rest-api-design/SKILL.md) | method | Resources, methods, statuses, representations, errors, concurrency, versioning, caching, authorization boundary, OpenAPI | A reviewable HTTP contract | Service behavior or framework setup |
| [graphql-design](skills/graphql-design/SKILL.md) | method | Types, nullability, connections, errors, mutations, cost limits, federation boundaries, deprecation | A reviewable schema contract | Resolver code or service behavior |
| [event-driven-design](skills/event-driven-design/SKILL.md) | method | Event meaning, schema evolution, ordering and partitioning, delivery semantics, idempotency, replay and retention | A reviewable event contract and consumer obligations | Broker installation or cluster operations |
| [distributed-systems](skills/distributed-systems/SKILL.md) | method | Consistency per operation, replication, partitioning, consensus, time and failure detection, ambiguous outcomes, multi-region recovery, capacity reasoning | A decision and the evidence that would reopen it | Fault injection, telemetry or incident command |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Service behavior and failure boundaries | [backend-design](skills/backend-design/SKILL.md) |
| Pattern matrix and migration reasoning | [pattern selection](skills/architecture-patterns/references/pattern-selection.md), [migration paths](skills/architecture-patterns/references/migration-paths.md) |
| HTTP contract review and compatibility | [checklist](skills/rest-api-design/references/rest-contract-checklist.md), [versioning](skills/rest-api-design/references/versioning-and-compatibility.md) |
| GraphQL schema review and cost policy | [schema review](skills/graphql-design/references/schema-review.md), [security and cost](skills/graphql-design/references/security-and-cost.md) |
| Event contract and broker-specific examples | [event checklist](skills/event-driven-design/references/event-contract-checklist.md), [Kafka patterns](skills/event-driven-design/references/kafka-patterns.md) |
| Cross-boundary failure and consistency | [failure and consistency](skills/distributed-systems/references/failure-and-consistency.md), [resilience checklist](skills/distributed-systems/references/resilience-checklist.md) |
| Provenance and fit | `Sources and fit` in each skill |

## Reading paths

1. **New endpoint or operation** → [backend-design](skills/backend-design/SKILL.md) → [rest-api-design](skills/rest-api-design/SKILL.md) or [graphql-design](skills/graphql-design/SKILL.md) → the project's existing design record → stack conventions for implementation.
2. **New asynchronous flow** → [backend-design](skills/backend-design/SKILL.md) → [event-driven-design](skills/event-driven-design/SKILL.md) → [distributed-systems](skills/distributed-systems/SKILL.md) when a cross-service guarantee is being claimed.
3. **Change an existing published contract** → consumer and version inventory in [backend-design](skills/backend-design/SKILL.md) → the matching interface method's evolution section → compatibility evidence.
4. **Structural refactor** → [architecture-patterns](skills/architecture-patterns/SKILL.md) → the architecture design activity for boundaries and options → the selected migration path.

## Boundaries

- **Architecture.** Service, data, client and deployment boundaries, option sets and the accepted decision belong to the architecture design activity. This package supplies backend forces and costs.
- **Data.** The stored representation, enforceable constraints, consistency boundaries and schema evolution belong to `database-development`; engine mechanics belong to the PostgreSQL package when selected. `backend-design` owns operation-level invariants and durable effects; a conflict reopens the data contract.
- **Delivery.** Pipeline shape, release authorization and served-outcome verification belong to delivery and tooling capabilities, not to these methods.
- **Record.** The design proposal, C4, sequence, state and compatibility artifacts belong to the artifact system and the project's artifact homes.
- **Scope.** Design-only work stops at a contract and verification needs. These skills do not grant authority to implement, migrate, publish a schema or deploy.

## Authority and optional tools

The package declares no MCP servers, runtime dependencies or external services. Reading a repository or running checks requires scope from the request and the relevant access. Installing the package does not select HTTP, GraphQL or event-driven integration, and it does not authorize a schema publication or a traffic change.

## Maintenance

Owning sources are `skills/*/SKILL.md` and their `references/`. Update this README when a method's decision ownership, the responsibility split or the package boundary changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests. Recheck dated sources before changing normative protocol claims.
