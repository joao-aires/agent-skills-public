# Engineering change record: local habit tracker CLI

## 1. Overview and lifecycle

**Change.** Build a small, local daily-habit tracker: add habits, mark today done, show a current streak per habit, and keep everything in one JSON file using only the Python standard library.

**Current outcome.** Implemented and verified locally on 2026-11-15. The command surface, streak rule, data format, tests and documentation exist in this workspace. Next action: the requester uses it for a short real trial and decides whether planned rest days or packaging are needed. Owner: requester.

**Readiness disposition:** **ready with limitations** for personal local use. The verified scope is the requirements below on one platform; no real-use evidence, packaging, concurrency safety or cross-platform support exists. Not ready for release or shared/multi-user use.

**Lifecycle claims.**

| Claim | Status | Evidence |
| --- | --- | --- |
| Requirements and design | Accepted for the slice | [PRD](../product/prd.md), [design proposal](../design/design-proposal.md), [streak cases](../design/streak-cases.md) |
| Implemented | Yes, local source | `habits.py` at the content hash below |
| Verified locally | Yes | 44 automated tests and an 18-command CLI transcript at the same revision |
| Released | Not applicable | No package, install or distribution was produced |
| Real-use value | Not measured | No usage period was run |

**Change identity.** Worktree: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/ideation`. This directory is not a Git repository, so the revision is a local-only content hash, **not** a commit and **not** published; there is no URL.

- `habits.py` — SHA-256 `00fad9c5e5ccfcbfbc6e072fc0eb6543509ceb7057b1e4808a2cd82694b13414`
- `test_habits.py` — SHA-256 `33025bb6a3dce43c0b83306f819cfdf0ef66a107ec6859dbed66dd772136915a`

**Links.** [README](../../README.md), [PRD](../product/prd.md), [design proposal](../design/design-proposal.md), [streak cases](../design/streak-cases.md), [verification](../evidence/verification.md), [CLI transcript](../evidence/cli-transcript.md), [test output](../evidence/test-output.txt).

## 2. Problem and scope

The requester tracks a few daily habits and currently has no single place that answers "did I do it today?" and "is the run still alive?" without manual counting. The supplied [rough idea](../../IDEA.md) is personal-use, local, JSON-backed and dependency-free; it deliberately leaves command names, the data model and missed-day behavior undecided.

In scope: 3–10 daily habits, one completion per local calendar day, current and longest streak, today's status, last completion, backfill, undo, removal with confirmation, one JSON file, clear errors and exit codes.

Out of scope: accounts, sync, multi-user access, reminders, notifications, weekly quotas, planned rest days, per-habit schedules, time-of-day tracking, analytics, import/export, encryption, packaging and deployment. The product rationale and non-goals are in the [PRD](../product/prd.md#scope-and-non-goals).

Existing behavior: **greenfield; no implementation existed.** The only prior artifact is the request in `IDEA.md`.

## 3. Requirements and acceptance

Requirements below were derived from the request and the recorded assumptions and treated as accepted for this implementation; the requester's separate sign-off of these specific behaviors is not recorded. "Verified" means the named test or transcript ran at the revision in section 1. It does not mean real-use acceptance.

| ID | Actor and action | Observable result | Status | Evidence |
| --- | --- | --- | --- | --- |
| R1 | Add a habit with a name | A slug id is returned; one record is stored; a case-insensitive duplicate name is refused without changing the file | Verified | `test_add_creates_file_and_lists_habit`, `test_duplicate_name_is_rejected_without_writing` |
| R2 | Add names that collide after slugging, or use non-ASCII | Ids stay unique (`read`, `read-2`); `Café` gets `cafe` | Verified | `test_colliding_slug_gets_a_suffix`, `test_unicode_name_gets_ascii_slug` |
| R3 | List habits | Each habit shows id, name, current streak, today yes/no and last completion; an empty store explains the next command | Verified | `test_add_creates_file_and_lists_habit`, `test_list_shows_each_habit_independently`, `test_empty_list_explains_next_step` |
| R4 | Mark a habit done today | The completion is stored and the reported streak becomes 1; repeating the command is a harmless no-op and does not duplicate the date | Verified | `test_done_is_idempotent` |
| R5 | Complete consecutive days, including backfill | Current streak counts the consecutive run; three consecutive days report 3 | Verified | `test_backfilled_consecutive_days_build_streak`, `StreakTests` |
| R6 | Check before marking today | A run through yesterday still reports its length, with `TODAY no` and "today not marked" in `show` | Verified | `test_unmarked_today_keeps_yesterday_streak_active`, `StreakTests.test_unmarked_today_keeps_yesterdays_streak_active` |
| R7 | Miss a calendar day | The current streak is 0 and history is retained; the next completion starts at 1 | Verified | `test_missed_day_resets_streak_but_keeps_history`, `StreakTests.test_two_day_old_completion_is_zero` |
| R8 | Undo a completion | The date is removed and the streak recalculates; undoing an unmarked day reports an error | Verified | `test_undo_today_removes_only_that_day`, `test_undo_yesterday_breaks_the_run`, `test_undo_can_remove_a_future_entry_from_edited_data` |
| R9 | Backfill or write a future date | A past date is accepted; a future date is refused with exit 1 and no stored change | Verified | `test_future_date_is_rejected`, `test_backfilled_consecutive_days_build_streak` |
| R10 | Persist and reload | The JSON file is versioned, atomically replaced, and leaves no temporary file; missing parents are created | Verified | `test_add_creates_file_and_lists_habit`, `test_write_leaves_no_temporary_files`, `DataPathTests` |
| R11 | Encounter corrupt or unsupported data | The command exits 1 with a diagnostic and does not overwrite the file | Verified | `test_corrupt_json_is_reported_and_not_overwritten`, `test_unsupported_data_version_is_rejected`, `test_duplicate_ids_are_rejected` |
| R12 | Refer to a habit | Exact id, case-insensitive id or case-insensitive name resolves; an unknown reference exits 1 without creating a file | Verified | `test_reference_by_name_and_case`, `test_unknown_habit_fails_without_creating_a_file` |
| R13 | Use invalid input or remove a habit | Malformed dates and unknown commands exit 2; removal without `--yes` exits 1 and preserves the habit; removal with `--yes` deletes it | Verified | `test_malformed_date_is_a_usage_error`, `test_unknown_command_is_a_usage_error`, `test_remove_requires_yes_and_deletes_history`, `test_empty_name_is_rejected` |
| R14 | Choose the data file and read help | `--file` wins over `HABITS_FILE`, then XDG, then home; no arguments prints help; `--version` works | Verified | `DataPathTests`, `test_habits_file_environment_variable`, `test_no_arguments_prints_help`, `test_version_flag` |

Failure paths worth stating explicitly:

- Unknown habit: exit 1, stderr diagnostic, no file created if none existed.
- Future completion: exit 1, no change.
- Corrupt JSON: exit 1, original bytes preserved.
- Duplicate name: exit 1, original file bytes preserved.
- Remove without confirmation: exit 1, habit and history preserved.
- Malformed date or unknown command: exit 2 from argument parsing.

## 4. Solution design

**Baseline:** greenfield; no implementation existed. The full alternatives and tradeoffs are in the [design proposal](../design/design-proposal.md); the chosen rule is specified in [streak cases](../design/streak-cases.md).

**Affected software type:** `library-cli` — the product is a command surface, its local persistence and its errors. Backend, frontend and AI components are **not affected**: there is no service, screen or model. There is no multi-type seam; the only boundary is the local filesystem.

**Chosen behavior.** Option A: the current streak is a consecutive calendar-day run ending today, or ending yesterday when today is unmarked. A missed day resets it; future dates do not count. The streak is derived from stored completions on every read, so no stale counter can survive an undo or hand edit.

**Data shape, version 1:**

```json
{
  "version": 1,
  "habits": [
    {
      "id": "read",
      "name": "Read",
      "created_on": "2026-11-15",
      "completions": ["2026-11-14", "2026-11-15"]
    }
  ]
}
```

- `id` is a lowercase ASCII slug, unique within the file; collisions get `-2`, `-3`.
- `name` is unique case-insensitively; it is display text and may contain spaces.
- `created_on` is metadata; historical completions may predate it.
- `completions` is a sorted, de-duplicated list of local calendar dates.
- Unknown fields are ignored; an unknown `version` is refused.

**Command surface and compatibility.** Documented in the [design proposal § Surface and compatibility](../design/design-proposal.md#surface-and-compatibility) and the README. Exit codes: 0 success/no-op, 1 data or habit error, 2 usage error. Standard output carries results; stderr carries diagnostics. Python standard library only; exercised on Python 3.14.7 / macOS 27.0.1 only. No packaging or install path exists.

**Failure and recovery.** Writes use a same-directory temporary file, `fsync`, and `os.replace`, so a crash cannot leave a half-written JSON document. A corrupt file is refused rather than silently replaced. There is no concurrency lock: two simultaneous writers can lose one update. That is recorded as a limit, not a production claim.

**Rejected directions.** Strict today-required (B) made a normal morning check look broken. Rolling quota (C) lost the requested day streak and needed per-habit targets. Per-habit schedules (D) added configuration, migration and an off-schedule policy beyond the slice.

## 5. Implementation strategy

Delivered in four increments, each exercised before the next:

1. **Streak core, test-first.** Wrote the pure date cases first (red because the module did not exist), then `current_streak`, `longest_streak` and data-path resolution. 15 core tests passed.
2. **Persistence and read path.** Added the versioned JSON store, atomic replacement, slug/id creation, `add` and `list`; exercised through the shipped script with a temporary file.
3. **Mutating commands and failures.** Added `done`, `undo`, `show`, `remove`, date validation, confirmation and diagnostics; covered idempotency, backfill, missed days and corrupt data.
4. **Review and repair.** Tightened weak assertions, fixed four presentation/contract defects (recorded in the [verification review](../evidence/verification.md#review-findings-and-repairs)), and regenerated the transcript.

No migration, compatibility shim, rollout or rollback applies: this is a new local file with a version guard. The script is run directly; there is no build step.

**Ready to start:** nothing remains for this slice. **Blocked/deferred:** planned rest days, weekly targets and packaging await a product decision; real-use evidence is not available.

## 6. Verification and release

**Revision and environment.** Local-only workspace at the path in section 1; not published, no URL. Content hashes: `habits.py` `00fad9c5…b13414`, `test_habits.py` `33025bb6…6915a`. Environment: macOS 27.0.1, Python 3.14.7, zsh. Full environment and hash table: [verification](../evidence/verification.md#revision-and-environment).

**Commands actually run.**

| Command | Observed result |
| --- | --- |
| `python3 -m unittest -v` | `Ran 44 tests in 4.332s` — `OK` (full output in [test-output.txt](../evidence/test-output.txt)) |
| `python3 -m py_compile habits.py test_habits.py` | Exit 0, no output |
| 18-command CLI session with `--file`/`--today` | All expected exit codes; outputs preserved in [cli-transcript.md](../evidence/cli-transcript.md) |
| Real-date smoke: `HABITS_FILE=… add Stretch`, `done stretch`, `list` | Added, marked on 2026-11-15, listed with streak 1 and `TODAY yes` |

The CLI session covered: empty list, add, idempotent done, backfill, two-habit list, detailed show, missed-day reset, undo, refused removal, confirmed removal, unknown habit and a future date. The transcript shows the exact stdout/stderr and exit status. Duplicate-name, corrupt-file and unsupported-version protection were exercised by the test suite rather than the transcript.

**Review.** A change-level review found and repaired: a test helper that shadowed `TestCase.fail()` and corrupted assertion messages; repeated date labels in `show`; malformed dates exiting 1 while the documented usage-error code is 2; a removal message that counted completions as "days of history"; and future entries that could not be undone. All repairs were re-tested. The full findings and dispositions are in [verification](../evidence/verification.md#review-findings-and-repairs).

**Release.** Not released. No package, install, service, deployment or user distribution was produced. The only verified boundary is local invocation from this workspace.

**Not exercised.** Real personal use over days; other Python versions; Linux/Windows; concurrent writers; disk-full and permission-failure paths beyond the code's error handling; symlinked data files; very large histories; terminal width and non-ASCII display; timezone travel. These are limits, not passes.

## 7. Decision history and references

| Date | Decision | Owner | Rationale | Status |
| --- | --- | --- | --- | --- |
| 2026-11-15 | Choose Option A: consecutive run, active through yesterday, missed day resets | Requester (delegated) | Preserves a live run while keeping today's status explicit; no schedule/quota model | Accepted for slice |
| 2026-11-15 | One versioned JSON document with derived streaks and name-derived slug ids | Requester constraint + implementation | Local, human-editable, no service; derived totals cannot go stale | Accepted |
| 2026-11-15 | Allow `undo` to remove future-dated entries | Implementation review | Recovery for clock skew or hand edits, without weakening the write-time future check | Accepted |
| — | Planned rest days, weekly targets, packaging, real-use trial | Requester | Need evidence from use; not required by the slice | Open |

**References.** [IDEA.md](../../IDEA.md), [PRD](../product/prd.md), [design proposal](../design/design-proposal.md), [streak cases](../design/streak-cases.md), [README](../../README.md), [verification](../evidence/verification.md), [CLI transcript](../evidence/cli-transcript.md), [test output](../evidence/test-output.txt).
