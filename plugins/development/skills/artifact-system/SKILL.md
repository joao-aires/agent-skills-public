---
name: artifact-system
description: Maintain engineering artifacts across intent, change, system knowledge, implementation, delivery and entry planes. Use to choose an artifact type, resolve its home, apply its contract and quality bar, and check cross-artifact consistency.
user-invocable: false
metadata:
  kind: system
  origin: local
  scope: generic
  invocation: agent
  role: support
---

# Artifact system: one model, many artifact types

An **engineering artifact** is a durable, addressable unit of engineering intent, knowledge, implementation or evidence. ECRs, PRDs, roadmaps, RFCs, ADRs, issues, PRs, architecture views, runbooks, READMEs, code and tests are all artifacts. The ECR is the coordination spine for a change, not the only artifact.

Use [the development workflow](../activity-system/SKILL.md) for activity selection. The requested activity sets the stopping point and write authority.

## Reading path

| Need | Read |
| --- | --- |
| Understand the shared model, planes and relations | [Artifact model](references/model.md) |
| Choose the type, plane and contract | [Artifact catalog](references/catalog.md) |
| Resolve where the artifact lives | [Artifact homes](references/homes.md) |
| What must this artifact contain? | Its [contract](references/contracts/README.md) |
| Is it sufficient, navigable and readable? | [Artifact quality bar](references/quality-bar.md) |
| Are the artifacts consistent and ready? | [Artifact assurance](references/assurance.md) |
| Does it need a diagram or view? | [Diagram lifecycle](references/diagram-lifecycle.md) |
| Where and how do I publish a coordination artifact? | [Coordination storage](references/storage/coordination.md) |

Read the contract before authoring the artifact. Resolve the home before creating or moving it. Apply the quality bar to every artifact you create or materially update.

## The core model

- **Artifact type** determines the contract: ECR, PRD, ADR, issue, PR, architecture set, runbook, work product, release note, README or guide.
- **Plane** describes the primary role: intent, coordination, system knowledge, implementation, delivery or entry. It is not a storage location.
- **Home** is where the authoritative copy lives: engineering workspace, application repository, tracker, git provider or operations repository. A type can move homes without changing its contract.
- **Maturity** is per claim: proposed, accepted, implemented, verified, released, superseded, active or retired.
- **Relations** connect artifacts: derives from, informs, decides, proposes, implements, verifies, documents, projects, supersedes, releases, operates.
- **Evidence** backs each claim: source revision, command, test, CI run or runtime observation.

Read [the artifact model](references/model.md) for the fields and plane table. Use [artifact homes](references/homes.md) and the repository map to resolve the actual location. Do not infer a home from a plane.

## Maintain the artifact system

1. **Discover** existing artifacts, their authorities, homes and links before creating anything. Read project instructions and the repository artifact home map. Never create an unrelated second authority.
2. **Classify** the artifact type and primary plane using the [catalog](references/catalog.md). Identify secondary relations; do not force a cross-plane artifact into one box.
3. **Resolve the home** with [artifact homes](references/homes.md). Use the established home; if none exists, choose the type default within authorized scope and record a portable pointer.
4. **Read the contract** for the artifact type. Fill each section to its sufficiency floor, not just its heading. A section that only links elsewhere for its substance is an index, not a record.
5. **Use the domain method** for the subject (product, architecture, operations, security, API) and available writing-craft expertise for the prose. The contract states the outcome; the domain and craft skills teach how to achieve it.
6. **Apply the [quality bar](references/quality-bar.md)**: self-contained context, explicit maturity and evidence, reader sufficiency, resolvable links, render fidelity and one authority.
7. **Check at handoffs** with [artifact assurance](references/assurance.md): consistency, convergence, coverage and freshness across the artifact graph.
8. **Persist and report** the actual home, revision and access. A tool call is not proof that the reader can open the artifact.

For a coordination change, the ECR remains the evolving account. For repository knowledge, the application repository remains the authority for implemented state. For a work product, language/framework guidance owns the implementation quality; this system owns its identity, home, relations and evidence.

## The authoritative layers

