---
name: engineering-artifacts
description: Maintain structured engineering change records, phase outcomes and audience-appropriate issue/PR views without duplicating canonical application knowledge. Apply for every engineering SDLC activity, including end-to-end develop and small fixes.
user-invocable: false
metadata:
  scope: generic
  invocation: agent
  role: support
---

# Engineering artifacts: one change, reviewable outcomes

Apply this method to **every performed engineering activity**, whether it starts at `refine`, `design`, `plan`, `implement`, `test`, `review`, `release` or a single `develop` engagement. The entry-point task owns engineering execution; this method owns artifact shape, semantic completeness, continuity and audience-specific presentation. Read [engineering-workspace](../engineering-workspace/SKILL.md) for locating and persisting records. Neither method invokes explicit-only task skills nor grants repository, tracker, publication or deployment authority.

## The authoritative layers

1. **Application baseline** lives in the application repository's established documentation: implemented system C4 views, critical runtime/journey sequences, contracts, operating knowledge and durable decisions. Distinguish implementation from deployment.
2. **Engineering change record (ECR)** lives in the configured engineering workspace **parallel to the code**. It records the intended change, requirements, proposed target views, alternatives, plan, evidence, outcomes and history. Use one stable identity per coherent change; a project-level ECR can link smaller bounded execution records.
3. **Coordination and review views** (issues, PRs, project updates) communicate selected facts to their audiences. They do not become divergent copies of the ECR or authorize changes because they exist.

Read [the ECR content contract](references/engineering-change-record.md) for seven required sections, status semantics, stage-specific readiness and a compact example. Apply [artifact assurance](references/assurance.md) at consequential dependency boundaries: structural integrity, requirement/design/plan consistency, evidence-based convergence and PR/diff alignment. Where accessible, the bundled [Markdown checker](scripts/check_ecr.py) performs deterministic **shape-only** validation; it cannot establish semantic correctness or approvals. Read [adjacent artifacts](references/artifact-types.md) when product documents, a technical RFC, ADR, diagrams or verification records have independent ownership. Read [audience views](references/audience-views.md) for issues, PRs and stakeholder updates. For architecture or user journeys, read [diagram lifecycle](references/diagram-lifecycle.md).

## Within every SDLC activity

- **Discover** the ECR and referenced PRD, requirements, current architecture and existing work/PR first. Never create an unrelated second authority or reconstruct agreed decisions from memory alone.
- **Read the relevant sections and baseline at the known revision**, identifying accepted, proposed, unknown, implemented, verified and released claims. Treat evidence in the code/repo and runtime separately from text in the workspace.
- **Produce the phase outcome** in the standard ECR section(s) or an explicit linked supporting document. Even a narrow fix records the problem, change, checks and diagram-impact disposition; it may use compact prose, but missing sections must say *not applicable* or *pending*, not disappear.
- **Check handoff readiness** using the assurance method and the **next actual consumer**, not a ceremonial phase gate. Assess structural shape when possible, then compare accepted requirements, proposed designs/diagrams, plan coverage and evidence. Report **ready**, **ready with limitations** or **blocked**, supported by precise contradictions, missing decisions and actual revisions. Correct contradictions within accepted constraints and recheck dependent artifacts; do not implement a behavior whose consequential premise is blocked.
- **Persist or report precisely** using the configured workspace and available authorized access. Provide links/revisions and the next unanswered decision. If persistence is blocked, return the completed structured artifact inline and say it is **not persisted**; do not claim a ticket, file or PR was updated.
- **Update related summaries** (issue or PR) only where configured and authorized, reconciling their statuses with the ECR. A PR is a reviewer view over the implementation, not a replacement specification.

## Quality gates, without phase-gate theatre

Every performed outcome identifies who/what it affects, material choices, their acceptance status, actual evidence and unresolved blockers. Before claiming a complete implementation, compare its actual source/test behavior with accepted requirements and the target design (including failure/authorization paths), record uncovered outcomes as nonconverged, and avoid rewriting requirements to make incomplete code appear correct. Before PR readiness, reconcile the cumulative base-to-head diff, reviewer summary and current-head checks. These are agent-assisted assessments unless separately wired into an executable gate. Validate references and contradictions, not just headings; avoid invented check results, diagram nodes, file paths, stakeholder signoffs or SLOs. Link decisions to affected requirements, implementation slices and verification where useful, but do not require synthetic numeric IDs or a traceability spreadsheet for a small feature.

Standardization means **consistent sections and statuses**, not identical word counts, a separate file per phase, a ticket per task or mandatory approvals. Unperformed phases remain pending and are not represented as completed. For a substantive architecture change, diagrams/RFCs are expected; a styling fix should explain their non-applicability rather than fabricate them. Superseded decisions must remain traceable and no proposed design is labeled current simply because it was accepted.

## Composition

Engineering specialists remain responsible for actual domain content: [requirements-engineering](../requirements-engineering/SKILL.md), [system-design](../system-design/SKILL.md), [system-mapping](../system-mapping/SKILL.md), and available architecture-documentation/interface design methods. This skill validates their outputs and relationships; it does not regenerate diagrams or independently decide architecture. Storage and provider-specific mechanics belong solely to engineering-workspace. Contribution/publishing actions remain with the entry point and git-contributions.
