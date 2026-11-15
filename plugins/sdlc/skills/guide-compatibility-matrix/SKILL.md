---
name: guide-compatibility-matrix
description: Guide to producing and reviewing a compatibility matrix. Use for public surfaces, versions, platforms, runtimes, deprecation, migration and consumer evidence across libraries, CLIs and APIs.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Compatibility matrix guide

Read [activity system](../activity-system/SKILL.md) for scope, the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for authority and [software types](../artifact-system/references/software-types.md) for the library/CLI or backend evidence.

A compatibility matrix is a **view artifact** of what a consumer may depend on. It turns “it works” into a bounded claim across versions, platforms and runtimes.

## Reader question

Can a consumer tell whether this surface works for their version, platform and runtime, what is deprecated, and what breaks on upgrade?

## When to use

- a library, SDK, CLI or API has external consumers;
- several runtime, platform or dependency versions are supported;
- a breaking change, deprecation or migration is proposed;
- the design decision depends on consumer compatibility rather than only the implementation.

Do not use a matrix as a substitute for a contract or a real consumer test.

## Minimum content

- the public surface in scope;
- supported versions, platforms, runtimes and dependency ranges;
- tested combinations and the evidence for each;
- unsupported combinations and the failure mode;
- deprecation and migration policy;
- the date or revision of the claim;
- the consumer or environment used for verification.

## Structure and quality

- One row per meaningful combination; do not hide gaps in a note.
- Distinguish supported, tested, best-effort and unsupported.
- Record the exact version or revision, not “latest.”
- Link the consumer test, CI job or environment.
- Keep the surface and the compatibility claim separate from the marketing promise.
- Update the matrix when the contract or supported range changes.

## Common failures

- claiming support from a build, not a consumer run;
- “works on my machine” as a compatibility row;
- omitting platform or runtime combinations that are known to fail;
- an unversioned “latest” claim;
- mixing deprecation, support and migration policy;
- using the matrix as a substitute for an API contract.

## Authority, home and review

- **Authority:** the API or public-surface contract; the matrix records the claim.
- **Home:** repository docs, release notes or the package's compatibility page.
- **Review:** use [design review](../design/references/design-review.md) and [artifact assurance](../artifact-system/references/assurance.md).

## Specialist route

Use `backend-design` for service contracts, library/CLI guidance for packaging, `typescript-development` or `go-development` for their ecosystems, and `development-tooling` for CI and consumer checks. The matrix does not replace the contract.

## Handoff

Record the surface, versions, tested combinations, evidence and unsupported cases in the design proposal or release note. Do not claim compatibility from a local build alone.
