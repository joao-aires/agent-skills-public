# Artifact catalog: choose the type, plane, home and contract

Use this reference to decide **which artifact** a change or inquiry needs, what role it plays, where it lives, and which contract governs it. Read the [artifact model](model.md) for the shared fields and [artifact homes](homes.md) for the resolution method.

The ECR is the default coordination artifact for a coherent engineering change. A standalone inquiry can end with a research report. Other artifacts exist when their concern, audience or lifetime justifies them. Do not create one merely because it appears here.

## Artifacts by plane

| Plane | Artifact | Owns | Default home | Contract |
| --- | --- | --- | --- | --- |
| Intent | Product brief / PRD | User problem, audience, value, priority, product success, non-goals and product risks | Product/project workspace or established product-document home | [Product brief](contracts/prd.md) |
| Intent | Roadmap | Outcomes and sequencing across changes, prerequisites, owners and proposed versus committed work | Product/project workspace | [Roadmap](contracts/roadmap.md) |
| Coordination | ECR | Change-specific scope, requirements, target design, plan, verification and history | Engineering workspace | [ECR](contracts/ecr.md) |
| Coordination | Research report | Question, recommendation, primary sources, observed evidence and limits, alternatives and open decisions | Engineering workspace | [Research report](contracts/research-report.md) |
| Coordination | RFC | Proposal with its own audience, current state, target views, alternatives and trade-offs | Engineering workspace or durable `docs/rfcs/` | [RFC](contracts/rfc.md) |
| Coordination | Issue | Work intent, ownership, acceptance, dependencies and evidence link | Configured tracker | [Issue](contracts/issue.md) |
| Coordination | Pull request | Actual diff, why and what changed, design variation, validation and risk | Git provider | [Pull request](contracts/pr.md) |
| System knowledge | Architecture set | Context, container, component, runtime, data, interface, deployment, quality and decision views | Application repository `docs/architecture/` or a dedicated architecture repository | [Architecture set](contracts/architecture-set.md) |
| System knowledge | Decision record (ADR/PDR) | Consequential decision, context, alternatives, consequences, owner, date and status | Application repository `docs/decisions/`; engineering workspace while proposed | [Decision record](contracts/adr.md) |
| System knowledge | Runbook | Trigger, impact, diagnosis, mitigation, verification and escalation for a known condition | Operations repository `ops/<application>/runbooks/` or `docs/operations/` | [Runbook](contracts/runbook.md) |
| System knowledge | API reference / SLO | Generated contract or monitored target with owner and evidence | Contract source plus docs index; monitoring system or operations home | Use available API/reliability expertise and link the evidence. |
| Implementation | Code, tests, migrations, configuration | Implemented behavior and its verification | Application repository | [Work product](contracts/work-product.md) |
| Delivery | Release note / changelog | What shipped, to which target, with migration, verification and recovery | Git provider release or `CHANGELOG.md` | [Release note](contracts/release-note.md) |
| Delivery | Deployment record, incident, postmortem | Actual target state, observed behavior and learning | Delivery/operations home | Use the relevant delivery/operations method and link the evidence. |
| Entry | README | Repository purpose, quickstart, docs map, status and limits | Application repository root | [Repository README](contracts/repository-readme.md) |
| Entry | Guide / tutorial | Bounded task or learning path with verification and recovery | `docs/guides/` or docs site | [Guide](contracts/guide.md) |
| Entry | Glossary | Shared domain and system terms | `docs/glossary.md` or docs site | Use the docs index; keep terms consistent across artifacts. |

## Maturity and evidence by artifact

Each artifact states its own maturity. Do not promote a later phase's claim into an earlier artifact.

