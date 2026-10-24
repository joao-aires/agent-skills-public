---
name: database-design
description: Design or evolve stored data, constraints, transactions and migration
  behavior independently of a database engine. Use for persistence choices, schema
  changes, consistency boundaries and data lifecycle decisions.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# Design data around invariants and use

Start with the accepted domain, workloads and data lifecycle. Identify authoritative records, derived representations, ownership, access paths and the consequences of stale, missing or conflicting data. Preserve the selected storage model unless evidence and scope justify changing it. A small schema change need not reopen the entire architecture.

## Choose representations and consistency boundaries

### Invariants

Describe the facts that must still be true after any accepted operation, including concurrent operations. Identify how records are recognized, which values must be unique, which relationships are valid, and who owns the data. Distinguish an application convenience from a rule whose violation would make stored state invalid.

Put enforceable invariants in the durable store when it can express them. Keep application coordination for rules that span operations or external systems, and explain how a partial failure is detected and recovered. This makes the schema and transaction decisions follow from the domain rather than from a list of preferred data types.

- Determine which guarantees belong in durable constraints and which need coordinated application behavior.
- Consider deletion, history and correction semantics before choosing keys and references.
- Document units, precision, null/absent meanings and time semantics where ambiguity changes behavior.

### Storage and derived representations

Use expected reads, writes, distribution, growth and failure tolerance to compare relational, document, key/value, object, search or analytical storage.

- Extra representations carry synchronization and recovery costs.
- Treat replicas, caches and indexes as derived until their authority and consistency contract are explicit.
- Workload or availability requirements must justify denormalization, partitioning or a new engine.

### Atomic operations

Identify which changes must become visible together for the business result to be valid. Follow two operations that can overlap and ask what happens when each reads the old state before either writes. Choose constraints, conditional writes, locks or transaction isolation that preserve the actual rule, and define whether a conflict is rejected, retried or merged.

Distinguish repeating an attempt from performing a new business operation. A retry after an uncertain response needs an identity or reconciliation rule that prevents an unintended second effect. Specify how stale writers are detected when overwriting newer state would violate the contract.

A transaction in one store does not make remote side effects atomic. Derive idempotency or reconciliation needs from actual failure boundaries, using suitable service-design expertise when available.

## Evolve without losing the contract

Assess readers, writers, queued work and supported application versions against a schema change.

- Separate structural changes, data conversion and final cleanup.
- Choose compatibility steps, bounded resumable backfills and validation from deployment constraints; an expand/migrate/contract approach is useful when versions overlap.
- Define completion, rejected/ambiguous data handling and recovery before irreversible conversion.

Code rollback may not undo stored data changes.

Include access, retention, export and deletion across derived stores, providers and restored backups. Define recovery objectives and seek operating expertise for actual restoration evidence. Distinguish missing guidance from missing database access; neither authorizes connecting to an unspecified target.

## Establish useful evidence

Verify invariants under relevant races and failures, migration from representative existing data, old/new consumer compatibility, access isolation and persisted behavior. Select matching engine/driver expertise from available descriptions; otherwise use project evidence and version-matched first-party documentation. Return the accepted/proposed data decisions, change strategy and actual verification limits at the requested stopping point.
