# Output and exit codes

The output contract is what makes a CLI usable by another program. A human can recover from a surprising message; a pipeline cannot. Decide the stream, the shape and the status once, then test them at the process boundary.

Exact Unix status and utility conventions belong to [POSIX](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_08_02); human-facing output conventions belong to [clig.dev](https://clig.dev/); the color opt-out is [NO_COLOR](https://no-color.org/). This reference owns the local contract: what your callers may rely on.

## Stream contract

| Stream | Carries | Never carries | Usable when |
| --- | --- | --- | --- |
| `stdout` | The requested result: records, a report, or the JSON document | Logs, warnings, prompts, progress, ANSI when piped | Piped to a file or another program |
| `stderr` | Diagnostics, warnings, errors, prompts, progress, human hints | The primary result a caller parses | Redirected away without losing the result |
| `stdin` | Data or answers the caller explicitly supplies | Implicit answers in a non-interactive run | Piped input or an interactive terminal |

If a caller redirects stdout to a file, that file contains the result and nothing else. If the caller redirects stderr to `/dev/null`, the result is still complete. `stderr` is not automatically an error stream: label only actual failures as errors.

## Choosing output modes

| Mode | Default? | Consumer | Contract |
| --- | --- | --- | --- |
| Human output | Yes | A person at a terminal | Stable meaning; presentation may include color and layout |
| `--plain` | No | `grep`, `awk`, `cut`, line-oriented scripts | One record per line, no color, borders or record-splitting wraps |
| `--json` | No | Programs | One valid JSON document, or JSON Lines for a record stream |
| `--quiet` | No | Scripts that need only the result or status | Suppresses nonessential human output; errors remain |
| `--verbose`/`--debug` | No | Diagnosis | More detail on stderr; does not change the result contract |

- Give human output a machine equivalent; do not require a caller to scrape prose.
- Do not switch schema because stdout is a pipe. TTY detection may change color, width, pager and progress only.
- Make `--json` and `--plain` mutually exclusive unless you define their combination; reject rather than guess.
- `--quiet` must not hide errors or change the exit status. Warnings stay on stderr in every mode and may also appear in a `warnings` array.
- Do not localize machine output.

## JSON output contract

One document on success:

```json
{
  "schemaVersion": "1",
  "ok": true,
  "data": {"id": "prj_01J8Z9", "name": "billing", "createdAt": "2026-11-16T10:42:18Z"},
  "warnings": []
}
```

On failure, the same envelope with `"ok": false` and `"error": {"code", "message", "hint"?, "details"?}`. Choose one stream for that error document and use it for every command.

| Decision | Recommendation | Reason |
| --- | --- | --- |
| Error stream | JSON error on stdout plus a short hint on stderr, or structured errors on stderr with empty stdout | Either is defensible; inconsistency between commands is not |
| Record streams | JSON Lines, one object per line | Constant memory and incremental consumption |
| Schema version | Integer or string in every document | Consumers detect a breaking change |
| Partial failure | `ok:false` plus per-item results, nonzero exit | Successful items are not lost |
| Timestamps and identifiers | ISO 8601 UTC strings; identifiers as strings even when numeric-looking | Stable across locales, precision and formatting |
| Money and quantities | Integer minor units or decimal strings, with a unit | No binary floating-point ambiguity |
| Null versus absent | Absent for "not requested"; `null` for "known to be empty" | Callers can distinguish the cases |
| Pagination | Opaque `nextCursor`; no offset arithmetic required | Stable across changing data |
| Secrets | Never included, including nested fields | JSON is easy to log and share |

Do not print a human sentence before or after the document, pretty-print by default for a pipe, emit one document per log line, rename or retype a field in a patch release, or return `ok:true` when a requested item failed. Prefer JSON Lines for record streams: a caller can process the first line before the command finishes. Use one document when the result is genuinely one object.

## Exit codes

| Code | Conventional meaning | Ownership |
| --- | --- | --- |
| `0` | Success, including a documented no-op or dry run | The tool |
| `1` | General or operational failure | The tool |
| `2` | Usage error: invalid flag, operand or combination | The tool, by common convention |
| `3`–`125` | Application-defined failure classes; document each one | The tool |
| `126`, `127` | Found but not executable; not found | The shell |
| `128 + N` | Terminated by signal `N`; `130` is SIGINT, `143` is SIGTERM | The shell or runtime |

- Exit status is public API. Test it and mention changes in release notes.
- Return `0` only when the requested effect is true. A dry run that reported a valid plan is a success; one that failed to read its target is not.
- Do not use `1` for "no changes" or "no matches", or `2` for authentication or configuration failures. Return `0` with a `changed`/`matches` field unless a distinct status is part of the documented contract.
- Return nonzero on partial failure and include successful and failed items so the caller can retry only what failed.
- Return `0` for `--help` and `--version`. Warnings do not change a successful status; if a warning makes the result unsafe, it is an error.
- Keep application codes in the portable `0`–`125` range. On Windows, signal status is not identical to Unix; document what callers can rely on.

## TTY detection and presentation

Check each stream separately: a terminal on stdout does not imply a terminal on stdin, and stderr is redirected independently.

| Condition | Color | Progress | Pager | Prompt |
| --- | --- | --- | --- | --- |
| All streams TTY | Allowed | On stderr | Allowed | Allowed |
| stdout piped | Off for stdout | On stderr if TTY | No | Allowed if stdin TTY |
| stdin piped | Allowed for stdout | On stderr if TTY | Allowed | No; read stdin or fail |
| CI, `TERM=dumb` | Off unless forced | Stage lines, no animation | No | No |
| `NO_COLOR` set non-empty | Off | Unchanged | Unchanged | Unchanged |

- A color code or cursor movement written to a file or log is a defect. Detect width with a sane fallback, and use ASCII when the encoding is unknown.
- Put prompts on stderr when the result is on stdout, and flush before reading.

## Progress and cancellation

Progress answers "is it working?"; it is not the record of what happened.

- Show the current stage and, for a bounded loop, the item count. Throttle updates and leave a final summary line that survives the display being cleared.
- Use stderr only. Respect `--no-progress`; let `--quiet` suppress progress and other nonessential messages.
- On the first SIGINT or SIGTERM: stop accepting work, signal children, flush and close owned resources, remove owned temporary paths, and report whether partial effects were rolled back, are resumable, or need reconciliation. Exit `130` or `143`.
- On a second signal, exit promptly. A trap cannot handle SIGKILL: if the operation leaves durable state, provide resume or reconcile rather than claiming cleanup always runs.

## Broken pipes and large output

A downstream consumer may close early (`tool list | head`). Treat it as normal: catch the condition, stop producing output, print no stack trace, clean up owned resources, and exit with the documented status — commonly `0` for an intentional short read or `141` (`128 + SIGPIPE`) where the platform reports it. Stream records rather than buffering an unbounded result, and make truncation visible if the command promises a complete set.

## Test matrix

| Case | Assert |
| --- | --- |
| Success, human and `--json` | Result on stdout, no diagnostics; valid JSON with matching fields and types |
| Failure, `--json` | Documented error stream; nonzero exit; no partial prose on stdout |
| Unknown flag or missing value | Exit `2`; usage on stderr; names the missing flag; no mutation |
| Operational failure | Documented failure code; actionable message |
| No-op | Exit `0`; `changed:false` or equivalent |
| Partial batch failure | Nonzero; successful and failed items present |
| stdout piped to `head` | No traceback; documented status |
| stdin is a pipe, prompt needed | No prompt; nonzero; names the supplying flag |
| `--no-input` | No prompt; same failure path |
| stderr not a TTY, `NO_COLOR`, `TERM=dumb` | No color, progress or animation |
| SIGINT/SIGTERM during work | `130`/`143`; cleanup and partial-state message |
| Very large stream, non-UTF-8 locale | Bounded memory, incremental records; machine output stable |

## Common failures

- Logs, warnings or progress on stdout; human text before a JSON document.
- Pretty-printing or ANSI color in a redirected file.
- JSON field renames or type changes without a schema change.
- Errors sometimes on stdout, sometimes on stderr; `ok:true` despite failed items.
- Exit `1` for "no changes" or `2` for a non-usage failure; application codes above `125`.
- A successful warning path that returns nonzero, or a failed path that returns zero.
- Prompts in CI; a progress animation in a log; a stack trace for a broken pipe.
- Secrets in an error document or debug log; locale-dependent numbers or dates.
- A pager started when stdout is a pipe.

## Handoff

Record the stream contract, the JSON schema and version, the exit-code table, the TTY and prompt rules, and the cancellation behavior. Attach process-level tests for each applicable matrix row. Distinguish what was observed from what is intended: a local run with a TTY does not establish the CI or piped behavior.
