# Verification evidence

**Claim verified locally:** the habit CLI satisfies requirements R1–R14 in the [ECR](../change/ecr.md#3-requirements-and-acceptance) at the revision below. **Not verified:** real personal use, other platforms/interpreters, concurrency, packaging. **Release:** none.

Verification date: 2026-11-15. All observations below were made in this workspace.

## Revision and environment

This directory is not a Git repository. The revision is a local-only content hash, **not a commit**, **not published**, with **no URL**.

| Item | Observed value |
| --- | --- |
| Workspace | `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/ideation` |
| `habits.py` SHA-256 | `00fad9c5e5ccfcbfbc6e072fc0eb6543509ceb7057b1e4808a2cd82694b13414` |
| `test_habits.py` SHA-256 | `33025bb6a3dce43c0b83306f819cfdf0ef66a107ec6859dbed66dd772136915a` |
| OS | macOS 27.0.1 |
| Python | CPython 3.14.7 |
| Shell | zsh |
| Git | Not a repository; no commit or branch identity exists |

The documentation files are records at the same date; they are not part of the executable revision. No package, service or deployment was produced.

## What was exercised

| Layer | Tests | Seam |
| --- | --- | --- |
| Pure streak and date rules | 11 | `current_streak`, `longest_streak`, `parse_date` with explicit dates |
| Data-path precedence | 4 | `resolve_data_path` with patched environment |
| Shipped CLI | 29 | `python3 habits.py` as a subprocess with an isolated `--file`, fixed `--today`, cleared `HABITS_FILE`/`XDG_DATA_HOME`, and a temporary working directory |
| **Total** | **44** | |

The CLI layer observes stdout, stderr and exit status. It does not import command handlers directly, so argument parsing, file creation, persistence and diagnostics are part of what ran. Tests use known literal dates and expected values derived from the [streak cases](../design/streak-cases.md), not a reimplementation of the calculation.

## Commands and observed results

### Automated suite

```text
$ python3 -m unittest -v
...
Ran 44 tests in 4.332s

OK
[exit 0]
```

Full output: [test-output.txt](test-output.txt). The suite includes 11 pure streak tests, 4 path tests and 29 CLI tests. Wall time varies by run; the captured output is one observation, and later runs passed the same 44 tests.

### Compilation check

```text
$ python3 -m py_compile habits.py test_habits.py
(no output)
[exit 0]
```

### CLI transcript

```text
$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 <command>
```

An 18-command session exercised empty state, add, idempotent done, backfill, list, show, a missed-day reset, undo, refused and confirmed removal, an unknown habit and a future date. Exit codes were 0 for success/no-op and 1 for the three expected failures. Exact stdout/stderr and exit codes: [cli-transcript.md](cli-transcript.md).

Representative observed results:

- `list` before any data: `No habits yet. Add one with: python3 habits.py add "Read"`, exit 0.
- Two consecutive completions: `list` row with `STREAK 2`, `TODAY yes`, `LAST DONE 2026-11-15`.
- A run through yesterday with today unmarked: `show` reported `2 days (through 2026-11-14; today not marked)`.
- Completion on Nov 12 and 13, viewed on Nov 15: `STREAK 0`, history retained at `LAST DONE 2026-11-13`.
- Future date: `habits: cannot mark a future date (2026-11-16) as done; today is 2026-11-15`, exit 1.
- Unknown habit: `habits: no habit matches 'nope'; run 'list' to see ids`, exit 1.
- Remove without confirmation: exit 1, habit preserved; with `--yes`: removed with `2 completions`.

### Real-date smoke (no `--today`)

```text
$ python3 habits.py add Stretch
Added "Stretch" with id stretch. [exit 0]

$ python3 habits.py done stretch
Marked "Stretch" done on 2026-11-15. Current streak: 1 day. [exit 0]

$ python3 habits.py list
ID       NAME     STREAK  TODAY  LAST DONE
stretch  Stretch       1  yes    2026-11-15
[exit 0]
```

This used `HABITS_FILE` pointing at a temporary file, so the default local date and the environment-variable path were exercised together. The authored home path was not modified.

A separate permission probe created the data file under a new parent directory: the file mode was `0600` and the directory `0755`. The user-only file mode comes from the temporary file used for the atomic replacement.

### Help

```text
$ python3 habits.py --help
[exit 0]
```

Rendered text: [help.txt](help.txt). It states the streak rule, data-file precedence and exit codes. No arguments also prints help and exits 0.

## Acceptance summary

| Requirement group | Result |
| --- | --- |
| Add, id, duplicate rejection, list, empty state | Verified |
| Done, idempotency, consecutive run, active-through-yesterday, missed-day reset | Verified |
| Undo, backfill, future-date rejection, removal confirmation | Verified |
| Versioned JSON, atomic write, corrupt/unsupported refusal, duplicate-id refusal | Verified |
| References, malformed dates, unknown commands, data-path precedence, help/version | Verified |
| Real-use value and retention | **Not measured** |

The exact test-to-requirement mapping is in the [ECR](../change/ecr.md#3-requirements-and-acceptance). A green suite proves the defined behavior at this revision, not user benefit.

## Review findings and repairs

A change-level review read the implementation against the accepted behavior and the CLI contract. Findings and dispositions:

| # | Finding | Impact | Repair | Recheck |
| --- | --- | --- | --- | --- |
| 1 | Test helper `fail()` shadowed `unittest.TestCase.fail()`, so an assertion failure re-invoked the CLI with the failure message as an argument | A failing test produced a misleading argparse error instead of the real assertion; also invalidated that test's failure behavior | Renamed helpers to `cli_ok`/`cli_fail` | Full suite re-ran; corrupted-file assertion then correctly exposed a wrong substring expectation, which was fixed |
| 2 | `show` printed each date twice (`2026-11-09  -  2026-11-09`) | Recent history was noisy and harder to scan | Replaced the duplicate label with weekday plus `today` | CLI transcript regenerated and inspected |
| 3 | Malformed `--date` exited 1 while help promised 2 for usage errors | Output/exit contract disagreed with documentation | Added argparse date type so malformed dates exit 2; future dates remain domain errors with exit 1 | `test_malformed_date_is_a_usage_error` passes |
| 4 | Removal said "2 days of history" for two completions | Implied a time span rather than a count | Changed to "2 completions"; singular covered | `test_remove_requires_yes_and_deletes_history` passes |
| 5 | A future-dated completion could not be undone | Hand-edited or clock-skew data was unrecoverable through the CLI | Removed the future check from `undo`; write-time future rejection stays | `test_undo_can_remove_a_future_entry_from_edited_data` passes |
| 6 | Several list assertions used weak substring checks such as `assertIn("1", row)` | Could pass for the wrong column or an unrelated digit | Added a row parser and asserted streak/today/last-done columns | Full suite passes with the tighter assertions |
| 7 | The first capture of the transcript exposed the duplicate-date display (finding 2) | Caught by reading the observed output rather than trusting the code | Fixed and recaptured | Transcript inspected again |

No open correctness finding remains for the verified scope.

## Limits and unverified claims

- **No real-use trial.** The tool was exercised for seconds in automation, not used daily for a week. The product success signal remains unmeasured.
- **One environment.** Only CPython 3.14.7 on macOS 27.0.1 was executed. Other Python versions and Linux/Windows are not claimed.
- **No concurrency safety.** Writes are atomic per file but there is no lock; two simultaneous processes can lose one update.
- **No packaging.** The script is run from this directory. A clean consumer install was not tested because there is no package.
- **Plaintext data.** The file contains habit names and dates, readable by the owner and anyone with access to the account. No encryption.
- **Edge paths not exercised:** disk full, permission denied on an existing writable-looking path, symlinked data file, very large history, terminals narrower than the table, timezone travel, DST transitions (dates only, so no clock arithmetic), and process interruption during `os.replace`.
- **No backup or recovery command.** Backups are the owner's responsibility.
- **No release.** No artifact was published, installed or deployed; no production claim is made.

## Evidence files

- [test-output.txt](test-output.txt) — full `python3 -m unittest -v` output, 44 tests.
- [cli-transcript.md](cli-transcript.md) — 18-command observed session with stdout/stderr and exit codes.
- [help.txt](help.txt) — observed `--help` output.
- [ECR verification section](../change/ecr.md#6-verification-and-release) — claim-level summary and release status.
