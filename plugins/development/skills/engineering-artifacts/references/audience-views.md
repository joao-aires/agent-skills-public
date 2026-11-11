# Issue, PR and stakeholder views: preserve audience ownership

An ECR owns the evolving engineering account; an issue owns the **intended work and coordination**; a PR owns **the submitted implementation and review evidence**. Repeat the context, constraints, acceptance and evidence the reader needs to act independently. Keep material decisions and statuses consistent across views and link to the record that owns them. Only publish/edit when explicitly authorized and when the provider is configured/accessible.

## Issue / work item — product and implementer audience

Write a task title that names the intended outcome. Lead with the problem, then give the work, scope boundaries and observable acceptance. Include ownership, dependencies and blockers when they affect pickup. Use descriptive links to the ECR or design for details. Format commands and code identifiers as inline code.

- **Draft.** Use this view when someone needs to pick up or coordinate a bounded piece of work. Requirements analysis can produce an issue for an agreed outcome. Implementation preparation can identify independently actionable slices when coordination warrants them.
- **Publish.** Locate the existing issue through [engineering workspace](../../engineering-workspace/SKILL.md). Reuse it when its scope matches. Use the configured tracker to create or update an issue within authorized scope. If publishing is outside scope, return the draft when useful.
- **Review.** Read the saved issue on its own. Check that the reader can identify what to do, what is outside scope and how to verify success. Apply the [content and presentation review](../SKILL.md#review-each-artifact-before-handoff) and retain the verified link.
- **Close.** Preserve intent and applicable acceptance. Add the actual result, evidence and remaining work.

## PR — reviewer audience

Use the repository's existing contribution template where present. Explain concisely:
1. **Why and linked intent:** ECR/issue/PRD if accessible.
2. **What actually changed:** functional behavior, affected boundaries and caller compatibility. Name changed defaults, accepted inputs or failure behavior when they matter to a reviewer.
3. **Design impact:** significant current-vs-target differences, actual diagram/ADR changes, rationale and departures from accepted proposal.
4. **Validation performed:** exact revision/commands and observations, failures/coverage limits and linked evidence.
5. **Release/operating effects and remaining risks:** migration, compatibility, observability/recovery, follow-ups where relevant.

Verify each link in the intended publication context. A local relative link needs an accessible destination before publication. Link the target diagrams for reviewers; also point to reconciled canonical docs where changed. Keep PR information useful if the external workspace is temporarily unavailable (a short scope/acceptance summary and test evidence). Do not paste all ECR sections or attach private workspace content to a public PR; respect access tiers and minimize sensitive details. A proposed state must not appear under "implemented".

## Product/leadership and operations readers

A project update focuses on outcome, progress, material decisions, blockers, confidence and next action. Operational handoff focuses on observable failure/restore/release behavior, targets, runbook links and actual release state. These are **views** of existing accepted knowledge and evidence; never claim checks based on summary text.

## Publication and synchronization

The entry-point task or existing git-contributions/work-tracker capability performs authorized publishing. Engineering-artifacts chooses which information matters to a reader; engineering-workspace resolves where documents live; neither grants permission to create issues or post PR comments. When an ECR evolves, update affected published summaries only if their meaning changed and edits are authorized; preserve canonical links and avoid two authoritative ECR copies.
