# Data model contract: the durable facts and their rules

A **data model** explains the logical facts a system keeps, how they relate, who owns them and which rules must remain true. It covers entities, identity, lifecycle, invariants, consistency, retention, access and evolution. It is system knowledge, not a table inventory and not a copy of the physical schema.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the application repository at `docs/architecture/data-model.md` when the model is durable architecture knowledge. Use a database workspace or package-local documentation when the model belongs to a database or package rather than the whole application, and link it from the architecture set.

Read the [data model guide](../../../guide-data-model/SKILL.md) for writing conventions, examples and review checks.

## Reader questions

A reader who was not in the design conversation must be able to answer:

1. Which system or domain does the model cover, at what revision, and what is out of scope?
2. What are the entities, and what does each represent?
3. How do entities relate, with what cardinality, optionality and rule?
4. Who owns each record or aggregate, and where is the tenancy or access boundary?
5. How is each entity identified, and what makes a duplicate?
6. How does a record move through creation, correction, archival and deletion?
7. Which invariants must remain true, and where are they enforced?
8. Which changes must be consistent together, and what happens under concurrency or partial failure?
9. How long is data retained, who may access it, and how is it exported or deleted?
10. How does the model change without breaking existing readers, writers or stored data?
11. What is current, what is proposed, and which decisions remain open?

## Contract

```markdown
# <System or domain> data model

## Scope and status
Systems, stores and domains covered; current, proposed, mixed or retired;
revision; what is out of scope.

## Entities and relationships
Each entity's meaning and granularity; relationships with cardinality,
optionality and the rule each expresses. A text equivalent for any diagram.

## Identity and keys
How each entity is recognized, what must be unique, duplicate detection and
reference stability.

## Ownership and tenancy
Record and aggregate owners; tenant or access boundary; shared and cross-tenant
reads or writes; who may change what.

## Lifecycle
Creation, state transitions, correction, archival, deletion and restoration.

## Invariants
Facts that must remain true; enforcement point or coordinating behavior; what
happens when violated.

## Consistency
Changes that must become visible together; conflict handling; derived stores,
caches, replicas and their authority.

## Retention, access and deletion
Retention periods and reasons; access rules; export and deletion across primary,
derived and backup stores.

## Compatibility and evolution
Supported readers and writers; deprecation window; validation and rollback
limits; link the migration plan for expand, migrate and contract steps.

## Evidence and open decisions
Schema, migrations, constraints, tests, observed data and decisions at a named
revision; unresolved choices and owners.
```

Guidance:

- **Scope and status.** Name the system or domain, the stores covered and the revision. State what is excluded. Mark current, proposed, mixed or retired; a proposed target model is not implemented because it was accepted.
- **Entities and relationships.** Define what one record represents and why the entity exists. Express relationships as rules with cardinality and optionality. Include a short text explanation of the important relationships so a diagram is not the only authority.
- **Identity and keys.** Separate identity from attributes. Say how an entity is recognized, what must be unique and how duplicates are detected or merged. Identify references whose stability matters across changes.
- **Ownership and tenancy.** Name the owner of each consequential record or aggregate. State the tenant or access boundary, what a shared read means and who may write across it. Do not leave tenancy as an implied application rule.
- **Lifecycle.** Describe creation, meaningful state transitions, correction, archival, deletion and restoration. Distinguish soft delete, history, anonymization and hard delete; they are different promises.
- **Invariants.** List facts that must remain true after any accepted operation, including concurrent ones. Name the durable constraint or coordinating behavior that enforces each, and the detection and recovery path when it cannot be enforced in one store.
- **Consistency.** Tie consistency boundaries to business operations. State which changes must commit together, how conflicts are rejected, retried or merged, and which replicas, caches or indexes are derived rather than authoritative.
- **Retention, access and deletion.** Give periods and their reasons, access rules and the export and deletion path across primary, derived and backup stores. Note legal or contractual constraints without inventing approval.
- **Compatibility and evolution.** Describe the change as readers and writers experience it. Separate structural change, conversion and cleanup; state validation, completion and rejected or ambiguous data handling. A code rollback does not reverse a data change.
- **Evidence and open decisions.** Link the schema, migrations, constraints, tests or observed data at a named revision. List unresolved ownership, lifecycle or compatibility choices with their owners. Do not claim enforcement from an ERD alone.

Physical schema detail — column types, indexes, partitioning, engine constraints and DDL — belongs to database and technical implementation guidance. Link the schema or migration instead of duplicating it here.

## Current versus proposed

Keep the distinction explicit:

- **Current** means implemented and evidenced at a linked revision.
- **Proposed** means a target model in a design record or change record, not yet implemented.
- **Mixed** means part of the model is current and part is proposed; label the parts.
- **Retired** means no longer authoritative; link the replacement.

Do not update the canonical current model to match a proposal. Reconcile it after the migration and implementation evidence land.

## Handoff

The design, implementation and operations readers need entity meanings, relationships, ownership and tenancy, identity, lifecycle, invariants, consistency boundaries, retention, compatibility approach and open decisions. Link the physical schema and migrations rather than copying them. See [handoff](../handoff.md).

## Home and maintenance

| Change | Update |
| --- | --- |
| New or changed entity, relationship or granularity | Entities, relationships and identity |
| Ownership, tenancy or access rule | Ownership and tenancy; access section |
| Creation, correction, archival or deletion behavior | Lifecycle and retention |
| New or changed business invariant | Invariants and its enforcement evidence |
| Transaction boundary, conflict or derived store | Consistency |
| Retention, export or deletion obligation | Retention, access and deletion |
| Schema or compatibility change | Compatibility and evolution; link the migration |
| Accepted consequential data decision | Link the decision record and affected sections |
| Implementation or migration completed | Status, evidence and current versus proposed state |

Update the model when the durable facts or their rules change, not only when a column changes. A migration updates evidence; it does not by itself explain ownership or invariants.

## Review

Use the [cold-reader test](../quality-bar.md#3-reader-sufficiency). Can a contributor explain each entity, its owner and its lifecycle, name the invariants and their enforcement, and describe a compatible change without opening the schema? If not, the document is a table inventory.

Check the model against the schema, migrations and observed data at the named revision. A consistent diagram can still misstate ownership or enforcement; report model accuracy and diagram rendering as separate limitations.
