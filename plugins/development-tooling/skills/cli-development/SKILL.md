---
name: cli-development
description: >-
  Design or review a command-line application's public surface: command grammar,
  input precedence, streams and exit codes, interactivity, help and completion,
  portability, packaging, updates and compatibility. Use when shaping a new CLI or
  changing an existing one, independent of the implementation language.
metadata:
  kind: method
  origin: local
  pack: technical
  domain: tooling
  phase: design
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# CLI development

A command-line application is an interface with several kinds of caller at once: a person at a terminal, a script that consumes its stdout, a CI job with no TTY, and another program that depends on its exit status. Design the surface around those callers rather than around the implementation language or the first convenient parser.

This skill owns the design and review of that surface. It does not own shell script implementation: `bash-engineering` covers quoting, argument arrays, `errexit`/`pipefail`, Bash portability and side-effect safety. When the CLI is a Bash program, both apply — this skill decides what the command means to a caller, and that skill keeps the implementation honest.

It also does not own the software type. `library-cli` in the artifact system lists the evidence a design record must show for a published package, SDK or command-line tool. This skill supplies the method and review criteria for the command surface; it does not add a software type or replace that evidence list.

## Reading path

| Need | Read |
| --- | --- |
| Review a command surface before implementation | [Contract checklist](references/cli-contract-checklist.md) |
| Decide stream, JSON, error and exit-code behavior | [Output and exit codes](references/output-and-exit-codes.md) |
| Choose distribution, updates, platform claims and deprecation | [Packaging and compatibility](references/packaging-and-compatibility.md) |
| Required evidence for a library/CLI component | `library-cli` software type |
| Shell implementation and failure propagation | [Bash engineering](../bash-engineering/SKILL.md) |
| Verification method and evidence boundaries | `test` |
| Compatibility claims and tested combinations | `guide-compatibility-matrix` |

## Modes and scope

| Request | Work |
| --- | --- |
| Design a new CLI | Frame the consumer, choose the grammar, decide input precedence, streams, exit codes, interaction, discovery and delivery, then record the accepted surface. |
| Change an existing CLI | Preserve the documented surface where possible; decide whether the change is additive or breaking; update help, completion, tests and compatibility notes together. |
| Review a CLI | Apply the [contract checklist](references/cli-contract-checklist.md), observe the built executable where possible, and report findings with the evidence boundary. |

Do not let a parser library's defaults become the interface by accident. The framework can generate help, completion and errors, but the tool still owns the names, defaults and behavior a caller depends on.

## Frame the surface

Establish the primary consumer, the task the command supports and the context it runs in:

- an interactive human, a script or CI job, or another program consuming structured output;
- a single-command utility or a multi-command tool;
- a one-shot operation, a long-running operation, or a stateful tool with configuration and cached data;
- local-only or networked, read-only or mutating, and whether failure can leave partial state.

The executable name, command tree, flags, output and exit status are public API even when the project is small. Record the decisions that a consumer would notice. Scale the record to the change: a local flag addition needs a short note; a new command tree, distribution channel or compatibility policy needs a design proposal.

Prefer one recognizable job per command. Subcommands are appropriate when related operations share identity, configuration, help and storage. Do not create a command tree to avoid choosing a default.

## Command grammar and naming

Choose one grammar and keep it consistent across the tool:

```
tool [global flags] <noun> <verb> [flags] [operands]
tool [global flags] <verb> [flags] [operands]
```

Noun-verb (`tool project create`) reads well for object-oriented tools; verb-noun (`tool create-project`) is flatter and easier to complete for small tools. Either works. Mixing both, or using a different verb for the same operation, makes the tool feel larger and less predictable than it is.

