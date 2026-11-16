# Output and exit codes

The output contract is what makes a CLI usable by another program. A human can recover from a surprising message; a pipeline cannot. Decide the stream, the shape and the status once, then test them at the process boundary.

## Contents

- [Stream contract](#stream-contract)
- [Choosing output modes](#choosing-output-modes)
- [JSON output contract](#json-output-contract)
- [Exit codes](#exit-codes)
- [TTY detection and presentation](#tty-detection-and-presentation)
- [Progress and cancellation](#progress-and-cancellation)
- [Broken pipes and large output](#broken-pipes-and-large-output)
- [Examples of good and bad output](#examples-of-good-and-bad-output)
- [Test matrix](#test-matrix)
- [Common failures](#common-failures)

## Stream contract

| Stream | Carries | Never carries | Usable when |
| --- | --- | --- | --- |
| `stdout` | The requested result: records, a report, or the JSON document | Logs, warnings, prompts, progress, ANSI when piped | Piped to a file or another program |
| `stderr` | Diagnostics, warnings, errors, prompts, progress, human hints | The primary result a caller parses | Redirected away without losing the result |
| `stdin` | Data or answers the caller explicitly supplies | Implicit answers in a non-interactive run | Piped input or an interactive terminal |

The rule is simple: if a caller redirects stdout to a file, that file should contain the result and nothing else. If the caller redirects stderr to `/dev/null`, the result should still be complete.

`stderr` is not automatically an error stream. Progress and prompts belong there because they are messages to the human, not data for the next program. Do not label every stderr line `ERROR`; reserve that for actual failures.

## Choosing output modes

| Mode | Default? | Consumer | Contract |
| --- | --- | --- | --- |
| Human output | Yes | A person at a terminal | Stable meaning, presentation may include color and layout |
| `--plain` | No | `grep`, `awk`, `cut`, line-oriented scripts | One record per line, no color, no borders, no wrapping that splits records |
| `--json` | No | Programs | One valid JSON document, or JSON Lines for a record stream |
| `--json` + `--pretty` | No | A person inspecting structured data | Same schema, indented for reading; not the default for pipes |
| `--quiet` | No | Scripts that need only the result or status | Suppresses nonessential human output; errors remain |
| `--verbose`/`--debug` | No | Diagnosis | More detail on stderr; does not change the result contract |

Rules:

- Default to human output, but make the human output's data available in a machine mode. Do not require a caller to scrape prose.
- Do not switch the schema automatically because stdout is a pipe. TTY detection may change color, width, pager and progress; it must not change the meaning or fields of the result.
- Make `--json` and `--plain` mutually exclusive unless you define their combination. Reject the combination rather than guessing.
- Keep `--quiet` from hiding errors or changing the exit status.
- Send warnings to stderr in every mode. In JSON mode, a warning may also appear in a `warnings` array, but the human warning still belongs on stderr.
- Do not localize machine output. Translate human messages only when the tool actually supports localization.

## JSON output contract

One document on success:

```json
{
  "schemaVersion": "1",
  "ok": true,
  "data": {
    "id": "prj_01J8Z9",
    "name": "billing",
    "owner": "platform",
    "createdAt": "2026-11-16T10:42:18Z"
  },
  "warnings": []
}
```

One document on failure:

```json
{
  "schemaVersion": "1",
  "ok": false,
  "error": {
    "code": "config_invalid",
    "message": "user config contains an unknown key",
    "hint": "remove `colour` or run `tool config migrate`",
    "details": {
      "path": "/Users/example/.config/tool/config.toml",
      "key": "colour"
    }
  }
}
```

Recommended defaults:

| Decision | Recommendation | Reason |
| --- | --- | --- |
| Success shape | `{schemaVersion, ok, data, warnings}` | One predictable envelope; callers can branch on `ok` |
| Failure shape | `{schemaVersion, ok:false, error:{code,message,hint,details?}}` | Stable machine code plus a human-readable message |
| Error stream | JSON error document on stdout, short hint on stderr | The command's product is a JSON document; callers parse one stream |
| Alternative | Structured errors on stderr, empty stdout | Defensible for tools whose stdout must remain a pure result stream |
| Record streams | JSON Lines, one object per line | Constant memory and incremental consumption |
| Schema version | Integer or string in every document | Consumers can detect a breaking change |
| Partial failure | `ok:false` plus per-item results, nonzero exit | Successful items are not lost |
| Timestamps | ISO 8601 UTC strings | Stable across locales and time zones |
| Identifiers | Strings, even when numeric-looking | Avoid precision and formatting surprises |
| Money/quantities | Integer minor units or decimal strings, with a unit | No binary floating-point ambiguity |
| Null versus absent | Define both; prefer absent for "not requested" and `null` for "known to be empty" | Callers can distinguish the cases |
| Pagination | Opaque `nextCursor`; no offset arithmetic required | Stable across changing data |
| Secrets | Never included; redact nested fields too | JSON is easy to log and share |

Do not:

- print a human sentence before or after the JSON document on stdout;
- pretty-print by default when stdout is not a TTY;
- emit one JSON document per log line and call it a stream;
- rename or retype a field in a patch release;
- return `ok:true` when a requested item failed;
- include absolute home paths or tokens in error details unless the caller asked for diagnostics.

If your tool emits multiple records, prefer JSON Lines over a giant array. A caller can process the first line before the command finishes, and a truncated stream still yields complete records. Use a single document when the result is genuinely one object or when a caller needs the whole aggregate.

## Exit codes

| Code | Conventional meaning | Ownership |
| --- | --- | --- |
| `0` | Success, including a documented no-op or dry run | The tool |
| `1` | General or operational failure | The tool |
| `2` | Usage error: invalid flag, operand or combination | The tool, by common convention |
| `3`–`125` | Application-defined failure classes | The tool; document each one |
| `126` | Command found but not executable | The shell |
| `127` | Command not found | The shell |
| `128 + N` | Terminated by signal `N`; `130` is SIGINT, `143` is SIGTERM | The shell/runtime |
| Above `125` | Reserved for shell and signal semantics | Not the tool's application codes |

Rules:

- Exit status is public API. Test it and mention changes in release notes.
- Return `0` only when the requested effect is true. A dry run that reported a valid plan is a success; a dry run that failed to read its target is not.
- Do not use `1` for "no changes" or "no matches" by default. Return `0` and expose a field such as `"changed": false` or `"matches": []`. If scripts genuinely need a distinct status, document it and keep it stable.
- Do not use `2` for authentication or configuration failures. Callers interpret `2` as a usage error.
- Never assign application meanings to `126` and `127`, or to values above `125`.
- Return nonzero on partial failure. Include the successful and failed items in the result so the caller can retry only what failed.
- Return `0` for `--help` and `--version`. A help request is not an error.
- Warnings do not change a successful status. If a warning makes the result unsafe to use, it is an error, not a warning.
- Keep application codes in the portable `0`–`125` range even on platforms that allow wider process statuses; shells and wrappers may truncate or reinterpret them.
- On Windows, signal exit status is not identical to Unix. Document the behavior if callers depend on it; do not claim a portable `130` where the platform does not provide it.

| Situation | Exit | Output |
| --- | --- | --- |
| Project created | `0` | Human confirmation or JSON `ok:true` |
| Plan produced, nothing applied | `0` | Plan, `changed:false` |
| Unknown flag | `2` | Usage on stderr, no mutation |
| Missing config file explicitly requested | `1` or a documented config code | Error naming the path |
| Authentication rejected | `1` or a documented auth code | Error with the login command |
| Batch of 10, 3 failed | Nonzero | Per-item results plus summary |
| User pressed Ctrl-C | `130` | Interrupt message and partial-state note |
| `tool ... \| head` closed the pipe | Documented; often `0` or `141` | No traceback |

## TTY detection and presentation

Check each stream separately. A terminal on stdout does not imply a terminal on stdin, and stderr may be redirected independently.

| Condition | Color | Progress | Pager | Prompt |
| --- | --- | --- | --- | --- |
| stdout TTY, stdin TTY | Allowed | On stderr if stderr TTY | Allowed | Allowed |
| stdout pipe, stdin TTY | Off for stdout | On stderr if TTY | No | Allowed for input |
| stdout TTY, stdin pipe | Allowed for stdout | On stderr if TTY | Allowed | No; read stdin or fail |
| stdout pipe, stderr pipe | Off | Off | No | No |
| CI (`CI=true`) | Off unless forced | Stage lines, no animation | No | No |
| `NO_COLOR` set and non-empty | Off | Unchanged | Unchanged | Unchanged |
| `TERM=dumb` | Off | Off | No | Allowed if stdin TTY |
| `--color=always` | On where the stream can accept it | Unchanged | Unchanged | Unchanged |
| `--no-color` | Off | Unchanged | Unchanged | Unchanged |

Additional rules:

- Disable color when either the relevant stream is not a TTY or the caller opted out. A color code written to a file is a defect.
- Do not animate a spinner or progress bar through a pipe. A carriage return does not erase a line in a log file.
- Detect width with a sane fallback (often 80 columns) and do not assume unlimited width.
- Use ASCII fallbacks when the terminal encoding is unknown; do not make box-drawing characters part of the data contract.
- Do not clear the screen or move the cursor outside an interactive TTY.
- Put prompts on stderr when the result is on stdout, so a script that captures stdout does not capture the question. Flush before reading.

## Progress and cancellation

Progress exists to answer "is it working?" It should not become the record of what happened.

- Show the current stage and, for a bounded loop, the item count. Estimated time is optional and should be omitted when it is not credible.
- Throttle updates. Redrawing on every item can dominate the runtime and flood a terminal.
- Print a final line or summary that remains after the progress display is cleared, so a log reader sees the outcome.
- Use `stderr` only. `--json` consumers should not receive progress on stdout.
- Respect `--no-progress`; let `--quiet` suppress progress and other nonessential messages.

For cancellation:

1. On the first SIGINT or SIGTERM, stop accepting new work and signal children.
2. Close or flush owned resources and remove owned temporary paths.
3. Report whether partial effects were rolled back, are resumable, or need reconciliation.
4. Exit with `130` or `143` by convention.
5. On a second signal, exit promptly without waiting for a graceful path that is already stuck.

A trap cannot handle SIGKILL. If the operation can leave durable state, provide a resume or reconcile command rather than claiming cleanup will always run.

## Broken pipes and large output

A downstream consumer may close early (`tool list | head`). Treat this as normal:

- catch the broken-pipe condition;
- stop producing output;
- do not print a stack trace;
- clean up owned resources;
- exit with the status you documented, commonly `0` for an intentional short read or `141` (`128 + SIGPIPE`) where the platform reports it.

Do not buffer an unbounded result in memory just to print it later. Stream records when the consumer may stop early, and make truncation visible if the command promises a complete set.

## Examples of good and bad output

Bad: progress on stdout corrupts the result.

```console
$ tool export --json > export.json
Exporting 120 records...
{"records":[...]}
```

`export.json` is not valid JSON because the status line came first.

Good:

```console
$ tool export --json > export.json
Exporting 120 records...        # stderr, TTY only

$ jq '.records | length' export.json
120
```

Bad: a JSON error on stdout in one command and on stderr in another, so a caller cannot write one parser.

Good: choose the contract, document it, and test every command against it.

Bad: an unstable field name.

```json
{"schemaVersion":"1","ok":true,"data":{"projectName":"billing"}}
```

then in a patch release:

```json
{"schemaVersion":"1","ok":true,"data":{"name":"billing"}}
```

Good: keep `projectName`, or add `name` and deprecate the old key with a schema version change.

Bad: exit `2` for "no matching records" because the author wanted scripts to detect emptiness. `2` now means both usage error and empty result.

Good:

```json
{"schemaVersion":"1","ok":true,"data":{"matches":[]}}
```

with exit `0`; scripts use the field, not a repurposed status.

Bad: a prompt appears when stdin is a pipe.

```console
$ echo "" | tool delete billing
Really delete billing? [y/N]
```

The command hangs or consumes the empty line and proceeds unpredictably.

Good:

```console
$ echo "" | tool delete billing
error: confirmation required; pass --confirm billing
```

## Test matrix

| Case | Assert |
| --- | --- |
| Success, human mode | Result on stdout; no diagnostics on stdout |
| Success, `--json` | Valid JSON; schema fields and types match |
| Failure, `--json` | Documented error stream; nonzero exit; no partial prose on stdout |
| Unknown flag | Exit `2`; usage on stderr; no mutation |
| Missing required value | Exit `2`; names the missing flag or argument |
| Operational failure | Documented failure code; actionable message |
| No-op | Exit `0`; `changed:false` or equivalent |
| Partial batch failure | Nonzero; successful and failed items present |
| stdout piped to `head` | No traceback; documented status |
| stdin is a pipe, prompt needed | No prompt; nonzero; names the supplying flag |
| `--no-input` | No prompt; same failure path |
| stderr not a TTY | No color or progress |
| `NO_COLOR` set | No color |
| `TERM=dumb` | No animation |
| SIGINT during work | Exit `130`; cleanup and partial-state message |
| SIGTERM during work | Exit `143`; cleanup and partial-state message |
| Very large stream | Bounded memory; records arrive incrementally |
| Non-UTF-8 locale | Machine output remains stable |

## Common failures

- Logs, warnings or progress on stdout.
- A `--json` mode that emits human text before the document.
- Pretty-printing by default for a piped consumer.
- ANSI color in a redirected file.
- JSON field renames or type changes without a schema change.
- Errors sometimes on stdout, sometimes on stderr.
- `ok:true` despite failed items.
- Exit `1` for "no changes" or `2` for a non-usage failure.
- Application codes above `125`, or reuse of `126`/`127`.
- A successful warning path that returns nonzero, or a failed path that returns zero.
- Prompts in CI.
- Progress animation in a log.
- A stack trace for a broken pipe.
- Secrets in an error document or debug log.
- Date, number or boolean formatting that changes with the locale.
- A pager started when stdout is a pipe.

## Handoff

Record the stream contract, the JSON schema and version, the exit-code table, the TTY and prompt rules, and the cancellation behavior. Attach process-level tests for each row of the matrix that applies. Distinguish what was observed from what is merely intended: a local run with a TTY does not establish the CI or piped behavior.
