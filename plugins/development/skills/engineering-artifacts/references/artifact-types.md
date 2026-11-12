# Adjacent artifact contracts and authority

Use this reference when the ECR links work with its own audience, owner or lifecycle. A linked document is a **distinct authority**, not a duplicate of an ECR section. The engineering workspace may be a file set or external document service. The application's code repository retains canonical **implemented/current** docs and conventional durable decisions.

| Artifact | Owns / expected content | Authoritative home |
| --- | --- | --- |
| PRD or product brief | User problem, audience, jobs/journeys, value, priority, product success, non-goals, high-level scope, known product risks | Product/project area of engineering workspace or an established product-document home |
| Roadmap | Outcomes and sequencing across changes, prerequisites, owners and milestones when known, with proposed versus committed work visible | Established product/project workspace, linked to the relevant ECRs |
| ECR | Change-specific scope, detailed accepted/proposed requirements, target architecture/UX, delivery plan, verification and history | Engineering workspace, linked to PRD/issue as appropriate |
| Engineering research report | Question, recommendation, primary sources, observed evidence and its limits, alternatives and open decisions | Configured engineering workspace. Link from the ECR if it informs an existing change |
| RFC / substantive design proposal | Question and constraints, current state, target C4/sequence views, alternatives, quality/trust/operating trade-offs, migration and unresolved decisions | Engineering workspace linked from ECR; optional for narrow changes |
| ADR | Consequential decision, context, alternatives, reasons, owner, date and status (proposed/accepted/superseded), consequences and implementation link | Application repository's established decisions location when architectural knowledge must outlive the change; during exploration a proposal may remain in ECR/RFC |
| Current architecture | Evidence-backed C4 context/container and selected components, current critical sequences/contracts, deployment distinctions and revision | Application repository's canonical docs, established by system mapping/architecture documentation |
| Target architecture | Proposed C4/sequence/journey states, affected boundaries, assumptions and differences from a pinned baseline | ECR/RFC, **not** the app's implemented-state pages until reconciled |
| Implementation plan | Dependency-ordered increments, tests, compatibility, migration/rollout | ECR section or linked workspace document if separately actionable |
| Verification record | Observed checks at explicit revision/target, result, coverage gap and unresolved risk | ECR section or linked CI/review evidence; executable tests live in app repo |
| Runbooks/SLOs | Operating procedures and monitored service behavior/targets with owner and evidence | Canonical application/operations documentation or actual monitoring system; ECR tracks proposed operational change |
| Issue / ticket | Ownership, work intent, actionability, acceptance, priority, dependencies and ECR link where applicable | Configured tracker if used; optional |
| Pull request | Actual diff, why/what changed, design variation, exact validation, risk and links | Git provider for the application repository |

## Choose a separate artifact when it needs its own review

Keep a bounded feature's requirements and rationale in its ECR. Use a PRD when product direction, outcomes or scope span changes or require independent product review. Use a roadmap when several changes need shared sequencing or ownership. Link each ECR to the relevant roadmap decision. Use a separate RFC when a proposal needs its own audience or decision process. Record an ADR when a consequential accepted choice needs to outlive the work. Use the [diagram lifecycle](diagram-lifecycle.md) for the affected structural and runtime views.

## Standalone engineering research

Open with the question, recommendation, strongest result and decision still needed. Compare viable alternatives on the same dimensions. Cite primary sources where they support a claim. Distinguish documented capabilities, observed outcomes and interpretation. Link runnable evidence or put it after decision material. State what evidence would change the recommendation and who owns the decision when known. The report may end at a recommendation or a decision request. Use the ECR for change implementation and release evidence when that work exists.

## A clear lifecycle for durable decisions

An RFC may be accepted before coding, but the target architecture remains *proposed relative to implementation*. If the project records accepted prospective ADRs in the repository, mark that status explicitly and never revise current C4 diagrams to claim the design is live. Reconcile the baseline and ADR consequences when implementation actually lands; retain decision history, drop stale duplicate target views only after their rationale is safely recorded.

For product direction involving several features, a single parent PRD and project ECR can inform feature ECRs and their issues. Use the same stable links/terminology; distinguish a project-level decision from a feature-level exception.

## Independence and authority

No requirement to create a PRD, issue, RFC, ADR or separate diagram merely because a list contains that artifact. An engineering change uses an ECR. A standalone inquiry can use a research report. Add other artifacts when their concern and independent audience or lifetime justify them. Do not put engineering workspace material into the application repo simply because filesystem storage is selected; the workspace may be a sibling directory or separate repository.

Do not claim a document was published or saved without checking its actual URL/path/revision. The storage method cannot manufacture stakeholder approval or architectural truth.