- Keep command names lowercase, short and pronounceable. POSIX's two-to-nine-character convention is a portability guide, not a hard limit for a modern product name; the practical constraint is typing, collision and shell completion.
- Limit depth to what a user can remember. Three levels is usually enough. Beyond that, prefer flags or a config file.
- Use the same verbs for the same operations across objects: `list`, `get`, `create`, `update`, `delete`, `apply`, `plan`. Do not alternate `remove`, `rm`, `destroy` and `delete` for the same effect.
- Treat aliases and abbreviated commands as compatibility commitments. Add them deliberately and document them; never reuse an old name for a different meaning.
- Prefer flags to ambiguous positional arguments. One positional type is usually fine (`tool delete <name>`); two different positional types are suspect; a variadic list of the same type is fine.
- Give every flag a long form. Add a short form only for a frequent flag at the level where it applies, so the short namespace stays useful.
- Reserve `-h`/`--help` for help and `--version` for version. Decide whether `-v` means verbose or version, not both. Reserve `-q`/`--quiet` for reduced output and `-n`/`--dry-run` for a truthful no-mutation preview.
- Use standard names where a convention exists: `--json`, `--output`, `--force`, `--dry-run`, `--quiet`, `--verbose`, `--no-input`, `--no-color`, `--config`.
- Support `--` as the end of option parsing, especially for pass-through commands and operands that may begin with `-`. Preserve everything after it as data.
- Make global flags work before and after the subcommand where the parser permits. If placement matters, document it; silent rejection of the common form is a usability defect.
- Treat unknown flags, unknown subcommands and excess operands as usage errors: show usage on stderr, exit nonzero and perform no mutation. A close match may be suggested, but never silently reinterpret an invalid command as a different one.
- Decide repeated-flag semantics (`last wins`, accumulate, reject) and optional-value semantics explicitly. Prefer an enum such as `--color=auto|always|never` over an ambiguous optional value.
- Running the tool with no subcommand should list commands or show concise help. It must not silently choose a destructive default.

## Inputs, configuration and precedence

Resolve values in a documented order:

```
flags > environment > project config > user config > defaults
```

An explicit `--config <path>` replaces config discovery rather than acting as another lower layer. If flags and environment still override that file, say so. A missing explicit path is an error, not a silent fallback to defaults.

- Discover project configuration from the working directory upward to a clear boundary such as the repository root. Do not read unrelated parent directories or remote configuration without saying so.
- Store user configuration, data, state and cache in the platform's conventional locations. On Unix-like systems follow the XDG base directories; use `%APPDATA%` and `%LOCALAPPDATA%` on Windows and `~/Library/Application Support`/`~/Library/Caches` on macOS.
- Use a stable environment prefix (`TOOL_...`) and document each variable. Environment variables are strings; validate and coerce them the same way as flags. Avoid hidden environment behavior that changes a command's meaning; `NO_COLOR`, `TERM`, `CI` and `TOOL_*` are the exceptions you document.
- Define merge behavior per key and per file: replace, merge, append or reject. Decide what an empty value, an unset key and an explicit null mean. "It depends on the format" is not a contract.
- Provide a way to inspect effective configuration with secrets redacted, such as `tool config show`. This is often the fastest support diagnostic.
- Write configuration only on an explicit command. Use atomic replacement, preserve file permissions and keep credential files private (mode `0600` on Unix). Do not rewrite unrelated user keys or comments merely because the tool parsed the file.
- A non-interactive run must not depend on a value that only a prompt can supply. If a required value is missing, fail with the flag or environment variable that provides it.

Do not read secrets from flags or positional arguments: they appear in process listings and shell history. Accept them through a protected file, stdin, an OS keychain or a credential helper, and offer `--password-file`-style options where a file is appropriate. Document the residual exposure of environment variables.

## Streams and output

- `stdout` carries the requested result: records, a rendered report, or the JSON document. It must remain usable when piped.
- `stderr` carries diagnostics, warnings, progress, prompts and human hints. Logs must not contaminate a result stream.
- A `--json` mode emits one valid JSON document on success, or one JSON Lines record per item for streams. Keep field names, types and nesting stable. Add optional fields rather than renaming or retyping existing ones.
- Keep machine output locale-independent: UTF-8, ISO 8601 timestamps in UTC, decimal points as `.`, stable identifiers as strings, and no translated field names.
- TTY detection changes presentation, not meaning. Color, progress animation, pager use and column layout may differ between a terminal and a pipe; the data set and exit status should not.
- Disable color when the relevant stream is not a TTY, when `NO_COLOR` is set and non-empty, when `TERM=dumb`, or when `--no-color` is passed. Respect `--color=always` only where the caller explicitly asks for it.
- Use a pager only when the output stream is a TTY. Send one record per line in table or plain modes so `grep`, `awk` and `wc` behave predictably.
- Support `-` for stdin or stdout only where the command documents it. If stdin is the primary input and is an interactive terminal, show help or a clear hint instead of hanging.
- Handle a closed downstream pipe without a stack trace. Stop writing, clean up owned resources and exit with the documented status.
- With `--json`, choose one contract for structured errors and keep it. The recommended default is a JSON error document on stdout plus a short human hint on stderr, because the command's product is a JSON document. Structured errors on stderr are also defensible; inconsistency between commands is not.

