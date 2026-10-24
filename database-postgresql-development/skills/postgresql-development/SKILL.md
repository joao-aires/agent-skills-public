---
name: postgresql-development
description: Develop or review PostgreSQL schemas, transactions, migrations and access
  policies. Use for SQL, data integrity, concurrency and engine-specific persistence
  behavior with the actual application roles and server version.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: PostgreSQL
  references: ../../references/sources.md
user-invocable: true
---

# Implement the PostgreSQL data contract

Identify the actual PostgreSQL version, hosting model, extensions, application roles, driver and migration tooling. Preserve accepted project choices. Establish the affected invariants and workload; if broader design is unresolved, use available data/service-design expertise or project evidence without requiring another plugin. Read [source selection](../../references/sources.md) for provenance and version-matched primary references.

## Represent facts and authority

Choose types, constraints and keys from meaning and access patterns:

- Use appropriate numeric/time semantics; distinguish null, empty and absent values.
- Enforce durable uniqueness and relationships where they express the contract.
- Consider JSONB, arrays, generated columns, partitioning and extensions with their update, validation, indexing and operational consequences.

Use parameterized values through the actual driver; dynamic identifiers need separate validation/quoting. Derive tenant/resource authority from verified context. Application authorization remains necessary for allowed operations.

### When using row-level security

Row-level security evaluates access under the database role and policy context of the statement. Establish how trusted application identity reaches that context and which code can change it. A custom session variable alone does not establish a trusted identity; an untrusted caller must not be able to choose the tenant that the policy trusts.

Check both which existing rows an operation can reach and which proposed row values it may create or retain. Exercise the policy through the application's actual role and connection-pool behavior, because a privileged migration or table-owner session may bypass the restriction being tested. Verify:

| Boundary | Check |
| --- | --- |
| Execution role | Ownership and BYPASSRLS/superuser behavior |
| Policy behavior | USING and WITH CHECK semantics, including relevant functions/views |
| Connection context | Who can set it and how pools scope/reset it |
| Evidence | Cross-tenant reads and writes through the actual application role |

## Handle concurrent operations deliberately

Start from the concurrent operations that could violate the rule. Prefer a database constraint or atomic statement when it expresses the rule directly. When an operation reads and then decides what to write, establish which concurrent changes the selected isolation and locking behavior permits before assuming the earlier read remains valid.

Treat a retryable transaction failure as a request to repeat the complete logical transaction with fresh reads. Keep attempts bounded and account separately for external effects, which the database cannot roll back. Choose transaction/isolation and locking behavior for the invariant.

- Keep transactions bounded and avoid waiting on remote work while holding locks.
- Use constraints and atomic statements where they settle races.
- For serializable/deadlock retries, repeat the complete logical transaction safely, with bounded attempts and durable side-effect handling.
- Give advisory locks a stable ownership/lifecycle convention; they do not replace constraints or authorization.

## Change schemas with operational evidence

Examine lock modes, table size, existing values, write traffic, replicas and concurrent application versions before migration.

- Where appropriate, separate compatible structure, bounded backfill, constraint validation and cleanup.
- Choose index creation for the deployment. Concurrent creation has transaction, failure and invalid-index consequences; it is not required for every index.
- Set bounded lock/statement behavior through the accepted tooling and plan retry/forward recovery.
- Verify before removing old representations.

## Verify the affected contract

- Exercise SQL and migrations on representative PostgreSQL data with actual roles, not an engine substitute.
- Inspect persisted state after failures, duplicate/conflicting requests and version transitions.
- Report proposed versus executed work. Keep live mutation inside the user's named target and authorization.
