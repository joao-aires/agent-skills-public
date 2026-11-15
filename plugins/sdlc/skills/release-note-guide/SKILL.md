---
name: release-note-guide
description: Guide to writing a release note or changelog. Covers what shipped, target, changes, migration, compatibility, verification and rollback.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: delivery
  phase: release
  scope: generic
  invocation: both
  role: support
---

# Release note guide

A release note tells users, operators or maintainers what actually shipped, to which target, and what they must do about it. It is not a marketing announcement and not a list of every commit.

## Reader questions

1. What shipped, and to which target or audience?
2. What changed for the user or operator?
3. What breaks, changes, migrates or needs action?
4. How was it verified, and what remains unverified?
5. How can it be rolled back or recovered?
6. Where are the authoritative details?

## Minimum content

- release identity, date and target;
- summary of the user/operator-visible change;
- changes by category: added, changed, fixed, removed, security;
- migration and compatibility;
- verification and known limits;
- rollback or recovery;
- references to the change record, PR, runbook and incidents.

## Structure and quality

- Write for the reader who consumes the release, not the team that built it.
- Separate “built” from “released” and “verified.”
- Call out breaking changes and required actions first.
- Use consistent versioning and a stable changelog format.
- Do not turn internal refactors into user-facing news.
- State the target and rollout state.
- Link detail; do not copy the whole PR.
- Keep historical entries; do not rewrite released notes.

## Common failures

- marketing copy in a technical release note;
- a commit list with no user meaning;
- no breaking-change or migration warning;
- “released” based on a merge or build;
- no target or rollout state;
- missing rollback or recovery;
- rewriting past entries;
- leaking secrets or internal identifiers.

## Review

Read the note as a consumer or operator:

- Do you know what changed and whether it affects you?
- Are required actions and breaking changes obvious?
- Is the target and rollout state clear?
- Is verification and rollback covered?
- Can you reach the authoritative detail?

## Handoff

The operations reader needs the target, changes, migration, verification and rollback. The user reader needs the behavior change and required action. A release note does not prove production success; link the observed state.
