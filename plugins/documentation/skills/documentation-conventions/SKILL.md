---
name: documentation-conventions
description: Organize application knowledge and update affected PRDs, architecture,
  schemas, plans, decisions and runbooks when implementation or accepted decisions
  change. Use during planning, feature changes, migrations, deployment changes or
  documentation reviews.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [composition guidance](../../COMPOSITION.md) for skill selection and invocation boundaries.


# Keep documentation useful

For architecture baselines or substantive architecture/interface changes, read [architecture-documentation](../architecture-documentation/SKILL.md) for views, runtime/lifecycle boundaries, API analysis and source-backed verification.

When writing or revising prose, read and apply [documentation-writing](../documentation-writing/SKILL.md) for reader purpose, explanations, examples, precision and presentation. This skill owns document responsibilities and maintenance; the writing skill guides authoring and reader review.

Use `documentation/` with a short index and these areas as needed:

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

Keep a PRD focused on problem, users, outcomes, scope and acceptance criteria; keep the roadmap about priorities rather than duplicating implementation tasks. Record an ADR for a consequential choice with alternatives and tradeoffs. Keep routine reversible choices in the current plan or change description. Link the decision log to ADRs; supersede historical decisions rather than rewriting history.

## Keep responsibilities separate

Put product objectives and metric definitions in the PRD by default. Extract analytics engineering when event schemas, collection, privacy or data-quality rules need their own contract; keep targets in one place and do not install tracking merely to complete documentation.

Separate requirements and constraints from their design response. The current architecture describes implemented behaviour. Put bounded target designs in work packages; use a separate target architecture for material cross-system change and retire it when fulfilled. Link requirements, decisions, work and verification rather than maintain competing baselines.

If progress tracking is useful, keep one view in the existing tracker or project notes; no new tracker or ledger is required. Where several packages need identification, preserve or agree stable IDs and a small kind vocabulary (feature, fix, refactor, docs, operations, research). Numbers identify work; priorities/dependencies determine order. Distinguish implementation, verification and deployment evidence. Reviews preserve findings; actionable follow-up belongs in linked work or an explicit disposition, with closure evidence. A proposed package does not authorize implementation.

Keep operations documentation broader than runbooks. For critical journeys, maintain useful outcome and latency/freshness indicators, denominators, time windows, target status, collection gaps, alert/runbook links and owners. Update them when journeys, dependencies or failure/retry boundaries change. Product outcomes and service reliability have different purposes. Do not equate an HTTP success, generated draft or model call with a completed user operation, or call an unapproved target a production promise. Keep telemetry minimal and exclude sensitive payloads.

## Synchronize the affected knowledge

Put this requirement in the application's AGENTS.md: update affected documentation alongside application changes and accepted decisions. Trace the change to the authoritative document:

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

## Check completion

Read affected docs against the actual change. Check commands, paths, links, boundary diagrams and acceptance criteria for drift. Summarize which knowledge changed, why, and any unresolved discrepancy. If no document is affected, say so briefly; avoid manufacturing documentation work. Prefer explanations of intent and tradeoffs over inventories of code files.

Use installed `humanizer` to edit human-readable prose when useful. Preserve the author's voice and technical meaning, including factual caveats; leave code, commands, paths, metadata and link targets intact.

When affected, keep journey/SLI contracts, signal schemas, runbooks, restore procedures and incident learning aligned with implementation. Use the operations skills for their substantive decisions; this skill keeps links, owners and evidence current without duplicating their records.
