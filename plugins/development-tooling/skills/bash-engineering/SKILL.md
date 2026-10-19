---
name: bash-engineering
description: Create, refactor and audit reliable Bash CLI utilities, build/operations
  scripts and CI action entrypoints with safe argument handling, explicit failure
  semantics, portability, testable side effects and useful documentation.
metadata:
  scope: stack-specific
  invocation: both
  stack: Bash
  version: '1.0'
  role: support
user-invocable: false
---

# Bash engineering

Use Bash for small command orchestration with a clear data and exit-status contract. Move substantial data modeling, API coordination or complex state management to a structured language when that makes maintenance simpler.

## Modes and discovery

- **Interactive/setup:** inspect the required shell version, OS/tools, CLI inputs and operational effects; explain design choices and implement the selected contract.
- **Feature/maintenance:** preserve documented interfaces and callers, correct failure/quoting behavior, and update examples/tests with changes.
- **Recurring review:** audit changed entrypoints and inline CI shell, identify reproducible defects, prepare bounded patches and fixture tests, and retain stable findings. Do not run remote mutations merely to test scripts.

Consult [references/bash-guide.md](references/bash-guide.md). For CI integration also read [references/action-boundaries.md](references/action-boundaries.md). Discover actual callers, local/CI environments, GNU/BSD requirements, secrets, stdout consumers and mutation scope before editing for deeper implementation details when needed.

## Workflow

1. Define arguments/options, defaults, required tools, stdout/stderr, exit codes, no-op behavior and side effects. Unknown/missing/invalid options must fail clearly; `--help` must work without credentials.
2. Keep caller data as data: quote expansions, use arrays and `"$@"`, avoid `eval`/constructed command strings, and use structured tools for JSON/YAML.
3. Implement explicit error checks for critical operations. Use shell options deliberately but account for `errexit`, substitutions, pipelines, conditionals and expected nonzero statuses.
4. Separate discovery/validation from mutation. Provide a truthful dry-run for operational mutations, bounded targets and idempotent/resumable behavior.
5. Scope variables/functions, avoid import-time side effects in libraries, preserve caller working directory and shell state, and use owned temporary paths with cleanup preserving failure status.
6. Make logs useful and sanitized; reserve stdout for machine results when that is the contract. Keep CI grouping/outputs at the wrapper boundary.
7. Validate syntax, ShellCheck and formatter consistency; add focused behavioral tests for argument boundaries, failure propagation, empty selection, no-op/dry-run and externally visible result.
8. Document supported shell/tool versions, usage and failure/recovery semantics. Verify the installed executable/entrypoint and callers, not just a sourced helper function.

## Completion evidence

Deliver scripts/wrapper/docs changes, interface compatibility, actual lint/syntax/test results and untested environment assumptions. For a recurring task, report stable defects and bounded remediation, including no changes needed when supported. Do not call a script safe because `set -euo pipefail` appears at its top.
