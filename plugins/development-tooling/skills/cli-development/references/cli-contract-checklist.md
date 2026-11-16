# CLI contract checklist

Use this checklist before implementing a new command surface or when reviewing a change to an existing one. It is a decision aid, not a release form. Mark each item **pass**, **fail**, **not applicable** or **not yet verified**, and name the evidence rather than the intention.

A small local command may pass with a short note for several sections. A published, multi-command or mutating tool should be able to answer every applicable item.

## How to use

1. Establish the primary consumer and the command's job.
2. Walk the sections that the change touches.
3. Turn each failure into a concrete surface change or an explicit limitation.
4. Keep the checklist result with the design record or review, not as a second specification.

## 1. Identity, grammar and naming

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Executable name is intentional | Short, pronounceable, unlikely to collide; matches the package and docs | Install test, `--help` |
| One recognizable job per command | The command's purpose fits in one sentence | Help text |
| Command tree is justified | Subcommands share identity, config or help; not added to avoid a default | Command tree |
| Grammar is consistent | One of noun-verb or verb-noun; same verb for the same operation | Help and completion |
| Depth is bounded | Usually no more than three levels | Command tree |
| Aliases are deliberate | Each alias has a reason and a compatibility owner | Docs and tests |
| No name reuse | A removed command or flag is not reassigned a new meaning | Changelog |
| Bare invocation is safe | Lists commands or shows concise help; never silently mutates | Manual run |

| Decision | Prefer | Avoid |
| --- | --- | --- |
| Single command or subcommands | Single when the tool has one job; subcommands when several related jobs share configuration | A command tree with one leaf, or a catch-all `run` command |
| Noun-verb or verb-noun | The form that matches the object model and completes cleanly | Mixing both in one tool |
| Long or short name | The shortest name users can type without ambiguity | Renaming later without an alias |

## 2. Arguments and flags

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Required inputs are explicit | Missing input produces usage and a nonzero exit | Tests |
| Positional arguments are unambiguous | At most one positional type, or a variadic list of one type | Help synopsis |
| Every flag has a long form | `--output`, not only `-o` | Help |
| Short flags are reserved | `-h` help; `-q` quiet; `-v` has one meaning; `-n` dry-run where meaningful | Help |
| Standard names are used | `--json`, `--force`, `--dry-run`, `--no-input`, `--no-color`, `--config` | Help |
| `--` terminates options | Pass-through and dash-leading operands work | Test |
| Global flags are usable in the documented positions | Both before and after the subcommand where the parser allows | Tests |
| Repeated flags are defined | Last wins, accumulate or reject — documented and tested | Tests |
| Boolean negation is clear | `--color`/`--no-color` or `--color=auto\|always\|never`, not both styles without a rule | Help |
| Unknown input is rejected | Unknown flag, subcommand or excess operand is a usage error with no mutation | Tests |
| Order independence is real | Flag order does not change meaning; operand order does where documented | Tests |

Good:

```
tool deploy --project billing --environment production --wait
tool logs --project billing --follow
tool project create --name billing --owner platform
```

Bad:

```
tool deploy prod billing now
```

The bad form has three positional values with no way to tell which is the environment, which is the project and which is a mode. It also invites an accidental deployment when an argument is omitted.

Good:

```
tool delete --project billing --confirm billing
```

Bad:

```
tool delete billing --yes
```

The second form makes an irreversible remote deletion look like a routine command. The first is scriptable but requires the operator to name the target.

## 3. Configuration and precedence

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Precedence is documented | `flags > environment > project config > user config > defaults` | Docs and tests |
| Explicit config path is defined | `--config` replaces discovery; a missing path is an error | Tests |
| Discovery boundary is defined | Walk stops at a repository or home boundary; no unrelated parents | Tests |
| Environment prefix is stable | `TOOL_*`; every variable documented | Docs |
| Environment values are validated | Same coercion and errors as flags | Tests |
| Merge semantics are defined | Per-key replace/merge/append; empty, unset and null are distinct | Tests |
| Effective config is inspectable | `tool config show` redacts secrets | Manual run |
| Writes are explicit | Only a config command writes; atomic replacement and permissions | Tests |
| No hidden reads | No undeclared file, network or credential lookup | Review |
| Secrets are not flags | File, stdin, keychain or credential helper | Review |

| Decision | Rule |
| --- | --- |
| Project and user config both exist | Define whether the nearer file replaces the farther one or merges key by key. Do not leave it to the parser. |
| Multiple config formats | Prefer one canonical format. If several are accepted, state precedence by file name and do not merge across formats silently. |
| Environment versus flag | Flag wins for the invocation. Environment is for the process context, not for overriding an explicit operator choice. |
| Config versus secret store | Config may name a credential profile; the secret itself belongs in a protected store. |
| Config file is malformed | Fail with the path and the parse error. Do not fall back to defaults unless the user explicitly asked for that. |

