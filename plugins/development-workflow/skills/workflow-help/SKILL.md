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

Read [task guidance](../../TASKS.md). Use its task catalogue and the client's observed skill/plugin inventory when available. Explain what to use for the user's current phase/outcome, give one or two copyable examples and state expected results/side effects. If no context is given, offer develop for a rough idea or the SDLC task menu for a specific phase.

Distinguish installed/observed skills and tools from this package's catalogue and optional bundles; do not claim a tracker, MCP, browser or credential is available without evidence. Explain plugin-qualified commands where the client supports them, otherwise plain-language invocation; do not invent a universal alias or shell flag parser. The client's built-in help is separate. Cover explicit user/automation starts versus supporting guidance, interactive questions versus unattended blockers, and the current action policy. Help is read-only: do not run setup, probes, tests, installs, create schedules or begin the suggested activity. Link the usage/SDLC guides through their published URLs when useful.
