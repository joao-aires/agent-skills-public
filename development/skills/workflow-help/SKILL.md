---
name: workflow-help
description: Explain this plugin toolkit, available task entry points and supporting
  skills by SDLC phase or requested outcome. Use for help, command discovery, invocation
  syntax, automation examples and choosing a next development activity without starting
  it.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Workflow help

## Explain the next useful activity

Read [task guidance](../../TASKS.md). Use its task catalogue and the client's observed skill/plugin inventory when available. If the stopping point is unclear, distinguish product direction, design/plan, implementation and assessment. Explain how to seek product discovery and prioritization expertise for an unresolved product problem, or develop when working software is requested; reuse accepted context for a defined feature or defect.

1. Choose the activity whose stopping point matches the request. Explain what the user will have afterward: a product decision, requirements, a design, working code, or an assessment. This is more useful than presenting every activity as a compulsory sequence.
2. Describe the expertise that would help with that work and identify an actual matching skill only after observing its availability. Explain which guidance supports the activity without expanding its scope.
3. Give one or two copyable requests using syntax supported by the client. Include enough context to show the intended outcome and stopping point.


## Explain availability and action boundaries

Distinguish installed/observed skills and tools from this package's catalogue and optional bundles; do not claim a tracker, MCP, browser or credential is available without evidence.

- Explain plugin-qualified commands where the client supports them, otherwise plain-language invocation; do not invent a universal alias or shell flag parser. The client's built-in help is separate.
- Cover explicit user/automation starts versus supporting guidance, interactive questions versus unattended blockers, and the current action policy.
- Help is read-only: do not run setup, probes, tests, installs, create schedules or begin the suggested activity.
- Link the usage/SDLC guides through their published URLs when useful.

A specialist can also be requested directly when available; selecting a discipline does not start a full lifecycle. Recommend the next activity without firing explicit-only skills, probing accounts or beginning work. Preserve the difference between catalogue entries and observed availability.