Common failure: a tool reads `~/.toolrc`, `./tool.toml`, `TOOL_*` and a flag, but only documents the flag. A user then cannot explain why their explicit `--region` is ignored by a project file that sets an environment-specific region.

## 4. Streams and output

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| stdout is the result | Piping stdout yields only data or the rendered result | Test |
| stderr is diagnostics | Logs, warnings, prompts and progress never enter stdout | Test |
| `--json` is valid | One document, or JSON Lines for record streams | Schema test |
| JSON is stable | Field names and types do not change in a patch or minor release | Schema test |
| Human and machine modes are distinct | `--json`, `--plain` and default human output have documented purposes | Help |
| TTY changes presentation only | Color, progress, pager and width may differ; data and exit status do not | Tests |
| Color can be disabled | Non-TTY, `NO_COLOR`, `TERM=dumb`, `--no-color` | Tests |
| Tables are line-oriented | One record per line; `--plain` available when layout would break parsing | Test |
| Pager is TTY-only | No pager in a pipe or CI | Test |
| `-` is documented | stdin/stdout meaning is explicit; no implicit stdin consumption | Help |
| Closed pipe is handled | No traceback when `tool ... \| head` closes early | Test |
| Encoding is stable | UTF-8; no locale-dependent numbers or dates in machine output | Schema test |

| Output mode | Use when | Must not |
| --- | --- | --- |
| Default human | A person is reading the terminal | Emit a different data contract than `--json` |
| `--plain` | A human table needs stable line-oriented parsing | Include colors, borders or multi-line cells |
| `--json` | A program consumes the result | Include logs, prompts or progress on stdout |
| `--quiet` | Only the result or exit status matters | Hide errors |
| `--verbose`/`--debug` | Diagnosis is requested | Expose secrets or change the result |

Common failure: the default human mode prints a friendly sentence to stdout, while `--json` prints a document. A script that omits `--json` gets prose and fails later. Either keep human output on stdout as the documented default for humans, or make the machine mode the explicit contract and never mix the two.

## 5. Errors and exit status

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Success is `0` | Including a documented no-op or dry run | Tests |
| Usage errors are distinct | Usually `2`; documented if used | Tests |
| General failure is `1` | Operational failure that is not a usage error | Tests |
| App-specific codes are documented | `3`–`125`, stable meaning, not reused | Docs |
| `126`/`127` are not repurposed | Left to shell execution failures | Review |
| Signal status is conventional | `130` for SIGINT, `143` for SIGTERM | Tests |
| Partial failure is nonzero | Per-item results retained; not silently dropped | Test |
| Error message is actionable | What failed, why, and the fixing command or flag | Review |
| Debug output is opt-in | Stack trace only with `--debug` or equivalent | Test |
| Exit code is stable | Not changed without a compatibility note | Changelog |

| Situation | Exit | Why |
| --- | --- | --- |
| Command completed | `0` | The requested effect is true |
| Nothing to do | `0` by default; document a distinct code if callers need one | A no-op is not a failure |
| Invalid flag or operand | `2` (common) | Usage error, no effect |
| Missing credential | `1` or a documented auth code | Operational failure |
| Partial batch failure | Nonzero | The requested whole did not succeed |
| Interrupted | `130`/`143` | Shell convention for signals |
| Shell could not execute | `126`/`127` | Reserved by the shell, not by the tool |

Common failure: using `2` for "configuration changed" or `1` for "no matches". Callers already interpret those values as usage and general failure respectively. Prefer `0` plus a structured `changed` or `matches` field unless a distinct status is part of the documented contract.

## 6. Interaction and cancellation

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Prompt only with a TTY | Piped or CI stdin never blocks on a prompt | PTY and pipe tests |
| Prompt is not required | Every prompted value has a flag or environment alternative | Help |
| `--no-input` disables prompts | Missing input fails with the supplying flag | Test |
| Confirmation matches severity | Remote/bulk/destructive actions require explicit consent | Test |
| Secrets are hidden | No echo, no logging, no argv exposure | Review and test |
| Dry run is truthful | Reads and plans; no target mutation | Test |
| Progress is stderr and TTY-only | CI gets stage lines, not cursor animation | Test |
| Ctrl-C is responsive | New work stops; children and owned temp files handled | Test |
| Partial state is explained | Rolled back, resumable or needs reconciliation | Docs and test |
| Second interrupt exits | No infinite cleanup loop | Manual test |

| Severity | Example | Confirmation |
| --- | --- | --- |
| Mild | Delete one local scratch file named by the user | Usually none; the command name is the consent |
| Moderate | Delete a directory, bulk-update local data, change a remote resource | Prompt when interactive; `--yes` or `--force` in scripts |
| Severe | Delete a remote project, rotate credentials, irreversible bulk migration | Type the target name or pass `--confirm=<name>`; support `--dry-run` |

