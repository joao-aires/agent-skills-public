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

Use Bash to orchestrate commands when the inputs, outputs and failure behavior remain easy to follow. Design the script as an interface: establish what its caller supplies, what stdout means, what diagnostics go to stderr, and which exit status signals failure. Preserve those contracts when changing a script used by other commands or CI.

Follow critical commands through failure as carefully as through success. Decide whether the next action is still valid after a command fails and preserve that result through logging and cleanup. Shell options support that design but do not replace explicit reasoning about pipelines, substitutions and expected nonzero statuses. Move substantial data modeling, API coordination or complex state management to a structured language when that makes maintenance simpler.

## Modes and discovery

- **Interactive/setup:** inspect the required shell version, OS/tools, CLI inputs and operational effects; explain design choices and implement the selected contract.
- **Feature/maintenance:** preserve documented interfaces and callers, correct failure/quoting behavior, and update examples/tests with changes.
- **Recurring review:** audit changed entrypoints and inline CI shell, identify reproducible defects, prepare bounded patches and fixture tests, and retain stable findings. Do not run remote mutations merely to test scripts.

Discover actual callers, local/CI environments, GNU/BSD requirements, secrets, stdout consumers and mutation scope before editing. Consult [the Bash guide](references/bash-guide.md) for deeper implementation details; for CI integration also read [action boundaries](references/action-boundaries.md).

## Define the command interface

Establish arguments/options, defaults, required tools, stdout/stderr, exit codes, no-op behavior and side effects. Unknown, missing and invalid options must fail clearly; `--help` must work without credentials. If another program consumes stdout, reserve it for the documented result and send useful sanitized diagnostics elsewhere. Keep CI grouping/outputs at the wrapper boundary so the underlying tool retains a normal CLI contract.

## Preserve data and failure meaning

Pass caller values as arguments without reconstructing them as shell syntax. Quote expansions, use arrays and `"$@"`, avoid `eval`/constructed command strings, and use structured tools for JSON/YAML. This keeps spaces and special characters in a value from changing the operation selected by the script.

Check critical failures explicitly. Account for `errexit`, substitutions, pipelines, conditionals and expected nonzero statuses when deciding what stops execution. Preserve the original failure through diagnostic collection and cleanup so a successful final command cannot conceal the failed operation.

## Control side effects and cleanup

Separate discovery and validation from mutation. Resolve a bounded target set, recheck consequential preconditions and provide a truthful dry-run for operational mutations. Design reruns to identify completed work or resume safely, rather than repeating an ambiguous effect.

Scope variables/functions, avoid import-time side effects in libraries, and preserve caller working directory and shell state. Use owned temporary paths and cleanup that preserves failure status. Cleanup should remove the script's temporary work without deleting unrelated or surviving user data.

## Verify the executable and its callers

Validate syntax, ShellCheck and formatter consistency, then test the behaviors the command promises: argument boundaries, failure propagation, empty selection, no-op/dry-run and the externally visible result. Verify the installed executable/entrypoint and actual callers, not just a sourced helper function.

Document supported shell/tool versions, usage and failure/recovery semantics so a caller can distinguish a completed no-op from a failed attempt.

## Completion evidence

Deliver scripts/wrapper/docs changes, interface compatibility, actual lint/syntax/test results and untested environment assumptions. For a recurring task, report stable defects and bounded remediation, including no changes needed when supported. Do not call a script safe because `set -euo pipefail` appears at its top.
