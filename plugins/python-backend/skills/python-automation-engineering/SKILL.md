---
name: python-automation-engineering
description: "Design, implement, review and maintain useful Python operational automations and reporting tools with ergonomic CLIs, typed boundaries, reproducible projects, complete API collection, resumable mutations and verified outcomes."
metadata:
  scope: stack-specific
  invocation: both
  stack: Python
  version: "1.0"
---

# Python automation engineering

Build a tool other people and unattended workers can run, understand and recover. Automating a command is worthwhile when it reduces toil or improves consistency without concealing partial failure.

## Modes and discovery

- **Interactive/setup:** identify the user's operational decision/problem, consumers, frequency, inputs/outputs, API privileges and success criteria; implement the simplest maintainable tool.
- **Feature/maintenance:** preserve CLI/output contracts, local project manager and runtime, improve the affected boundaries, tests and documentation.
- **Recurring review:** inspect changed code/dependencies and prior run evidence, identify reproducible correctness/usability gaps, prepare bounded fixes and fixtures, and maintain stable findings. Run against live systems only within the configured read/mutate policy.

Consult [references/automation-guide.md](references/automation-guide.md). Discover the nearest README/pyproject/lock/entrypoint in multi-tool repositories; do not assume a global Python version or migrate dependency managers just for consistency for deeper implementation details when needed.

## Workflow

1. Define intended operational value, target/selection, source completeness, user/machine output, exit codes, mutation/recovery model and ownership.
2. Use a reproducible local project with supported Python, declared dependencies/dev checks and a documented entrypoint. Keep setup/help independent of credentials and remote side effects.
3. Separate CLI/config validation, orchestration, pure planning/transformations, API/I/O clients and reporting. Use typed models at boundaries; validate external data deliberately.
4. Implement finite timeouts, correct pagination including nested collections, safe retry classification, bounded concurrency and explicit partial-data/error states. Manage client lifetimes.
5. Separate read/plan/apply, truthful dry-run, deterministic selection, stable identity and rechecked preconditions. Make retry/rerun/cancellation resumable and avoid duplicate tickets or unintended deletes.
6. Produce versioned structured results with provenance/completeness, UTC-aware timestamps and useful summaries; write exports atomically and protect sensitive content.
7. Test contracts: no-op, invalid input, missing credentials, pagination, rate-limit/timeouts, partial failures, repeated run, conflict and dry-run having no writes. Test the packaged CLI, not only a helper.
8. Document quick start, exact inputs/defaults, permissions, output/limitations, automation/scheduling examples and recovery. Measure the intended value and maintenance cost without claiming causality from correlations.

## Completion evidence

Deliver project/code/docs changes, tests/lint/type/package or CLI smoke checks appropriate to the change, data/mutation completeness and actual outcome evidence. Distinguish a configured tool, local fixture verification and live verified operation. “No candidates” is not equivalent to “API collection failed.”
