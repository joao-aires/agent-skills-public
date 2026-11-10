# Engineering Change Record: required content contract

An ECR is the **durable, reader-oriented specification of one coherent engineering change**, not a commit log, a ticket dump, or the current application architecture. An engineering workspace owns its location; the application's repository owns actual implementation and canonical current-state documentation. A project ECR may cover several work packages, each with its own links and review status. The ECR's format is Markdown-like prose with stable headings; **no YAML/JSON manifest or prescribed file tree is required**.

## Seven required sections

Every ECR, including a compact single-file fix, has these headings in this order. Use truthful `Pending`, `Not applicable — reason`, or `Blocked — decision/evidence needed` for content not yet established. This makes the format predictable without presenting future work as finished.

### 1. Overview and lifecycle
- Short title and stable change identity (existing tracker ID/link if any; otherwise workspace-relative reference).
- Purpose, scope of ECR and affected application(s), reader/decision owner, current activity/stage and relevant source revision.
- ECR status versus claim status: proposed, accepted, implemented, verified, released, superseded are **separate statements**; report which claim has which evidence.
- Links to parent PRD/project, implementation issues and PRs where they exist. Do not create them just to fill a field.

### 2. Problem and scope
- Current observed problem, actor/customer impact, intended outcome, inclusions/exclusions, important existing behavior and assumptions.
- Distinguish supplied evidence from hypotheses and approved product direction. Link to PRD for product-wide value/priority; do not copy the entire PRD.

### 3. Requirements and acceptance
- Actors and permitted actions, functional behavior, relevant quality/security/operating constraints, denied/partial/failure paths and compatibility.
- Observable acceptance cases and the open decisions preventing readiness. Label material requirements accepted/proposed/unknown.
- User journey/wireflow when interaction work benefits from it; no invented design mechanism or arbitrary SLO.

### 4. Solution design
- Existing-system baseline at source revision and **proposed** system/UX/service behavior; selected approach, meaningful alternatives, trade-offs, data/authority boundaries, failure and migration consequences.
- Link/attach target C4 context/container/component views and critical sequence/journey diagrams when applicable, keeping **current-versus-target** and status explicit. See [diagram lifecycle](diagram-lifecycle.md).
- Link a separately maintained RFC for complex proposals and a canonical ADR for an accepted consequential decision; don't duplicate their full rationale.
- Record acceptance/decision owner; a draft proposal cannot silently satisfy an implementation dependency.

### 5. Implementation strategy
- Ordered deliverable increments, affected contracts/components, prerequisites, compatibility/migrations, verification per slice, delivery/rollback and remaining implementation blockers.
- Links to execution issues only if coordination warrants them; no obligatory ticket graph or folder-by-folder plan.

### 6. Verification and release
- What was actually exercised, at which revision/target, outcome and evidence path; failed, skipped, unavailable and blocked checks.
- Variance from proposed design, material review findings, remaining risk, documentation reconciliation and release/readiness versus actual deployed state.
- Link CI/review/run evidence and PR(s); never turn a green build into proof of user-visible behavior.

### 7. Decision history and references
- Accepted/rejected/superseded choices, owner and rationale, outstanding questions and disposition; links to canonical PRD/RFC/ADR, diagrams, baseline, issues/PRs and runtime evidence.
- History is a readable set of **consequential changes**, not an automatically appended full activity log.

## Phase completion and consumer checks

| Completed activity | ECR evidence required before describing it as ready |
| --- | --- |
| Refine | Outcome, acceptance and constraints are sufficient for design; missing decision owner named |
| Design | Proposed target and relevant diagram changes are understood, material alternatives resolved or blocked |
| Plan | Dependency-ordered increments reference accepted requirements/design; verification and migration covered |
| Implement | Actual change/revision, deviations, relevant canonical-doc edits and checks reported |
| Test/review | Observations and findings tied to the checked revision; untested claims not promoted |
| Release | Actual artifact/target, gates, recovery and promotion/verification status stated precisely |
| Maintenance | Findings, incidents, signals and remediation linked to affected requirements/decisions as needed |

Entry points may stop earlier; no task automatically authorizes later phases. The ECR is updated incrementally and the reader must be able to tell what is pending. At each completed/attempted handoff, add the readiness disposition and consequential findings in the relevant section (without creating a mandatory eighth section). Follow [artifact assurance](assurance.md) for contradictions, source/test convergence, PR alignment and truthfulness limits. For accessible local Markdown files, [check_ecr.py](../scripts/check_ecr.py) checks seven-section structure only; a passing structural result never proves semantic acceptance or execution.

## Compact example (small bug)

Use the same seven headings in a single compact record:
1. Overview: language selector intermittently fails to persist; local fix at revision X.
2. Problem: rapid changes race persistence; existing selected-language behavior protected.
3. Requirements: last valid selection persists; reproduce rapid changes and reload.
4. Solution: update the existing state synchronization; **no architecture boundary or diagrams affected**.
5. Strategy: focused code change plus regression test; no migration.
6. Verification: real command/result/revision; failures explicitly named; no release claimed.
7. Decisions: reuse existing state owner; link PR if authorized.

Keep the artifact inspectable and meaningful, not padded. For a major new system, the same headings grow, and separate supporting diagrams, PRDs and RFCs are justified.
