---
name: documentation-conventions
description: Decide what project knowledge to document and where its canonical
  home belongs; maintain affected PRDs, architecture, schemas, decisions and runbooks.
  Use before adding durable documentation and during planning, implementation,
  migrations, deployment changes or documentation reviews.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [composition guidance](../../COMPOSITION.md) for skill selection and invocation boundaries.


# Keep documentation useful

**Separate change records from implemented knowledge.** A standardized ECR and proposed C4/sequence/RFC diagrams belong in the authorized **engineering workspace** (filesystem folder outside the application repo or a connected document provider). The application's canonical documentation owns verified/current architecture, contracts, ADR history, runbooks and release/operations facts. A target design accepted by a team is not automatically implemented or deployed. Read the existing project documentation index, resolve current versus proposed state, and update affected canonical pages only as evidence justifies. The ECR's owner/format is defined by the engineering workflow, not this knowledge-placement skill.

For architecture baselines or substantive architecture/interface changes, read [architecture-documentation](../architecture-documentation/SKILL.md) for views, runtime/lifecycle boundaries, API analysis and source-backed verification.

When writing or revising prose, read and apply [documentation-writing](../documentation-writing/SKILL.md) for reader purpose, explanations, examples, precision and presentation. This skill owns document responsibilities and maintenance; the writing skill guides authoring and reader review.

## Find the canonical home before creating a document

When a task would add a durable project document or substantially split or relocate existing material, inspect the applicable repository instructions, README, documentation index/navigation, related pages and their links. Check the relevant source code/contracts and accepted decisions where factual authority matters. Search by the reader's question and project terminology, not just a proposed filename. Keep discovery proportional: a focused edit needs nearby sources, while cross-cutting knowledge may require tracing several owners.

Determine what the reader needs to know, whether the information is implemented behaviour, an accepted decision, a proposal or temporary work, and which existing document is authoritative for that responsibility. Then choose the least duplicative destination:

| Evidence | Action |
| --- | --- |
| An existing authoritative page answers the same reader question | Update that page or an appropriate section; link to it from other contexts rather than restating its contract. |
| The subject has a distinct durable purpose, audience or lifecycle that the existing pages cannot serve clearly | Create a focused document in the established structure, with an index/parent entry and links from related authoritative pages. |
| The information is provisional, task-specific or short-lived | Keep it in the existing proposal, plan, work record or PR until durable documentation is justified. |
| The authoritative detail is generated from code or configuration | Update its owning source or generator when authorized, and link the generated result rather than maintaining another copy. |

Placement follows information ownership and how readers navigate the project, not the file an agent happened to edit. A consequential architectural decision can warrant an ADR even when current architecture and operations pages also need updates; an ordinary reversible implementation choice usually does not. If an explicit user-requested file or location conflicts with an established owner, surface the conflict and preserve the requested scope rather than silently reorganizing the repository.

Before adding a file, be able to explain its independent reader question, why an existing document cannot answer it adequately, its canonical location and how readers will find it. This is an authoring decision, not a mandatory approval ceremony or separate report. For example, implementing saved-search sharing may require edits to existing product acceptance, authorization and data-contract pages, not a new document for each changed component.

For a new project without an established documentation layout, start with a short `docs/` index and add these areas only as needed:

| Area | Useful content |
| --- | --- |
| `product/` | PRD: problem, users, outcomes, scope, acceptance criteria and success measures; roadmap |
| `architecture/` | Overview, C4 context/containers, data model, schemas and contracts |
| `decisions/` | Short ADRs and a decision log linking consequential choices |
| `plans/` | Identified work packages, progress, risks and open questions |
| `ux/` | Shared design principles, tokens and interaction patterns |
| `operations/` | Setup, deployment, runbooks, recovery and critical-journey observability/SLIs/SLOs |
| `verification/` | Important user journeys, testing approach and known limitations |

## Choose what to record

Preserve existing documentation conventions. Start with documents that answer real questions, not an empty folder checklist. Use C4 context/containers for system boundaries; add component detail only when useful. Use arc42 as an optional architecture outline and MADR for lightweight ADRs.

