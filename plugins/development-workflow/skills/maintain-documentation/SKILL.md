---
name: maintain-documentation
description: Organize application knowledge and update affected PRDs, architecture, schemas, plans, decisions and runbooks when implementation or accepted decisions change. Use during planning, feature changes, migrations, deployment changes or documentation reviews.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Keep documentation useful

Use `documentation/` with a short index and these areas as needed:

| Area | Useful content |
| --- | --- |
| `product/` | PRD: problem, users, outcomes, scope, acceptance criteria; roadmap |
| `architecture/` | Overview, C4 context/containers, data model, schemas and contracts |
| `decisions/` | Short ADRs and a decision log linking consequential choices |
| `plans/` | Current implementation plans, risks and open questions |
| `ux/` | Shared design principles, tokens and interaction patterns |
| `operations/` | Setup, deployment, configuration, runbook and recovery |
| `verification/` | Important user journeys, testing approach and known limitations |

## Choose what to record

Preserve existing documentation conventions. Start with documents that answer real questions, not an empty folder checklist. Use C4 context/containers for system boundaries; add component detail only when useful. Use arc42 as an optional architecture outline and MADR for lightweight ADRs.

Keep a PRD focused on problem, users, outcomes, scope and acceptance criteria; keep the roadmap about priorities rather than duplicating implementation tasks. Record an ADR for a consequential choice with alternatives and tradeoffs. Keep routine reversible choices in the current plan or change description. Link the decision log to ADRs; supersede historical decisions rather than rewriting history.

## Synchronize the affected knowledge

Put this requirement in the application's AGENTS.md: update affected documentation alongside application changes and accepted decisions. Trace the change to the authoritative document:

| Change | Check and update |
| --- | --- |
| User-visible behavior or scope | PRD acceptance criteria, affected UX/journey description |
| System boundary or dependency | Architecture view, contracts, consequential ADR |
| Persistence or ownership | Data model, generated schema/API contract, migration/recovery notes |
| Configuration or deployment | Setup commands, environment variable names, runbook |
| Verification boundary | Journey coverage and known gaps |

For example, adding private saved searches changes ownership rules, the data model/API contract and user acceptance criteria. Update those facts in their existing homes; do not create a separate document for every changed file. A styling-only fix need not rewrite the PRD when behavior is unchanged.

Generate schemas from code when practical and link them rather than maintaining conflicting copies. Keep credentials and private data out of examples. Distinguish implemented behavior, approved plans, assumptions and superseded decisions; do not mark a roadmap item delivered before verification.

## Check completion

Read affected docs against the actual change. Check commands, paths, links, boundary diagrams and acceptance criteria for drift. Summarize which knowledge changed, why, and any unresolved discrepancy. If no document is affected, say so briefly; avoid manufacturing documentation work. Prefer explanations of intent and tradeoffs over inventories of code files.
