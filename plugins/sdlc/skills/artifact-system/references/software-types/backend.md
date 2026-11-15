# Backend

## What this is

Software that serves other software: APIs, services, workers, cron jobs, queue consumers and event handlers. It has no graphical user interface of its own; its behavior is judged through contracts, stored effects and failure handling.

## Design record must show

- the operations or jobs the service supports and their callers;
- the contract: request/response, events or commands, errors and versioning;
- which component owns the durable record and which checks permit the action;
- what must succeed together and what may complete later;
- concurrency, retry, idempotency and duplicate suppression;
- failure, timeout, cancellation and recovery behavior;
- data ownership, migration and compatibility;
- a sequence or contract artifact that lets a reviewer judge the direction.

## Typical artifacts

Use the guide for the view that answers the question:

- [C4 view](../../../c4-view-guide/SKILL.md) for boundaries and responsibilities;
- [sequence view](../../../sequence-view-guide/SKILL.md) for ordering, retry and failure;
- [state machine](../../../state-machine-guide/SKILL.md) for long-running or multi-step work;
- [compatibility matrix](../../../compatibility-matrix-guide/SKILL.md) for consumers, versions and platforms.

Typical artifacts also include an API or event contract sketch, OpenAPI/protobuf/schema, data ownership or entity relationship view, and deployment or topology view. Use the [architecture-set contract](../contracts/architecture-set.md) for durable proposed or current C4/sequence views.

## Seam decisions

When the backend serves a frontend, AI component or external consumer, decide once:

- error and denial semantics the consumer maps to behavior;
- empty, not-found, conflict and validation distinctions;
- pagination, ordering and freshness;
- authentication, authorization and tenant boundaries;
- idempotency, retry and duplicate-submit behavior;
- versioning and compatibility guarantees.

## Variants and constraints

| Variant | Constraint owner |
| --- | --- |
| REST API | `backend-development` — resources, contract, versioning |
| GraphQL, gRPC or event-driven service | `backend-development` plus the accepted protocol guidance |
| Worker, cron or queue consumer | `backend-development` — durable work, retries, completion |
| SaaS backend | `saas-development` + `backend-development` — tenancy, entitlements, billing |
| Python/FastAPI service | `backend-python-development` — conventions and persistence |
| PostgreSQL schema | `database-postgresql-development` — schema, transactions, performance |
| JVM/Kubernetes/AKS runtime | `operations-platforms` — resources, tuning, cost |

These are constraints, not separate software types.

## Verification that counts

- contract or integration test against the real consumer shape;
- concurrency and retry behavior exercised;
- duplicate suppression or idempotency observed;
- migration and rollback checked on populated data;
- failure and recovery behavior observed, not inferred;
- the deployed or intended target distinguished from a local run.

## Optional specialists

`backend-design`, `backend-python-development`, `database-*`, `security-and-privacy-design`, `security-auth-development`, `observability`, `data-recovery` and `operations-platforms` as applicable. If absent, retain the contract, ownership, failure and evidence reasoning.

## Not required

Wireframes, visual direction, UI accessibility or a rendered interface slice.

## Example

A saved-searches API:

```markdown
- Affected type: backend
- Operations: create, list, delete
- Ownership: saved search belongs to the authenticated user
- Contract: request/response, errors, pagination
- Failure: duplicate create, retry safety, partial failure
- Artifact: sequence for create/retry plus contract sketch
- Frontend: not affected — no UI in this change
```
