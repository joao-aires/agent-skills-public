# Pull request contract: the reviewer's view

A pull request owns the **submitted implementation and review evidence**. The ECR owns the evolving engineering account; an issue owns intended work and coordination. The PR is a projection for reviewers, not a second ECR.

Apply the [artifact quality bar](../quality-bar.md). A reviewer who has not read the conversation or the private ECR must be able to understand why the change exists, what actually changed, what could break, and what was checked at the current head.

## Contract

Use the repository's existing contribution template where present. If none exists, use this structure:

```markdown
## Why
The problem and the linked intent (ECR, issue or product brief).

## What changed
The actual behavior, affected boundaries, and caller or consumer compatibility.

## Design impact
Significant current-versus-target differences, diagram or ADR changes,
rationale, and departures from the accepted proposal.

## Validation
Exact revision, commands or scenarios, observations, failures and coverage
limits. Evidence must be at the current head.

## Release and risk
Migration, compatibility, observability, recovery, rollout, and remaining risk.
```

Guidance for each part:

- **Why.** Lead with the concrete problem and the resulting behavior for someone outside the conversation. Link the authoritative intent. Do not assume the reader can open a private ECR; include a short self-contained summary.
- **What changed.** Describe behavior, not a file list. Name changed defaults, accepted inputs, new failure behavior and compatibility effects when they matter to a reviewer.
- **Design impact.** Call out significant current-versus-target differences, actual diagram or ADR changes, the rationale, and any departure from the accepted design. If there is no design impact, say so and link the evidence.
- **Validation.** Give the exact revision or head SHA, the command or scenario, the environment, and the observed result. Link CI, logs or review evidence. State failed, skipped and unavailable checks. A check at an older head does not establish the current head.
- **Release and risk.** Include migration, compatibility, observability, recovery and rollout only when material. State what is not claimed: merged is not deployed, and passing CI is not user-visible verification.

## Link obligations

Use the [link rules](../quality-bar.md#4-resolvable-navigation). A PR body should link:

- The head commit or SHA, and the base if useful for the cumulative diff.
- The ECR, issue or product brief that owns the intent.
- The checks, CI run or review evidence at the current head.
- Affected diagrams or ADRs, and reconciled canonical docs where changed.
- Any follow-up issue for remaining work.

Do not write "the ECR" or a bare SHA. If the ECR is private, provide a self-contained reviewer summary and say that the link requires access.

## Visibility and private workspaces

A public PR must be useful without exposing private workspace content. Keep a short scope, acceptance and test-evidence summary in the PR. Link the private record only if the audience can access it. Do not paste the ECR body, private user data or internal decision history into a public review.

## Before declaring review-ready

Apply [artifact assurance](../assurance.md) to the **cumulative base-to-current-head diff**, not just the latest commit:

- Compare the actual diff with the PR description and the accepted ECR intent.
- Confirm the current-head checks, not an earlier run.
- Identify design deviations, canonical-doc changes and operational risk.
- Report a precise PR-description finding when editing is not authorized.
- Leave merge and approval authority with the repository policy and the authorized human or host.

The PR is review-ready when a reviewer can understand the change, reproduce the validation, see the remaining risk, and open every cited source.

## Example

> **Why.** Rapid language changes can persist an older selection. The state writer completes out of order, so a slower earlier write can overwrite a newer choice. Linked ECR: [language preference persistence](https://example.invalid/ecr).
>
> **What changed.** The existing state owner now applies a monotonic revision guard and ignores a completed write older than the newest applied revision. The public preference shape and storage key are unchanged.
>
> **Design impact.** No architecture, data-ownership or journey change. No C4, sequence or ADR update; the existing state owner remains the authority boundary.
>
> **Validation.** Head `app@<full-sha>` ([commit](https://example.invalid/app/commit)). `npm test -- language-preference` → 12 passed, 0 failed. Before the fix: 2 failed (rapid-change convergence and rejected-save preservation). CI run linked at this head. Not exercised: real browser quota failure and production telemetry.
>
> **Release and risk.** No migration. A rejected save still preserves the previous selection; user-facing failure feedback remains open with the product owner. Not deployed. Merge and release remain with the maintainer.
