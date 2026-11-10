---
name: engineering-artifacts
description: Maintain engineering change records, research reports and issue or PR views. Use to decide which engineering artifacts a change or inquiry needs and assess their consistency with decisions, implementation and evidence.
user-invocable: false
metadata:
  scope: generic
  invocation: agent
  role: support
---

# Engineering artifacts: one change, reviewable outcomes

Record each performed activity on an engineering change in its ECR or a linked artifact. For a standalone inquiry, produce a [research report](references/artifact-types.md#standalone-engineering-research) suited to the decision. Use [the development workflow](../../WORKFLOW.md) for activity selection and [engineering-workspace](../engineering-workspace/SKILL.md) for discovery and persistence. The requested activity sets the stopping point and write authority.

## The authoritative layers

1. **Application baseline** lives in the application repository's established documentation: implemented system C4 views, critical runtime/journey sequences, contracts, operating knowledge and durable decisions. Distinguish implementation from deployment.
2. **Engineering change record (ECR)** lives in the configured engineering workspace **parallel to the code**. It records the intended change, requirements, proposed target views, alternatives, plan, evidence, outcomes and history. Use one stable identity per coherent change; a project-level ECR can link smaller bounded execution records.
3. **Coordination and review views** (issues, PRs, project updates) communicate selected facts to their audiences. They do not become divergent copies of the ECR or authorize changes because they exist.

Read [the ECR content contract](references/engineering-change-record.md) for seven required sections, status semantics, stage-specific readiness and a compact example. Apply [artifact assurance](references/assurance.md) at consequential dependency boundaries: structural integrity, requirement/design/plan consistency, evidence-based convergence and PR/diff alignment. Validate the standard seven sections and honest dispositions directly from the authoritative document, allowing legitimate nested Markdown headings and provider-native formats. No bundled parser, mandatory command or external service is required. Read [adjacent artifacts](references/artifact-types.md) when product documents, a technical RFC, ADR, diagrams or verification records have independent ownership. Read [audience views](references/audience-views.md) for issues, PRs and stakeholder updates. For architecture or user journeys, read [diagram lifecycle](references/diagram-lifecycle.md).

## Maintain a change record

- **Discover** the ECR and referenced PRD, requirements, current architecture and existing work/PR first. Never create an unrelated second authority or reconstruct agreed decisions from memory alone.
- **Read the relevant sections and baseline at the known revision**, identifying accepted, proposed, unknown, implemented, verified and released claims. Treat evidence in the code/repo and runtime separately from text in the workspace.
- **Produce the phase outcome** in the standard ECR section(s) or an explicit linked supporting document. Even a narrow fix records the problem, change, checks and diagram-impact disposition; it may use compact prose, but missing sections must say *not applicable* or *pending*, not disappear.
- **Check handoff readiness** using the assurance method and the **next actual consumer**, not a ceremonial phase gate. Assess structural shape when possible, then compare accepted requirements, proposed designs/diagrams, plan coverage and evidence. Report **ready**, **ready with limitations** or **blocked**, supported by precise contradictions, missing decisions and actual revisions. Correct contradictions within accepted constraints and recheck dependent artifacts; do not implement a behavior whose consequential premise is blocked.
- **Persist through the [engineering workspace](../engineering-workspace/SKILL.md).** Follow its storage choice and access rules. Report the verified record location or the reason the outcome is unpersisted.
- **Update related summaries** (issue or PR) only where configured and authorized, reconciling their statuses with the ECR. A PR is a reviewer view over the implementation, not a replacement specification.

## Quality gates, without phase-gate theatre

Every performed outcome identifies who/what it affects, material choices, their acceptance status, actual evidence and unresolved blockers. Before claiming a complete implementation, compare its actual source/test behavior with accepted requirements and the target design (including failure/authorization paths), record uncovered outcomes as nonconverged, and avoid rewriting requirements to make incomplete code appear correct. Before PR readiness, reconcile the cumulative base-to-head diff, reviewer summary and current-head checks. These are agent-assisted assessments unless separately wired into an executable gate. Validate references and contradictions, not just headings; avoid invented check results, diagram nodes, file paths, stakeholder signoffs or SLOs. Link decisions to affected requirements, implementation slices and verification where useful, but do not require synthetic numeric IDs or a traceability spreadsheet for a small feature.

Standardization means **consistent sections and statuses**, not identical word counts, a separate file per phase, a ticket per task or mandatory approvals. Unperformed phases remain pending and are not represented as completed. For a substantive architecture change, diagrams/RFCs are expected; a styling fix should explain their non-applicability rather than fabricate them. Superseded decisions must remain traceable and no proposed design is labeled current simply because it was accepted.

## Composition

The engineering artifact method owns applicability, content contracts, status and evidence checks. [Requirements engineering](../requirements-engineering/SKILL.md) derives the acceptance contract. [System design](../system-design/SKILL.md) owns proposed architecture and tradeoffs, and [system mapping](../system-mapping/SKILL.md) traces the implemented baseline. Use available architecture documentation expertise to select and maintain useful views. Use reader-oriented writing expertise for structure, wording, comparisons and navigation once the engineering content and ownership are clear. Review the outcome against both the reader's task and the actual source or evidence. [Engineering workspace](../engineering-workspace/SKILL.md) owns provider mechanics, and the entry point and Git contribution method own authorized publishing.
