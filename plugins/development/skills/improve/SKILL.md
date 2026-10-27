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

## Assess opportunities

Use the relevant codebase and history to find a problem that matters in practice. Look for changes that repeatedly touch unrelated modules, expensive operations in an important journey, failures that are difficult to diagnose, inconsistent interactions, or slow and unreliable development checks. Follow the evidence far enough to distinguish a cause from a disliked coding style.

For each worthwhile opportunity, make the proposal assessable:

- Identify who is affected and what evidence shows the problem.
- Explain the bounded change and how improvement would be measured.
- State which existing behavior needs protection.
- Compare likely value with implementation and maintenance cost.

No finding or no worthwhile change is valid. A bare request returns a short prioritized set of proposals rather than rewriting unrelated areas or creating tickets automatically.

## Implement an authorized improvement

A specific requested improvement can authorize bounded implementation. Keep a bare improvement assessment read-only; do not force another approval for routine choices already authorized.

1. Establish a baseline, diagnose the cause and define the desired outcome.
2. Make focused changes within scope. Preserve behavior through incremental refactoring and regression checks.
3. Compare results with the baseline and report the evidence.

Choose the relevant analysis without imposing another process:

| Concern | Examine and use |
| --- | --- |
| UX | Use available integrated interface-design expertise for interaction intent, visual critique and affected-surface consistency against the accepted design. Seek UX-writing expertise separately for consequential copy. Reuse existing decisions for narrow fixes rather than initiating a redesign. |
| Usability evidence | Use available research expertise for a requested study or actual observations. |
| Architecture | Examine responsibilities, dependency direction, ownership, coupling/change hotspots, seams and testability. Use codebase-design/domain-modeling where useful, without forcing deep-module vocabulary, HTML reports or interviews. |

More abstractions are not inherently better. Tracker proposals/creation and live experiments follow the task's explicit scope.