- Keep a PRD focused on problem, users, outcomes, scope and acceptance criteria; keep the roadmap about priorities rather than duplicating implementation tasks.
- Record an ADR for a consequential choice with alternatives and tradeoffs.
- Keep routine reversible choices in the current plan or change description.
- Link the decision log to ADRs; supersede historical decisions rather than rewriting history.

## Keep responsibilities separate

Put product objectives and metric definitions in the PRD by default. Extract analytics engineering when event schemas, collection, privacy or data-quality rules need their own contract; keep targets in one place and do not install tracking merely to complete documentation.

Give each record a purpose a reader can recognize. Requirements explain the outcome and constraints; a design explains how the system will meet them; the current architecture explains implemented behaviour. Keep those statuses explicit so a proposal is not mistaken for a supported capability.

Put bounded target designs in the relevant work description. Use a separate target architecture when a material cross-system change needs a durable view, and retire or reconcile it when fulfilled. Link requirements, decisions, work and verification so the reader can follow a choice into its implementation and evidence without maintaining competing baselines.

### Work tracking

If progress tracking is useful, keep one view in the existing tracker or project notes; no new tracker or ledger is required.

- Where several packages need identification, preserve or agree stable IDs and a small kind vocabulary (feature, fix, refactor, docs, operations, research).
- Numbers identify work; priorities/dependencies determine order.
- Distinguish implementation, verification and deployment evidence.
- Reviews preserve findings; actionable follow-up belongs in linked work or an explicit disposition, with closure evidence.

A proposed package does not authorize implementation.

### Operating knowledge

Keep operations documentation broader than runbooks.

- For critical journeys, maintain useful outcome and latency/freshness indicators, denominators, time windows, target status, collection gaps, alert/runbook links and owners.
- Update them when journeys, dependencies or failure/retry boundaries change.
- Product outcomes and service reliability have different purposes.
- Do not equate an HTTP success, generated draft or model call with a completed user operation, or call an unapproved target a production promise.
- Keep telemetry minimal and exclude sensitive payloads.

## Synchronize the affected knowledge

Give the application's AGENTS.md a concise, applicable rule to inspect existing documentation and its canonical owners before adding files, then update affected documentation alongside application changes and accepted decisions. Keep the detailed method here or in the project's own documentation policy. Trace the change to the authoritative document:

| Change | Check and update |
| --- | --- |
| User-visible behavior or scope | PRD acceptance criteria, affected UX/journey description |
| System boundary or dependency | Architecture view, contracts, consequential ADR |
| Persistence or ownership | Data model, generated schema/API contract, migration/recovery notes |
| Configuration or deployment | Setup commands, environment variable names, runbook |
| Verification boundary | Journey coverage and known gaps |
| Critical journey, dependency or retry behaviour | Operations indicators/targets, telemetry gaps and alert/runbook assumptions |

For example, adding private saved searches changes ownership rules, the data model/API contract and user acceptance criteria. Update those facts in their existing homes; do not create a separate document for every changed file. A styling-only fix need not rewrite the PRD when behavior is unchanged.

Generate schemas from code when practical and link them rather than maintaining conflicting copies. Keep credentials and private data out of examples. Distinguish implemented behavior, approved plans, assumptions and superseded decisions; do not mark a roadmap item delivered before verification.

When a change affects repository instructions, use available scoped instruction-authoring and maintenance expertise. Keep durable working-command pointers and non-obvious project rules there; keep detailed procedures in their canonical documents. Check session learnings for evidence, lasting relevance and the appropriate scope before recording them, and correct or remove stale guidance rather than continually appending exceptions.

## Check completion

Read affected docs against the actual change. Check commands, paths, links, boundary diagrams and acceptance criteria for drift. For new or moved pages, verify index/parent discovery, related inbound links, and the absence of competing current baselines; repair stale navigation within scope. Summarize which knowledge changed, why, and any unresolved discrepancy. If no document is affected, say so briefly; avoid manufacturing documentation work. Prefer explanations of intent and tradeoffs over inventories of code files.

Use installed `humanizer` to edit human-readable prose when useful. Preserve the author's voice and technical meaning, including factual caveats; leave code, commands, paths, metadata and link targets intact.

When affected, keep journey/SLI contracts, signal schemas, runbooks, restore procedures and incident learning aligned with implementation. Use the operations skills for their substantive decisions; this skill keeps links, owners and evidence current without duplicating their records.
