# Compatibility matrix contract: the bounded consumer claim

A **compatibility matrix** is a design or delivery artifact that states which versions, platforms, runtimes and consumer combinations a public surface supports, and the evidence for each claim.

It is not the API contract. It is the bounded claim a consumer can rely on.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). Read [guide-compatibility-matrix](../../../guide-compatibility-matrix/SKILL.md) for support categories, evidence and review conventions.

## Reader questions

1. What public surface is in scope?
2. Which versions, platforms, runtimes and dependency ranges are supported?
3. Which combinations were actually tested, and where is the evidence?
4. Which combinations are unsupported, best-effort or known to fail?
5. What is deprecated, and what is the migration path?
6. How current is the claim, and what consumer was used?

## Contract

```markdown
# <Surface> — compatibility matrix

## Surface and scope
The public API, package, CLI or contract in scope.

## Support categories
Supported, tested, best-effort and unsupported definitions.

## Matrix
One row per meaningful combination: surface version, platform/runtime,
dependency range, status and evidence.

## Deprecation and migration
Deprecated surfaces, replacement, removal target and migration notes.

## Evidence
Consumer test, CI job, environment, revision or date.

## Unsupported cases
Known failures, limits and what the consumer should do instead.
```

## Handoff

The consumer needs the supported and unsupported combinations and the evidence. The release owner needs the bounded claim and any deprecation or migration commitment. See [handoff](../handoff.md).

## Maturity

Use **draft**, **published** and **superseded**. A published matrix still dates its claim; a build is not a consumer test.

## Review

- Can a consumer find their version, platform and runtime?
- Is each claim supported by a consumer test or observation?
- Are unsupported and best-effort cases explicit?
- Is deprecation and migration clear?
- Is the date or revision current enough to trust?
