---
name: guide-issue
description: Guide to writing an actionable issue. Covers context, intended outcome, scope, acceptance, constraints, verification, dependencies and ownership.
user-invocable: true
metadata:
  kind: guide
  origin: local
  pack: sdlc
  domain: development
  phase: implementation
  scope: generic
  invocation: both
  role: support
---

# Issue guide

An issue is intended work for someone who needs to pick it up without the original conversation. It is not a second specification, a design document or a status diary.

## Reader questions

1. What is the context and why does this work exist?
2. What outcome is intended, and what is explicitly not?
3. What acceptance tells the implementer the work is done?
4. What constraints, dependencies and risks apply?
5. How should the result be verified?
6. Who owns the work, and what is blocked?

## Minimum content

- context and problem;
- intended outcome and user/system value;
- scope and non-goals;
- observable acceptance;
- constraints and dependencies;
- verification expectation;
- owner, status and links to the authoritative change record.

## Structure and quality

- Write for an implementer who has the issue but not the chat.
- Keep the issue bounded; split work that has independent outcomes.
- Make acceptance observable; “works well” is not acceptance.
- Link the decision, design, specification or ECR instead of copying it.
- State what is unknown or blocked.
- Keep the issue and the pull request views consistent on scope and status.
- Update the issue when the scope or acceptance changes; do not leave stale text above the new state.

## Common failures

- a title with no context;
- acceptance that restates the title;
- a second full design document in the issue;
- hidden dependencies or owners;
- “done” based on a merge without verification;
- no distinction between the issue’s intended work and the actual PR diff;
- a catch-all issue that never closes.

## Review

Use the issue-only pickup test:

- Could someone start this work from the issue and its links?
- Do they know the outcome, scope, acceptance and verification?
- Are dependencies and blocked work explicit?
- Is the owning record linked?
- Would the implementer know when to stop?

## Handoff

The implementer needs the outcome, scope, acceptance, constraints, verification and dependencies. The issue may summarize the change record and link it; it should not become a competing authority.
