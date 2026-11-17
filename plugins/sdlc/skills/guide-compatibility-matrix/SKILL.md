---
name: guide-compatibility-matrix
description: Guide to producing and reviewing a compatibility matrix. Use for public surfaces, versions, platforms, runtimes, deprecation, migration and consumer evidence across libraries, CLIs and APIs.
user-invocable: true
metadata:
  kind: guide
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Compatibility matrix guide

A compatibility matrix turns “it works” into a bounded claim across versions, platforms and runtimes. It is written for the consumer who must decide whether they can depend on the surface.

## Reader questions

1. What public surface is in scope?
2. Which versions, platforms, runtimes and dependency ranges are supported?
3. Which combinations were actually tested, and where is the evidence?
4. Which combinations are unsupported, best-effort or known to fail?
5. What is deprecated, and what is the migration path?
6. How current is the claim?
7. What consumer or environment was used to verify it?

## When to use

- a library, SDK, CLI or API has external consumers;
- several runtime, platform or dependency versions are supported;
- a breaking change, deprecation or migration is proposed;
- a design decision depends on consumer compatibility rather than only the implementation;
- support claims are being made in docs, release notes or marketing.

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
- using the matrix as a substitute for an API contract;
- a matrix that is never updated after release.

## Review

Read the matrix as a prospective consumer:

- Can you find your version and platform?
- Is the claim supported, best-effort or unsupported?
- Is there evidence for the combination you need?
- Is the deprecation and migration path clear?
- Is the date or revision recent enough to trust?
- Does the matrix agree with the contract and release note?

## Handoff

Record the surface, versions, tested combinations, evidence and unsupported cases. The consumer should be able to decide whether to depend on the surface; the release owner should know what may be claimed. Do not claim compatibility from a local build alone.