| Artifact | Maturity states | Evidence expected | Must not claim |
| --- | --- | --- | --- |
| Product brief / PRD | Draft, proposed, accepted, superseded | User evidence, product decision, success signal | Implementation or verification |
| Roadmap | Draft, proposed, committed, superseded | Outcome, sequencing, owners, dependencies | Implementation or release |
| Decision record (ADR/PDR) | Proposed, accepted, superseded, deprecated | Decision context, owner, date, consequences | Implementation unless linked |
| Research report | Question, recommendation proposed, decision requested, accepted | Primary sources, observed probe results, limits | Production behavior or accepted design |
| RFC | Draft, proposed, accepted, rejected | Current state, target views, alternatives, trade-offs | Implemented or released |
| ECR | Proposed, accepted, implemented, verified, released, superseded, per claim | Phase-specific evidence at exact revisions | Later-phase claims |
| Issue | Ready, in progress, blocked, done, cancelled | Acceptance, dependencies, verification plan | Merged or released unless linked |
| Pull request | Draft, ready for review, merged, closed | Base-to-head diff, current-head checks, review | Deployed or production verified |
| Architecture set | Current, proposed, mixed, retired | Source, contract, runtime and decision evidence at a revision | Implemented when only proposed |
| Runbook | Draft, active, retired | Exercised steps, targets, recovery limits | Unexercised behavior |
| Work product | Proposed, implemented, verified, released, superseded | Commands, tests, CI or runtime observation at a revision | Deployment or user-visible success without evidence |
| Release note | Draft, released, superseded | Target, checks, promotion and observed state | Production success from a merge or build |
| README / guide | Current, draft, retired | Verified commands, paths and links | Unsupported status or unverified setup |

## Choose a separate artifact when it needs its own review

Keep a bounded feature's requirements and rationale in its ECR. Use a product brief or PRD when product direction, outcomes or scope span changes or require independent product review. Use a roadmap when several changes need shared sequencing or ownership, and link each ECR to the relevant roadmap decision.

Use a separate RFC when a proposal needs its own audience or decision process. Record an ADR or PDR when a consequential accepted choice must outlive the work. Use the [diagram lifecycle](diagram-lifecycle.md) for affected structural and runtime views. Add an issue when someone needs to pick up or coordinate bounded work. Add a pull request for the submitted diff and review evidence.

A linked document is a distinct authority, not a duplicate ECR section. The application's code repository retains canonical implemented and current-state documentation. The engineering workspace retains change-oriented records and standalone research.

## Standalone engineering research

A standalone inquiry can stop at a decision-oriented report. Use the [research report contract](contracts/research-report.md). If research supports an existing change, link or incorporate its conclusions in that change's ECR rather than creating a second narrative.

## A clear lifecycle for durable decisions

An RFC may be accepted before coding, but the target architecture remains **proposed relative to implementation**. If the project records accepted prospective ADRs, mark that status explicitly and never revise current architecture views to claim the design is live. Reconcile the baseline and ADR consequences when implementation lands; retain decision history, and drop stale duplicate target views only after their rationale is safely recorded.

For product direction involving several features, a single parent PRD and project ECR can inform feature ECRs and their issues. Use stable links and terminology; distinguish a project-level decision from a feature-level exception.

## Communication views

Product, leadership and operations readers need a **view** of existing accepted knowledge and evidence, not a new authority.

- A project update focuses on outcome, progress, material decisions, blockers, confidence and next action.
- An operational handoff focuses on observable failure, restore and release behavior, targets, runbook links and actual release state.

These views may summarise and link, but they must not claim checks based on summary text. Never turn a status update into a second ECR.

## Publication and synchronization

The entry-point task or Git contribution capability performs authorized publishing. This catalog chooses which information matters to a reader; [engineering workspace](storage/coordination.md) resolves change-artifact storage; [artifact homes](homes.md) and the repository map resolve repository artifacts. None grants permission to create issues or post PR comments.

When an artifact evolves, update affected published summaries only if their meaning changed and edits are authorized. Preserve canonical links and avoid two authoritative copies. Use the [quality bar](quality-bar.md) for link access and render checks.

## Independence and authority

No requirement to create a PRD, issue, RFC, ADR, architecture set or separate diagram merely because this catalog lists that artifact. An engineering change uses an ECR. A standalone inquiry can use a research report. Add other artifacts when their concern and independent audience or lifetime justify them. Do not put engineering workspace material into the application repository simply because filesystem storage is selected; the workspace may be a sibling directory or a separate repository.

Do not claim a document was published or saved without checking its actual URL, path or revision. The storage method cannot manufacture stakeholder approval or architectural truth.
