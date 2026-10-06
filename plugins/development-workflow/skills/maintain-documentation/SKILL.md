---
name: maintain-documentation
description: Organize application documentation and keep PRDs, architecture, data contracts, plans, decisions and operational guidance aligned with code.
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

Start with the documents that answer real questions. Use C4 for boundaries, arc42 as an optional architecture outline and MADR as a lightweight ADR format; do not create empty sections to satisfy a checklist.

Put a clear instruction in AGENTS.md: update affected documentation with application changes and decisions. Behavior changes affect the PRD; boundary changes affect architecture; persistence changes affect the data model; operational changes affect the runbook. Generate schemas from code when practical. Record meaningful decisions, and supersede historical ADRs rather than rewriting them.

Keep one authoritative place for each fact. Distinguish implemented behavior, plans and assumptions. Prefer concise explanations of intent and tradeoffs over inventories of files. Review whether the docs still describe the application accurately.
