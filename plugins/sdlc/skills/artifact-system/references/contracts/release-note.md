# Release note contract: what shipped, to whom, and what to watch

A **release note** records a delivery to a target for the people who must understand, operate or adopt it. It is delivery-and-operations-first, but it may also serve users and reviewers.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the git provider release or `CHANGELOG.md`; a docs site or `docs/releases/` may be the established alternate.

## Reader questions

A reader who was not in the conversation must be able to answer:

1. What shipped, and to which target or environment?
2. Who is affected, and what must they do differently?
3. What changed in behavior, contracts, configuration or data?
4. What migration, compatibility or downtime should they expect?
5. How was the release verified, and what remains unverified?
6. How do they roll back or recover if something goes wrong?
7. Where is the change record and the actual evidence?

## Contract

```markdown
# <Release or version>

## Summary
What shipped, for whom, and the target/environment.

## Changes
User-visible behavior, contracts, configuration, data and operating changes.

## Migration and compatibility
Required actions, deprecations, data changes and expected downtime.

## Verification
What was checked, at which revision/target, and what remains unverified.

## Rollback and recovery
The approved rollback/roll-forward path and its verification.

## References
ECR, PR, checks, deployment record, runbook and known issues.
```

Guidance:

- **Summary.** State the actual target and version. An artifact built or merged is not necessarily deployed.
- **Changes.** Describe behavior, not a commit list. Name breaking changes, defaults and required actions.
- **Migration and compatibility.** Give the operator or consumer the exact step and expected result. Link the migration or runbook.
- **Verification.** Use past tense. Link the checks at the released revision/target. Distinguish pre-release checks, smoke checks and observed production behavior.
- **Rollback and recovery.** State the approved path and who may execute it. Do not invent a rollback that was not tested or authorized.
- **References.** Link the ECR, PR, release artifact, deployment record and runbook using the [link rules](../quality-bar.md#4-resolvable-navigation).

## Maturity

A release note is written for an actual delivery. It may be **draft** before the target action, **released** after verified promotion, or **superseded** by a later release. Do not label a merged change as released, or a passing CI run as production verification.

## Home and maintenance

Keep one current release note per delivered version or target. Link the previous and next release where useful. When a later release supersedes it, preserve the historical note and mark it superseded rather than rewriting it.

## Review

Can a reader identify what changed, whether they must act, how the release was verified and how to recover? If the note only lists commits or says "various fixes," it is not a release note.
