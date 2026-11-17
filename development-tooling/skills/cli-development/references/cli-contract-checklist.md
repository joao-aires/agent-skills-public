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
| Aliases are deliberate | Each alias has a reason and a compatibility owner; a removed name is never reassigned | Docs and tests |
| Bare invocation is safe | Lists commands or shows concise help; never silently mutates | Manual run |

## 2. Arguments and flags

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Required inputs are explicit | Missing input produces usage and a nonzero exit | Tests |
| Positional arguments are unambiguous | At most one positional type, or a variadic list of one type | Help synopsis |
| Long and short forms are deliberate | Every flag has a long form; `-h` help; `-v` has one meaning | Help |
| Conventional names are used | `--json`, `--force`, `--dry-run`, `--no-input`, `--no-color`, `--config` | Help |
| `--` terminates options | Pass-through and dash-leading operands work | Test |
| Global flags are usable in documented positions | Both before and after the subcommand where the parser allows | Tests |
| Repeated and optional values are defined | Last wins, accumulate or reject; enums over ambiguous optional values | Tests |
| Unknown input is rejected | Unknown flag, subcommand or excess operand is a usage error with no mutation | Tests |
| Order independence is real | Flag order does not change meaning; operand order does where documented | Tests |

Two recurring grammar failures: several different positionals in a deployment command (`tool deploy prod billing now`), where an omitted value changes the target; and a destructive command whose only safeguard is `--yes`, where naming the target (`--confirm billing`) would be scriptable and safer.

## 3. Configuration and precedence

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Precedence is documented | `flags > environment > project config > user config > defaults` | Docs and tests |
| Explicit config path is defined | `--config` replaces discovery; a missing path is an error | Tests |
| Discovery boundary is defined | Walk stops at a repository or home boundary; no unrelated parents | Tests |
| Environment prefix is stable | `TOOL_*`; every variable documented and validated like a flag | Docs, tests |
| Merge semantics are defined | Per-key replace/merge/append; empty, unset and null are distinct | Tests |
| Effective config is inspectable | `tool config show` redacts secrets | Manual run |
| Writes are explicit | Only a config command writes; atomic replacement and permissions | Tests |
| No hidden reads | No undeclared file, network or credential lookup | Review |
| Secrets are not flags | File, stdin, keychain or credential helper | Review |

| Decision | Rule |
| --- | --- |
| Project and user config both exist | Define whether the nearer file replaces the farther one or merges key by key. Do not leave it to the parser. |
| Environment versus flag | Flag wins for the invocation. Environment is process context, not a way to override an explicit operator choice. |
| Config versus secret store | Config may name a credential profile; the secret itself belongs in a protected store. |
| Config file is malformed | Fail with the path and the parse error; do not fall back to defaults unless the user asked for that. |

## 4. Streams and output

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| stdout is the result | Piping stdout yields only data or the rendered result | Test |
| stderr is diagnostics | Logs, warnings, prompts and progress never enter stdout | Test |
| `--json` is valid and stable | One document, or JSON Lines for record streams; fields and types do not change in a patch or minor release | Schema test |
| Modes have distinct purposes | Default human, `--plain` and `--json` are documented | Help |
| TTY changes presentation only | Color, progress, pager and width may differ; data and exit status do not | Tests |
| Presentation can be disabled | Non-TTY, `NO_COLOR`, `TERM=dumb`, `--no-color`, `--no-progress` | Tests |
| Tables are line-oriented | One record per line; `--plain` available when layout would break parsing | Test |
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

## 5. Errors and exit status

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Success is `0` | Including a documented no-op or dry run | Tests |
| Usage errors are distinct | Usually `2`; documented if used | Tests |
| General failure is `1` | Operational failure that is not a usage error | Tests |
| App-specific codes are documented | Stable meaning, not reused, inside the portable range | Docs |
| `126`/`127` and signals are not repurposed | Left to shell execution and signal conventions | Review |
| Partial failure is nonzero | Per-item results retained; not silently dropped | Test |
| Error message is actionable | What failed, why, and the fixing command or flag | Review |
| Debug output is opt-in | Stack trace only with `--debug` or equivalent | Test |
| Exit code is stable | Not changed without a compatibility note | Changelog |

