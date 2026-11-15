# Verification and review

**Claim:** implemented and behavior-verified locally for the documented CLI on macOS. **Not released or deployed**; this is a single local script with no distribution channel.

## Revision and environment

The workspace is not a git repository, so there is no commit. The checked revision is the local file set below; it is **not published and has no URL**.

| Artifact | SHA-256 |
| --- | --- |
| [`habits.py`](../habits.py) | `87fca0b5c6bbdb605541f14bd388a3127021509ea464a7a58b7a9f844a600bd2` |
| [`test_habits.py`](../test_habits.py) | `0d965ce6f0eac4ce23b9e68992d4dac647edddee721f64f722b92a5acdc8870a` |

- Workspace: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/ideation` (local temporary workspace).
- Platform: macOS (Darwin), `python3` 3.14.7 and `/usr/bin/python3` 3.9.6.
- Clock for CLI runs: local date 2026-11-15.
- No network access, third-party package or service was used.

## Automated checks

```sh
python3 -m unittest -v
```

Observed:

```text
Ran 33 tests in 0.024s

OK
```

```sh
/usr/bin/python3 -m unittest -v
```

Observed:

```text
Ran 33 tests in 0.032s

OK
```

```sh
python3 -m py_compile habits.py test_habits.py
```

Observed: exit 0, `py_compile=ok`.

The 33 tests cover: the four streak states and future dates; duplicate/unsorted/malformed entries; add, duplicate add, whitespace-only names; idempotent `done`; unknown habits; empty `list` without file creation; table output and the at-risk line; future completions in displayed output; remove; corrupt JSON left untouched; unsupported and boolean schema versions; invalid dates; duplicate names in the file; load normalization; nested parent creation; temporary-file cleanup; `--file`/`HABITS_FILE`/home precedence; unknown-command exit; and help text.

## Acceptance evidence

Requirements are defined in [the ECR](ecr.md#3-requirements-and-acceptance); the product signals are in [the brief](product.md#success-signals).

| ID | Requirement | Observed evidence | Status |
| --- | --- | --- | --- |
| R1 | Add a habit; names unique ignoring case and repeated spaces; duplicate exits 1. | `CliTests.test_add_creates_a_versioned_file_with_normalized_name`, `test_add_duplicate_is_case_insensitive_and_keeps_one_habit`, `test_add_rejects_a_whitespace_only_name`; manual duplicate run exited 1. | Verified locally |
| R2 | Mark today done once; repeat is harmless; unknown habit exits 1. | `test_done_is_idempotent_for_the_same_day`, `test_done_unknown_habit_fails_without_creating_a_file`; manual run printed `Marked`, then `Already marked`; unknown run exited 1. | Verified locally |
| R3 | Streak rule: today counts; open today keeps yesterday's run; a full miss resets; future ignored. | Ten `StreakTests`; manual missed-day fixture below. | Verified locally |
| R4 | `list` shows every habit, streak, today status and an at-risk line. | `test_list_shows_streak_today_status_and_risk_hint`, `test_list_ignores_future_completions`; manual output below. | Verified locally |
| R5 | `remove` deletes the habit and its history. | `test_remove_deletes_the_habit_and_its_history`, `test_remove_unknown_habit_fails`; manual run below. | Verified locally |
| R6 | Local JSON v1; default home, `HABITS_FILE`, then `--file` precedence; `list` does not create a file. | `test_default_file_is_created_under_the_home_directory`, `test_habits_file_environment_variable_is_used`, `test_explicit_file_wins_over_the_environment_variable`, `test_list_empty_does_not_create_the_file`; `json.tool` accepted the produced file. | Verified locally |
| R7 | Invalid data exits 2 and is not overwritten; writes leave no temp file. | `test_corrupt_json_is_reported_and_not_overwritten`, `test_unsupported_schema_version_is_reported`, `test_boolean_schema_version_is_rejected`, `test_invalid_completion_date_is_reported`, `test_duplicate_names_in_the_file_are_reported`, `test_successful_write_leaves_no_temporary_file`; manual corrupt run exited 2 and the bytes were unchanged. | Verified locally |
| R8 | CLI contract: help, usage, exit codes 0/1/2. | `test_unknown_command_is_a_usage_error`, `test_help_exits_zero_and_explains_streak_grace`; `python3 habits.py --help` exited 0; manual usage error exited 2. | Verified locally |
| R9 | Standard library only; Python 3.9+ syntax; one file. | Imports are stdlib; the suite ran on 3.14.7 and 3.9.6. Other platforms untested. | Verified locally, macOS only |

## CLI transcript: main path

All runs used an explicit file so the real home directory was untouched:

```sh
D=/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/habits-final2
F="$D/habits.json"
```

```text
$ python3 habits.py --file "$F" list
No habits yet.
Add one with: habits.py add "Read 10 pages"
$ python3 habits.py --file "$F" add "Read 10 pages"
Added "Read 10 pages".
$ python3 habits.py --file "$F" add "Walk"
Added "Walk".
$ python3 habits.py --file "$F" done "read 10 PAGES"
Marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
$ python3 habits.py --file "$F" done "Read 10 pages"
Already marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
$ python3 habits.py --file "$F" list
NAME           STREAK  TODAY
Read 10 pages       1  done
Walk                0  not done
```

The produced file was accepted by `python3 -m json.tool` (`json=valid`) and contained one `2026-11-15` completion for the marked habit.

## CLI transcript: failure and data paths

```text
$ python3 habits.py --file "$F" add "read 10 pages"
habits: error: habit "Read 10 pages" already exists
duplicate-exit=1
$ python3 habits.py --file "$F" done "Meditate"
habits: error: no habit named "Meditate"; run "habits.py list" to see habits
unknown-exit=1
$ python3 habits.py --file "$F" remove walk
Removed "Walk" and 0 completions.
$ python3 habits.py --file "$F" list
NAME           STREAK  TODAY
Read 10 pages       1  done
$ printf '{ broken json' > "$D/corrupt.json"
$ python3 habits.py --file "$D/corrupt.json" add "Walk"
habits: error: /private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/habits-final2/corrupt.json is not valid JSON: line 1, column 3: Expecting property name enclosed in double quotes
corrupt-exit=2
file-after={ broken json
```

The corrupt file remained byte-for-byte unchanged. An unknown command produced argparse's usage diagnostic and `usage-exit=2`.

Environment precedence was exercised through the real CLI:

```text
$ HABITS_FILE="$D/env.json" python3 habits.py add "Stretch"
Added "Stretch".
$ HABITS_FILE="$D/env.json" python3 habits.py list
NAME     STREAK  TODAY
Stretch       0  not done
```

## Missed-day demonstration

The CLI can only mark today, so past days were placed in a fixture by hand. It was generated on 2026-11-15 with: `Journal` completed today, yesterday and two days ago; `Stretch` completed yesterday and two days ago; `Meditate` completed three days ago.

```text
$ python3 habits.py --file "$D/missed.json" list
NAME      STREAK  TODAY
Journal        3  done
Stretch        2  not done
Meditate       0  not done

At risk (not done today): Stretch
```

This observes all three display states: today's completion extends the run (`Journal`, 3), an open today preserves it until midnight (`Stretch`, 2, at risk), and a fully missed day resets it (`Meditate`, 0). The unit tests additionally assert that a completion two days old with yesterday missed yields 0.

## Review pass

The review followed the changed behavior from CLI parsing through storage and display, and checked the automated evidence rather than trusting the green run.

| Severity | Finding | Disposition |
| --- | --- | --- |
| High | The first date validator required every dash-separated component to be two characters, so valid `YYYY-MM-DD` years were rejected. The initial test run observed 7 failures and 1 error out of 30 tests. | Fixed the year-width check; reran to 30/30, then extended the suite. |
| Medium | Duplicate-add diagnostics echoed the user's input casing (`"read 10 PAGES"`) instead of the stored display name, making the message look like a second habit existed. | The message now names the existing habit; the assertion was updated. |
| Medium | Parent-directory creation in `save()` sat outside the `OSError` boundary, so a mkdir failure would print a traceback instead of a data error. | Moved inside the guarded block. |
| Low | The pure streak helper accepted compact ISO dates such as `20261115` on newer Pythons, while the file validator rejected them. | Tightened the helper to the exact `YYYY-MM-DD` shape and added a regression test. |
| Low | JSON `true` compares equal to `1` in Python, so `"version": true` passed the schema check. | Explicitly reject booleans and added a regression test. |
| Low | README and design counts were stale after tests were added. | Reconciled them to 33 and rechecked the final run. |

No unresolved material finding remains in the reviewed scope. The review did not change product behavior; the fixes either restored the intended behavior or made a failure diagnosable.

## Not verified / coverage gaps

- **Atomicity under a crash was not fault-injected.** The temporary-file-plus-replace path succeeded and left no `.tmp` file in tests, but an OS-level kill between `fsync` and `replace`, or directory-entry durability, was not exercised.
- **No concurrent-writer test.** The design assumes one writer; last-write-wins behavior was reasoned, not reproduced.
- **Only macOS was exercised.** Linux and Windows are unverified, including `os.replace` and path behavior.
- **Only Python 3.14.7 and 3.9.6 ran the suite.** The 3.9+ claim is based on those two versions, not a full version matrix.
- **The real home path was not written.** A fake `HOME` exercised the default path; the author's actual `~/.habits.json` was not touched.
- **Midnight and timezone transitions were not manipulated at the OS level.** Tests inject a fixed `today`; real clock rollover and travel were not observed.
- **Display alignment for double-width scripts and very long names was not tested.**
- **Long-term personal usability was not evaluated.** Passing behavior tests does not establish that the streak rule motivates the author.
- **No release.** There is no package, installer, deployment or published URL to verify.
