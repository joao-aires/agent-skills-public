---
name: improve
description: Assess codebase improvement opportunities or implement a specified improvement
  objective. Use for architecture, performance, reliability, testability, UX consistency
  or developer-experience work; bare invocation discovers prioritized evidence-backed
  opportunities.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Improve

Read [task guidance](../../TASKS.md). Read [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for baseline and verification, [git-contributions](../git-contributions/SKILL.md) for implementation when requested. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

A bare request surveys the relevant codebase/history and surfaces a short list of opportunities with evidence, likely value, scope, risks and verification. Name relevant aspects such as architecture, performance, reliability, UX consistency, tests and developer experience. No finding or no worthwhile change is valid. Return proposals rather than rewriting unrelated areas or creating tickets automatically.

A specific requested improvement can authorize bounded implementation within established scope. Establish a baseline, diagnose the cause, define desired outcomes, make focused changes and compare results; do not force another approval for routine choices already authorized. For UX changes use interaction-design before changing screens and track all affected surfaces. For architecture examine responsibilities, dependency direction, ownership, coupling/change hotspots, seams and testability; use codebase-design/domain-modeling when useful without forcing deep-module vocabulary, HTML reports or interviews. Preserve behavior through incremental refactoring and regression checks; more abstractions are not inherently better. Tracker proposals/creation and live experiments follow the task's explicit scope.
