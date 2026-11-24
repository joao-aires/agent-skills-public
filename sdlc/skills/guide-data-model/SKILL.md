---
name: guide-data-model
description: Guide to documenting a logical data model. Covers entities and relationships, ownership, identity and keys, lifecycle, invariants, consistency, retention, access and tenancy, compatibility, evidence and open decisions.
user-invocable: true
metadata:
  kind: guide
  domain: database
  phase: design
  scope: generic
  invocation: both
---

# Data model guide

A **data model** explains the durable facts a system keeps, how they relate, who owns them and which rules must remain true. It is logical system knowledge: entities, relationships, identity, lifecycle, invariants, consistency, retention and evolution. It is not a table inventory, an entity-relationship picture on its own, or a copy of the physical schema.

The `database-design` method owns logical and physical data design: entities, keys, invariants, migration mechanics and engine behavior. This guide owns the artifact — reader questions, required sections, evidence and review. The data model states what must be true and why; the schema implements it; link the migration or schema at a named revision rather than duplicating it.

## Reader questions

A reader who was not in the design conversation must be able to answer:

1. Which system or domain does the model cover, and what is out of scope?
2. What are the entities and what does each represent in the business or system?
3. How do entities relate, and what cardinality and optionality apply?
4. Who owns each record or aggregate, and what can another owner read or change?
5. How is each entity identified, and what makes a duplicate?
6. How does a record move through its lifecycle, including correction and deletion?
7. Which invariants must remain true, and where are they enforced?
8. Which changes must be consistent together, and what happens under concurrency or partial failure?
9. How long is data kept, who may access it, and how is it exported or deleted?
10. How does the model change without breaking existing readers and writers?
11. What is current versus proposed, and which decisions remain open?

## Minimum content

- scope, status, revision and the systems or stores covered;
- entities with their meaning, granularity and authoritative owner;
- relationships with cardinality, optionality and the rule each expresses;
- identity and keys: natural or surrogate identity, uniqueness, duplicate handling and references;
- ownership and tenancy: record owner, tenant boundary, sharing and cross-tenant rules;
- lifecycle: creation, state transitions, correction, archival, deletion and restoration;
- invariants: the facts that must remain true, their enforcement point and failure behavior;
- consistency: which changes must become visible together, conflict handling and derived data;
- retention, access and deletion: periods, legal or contractual constraints, export and backups;
- compatibility and evolution: readers, writers, supported versions, deprecation window and rollback limits; link the migration plan for expand/migrate/contract steps;
- evidence: schema, migrations, constraints, tests, observed data or decisions at a revision;
- current versus proposed state and any open decisions with owners.

## Structure and quality

- Lead with scope and the questions the model answers. A model that tries to cover every store at once explains none.
- Define each entity in domain terms before naming columns. A table named `record` with no meaning is not a model.
- State granularity: what one row or record represents. Ambiguous granularity causes duplicate and aggregation errors later.
- Describe relationships as rules, not just lines. "An account has many users; a user belongs to exactly one account" is testable; an unlabeled crow's foot is not.
- Separate identity from attributes. Say how a record is recognized, what must be unique, and how a duplicate is detected or merged.
- Make ownership and tenancy explicit. Name the owner of each record, the boundary that isolates tenants, and what a shared or cross-tenant read means.
- Treat replicas, caches, search indexes and analytics copies as derived until their authority and refresh contract are stated.
- Put invariants where they can be enforced. Distinguish a durable constraint from an application rule that spans operations or external systems, and explain how a partial failure is detected.
- Define consistency boundaries by business operation. Identify which changes must commit together and whether a conflict is rejected, retried or merged.
- State deletion and correction semantics before choosing keys and references. Soft delete, history, anonymization and hard delete are different promises.
- Record units, precision, time semantics and the meaning of absent or null values where they change behavior.
- Describe evolution as readers and writers see it. A schema change that compiles is not necessarily compatible; a code rollback does not undo stored data.
- Include a short text explanation of the important relationships so the model is usable without a rendered diagram.
- Distinguish current, proposed and retired parts. Do not present a proposed model as implemented.

## Common failures

- a table or column inventory with no entity meaning or ownership;
- an entity-relationship diagram with no text equivalent or relationship rules;
- physical types, indexes and engine mechanics presented as the logical model;
- every entity owned by "the database" or "the backend";
- no tenant boundary, or a tenancy rule that exists only in application code;
- ambiguous identity, so duplicates are discovered after the fact;
- no lifecycle, so deletion, correction and archival are undefined;
- invariants listed but not tied to an enforcement point;
- consistency assumed because two writes happen near each other;
- derived stores treated as authoritative;
- retention and deletion omitted, or backup copies forgotten;
- compatibility argued from schema shape while meaning, defaults or nullability changed;
- a proposed model labeled current, or a migration claimed as complete without evidence;
- no revision, owner or open decisions.

## Review

Read the model as an implementer, a data owner and an operator:

- Can you explain each entity and relationship without opening the schema?
- Is ownership, tenancy and access explicit for every consequential record?
- Are identity, uniqueness and duplicate handling unambiguous?
- Does every invariant name where it is enforced and what happens when it is violated?
- Are consistency boundaries tied to real business operations, including concurrency and partial failure?
- Are lifecycle, retention, export and deletion complete, including derived stores and backups?
- Is the compatibility story about readers and writers, not just columns?
- Is current versus proposed state clear, and are the evidence and open decisions linked?

## Handoff

The design, implementation and operations readers need the entity meanings, relationships, ownership and tenancy, identity, lifecycle, invariants, consistency boundaries, retention, compatibility approach and open decisions. Implementation guidance owns the physical schema and migration mechanics; link the schema and migrations at a named revision instead of copying them. Operations needs the retention, access, deletion and restoration behavior that affects running the system.

When implementation changes the durable facts, update the model with the change and its evidence. When a proposed model is accepted but not implemented, keep it visibly proposed and reconcile it after the migration lands.
