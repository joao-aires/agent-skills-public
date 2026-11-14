# Decision record contract: durable ADR and product decision record

A decision record owns **one consequential decision that must outlive the change**. An ADR records an architecture or engineering decision; a product decision record (PDR) applies the same contract to a product choice. The ECR or RFC may hold the exploration; the decision record preserves the accepted choice and its consequences.

Apply the [artifact quality bar](../quality-bar.md). The record is complete when a future reader can understand the decision, the alternatives, the consequences and when it should be revisited.

## Contract

```markdown
# Decision title

- **Status:** proposed | accepted | superseded | deprecated
- **Date:**
- **Owner:**
- **Supersedes / superseded by:**

## Context
The situation, constraints and forces that made a decision necessary.

## Options considered
The credible alternatives and the main trade-off of each.

## Decision
The chosen option, stated directly.

## Consequences
What becomes easier, what becomes harder, and what must change as a result.

## Links
Affected requirements, design, code, tests, diagrams and the ECR or RFC.
```

Guidance:

- **Title.** Name the decision, not the topic. "Use SQLite WAL for the local durable queue" is a decision; "Database choice" is not.
- **Status and ownership.** State one status and the decision owner. Record the date the decision was accepted, not the date the document was last edited.
- **Context.** Explain the forces and constraints. A reader should understand why the decision was needed without reading the whole ECR.
- **Options.** Include the credible alternatives and the main limit of each. Do not invent alternatives that were never considered; if the rationale is unknown, mark the gap.
- **Decision.** State the choice directly. Do not bury it in the context.
- **Consequences.** Include the positive and negative consequences, affected boundaries, migration or compatibility work, and what would trigger a revisit.
- **Links.** Link the affected requirements, design, code, tests, diagrams and the ECR or RFC. Use the [link rules](../quality-bar.md#4-resolvable-navigation).

## Immutability and supersession

An accepted decision record is **not rewritten** when the decision changes. Create a new record that supersedes it, and update the old record's status and `Superseded by` link. Correct typos and broken links in place; do not rewrite the rationale to match a later choice.

This preserves the decision history a future reader needs to understand why the system looks the way it does.

## When to create one

Create a decision record when an accepted choice is consequential, likely to be questioned later, and must outlive the change. Examples: a service or data boundary, a persistence or consistency mechanism, a public contract, a security or privacy trade-off, a provider commitment, or a product rule that constrains future work.

Do not create one for every implementation detail. A reversible local choice belongs in the ECR or code. During exploration, a proposed decision may remain in the ECR or RFC; promote it to a decision record only when it is accepted and durable.

## Relationship to other artifacts

- The **ECR or RFC** owns the exploration, alternatives and proposed design.
- The **decision record** owns the accepted choice and its consequences.
- **Current architecture documentation** owns the implemented current state; link the decision record rather than copying its rationale.
- A **product decision record** uses this contract with product-specific context and consequences.

## Example

> **Use SQLite WAL for the local durable queue**
>
> - **Status:** accepted · **Date:** 2026-11-13 · **Owner:** feature author · **Supersedes:** none
>
> **Context.** Producers need committed local acceptance and two independent same-host workers need one shared backlog. The change must preserve the zero-option in-memory API and cannot add an external service.
>
> **Options.** An in-process map cannot coordinate independent workers. Holding a write transaction across the receiver call would block all producers. A file-backed SQLite database with WAL and `synchronous=FULL` supports a committed local admission and a renewable claim without a separate service.
>
> **Decision.** Use an opt-in SQLite file, WAL mode and `synchronous=FULL`. Persist event identity, payload, completion and a renewable claim token/deadline. Use an atomic conditional update to claim work.
>
> **Consequences.** Producers can keep committing while deliveries wait. The database is a local durability boundary, not a multi-host guarantee. A receiver can still observe an ambiguous effect after a crash; receivers must deduplicate the stable event ID. Revisit if the deployment becomes multi-host or the receiver cannot deduplicate.
>
> **Links.** [ECR](https://example.invalid/ecr), [target sequence](https://example.invalid/diagram), baseline `queue@<full-sha>` ([commit](https://example.invalid/queue/commit)).