Read [output and exit codes](references/output-and-exit-codes.md) for the full stream, JSON and status contract.

## Interaction, progress and cancellation

Prompt only when `stdin` is an interactive terminal and the command is genuinely interactive. A prompt is an affordance, never the only way to supply a required value.

- Provide `--no-input` to disable all prompts. In a non-interactive run, fail with the flag or environment variable that supplies the missing input.
- Confirm consequential actions according to severity. Mild local actions may need no prompt; remote or bulk changes usually do; destructive actions should require typing a name or passing an explicit `--confirm=<name>` so the operation remains scriptable but hard to trigger by accident.
- Support `--dry-run` for consequential operations, and make it truthful: perform reads and planning, no mutations. A dry run that writes a cache or creates a lock in the target system is not a dry run.
- Read passwords without echo and never repeat a secret in an error, log, progress line or crash report.
- Send progress to `stderr`, only when that stream is a TTY, and throttle updates. Emit a plain stage line in CI instead of cursor animation. Provide `--no-progress` and let `--quiet` suppress nonessential output.
- Handle `SIGINT` and `SIGTERM`: stop accepting new work, cancel or wait for children, close files, remove owned temporary paths and exit with the conventional `128 + signal` status (`130` for SIGINT, `143` for SIGTERM). Say whether partial effects were rolled back, are resumable, or need reconciliation.
- A second interrupt should exit promptly. Cleanup after `SIGKILL` is impossible; persistent state needs recovery rather than a trap.

## Help, version and discovery

Help is part of the product, not a generated afterthought.

- Support `tool`, `tool --help`, `tool -h`, `tool help`, `tool help <command>` and `tool <command> --help` where the grammar allows. `--help` must work without configuration, credentials or network access.
- When required arguments are missing, show concise usage and exit nonzero. When help is explicitly requested, show the full page and exit `0`.
- Lead with examples. Put the common commands and flags first, then the complete list. Include the config and environment variables a user needs, a support or documentation link, and the exit-code meanings if they are not obvious.
- `--version` prints one stable line with the product version and, where useful, the build revision and target platform. Do not perform an update check or telemetry during `--help` or `--version`.
- Generate shell completion from the same command definition as help, for the shells you claim: bash, zsh, fish and PowerShell. Complete subcommands, flags, enum values and file paths; keep completion side-effect free and silent on stdout. Document installation and test the generated script.
- Make errors actionable: state what failed, why, and the command or flag that fixes it. Use a stable error code when callers need one. Keep raw stack traces behind `--debug` or a debug environment variable.

## Portability and delivery

State supported operating systems, architectures, runtimes and shells, and test the combinations you claim. "Cross-platform" without a tested matrix is a wish.

- Use platform path APIs and conventional data directories. Do not assume `/`, a case-sensitive filesystem, a writable current directory, an executable bit, a POSIX shell or a `HOME`.
- On Windows, account for `PATHEXT`, reserved device names, long paths, case-insensitive filesystems and different Ctrl-C behavior. Do not emit ANSI sequences unless the console supports them or the caller opted in.
- On macOS, sign and notarize distributed binaries where the delivery channel requires it; respect the platform cache and support directories.
- On Linux, state the libc expectation (glibc or musl) and whether the artifact is static. Do not assume systemd, a TTY, a package manager or a specific init system.
- In containers, assume no TTY, a minimal `PATH`, possibly no `HOME`, and a non-root user. `--no-input` and predictable config paths matter more there.
- Set `LC_ALL=C` (or an equivalent) for subprocesses whose output you parse. Never parse localized human output as a data contract.

Prefer the distribution channel the consumer already uses. A language package should install a proper console script and declare its runtime range; a standalone binary should publish per-platform archives with checksums and signatures; an OS package manager should own installation and upgrades. A container image is appropriate for a self-contained runtime, not as the only way to use a small developer tool.

