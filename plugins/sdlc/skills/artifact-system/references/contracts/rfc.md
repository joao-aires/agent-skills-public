# RFC contract: a proposal with its own audience

An RFC is a **substantive design proposal that needs its own review or decision process**. A bounded feature keeps its design in the ECR solution-design section. Use an RFC when the proposal spans changes, needs reviewers outside the change, or must be decided before an ECR can proceed.

Apply the [artifact quality bar](../quality-bar.md). The RFC is complete when a reviewer can understand the current state, the proposal, the alternatives, the consequences and the decision requested.

## Contract

```markdown
# Proposal title

## Status
Draft | proposed | accepted | rejected; owner and date.

## Problem and constraints
The situation, affected users or systems, and the constraints that shape the design.

## Current state
The existing behavior and architecture at a linked revision.

## Proposal
The target behavior, boundaries, contracts and affected surfaces.

## Alternatives
Credible options and their trade-offs on the same dimensions.

## Impact
Compatibility, migration, security/privacy, reliability, performance, cost,
operations and failure behavior.

## Open questions
What still needs a decision, who owns it, and what evidence would settle it.

## Links
Requirements, baseline, target diagrams, ADRs, ECR and related changes.
```

Guidance:

- **Status and ownership.** State whether the proposal is a draft, under review, accepted or rejected. Name the decision owner. An accepted RFC is still proposed relative to implementation until the code lands.
- **Current state.** Link the baseline revision and the relevant architecture or contract. Do not describe a proposed system as current.
- **Proposal.** Describe the target behavior and boundaries, including the denied, failure, retry and migration paths that matter to the decision.
- **Alternatives.** Compare credible options on the same dimensions. Explain why the proposal fits the constraints.
- **Impact.** Cover compatibility, migration, security/privacy, reliability, performance, cost, operations and recovery as applicable. Do not force irrelevant sections; say "not applicable" with the reason.
- **Open questions.** Name each decision, its owner and the evidence that would settle it. Do not hide an unresolved decision inside an implementation detail.
- **Links.** Link the baseline, target diagrams, ADRs, ECR and related changes using the [link rules](../quality-bar.md#4-resolvable-navigation).

## Relationship to other artifacts

- The **ECR** owns the change if one is being carried forward. A bounded feature's design belongs in its solution-design section.
- The **RFC** owns the proposal and its review when a separate audience or decision process is justified.
- **System design** expertise owns the design method: boundaries, contracts, failure and trade-offs. The RFC contract owns the document's reader completeness and status.
- An **ADR** owns a consequential accepted choice that must outlive the change. Link it from the RFC.
- **Current architecture documentation** owns the implemented state. The RFC's target views remain proposed until reconciliation.

## Maturity

An RFC moves from **draft** to **proposed** to **accepted** or **rejected**. It does not claim implemented or released. If implementation follows, the ECR owns the execution and verification evidence, and the current architecture documentation is updated only after the code lands.

## Reader test

A reviewer who was not in the conversation must be able to answer:

1. What problem does this proposal solve, and what constraints shape it?
2. What exists today, at which revision?
3. What exactly is proposed, including the denied and failure paths?
4. Which alternatives were considered, and why were they rejected?
5. What are the compatibility, migration, security, reliability and operating consequences?
6. What decision is requested, from whom, and what remains open?

## Example

> **Proposal: durable local webhook queue with renewable claims**
>
> **Status.** Proposed; owner feature author; 2026-11-13.
>
> **Problem and constraints.** The in-memory queue loses pending work on restart and cannot coordinate two same-host workers. The zero-option memory API must remain usable, and no external service is authorized.
>
> **Current state.** `createQueue()` stores jobs in a process-local array and removes a job before invoking the receiver at `queue@<full-sha>` ([commit](https://example.invalid/queue/commit)). The current dispatch sequence is linked below.
>
> **Proposal.** Add opt-in `createQueue({ databasePath, leaseMs })` backed by a local SQLite file. Persist event identity, canonical payload, completion and a renewable claim token/deadline. Use an atomic conditional update to claim one available or expired job. Mark a claimed job running before invoking the receiver; release only the current owner's claim on failure.
>
> **Alternatives.** Holding a write transaction across the receiver call would block producers. A process-local lock cannot coordinate independent workers. A separate queue service adds an unauthorized operational dependency.
>
> **Impact.** At-least-once delivery; receivers must deduplicate the stable event ID after an ambiguous crash. A local file is a single-host durability boundary, not a multi-host guarantee. No public HTTP contract changes. Migration is not applicable; the persistent store is new and the memory path remains the default.
>
> **Open questions.** Whether to expose failed-save feedback, and whether the receiver can deduplicate. Owners: product and integration owners.
>
> **Links.** [ECR](https://example.invalid/ecr), [current dispatch sequence](https://example.invalid/current), [target sequence](https://example.invalid/target), [ADR](https://example.invalid/adr).