1. **Application baseline** lives in the application repository: implemented architecture, contracts, runbooks and durable decisions. Distinguish implementation from deployment.
2. **Engineering change record** lives in the configured engineering workspace, parallel to the code. It records the intended change, requirements, proposed target views, alternatives, plan, evidence and history.
3. **Coordination and review views** (issues, PRs, project updates) communicate selected facts to their audiences. They do not become divergent copies of the ECR.
4. **Work products** (code, tests, migrations, configuration) implement and verify the change. They are artifacts with their own authority and evidence.

The [catalog](references/catalog.md) owns selection, authority and default homes. The [ECR contract](references/contracts/ecr.md) owns the seven sections, status semantics and phase readiness. The [issue](references/contracts/issue.md) and [PR](references/contracts/pr.md) contracts own their reader views. The [architecture-set](references/contracts/architecture-set.md), [runbook](references/contracts/runbook.md), [work-product](references/contracts/work-product.md), [release-note](references/contracts/release-note.md), [README](references/contracts/readme.md) and [guide](references/contracts/guide.md) contracts own their artifact types. The [research report](references/contracts/research-report.md), [RFC](references/contracts/rfc.md), [decision record](references/contracts/adr.md), [product brief](references/contracts/prd.md) and [roadmap](references/contracts/roadmap.md) contracts own the adjacent artifact types.

## Present outcomes

Open with the current outcome, the strongest evidence or evidence gap, and the next action or decision with its owner when known. State scope and disposition together. Use short paragraphs for rationale, lists for acceptance and actions, and tables when alternatives share meaningful comparison dimensions.

Apply the [artifact quality bar](references/quality-bar.md) in full:

- Write evidence in the past tense. "Will verify" is a plan, not verification.
- Link every commit, PR, issue, page, file and source, or mark it local-only with the repository, revision and worktree.
- Keep the current state first in each section. Put dated checkpoints and superseded evidence in a history subsection.
- Read back the published view and fix formatting, link or diagram defects before claiming persistence.
- Keep one authority per concern. Views link the authority; they do not replace it.

## Review each artifact before handoff

Review every artifact you create or materially update for content and presentation. Check claims, decisions, status and evidence against their authoritative sources. Read an issue or PR from its own reader's perspective. Apply the [issue-only pickup test](references/contracts/issue.md#the-issue-only-pickup-test) and the [cold-reader test](references/quality-bar.md#3-reader-sufficiency).

For saved artifacts, read back the published result and inspect the actual reader view where supported. Check headings, lists, tables, links and code formatting that matter to the handoff. For diagrams, compare saved and intended source, open the preview or linked rendering, and inspect it for semantic accuracy. Fix defects within scope and recheck. Name any limitation that cannot be verified.

## Quality gates, without phase-gate theatre

Every performed outcome identifies who or what it affects, material choices, their acceptance status, actual evidence and unresolved blockers. Before claiming a complete implementation, compare actual source and test behavior with accepted requirements and the target design, including failure and authorization paths. Record uncovered outcomes as nonconverged. Before PR readiness, reconcile the cumulative base-to-head diff, reviewer summary and current-head checks.

These are agent-assisted assessments unless separately wired into an executable gate. Validate references and contradictions, not just headings; avoid invented check results, diagram nodes, file paths, stakeholder signoffs or SLOs. Link decisions to affected requirements, implementation slices and verification where useful, but do not require synthetic numeric IDs or a traceability spreadsheet for a small feature.

Standardization means **consistent fields and statuses**, not identical word counts, a separate file per phase, a ticket per task or mandatory approvals. Unperformed phases remain pending and are not represented as completed. For a substantive architecture change, diagrams and RFCs are expected; a styling fix should explain their non-applicability rather than fabricate them. Superseded decisions remain traceable, and no proposed design is labeled current simply because it was accepted.

## Composition

The artifact system owns applicability, contracts, status, evidence, home resolution, link navigation and cross-artifact consistency. Domain methods own the subject: requirements engineering, system design, architecture explanation, operations, security and API contracts. Writing-craft expertise owns reader fit, explanation, structure and presentation. [Coordination storage](references/storage/coordination.md) owns coordination-artifact storage mechanics. [Project conventions](../project-conventions/SKILL.md) owns repository foundations and the artifact home map. The entry point and Git contribution method own authorized publishing.