| Situation | Exit | Why |
| --- | --- | --- |
| Command completed, or nothing to do | `0` | A no-op is not a failure unless a distinct code is documented |
| Invalid flag, operand or combination | `2` | Usage error, no effect |
| Missing credential or operational failure | `1` or a documented code | The requested effect is not true |
| Partial batch failure | Nonzero | The requested whole did not succeed |
| Interrupted, or shell could not execute | `130`/`143`, `126`/`127` | Signal and shell conventions, not application codes |

Common failure: using `2` for "configuration changed" or `1` for "no matches". Callers already read those as usage and general failure. Return `0` with a structured `changed` or `matches` field unless a distinct status is part of the documented contract.

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
| Version is one line | Version plus revision/platform where useful; stable format | Test |
| Completion is generated | Same command definition as help; covers subcommands, flags, enums and paths | Generation test, shell test |
| Completion is side-effect free | No network, no writes, no stdout noise | Review |
| Support path is visible | Docs or issue URL in top-level help | Review |
| Errors suggest a fix | Correct flag or next command, not just "invalid" | Review |

## 8. Portability, packaging and compatibility

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Platform claims are bounded | OS, architecture, runtime and shell listed, with untested rows marked | Compatibility matrix |
| Paths use platform APIs | No hardcoded `/`, `~` or case assumptions | Test |
| Config directories are conventional | XDG, `%APPDATA%`, `~/Library` | Test |
| Platform-specific behavior is tested | `PATHEXT`, long paths, Ctrl-C, no ANSI assumption, containers | CI or explicit unsupported |
| Install and uninstall are documented | Registry, archive, package manager or container; what remains after removal | Docs |
| Artifacts are verifiable | Checksums, signatures where the channel supports them | Release artifact |
| Update owner is clear | Package manager or explicit self-update; no update during ordinary commands | Docs |
| Compatibility policy is written | What counts as breaking and the deprecation window | Docs |
| Deprecation warns | stderr names replacement and removal version; old name still works | Test |
| Old names are not reused | Removal is a major change with migration notes | Review |

## 9. Security and privacy

| Check | Pass looks like | Evidence |
| --- | --- | --- |
| Secrets avoid argv | File, stdin, keychain or helper | Review |
| Secrets avoid logs | Redaction in normal, debug and crash output | Test |
| Credential files are private | Owner-only mode or ACL | Test |
| Telemetry is disclosed | Opt-in or documented opt-out; no secrets or paths | Review |
| Update metadata is verified | HTTPS plus signature or checksum | Review |
| Dependencies are pinned | Lockfile; reproducible build | Build |
| Pass-through is safe | `--` preserves caller arguments without shell evaluation | Test |
| Crash reports are bounded | No environment dump, tokens or full payloads | Review |

## 10. Review questions

- Can a new user discover the main task from bare invocation and one help page?
- Can a script predict stdout, stderr and exit status without parsing prose?
- Can an operator explain every value the command used, including config and environment?
- Can the command run unattended without hanging on a prompt or pager?
- Can a caller stop it without unexplained partial state?
- Does every claimed platform and install channel have evidence, and is a deprecated name still working with a dated warning?

## Common failures

- The command tree has both `project create` and `create-project`, or a flag means different things at global and subcommand levels.
- Two positionals of different types, with the order only explained in a blog post.
- Config discovery reads a parent outside the project, or `--config` is silently ignored when the file is missing.
- Logs or progress corrupt `--json`; JSON field names change in a patch release; pretty-printed ANSI output reaches a pipe.
- `1` means "no changes" and `2` means "authentication failed".
- A prompt appears in CI and hangs; a progress bar writes escape sequences into a log.
- `--help` performs a network update check; completion is stale because it is maintained by hand.
- The install script edits `.bashrc` without asking, or a self-update replaces the binary in a pinned CI job.
- A deprecated flag is removed in a minor release without a warning.
- A secret is accepted as `--token` and appears in `ps` and shell history.

## Handoff

Return the completed checklist with pass/fail/not-applicable marks, the evidence for each failure, and the surface decisions that changed. Name what remains unverified: an untested Windows build, an unexercised self-update path or a completion script that was generated but not loaded in its shell. The checklist is complete when a reviewer can see the contract, the tests that exercise it and the limits of the claim.
