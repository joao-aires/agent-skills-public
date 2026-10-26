---
name: python-automation-engineering
description: Design, implement, review and maintain useful Python operational automations
  and reporting tools with ergonomic CLIs, typed boundaries, reproducible projects,
  complete API collection, resumable mutations and verified outcomes.
metadata:
  scope: stack-specific
  invocation: both
  stack: Python
  version: '1.0'
  role: support
user-invocable: false
---

# Python automation engineering

Build a tool whose result remains understandable when no person watches it run. Establish what a complete result means, how the tool selects its targets, and what its caller should do after a partial failure. The command's exit status, structured output and human summary should agree about that state.

For API collection, track what was requested, what was actually visited and which part failed. An empty complete collection and an incomplete collection need different results.

For mutations, separate the intended operation from individual attempts so a resumed run can identify completed work, recheck preconditions and avoid repeating effects. Automating a command is worthwhile when it reduces toil or improves consistency without concealing partial failure.

## Modes and discovery

- **Interactive/setup:** identify the user's operational decision/problem, consumers, frequency, inputs/outputs, API privileges and success criteria; implement the simplest maintainable tool.
- **Feature/maintenance:** preserve CLI/output contracts, local project manager and runtime, improve the affected boundaries, tests and documentation.
- **Recurring review:** inspect changed code/dependencies and prior run evidence, identify reproducible correctness/usability gaps, prepare bounded fixes and fixtures, and maintain stable findings. Run against live systems only within the configured read/mutate policy.

Discover the nearest README/pyproject/lock/entrypoint in multi-tool repositories. Preserve its Python version and dependency manager unless migration is in scope. Consult [the automation guide](references/automation-guide.md) for deeper implementation details when needed.

## Design the tool around its operational result

Define the intended value, target selection, source completeness, user/machine output, exit codes, mutation/recovery model and owner. Choose an interface that lets a person inspect the result and an unattended caller determine whether it can continue.

Use a reproducible local project with supported Python, declared dependencies/dev checks and a documented entrypoint. Keep setup/help independent of credentials and remote side effects. Separate CLI/config validation, orchestration, pure planning/transformations, API/I/O clients and reporting where those responsibilities need independent testing. Use typed models at boundaries and validate external data deliberately.

## Collect complete data or describe the gap

Follow pagination through every required collection, including nested results. Record whether all selected targets were visited and preserve errors that leave the result incomplete. Use finite timeouts, bounded concurrency and retry rules that distinguish a transient read failure from a mutation whose result is uncertain. Manage client lifetimes so failed or cancelled runs release resources.

Produce versioned structured results with provenance/completeness, UTC-aware timestamps and useful summaries. Write exports atomically so a consumer cannot mistake a partially written file for a complete result, and protect sensitive content in both exports and diagnostics.

## Make operational changes recoverable

Separate read, plan and apply. Select targets deterministically, show what a dry-run actually inspected, and recheck consequential preconditions before applying a plan. Give work a stable identity so retry, rerun and cancellation can account for completed effects. Avoid duplicate tickets or unintended deletes when the previous attempt ended without a clear response.

Keep the recovery path visible to the caller: which work finished, which work failed and what must be reconciled before continuing. A dry-run must have no writes; it should not claim that an untested remote action succeeded.

## Test and document the shipped interface

Test the packaged CLI as well as its helpers. Cover the relevant no-op, invalid input, missing credentials, pagination, rate-limit/timeouts, partial failure, repeated run, conflict and dry-run contracts. Check that output and exit status agree about completeness.

Document quick start, exact inputs/defaults, permissions, output/limitations, automation/scheduling examples and recovery. Measure the intended value and maintenance cost without claiming causality from correlations.

## Completion evidence

Deliver project/code/docs changes, tests/lint/type/package or CLI smoke checks appropriate to the change, data/mutation completeness and actual outcome evidence. Distinguish a configured tool, local fixture verification and live verified operation. “No candidates” is not equivalent to “API collection failed.”
