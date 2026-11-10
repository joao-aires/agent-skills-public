# Issue, PR and stakeholder views: preserve audience ownership

An ECR owns the evolving engineering account; an issue owns the **intended work and coordination**; a PR owns **the submitted implementation and review evidence**. Status, summaries and deep links must agree, but bodies are not bidirectional replicas. Only publish/edit when explicitly authorized and when the provider is configured/accessible.

## Issue / work item — product and implementer audience

A bounded issue should normally include:
1. **Why/outcome:** the affected actor and value/defect.
2. **Scope/non-goals:** one deliverable, protected behavior and limitations.
3. **Acceptance:** observable success and important denial/failure outcomes, derived from the ECR or authoritative product requirement.
4. **Ownership/coordination:** priority, responsibility, dependencies and blocker/decision status when known.
5. **References:** ECR, parent PRD, accepted design and target diagrams when applicable, implementation PR(s).

It may be created before design. Do not demand planned architecture, a code estimate or acceptance signoff at issue intake. On refinement, update issue acceptance without copying the complete ECR. For a project/initiative, keep shared product/design documents at the parent and per-slice work in child issues. Filesystem-only workflows need no issue.

## PR — reviewer audience

Use the repository's existing contribution template where present. Explain concisely:
1. **Why and linked intent:** ECR/issue/PRD if accessible.
2. **What actually changed:** functional behavior and affected boundaries, not an aspirational plan.
3. **Design impact:** significant current-vs-target differences, actual diagram/ADR changes, rationale and departures from accepted proposal.
4. **Validation performed:** exact revision/commands and observations, failures/coverage limits and linked evidence.
5. **Release/operating effects and remaining risks:** migration, compatibility, observability/recovery, follow-ups where relevant.

Link the target diagrams for reviewers; also point to reconciled canonical docs where changed. Keep PR information useful if the external workspace is temporarily unavailable (a short scope/acceptance summary and test evidence). Do not paste all ECR sections or attach private workspace content to a public PR; respect access tiers and minimize sensitive details. A proposed state must not appear under "implemented".

## Product/leadership and operations readers

A project update focuses on outcome, progress, material decisions, blockers, confidence and next action. Operational handoff focuses on observable failure/restore/release behavior, targets, runbook links and actual release state. These are **views** of existing accepted knowledge and evidence; never claim checks based on summary text.

## Publication and synchronization

The entry-point task or existing git-contributions/work-tracker capability performs authorized publishing. Engineering-artifacts chooses which information matters to a reader; engineering-workspace resolves where documents live; neither grants permission to create issues or post PR comments. When an ECR evolves, update affected published summaries only if their meaning changed and edits are authorized; preserve canonical links and avoid two authoritative ECR copies.