- Do not make an unverified `curl | sh` the primary install path. If you offer one, pin a version, verify a checksum or signature, avoid `sudo`, and document the manual alternative.
- Install completion, man pages and license notices with the binary. Do not edit shell startup files without consent; print the `PATH` instruction instead.
- Prefer package-manager updates to self-update. If the tool updates itself, verify signed metadata, replace the executable atomically, keep a rollback path, avoid `sudo`, and require an explicit command or opt-in. Never update during an ordinary command, in CI, or without a way to disable the check.
- Version the surface with a documented scheme. Removing or renaming a command, flag, alias or output field, changing a default, changing an exit code or raising the minimum runtime is breaking. Deprecate on stderr with the replacement and removal version, keep the old behavior for the stated window, and remove it only in a major release.

Read [packaging and compatibility](references/packaging-and-compatibility.md) for distribution choices, platform matrices, update models and deprecation mechanics.

## Verify the surface

Test the built artifact as a subprocess with a controlled environment, not only the argument parser's unit tests. Invoke the installed entry point with a temporary `HOME`, config directories and working directory.

Cover the behaviors the surface promises:

- help and version without configuration or credentials;
- each main command, its missing and invalid inputs, and the documented failure path;
- the precedence chain and config discovery, including an explicit config path, a missing file and malformed content;
- stdout cleanliness, JSON validity and schema stability, and stderr diagnostics;
- exit status for success, usage errors, operational failures and partial failure;
- TTY versus pipe behavior, prompt refusal without a TTY and `--no-input`;
- progress suppression, color opt-out and a closed pipe;
- SIGINT/SIGTERM cleanup and the documented partial-state behavior;
- generated completion for each claimed shell;
- clean install, upgrade, downgrade or rollback, and uninstall in a clean environment;
- secret redaction in output, logs and crash reports.

Use exact assertions for machine output and exit codes; normalize human prose, timings and ANSI before comparing snapshots. Use a pseudo-terminal for prompts and progress, and pair it with a piped-stdin test that must not prompt. Record untested platforms as unsupported rather than implying they work.

## Sources and fit

These sources inform the method; the wording here is original.

- [Command Line Interface Guidelines](https://clig.dev/) — human-first design, composability, help, output, errors, arguments, interactivity and subcommands. The main fit for the human-facing surface.
- [POSIX.1-2024, Utility Conventions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) — option syntax, option-arguments, operands, `--` and option ordering. The fit for grammar that interoperates with Unix callers.
- [POSIX.1-2024, Exit Status for Commands](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_08_02) — the shell's use of `126`, `127` and the reserved range above `125`. The fit for not misusing status values.
- [GNU Coding Standards, Command-Line Interfaces](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html) and the [long-option table](https://www.gnu.org/prep/standards/html_node/Option-Table.html) — `--help`, `--version`, long options and shared option names. The fit for conventional flag spelling.
- [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46) — flags over ambiguous args, stream separation, help and version, prompting, tables, startup speed and XDG paths. The fit for product-oriented CLI judgment.
- [The Twelve-Factor App, III. Config](https://12factor.net/config) — configuration in the environment for deploy-varying values. The fit for why environment is a layer, not the whole precedence chain; flags still win for a one-off invocation.
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) — config, data, state and cache locations on Unix-like systems. The fit for not inventing a dot-directory layout.
- [NO_COLOR](https://no-color.org/) — the conventional color opt-out. The fit for respecting a caller's explicit presentation choice.
- [PyPA entry points specification](https://packaging.python.org/en/latest/specifications/entry-points/) — `console_scripts` packaging. The fit for Python command installation.
- [npm `package.json` `bin`](https://docs.npmjs.com/cli/configuring-npm/package-json#bin) — command shims for Node packages. The fit for JavaScript distribution.
- [Go modules reference: `go install`](https://go.dev/ref/mod#go-install) — versioned binary installation. The fit for Go distribution.
- [Semantic Versioning 2.0.0](https://semver.org/) — a shared vocabulary for compatible and breaking surface changes. The fit for the versioning and deprecation rules.

## Completion evidence

Deliver the accepted surface: command grammar and names, input precedence, stream and exit contract, interaction behavior, help and completion, distribution and update policy, and compatibility/deprecation policy. Link the completed [contract checklist](references/cli-contract-checklist.md) where a review record needs item-level evidence.

Report what was designed, implemented and verified separately. Include process-level test results, a clean-install or invocation result at the claimed entry point, generated help and completion samples when they changed, and the platforms and environments actually exercised. A successful local `--help` run does not establish packaging, Windows behavior or upgrade safety.

Do not claim a CLI is safe or compatible because it has tests, a version flag or a wrapper installer. The claim needs the boundary at which it was observed.
