---
name: cli-development
description: >-
  Expertise and methods for CLI design. Design or review a command-line application's public
  surface: command grammar, input precedence, streams and exit codes, interactivity, help and
  completion, portability, packaging, updates and compatibility. Use when shaping a new CLI or
  changing an existing one, independent of the implementation language. It informs the
  activity that composes it; that activity owns the decision and stopping point.
metadata:
  kind: method
  domain: tooling
  phase: design
  scope: generic
  invocation: both
user-invocable: true
---

# CLI development

A command-line application is an interface with several kinds of caller at once: a person at a terminal, a script that consumes its stdout, a CI job with no TTY, and another program that depends on its exit status. Design the surface around those callers rather than around the implementation language or the first convenient parser.

This skill owns the design and review of that surface. It does not own shell script implementation: `bash-engineering` covers quoting, argument arrays, `errexit`/`pipefail`, Bash portability and side-effect safety. When the CLI is a Bash program, both apply — this skill decides what the command means to a caller, and that skill keeps the implementation honest. It also does not own the software type: `library-cli` in the artifact system lists the evidence a design record must show for a published package, SDK or command-line tool. This skill supplies the method and review criteria for the command surface; it does not add a software type or replace that evidence list.

Exact conventions belong to their authorities: [clig.dev](https://clig.dev/) for human-facing behavior, [POSIX utility conventions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) and [exit status rules](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_08_02) for Unix interoperation, [GNU long options](https://www.gnu.org/prep/standards/html_node/Option-Table.html) for spelling, [XDG base directories](https://specifications.freedesktop.org/basedir-spec/latest/) for Unix-like storage, [Semantic Versioning](https://semver.org/) for compatibility vocabulary, and package-manager documentation for installation ([PyPA entry points](https://packaging.python.org/en/latest/specifications/entry-points/), [npm `bin`](https://docs.npmjs.com/cli/configuring-npm/package-json#bin), [`go install`](https://go.dev/ref/mod#go-install), plus the OS package format you ship). Read them for exact syntax; use this skill for what the caller receives and how you prove it.

## Reading path

- Review a surface or a change: [contract checklist](references/cli-contract-checklist.md).
- Decide streams, JSON, errors and status: [output and exit codes](references/output-and-exit-codes.md).
- Choose channels, updates, platform claims or deprecation: [packaging and compatibility](references/packaging-and-compatibility.md).
- Adjacent: `library-cli` for required evidence, `bash-engineering` for shell implementation, `test` when installed for the verification method, `guide-compatibility-matrix` for tested combinations.

## Frame the surface

Establish the primary consumer (interactive human, script or CI job, or another program consuming structured output), the job the command supports, and the context: single command or command tree, one-shot, long-running or stateful, local or networked, read-only or mutating, and whether failure can leave partial state.

The executable name, command tree, flags, output and exit status are public API even when the project is small. Record what a consumer would notice, scaled to the change: a local flag addition needs a short note; a new command tree, channel or compatibility policy needs a design proposal. Prefer one recognizable job per command; subcommands are appropriate when related operations share identity, configuration, help and storage, not as a way to avoid choosing a default. Do not let a parser library's defaults become the interface by accident — the framework may generate help, completion and errors, but the tool owns the names, defaults and behavior.

## Command grammar and naming

Choose one grammar and keep it consistent across the tool:

```
tool [global flags] <noun> <verb> [flags] [operands]
tool [global flags] <verb> [flags] [operands]
```

Noun-verb (`tool project create`) reads well for object-oriented tools; verb-noun (`tool create-project`) is flatter and easier to complete for small tools. Either works; mixing both, or using a different verb for the same operation, makes the tool feel larger and less predictable than it is.

- Use the same verbs for the same operations across objects (`list`, `get`, `create`, `update`, `delete`) and limit depth to what a user can remember — three levels is usually enough, then prefer flags or a config file.
- Treat aliases and abbreviated commands as compatibility commitments. Add them deliberately and document them; never reuse an old name for a different meaning.
- Prefer flags to ambiguous positionals. One positional type is usually fine (`tool delete <name>`); two different positional types are suspect; a variadic list of one type is fine.
- Give every flag a long form and a short form only for a frequent flag. Keep conventional spellings (`--help`, `--version`, `--json`, `--output`, `--force`, `--dry-run`, `--quiet`, `--verbose`, `--no-input`, `--no-color`, `--config`) and let the authorities above settle exact syntax.
- Support `--` as the end of option parsing, especially for pass-through commands and dash-leading operands, and preserve everything after it as data. Make global flags work before and after the subcommand where the parser permits; if placement matters, document it.
- Treat unknown flags, subcommands and excess operands as usage errors: usage on stderr, nonzero exit, no mutation. Decide repeated-flag (`last wins`, accumulate, reject) and optional-value semantics explicitly, preferring an enum such as `--color=auto|always|never` over an ambiguous optional value.
- Running with no subcommand lists commands or shows concise help; it must not silently choose a destructive default.

## Inputs, configuration and precedence

Resolve values in a documented order:

```
flags > environment > project config > user config > defaults
```

An explicit `--config <path>` replaces config discovery rather than acting as another lower layer. If flags and environment still override that file, say so. A missing explicit path is an error, not a silent fallback to defaults.

- Discover project configuration from the working directory upward to a clear boundary such as the repository root; do not read unrelated parent directories or remote configuration without saying so.
- Store user configuration, data, state and cache in the platform's conventional locations — XDG base directories on Unix-like systems, and the platform's documented equivalents on Windows and macOS. Do not invent a dot-directory layout.
- Use a stable environment prefix (`TOOL_...`) and document each variable. Environment values are strings; validate and coerce them as you do flags. Avoid hidden environment behavior that changes a command's meaning; `NO_COLOR`, `TERM`, `CI` and `TOOL_*` are the exceptions you document.
- Define merge behavior per key and per file (replace, merge, append, reject), and decide what an empty value, an unset key and an explicit null mean. "It depends on the format" is not a contract.
- Provide a way to inspect effective configuration with secrets redacted, such as `tool config show`. Write configuration only on an explicit command: atomic replacement, preserved permissions, owner-only credential files, and no rewriting of unrelated keys or comments.
- A non-interactive run must not depend on a value that only a prompt can supply. If a required value is missing, fail with the flag or environment variable that provides it.

Do not read secrets from flags or positionals: they appear in process listings and shell history. Accept them through a protected file, stdin, an OS keychain or a credential helper, and offer `--password-file`-style options where a file is appropriate. Document the residual exposure of environment variables.

## Streams and output

- `stdout` carries the requested result: records, a rendered report, or the JSON document. It must remain usable when piped.
- `stderr` carries diagnostics, warnings, progress, prompts and human hints. Logs must not contaminate a result stream, and not every stderr line is an error.
- A `--json` mode emits one valid JSON document on success, or one JSON Lines record per item for streams. Keep field names, types and nesting stable; add optional fields rather than renaming or retyping existing ones.
- Keep machine output locale-independent: UTF-8, ISO 8601 timestamps in UTC, decimal points as `.`, stable identifiers as strings, and no translated field names.
- TTY detection changes presentation, not meaning: color, progress, pager and column layout may differ between a terminal and a pipe; the data set and exit status must not.
- Disable color when the relevant stream is not a TTY, when `NO_COLOR` is set and non-empty, when `TERM=dumb`, or when `--no-color` is passed; respect `--color=always` only where the caller asked. Use a pager only on a TTY.
- Emit one record per line in plain modes so `grep`, `awk` and `wc` behave predictably, and support `-` for stdin or stdout only where documented. Handle a closed downstream pipe without a stack trace: stop writing, clean up owned resources, exit with the documented status.
- With `--json`, choose one contract for structured errors and keep it. A JSON error document on stdout plus a short human hint on stderr is defensible because the command's product is a JSON document; structured errors on stderr are also defensible. Inconsistency between commands is not.
- Exit status carries meaning: `0` only when the requested effect is true, usage errors distinguishable from operational failure, and shell-reserved values (`126`, `127`, `128 + signal`) left to the shell. Keep application codes in the portable range and treat a change to any status as a compatibility change.

Read [output and exit codes](references/output-and-exit-codes.md) for the stream, JSON, error and status contract.

## Interaction, progress and cancellation

Prompt only when `stdin` is an interactive terminal and the command is genuinely interactive. A prompt is an affordance, never the only way to supply a required value.

- Provide `--no-input`. In a non-interactive run, fail with the flag or environment variable that supplies the missing input, rather than waiting or guessing.
- Confirm consequential actions according to severity. Mild local actions may need no prompt; remote or bulk changes usually do; destructive actions should require typing a name or passing an explicit `--confirm=<name>`, so the operation stays scriptable but is hard to trigger by accident.
- Support `--dry-run` for consequential operations and make it truthful: reads and planning, no mutations. A dry run that writes a cache or creates a lock in the target system is not a dry run.
- Read passwords without echo and never repeat a secret in an error, log, progress line or crash report.
- Send progress to `stderr`, only when that stream is a TTY, and throttle updates; emit plain stage lines in CI. Provide `--no-progress` and let `--quiet` suppress nonessential output.
- Handle `SIGINT` and `SIGTERM`: stop accepting new work, cancel or wait for children, close files, remove owned temporary paths, say whether partial effects were rolled back, are resumable, or need reconciliation, and exit with the conventional `128 + signal` status (`130`, `143`). A second interrupt should exit promptly; cleanup after `SIGKILL` is impossible, so durable state needs recovery rather than a trap.

## Help, version and discovery

Help is part of the product, not a generated afterthought. Support `tool`, `tool --help`, `tool -h`, `tool help`, `tool help <command>` and `tool <command> --help` where the grammar allows; `--help` must work without configuration, credentials or network access.

- Missing required arguments show concise usage and exit nonzero; an explicit help request shows the full page and exits `0`.
- Lead with examples, then the common commands and flags, then the complete list. Include the config and environment variables a user needs, a support or documentation link, and exit-status meanings where they are not obvious.
- `--version` prints one stable line with the product version and, where useful, the build revision and target platform. No update check or telemetry during `--help` or `--version`.
- Generate completion from the same command definition as help, for the shells you claim: subcommands, flags, enum values and file paths, side-effect free and silent on stdout. Document installation and test the generated script.
- Make errors actionable: what failed, why, and the command or flag that fixes it. Use a stable error code when callers need one, and keep raw stack traces behind `--debug` or a debug environment variable.

## Portability and delivery

State supported operating systems, architectures, runtimes and shells, and test the combinations you claim. "Cross-platform" without a tested matrix is a wish.

- Use platform path APIs and conventional data directories. Do not assume `/`, a case-sensitive filesystem, a writable current directory, an executable bit, a POSIX shell or a `HOME`.
- Account for behavior that differs: Windows `PATHEXT`, reserved device names, long paths and Ctrl-C; macOS signing/notarization where the channel requires it; Linux libc and static-linking expectations. In containers assume no TTY, a minimal `PATH`, possibly no `HOME` and a non-root user.
- Set `LC_ALL=C` (or equivalent) for subprocesses whose output you parse. Never parse localized human output as a data contract.

Prefer the distribution channel the consumer already uses: a language package with a proper console script and declared runtime range, a standalone binary with per-platform archives, checksums and signatures, or an OS package manager that owns installation and upgrades. A container image suits a self-contained runtime, not a small developer tool's only path.

- Do not make an unverified `curl | sh` the primary install. If you offer one, pin a version, verify a checksum or signature, avoid `sudo`, and document the manual alternative.
- Install completion, man pages and license notices with the binary. Do not edit shell startup files without consent; print the `PATH` instruction instead.
- Prefer package-manager updates to self-update. If the tool updates itself, verify signed metadata, replace atomically, keep a rollback path, avoid `sudo`, and require an explicit command or opt-in. Never update during an ordinary command, in CI, or without a way to disable the check.
- Version the surface with a documented scheme. Removing or renaming a command, flag, alias or output field, changing a default, changing an exit code or raising the minimum runtime is breaking. Deprecate on stderr with the replacement and removal version, keep the old behavior for the stated window, and remove it only in a major release.

Read [packaging and compatibility](references/packaging-and-compatibility.md) for channel choice, platform evidence, update models and deprecation mechanics.

## Verify the surface

Test the built artifact as a subprocess with a controlled environment, not only the parser's unit tests: invoke the installed entry point with a temporary `HOME`, config directories and working directory. Use exact assertions for machine output and exit codes; normalize human prose, timings and ANSI before comparing snapshots, and use a pseudo-terminal for prompts and progress paired with a piped-stdin test that must not prompt.

- help and version without configuration or credentials;
- each main command with its missing and invalid inputs, and the documented failure path;
- precedence and config discovery, including an explicit path, a missing file and malformed content;
- stdout cleanliness, JSON validity and schema stability, and stderr diagnostics;
- exit status for success, usage errors, operational failure and partial failure;
- TTY versus pipe behavior, prompt refusal without a TTY, and `--no-input`;
- progress suppression, color opt-out, a closed pipe, and SIGINT/SIGTERM cleanup with the documented partial-state behavior;
- generated completion per claimed shell;
- clean install, upgrade, downgrade or rollback, and uninstall in a clean environment;
- secret redaction in output, logs and crash reports.

Record untested platforms as unsupported rather than implying they work.

## Completion evidence

Deliver the accepted surface: grammar and names, input precedence, stream and exit contract, interaction behavior, help and completion, distribution and update policy, and compatibility/deprecation policy. Link the completed [contract checklist](references/cli-contract-checklist.md) where a review record needs item-level evidence.

Report what was designed, implemented and verified separately: process-level test results, a clean-install or invocation result at the claimed entry point, generated help and completion samples when they changed, and the platforms actually exercised. A local `--help` run does not establish packaging, Windows behavior or upgrade safety, and tests, a version flag or a wrapper installer are not by themselves a compatibility claim.
