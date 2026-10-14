---
name: develop
description: Take a rough business idea, feature, refactor or improvement through
  clarification, design, implementation, testing and review in one requested engagement.
  Use for end-to-end development with consequential questions and explicit assumptions,
  not a promise of zero interaction or automatic deployment.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Develop

Read [task guidance](../../TASKS.md). Treat the rough idea as an outcome to shape, not an instruction to build every imagined feature. Inspect the repository and supplied references first. For a new product select a useful coherent first slice; for existing work preserve architecture, identity, UI and operations constraints. Use available strategy/domain guidance when it answers a real uncertainty.

Clarify material user/business outcomes, data/authority boundaries and high-impact UX/API/architecture choices before dependent work. Ask a small coherent set of decision-changing questions; retain answers already provided. State reversible assumptions for ordinary details and proceed within scope. In unattended mode return the concrete blocking decisions and useful independent findings instead of fabricating them.

Define concise acceptance and a proportionate plan. For meaningful frontend work establish the interaction/surface design with design-interactions before coding; for backend work establish authority, invariants, state/failure and compatibility contracts. Use text, wireframes or mockups to settle the actual uncertainty. No compulsory document template, design approval per screen or complete scaffold is required.

Continue through implementation, tests and review using relevant supporting skills directly. Do not depend on automatically invoking explicit-only task skills or bypass native controls to do so. Use the feature worktree/contribution flow, preserve unrelated edits and keep affected knowledge current. Verify the useful real journey, persisted state, denial and relevant failure cases; for broad UI changes reconcile every affected surface against the intended pattern. Fix material findings within scope and report remaining blockers/limits. End with implemented behavior and actual evidence; create/publish a PR only within the requested flow, and never infer merge/deployment authority. One-shot means one end-to-end request with appropriate questions, not guaranteed quality from a single generation.
