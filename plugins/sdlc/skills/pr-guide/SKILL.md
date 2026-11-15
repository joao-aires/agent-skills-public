---
name: pr-guide
description: Guide to writing a pull request description. Covers why, what changed, design impact, validation, risk, release and reviewer links.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: verification
  scope: generic
  invocation: both
  role: support
---

# PR guide

A pull request description helps a reviewer understand the diff and decide whether it is safe to merge. It is written for the reviewer, not for the author’s future self and not as a second ECR.

## Reader questions

1. Why does this change exist?
2. What changed, and what behavior is intentionally preserved?
3. What design or contract impact does the reviewer need to know?
4. What was actually validated, at which revision and environment?
5. What risk, migration, release or rollback concern remains?
6. Where are the authoritative requirements, design and issue?

## Minimum content

- why and intended outcome;
- what changed and what did not;
- design or contract impact;
- validation: commands, scenarios, results and revision;
- release, migration, rollback and risk;
- links to the issue, design, specification and related PRs;
- reviewer focus and open questions.

## Structure and quality

- Lead with the reason and the reviewer’s decision, not a file-by-file tour.
- Describe the actual diff, not the plan.
- Call out behavior changes, migrations and compatibility.
- Report failed, skipped or unavailable checks honestly.
- Distinguish local, CI and deployed evidence.
- Keep the PR small enough to review; split unrelated cleanup.
- Update the description when the head changes.
- Do not claim deployment or production success from a merge.

## Common failures

- an empty or “fixes bug” description;
- a summary that describes the plan rather than the diff;
- hidden design or contract changes;
- “tests pass” without the revision or result;
- a merge described as a release;
- unrelated refactors bundled into the change;
- stale validation after a new push;
- review comments answered only in chat.

## Review

Read the PR as the reviewer:

- Do you know why this exists and what to focus on?
- Can you trace the changed behavior to acceptance?
- Are design, compatibility and migration impacts clear?
- Is the validation at the current head?
- Is the risk and release path explicit?
- Are the authoritative links reachable?

## Handoff

The reviewer needs the why, diff intent, design impact, validation and risk. The release owner needs the migration and rollback notes. A merged PR is not a released or verified production change.