## 7. Help, version and completion

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| All help paths work | Bare, `-h`, `--help`, `help`, `help <cmd>`, `<cmd> --help` | Tests |
| Help is offline | No config, credential, network or update check | Test |
| Examples come first | Common invocations before the full flag list | Review |
| Version is one line | Version plus revision/platform where useful | Test |
| Version is scriptable | Stable format; `--json` if consumers need fields | Test |
| Completion is generated | Same command definition as help | Generation test |
| Completion covers values | Subcommands, flags, enums, file paths | Shell test |
| Completion is side-effect free | No network, no writes, no stdout noise | Review |
| Support path is visible | Docs or issue URL in top-level help | Review |
| Errors suggest a fix | Correct flag or next command, not just "invalid" | Review |

Good help excerpt:

```
tool project create --help

Create a project and register its owner.

USAGE
  tool project create --name <name> [--owner <team>] [--json]

EXAMPLES
  tool project create --name billing --owner platform
  tool project create --name billing --json

FLAGS
  --name <name>       Project name (required)
  --owner <team>      Owning team (default: current user)
  --json              Print the created project as JSON

ENVIRONMENT
  TOOL_API_URL        API endpoint (default: https://api.example.test/v1)
  TOOL_CONFIG         Config file (default: platform-specific user config)

EXIT STATUS
  0  Project created
  1  API or network failure
  2  Invalid arguments

https://example.test/docs/cli/project-create
```

Bad help excerpt:

```
Usage: tool [options]
```

It does not say what the tool does, which command to run, what the flags mean or where to get help.

## 8. Portability, packaging and compatibility

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Platform claims are bounded | OS, architecture, runtime and shell listed | Compatibility matrix |
| Paths use platform APIs | No hardcoded `/`, `~` or case assumptions | Test |
| Config directories are conventional | XDG, `%APPDATA%`, `~/Library` | Test |
| Windows behavior is tested | `PATHEXT`, long paths, Ctrl-C, no ANSI assumption | CI or explicit unsupported |
| Container behavior is tested | No TTY, minimal PATH, no HOME | Test |
| Install is documented | Registry, binary archive, package manager or container | Docs |
| Uninstall is documented | Files and config removal | Docs |
| Artifacts are verifiable | Checksums, signatures where the channel supports them | Release artifact |
| Update owner is clear | Package manager or explicit self-update | Docs |
| Compatibility policy is written | What counts as breaking and the deprecation window | Docs |
| Deprecation warns | stderr message names replacement and removal version | Test |
| Old names are not reused | Removal is a major change with migration notes | Review |

## 9. Security and privacy

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Secrets avoid argv | File, stdin, keychain or helper | Review |
| Secrets avoid logs | Redaction in normal, debug and crash output | Test |
| Credential files are private | `0600` on Unix; owner-only ACL on Windows | Test |
| Telemetry is disclosed | Opt-in or documented opt-out; no secrets or paths | Review |
| Update metadata is verified | HTTPS plus signature or checksum | Review |
| Dependencies are pinned | Lockfile; reproducible build | Build |
| Pass-through is safe | `--` preserves caller arguments without shell evaluation | Test |
| Crash reports are bounded | No environment dump, tokens or full payloads | Review |

## 10. Review questions

- Can a new user discover the main task from bare invocation and one help page?
- Can a script predict stdout, stderr and the exit status without parsing prose?
- Can an operator explain every value the command used, including config and environment?
- Can the command run unattended without hanging on a prompt or a pager?
- Can a caller stop it without leaving unexplained partial state?
- Does every platform and install channel in the claim have evidence?
- Is a deprecated name still working, and does its warning say when it will stop?
- Are secrets absent from process listings, logs and crash output?

## Common failures

- The command tree has both `project create` and `create-project`.
- A flag means different things at the global and subcommand levels.
- Two positionals of different types, with the order only explained in a blog post.
- Config discovery reads a parent directory outside the project.
- `--config` is silently ignored when the file is missing.
- Logs or progress are printed to stdout and corrupt `--json`.
- JSON field names change in a patch release.
- `--json` emits pretty-printed output with ANSI color codes.
- `1` means "no changes" and `2` means "authentication failed".
- A prompt appears in CI and hangs until timeout.
- A progress bar writes escape sequences into a log file.
- `--help` performs a network update check.
- Completion is stale because it is maintained by hand.
- The install script edits `.bashrc` without asking.
- A self-update replaces the binary in CI and breaks a pinned pipeline.
- A deprecated flag is removed in a minor release without a warning.
- A secret is accepted as `--token` and appears in `ps` and shell history.

## Handoff

Return the completed checklist with pass/fail/not-applicable marks, the evidence for each failure, and the surface decisions that changed. Name what remains unverified: an untested Windows build, an unexercised self-update path or a completion script that was generated but not loaded in its shell. The checklist is complete when a reviewer can see the contract, the tests that exercise it and the limits of the claim.
