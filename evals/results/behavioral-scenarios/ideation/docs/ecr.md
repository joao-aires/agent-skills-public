# Engineering Change Record: habits.py

## 1. Overview and lifecycle

This change turns the rough idea in [`IDEA.md`](../IDEA.md) into a small local habit tracker: `habits.py` adds, marks, lists and removes daily habits in one JSON file, with an explicit day-grace streak rule. It is implemented and **verified locally**; it is not packaged, released or deployed. The next action is ordinary personal use, with the open product decisions in section 3 parked unless daily use exposes a problem.

| Claim | Status | Evidence |
| --- | --- | --- |
| Product intent | Accepted | [Product brief](product.md), derived from `IDEA.md`. |
| Requirements | Accepted | Section 3; all R1–R9 verified locally. |
| Design | Accepted | [Design record](design.md), decision blocks dated 2026-11-15. |
| Implementation | Implemented | [`habits.py`](../habits.py) at local SHA-256 `87fca0b5c6bbdb605541f14bd388a3127021509ea464a7a58b7a9f844a600bd2`; not published. |
| Verification | Verified locally | 33 tests passed on Python 3.14.7 and 3.9.6; CLI exercised; see [verification](verification.md). |
| Review | Completed | Review findings recorded and resolved in [verification](verification.md#review-pass); no unresolved material finding. |
| Release | Not applicable | A local single-file tool with no distribution channel or deployed target. |

**Change identity:** local workspace `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/ideation`. The workspace is not a git repository, so there is no commit, issue, PR or URL. The file hashes in [verification](verification.md#revision-and-environment) identify the checked revision.

## 2. Problem and scope

At the baseline, the workspace contained only the request: no tracker, data file or command existed. The author wanted to record a few daily habits and see a current streak without an account, a hosted service, notifications or third-party packages. The request deliberately left the command names, data model and missed-day behavior undecided, so those became design work rather than assumed requirements.

**Intended outcome:** after a one-time `add`, the daily loop is one `done` command and one `list` command. The data stays in a human-readable local JSON file the author can copy and inspect.

**In scope:** add, done, list and remove; one completion per habit per local date; a day-grace current streak; a default home file with `HABITS_FILE` and `--file` overrides; validated JSON with safe writes; clear errors and exit codes; standard library only.

**Out of scope:** accounts, sync, reminders, notifications, GUI/TUI, backfill or editing past dates, undo, skip tokens/freezes, weekly targets, best streak, history view, charts, export, JSON output, multi-user access, locking, encryption, timezone-aware timestamps, packaging, localization and Windows/Linux compatibility claims.

**Evidence and assumptions:** the only product evidence is the author's request in `IDEA.md`; there was no interview or usage baseline. The design assumes one user, one writer at a time, a few habits, and the machine's local calendar date. These assumptions are stated in the product brief and design record, not presented as validated facts.

## 3. Requirements and acceptance

All requirements below are **accepted** and were **verified locally** at the revision in section 6. "Verified locally" means the named automated test or observed CLI run established the behavior on macOS; it is not a deployment or cross-platform claim.

| ID | Requirement | Observable acceptance | Evidence | Status |
| --- | --- | --- | --- | --- |
| R1 | A user can add a named habit. Names are unique after whitespace normalization and case folding; the first display name is kept. | `add "Read 10 pages"` then `add " read  10 PAGES "` exits 1, names the existing habit, and stores only one record. | `test_add_creates_a_versioned_file_with_normalized_name`, `test_add_duplicate_is_case_insensitive_and_keeps_one_habit`, `test_add_rejects_a_whitespace_only_name`; manual duplicate run. | Verified locally |
| R2 | A user can mark a habit done for today. Repeating the command the same day is harmless. An unknown habit exits 1 without creating a file. | First `done` stores exactly one date and prints the streak; second prints `Already marked`, exits 0, and stores no duplicate. | `test_done_is_idempotent_for_the_same_day`, `test_done_unknown_habit_fails_without_creating_a_file`. | Verified locally |
| R3 | Current streak counts consecutive days ending today; if today is open but yesterday is done, the run remains current until midnight; a fully elapsed missed day resets it to 0; future dates are ignored. | The four states in [the design state table](design.md#streak-state-table) display the stated streak and status. | Ten `StreakTests`; missed-day CLI fixture. | Verified locally |
| R4 | `list` shows every habit with current streak, whether it is done today, and an at-risk note for a non-zero streak still open today. | Table contains all habits; `TODAY` is `done` or `not done`; open run prints `At risk (not done today): ...`; no habits prints guidance. | `test_list_shows_streak_today_status_and_risk_hint`, `test_list_empty_does_not_create_the_file`, `test_list_ignores_future_completions`. | Verified locally |
| R5 | A user can remove a habit and all of its completions. Unknown habit exits 1. | `remove walk` deletes `Walk` and reports the completion count; subsequent `list` omits it. | `test_remove_deletes_the_habit_and_its_history`, `test_remove_unknown_habit_fails`; manual run. | Verified locally |
| R6 | Data lives in one versioned local JSON document. Resolution is `--file` > `HABITS_FILE` > `~/.habits.json`. `list` does not create a missing file; add does, including parent directories. | Produced file is valid JSON; explicit, environment and fake-home paths each write the expected file; empty `list` leaves no file. | `test_default_file_is_created_under_the_home_directory`, `test_habits_file_environment_variable_is_used`, `test_explicit_file_wins_over_the_environment_variable`, `test_list_empty_does_not_create_the_file`, `test_add_creates_missing_parent_directories`; `json.tool` accepted the file. | Verified locally |
| R7 | Invalid data is rejected without overwriting it: malformed JSON, unsupported version, invalid dates, duplicate names. Writes are atomic and leave no temporary file on success. | Corrupt input exits 2, names the line/column, and remains byte-for-byte unchanged; no `.tmp` remains after a successful add. | `test_corrupt_json_is_reported_and_not_overwritten`, `test_unsupported_schema_version_is_reported`, `test_boolean_schema_version_is_rejected`, `test_invalid_completion_date_is_reported`, `test_duplicate_names_in_the_file_are_reported`, `test_successful_write_leaves_no_temporary_file`; manual corrupt run. | Verified locally |
| R8 | The CLI has discoverable help, stable success/error output and exit codes 0 (success), 1 (input/domain) and 2 (data/usage). | `--help` exits 0 and explains the grace rule; unknown commands exit 2 with argparse usage; duplicate/unknown habits exit 1 on stderr. | `test_help_exits_zero_and_explains_streak_grace`, `test_unknown_command_is_a_usage_error`; manual runs. | Verified locally |
| R9 | The tool uses the Python standard library only, is one runnable file, and uses Python 3.9+ syntax. | Imports resolve without third-party packages; suite passes on 3.14.7 and 3.9.6. | Import list; both unittest runs. | Verified locally, macOS only |

**Quality and operating constraints:**

- **Data safety (accepted):** the tool must never silently replace an invalid file; a failed read/write must be diagnosable. Verified above. Crash-level durability and directory `fsync` were not tested.
- **Privacy and dependency surface (accepted):** no network, account, telemetry or third-party package. Verified by inspection and the import list.
- **Scale and latency (no numeric target):** the assumed workload is a few habits on a personal machine. No benchmark was set; a whole-file rewrite is accepted at this scale.
- **Compatibility (accepted with limits):** Python 3.9+ syntax and macOS behavior; Linux, Windows and other Python versions remain unverified.
- **Accessibility (limited):** output is plain text with labels and no color-only encoding. Terminal/screen-reader behavior was not assessed.

**Open product decisions (not blocking):** backfilling past days, best streak/history, skip days or weekly targets, timezone-aware boundaries. Owner: author. These are recorded in [product.md](product.md#open-decisions-and-owner) and were not treated as requirements.

## 4. Solution design

**Baseline:** greenfield. When the change started, the workspace contained only `IDEA.md`; no implementation, schema or running behavior existed.

**Affected software type:** `library-cli` — the change is a command surface, a file format and error/exit behavior. Frontend, backend and AI are **not affected**: there is no UI, service, database, network boundary or model. Because there is one local component, there is no cross-type seam and no C4/sequence diagram; the command surface, schema and streak state table in [design.md](design.md#linked-design-artifacts) are the artifacts a reviewer can judge.

**Selected approach (accepted):**

- **Streak:** day-grace calendar streak. Today completed → count back from today. Today open, yesterday completed → count back from yesterday and show `not done` plus an at-risk line. Otherwise 0. A full missed day resets. Future dates are ignored.
- **Storage:** one versioned JSON object; each habit holds `name`, `created` and a sorted, unique array of ISO completion dates. Missing file = empty database. Writes validate first, write a temporary file in the same directory, `fsync`, then `os.replace`.
- **Surface:** name-addressed `add`, `done`, `remove`, `list`; whitespace-normalized, case-insensitive matching; global `--file` before the command; `HABITS_FILE` and `~/.habits.json` fallbacks.
- **Errors:** domain errors exit 1; data and usage errors exit 2; expected errors print one diagnostic line, not a traceback.

**Alternatives and why they were rejected:** strict "must be done today" streak (misreports a run for most of the day); skip-token or weekly adherence (changes the meaning of "streak" and adds state); date-indexed map (per-habit history and removal become awkward); append-only event log (needs replay and compaction); ID-addressed commands (requires a lookup before each action); interactive menu (not scriptable). The full comparison, trade-offs and failure behavior are in [design.md](design.md).

**Decision owner:** the author, who is the sole user. Status: accepted 2026-11-15. Revisit if backfill, timezone travel, multiple writers or a best-streak/history need makes the rule or schema insufficient.

## 5. Implementation strategy and actual changes

The delivered slice was ordered so the risky behavior was observable early:

1. Implement the model, validation and store (`load`, `save`, `add_habit`, `mark_done`, `remove_habit`, `current_streak`).
2. Implement the CLI surface, output and exit handling.
3. Add a standard-library suite around the pure streak rules and the CLI paths, including corrupt data and idempotency.
4. Fix the failures the suite exposed, reconcile the documentation and perform the review pass.

**Actual changes:**

- [`habits.py`](../habits.py) — the complete single-file tool.
- [`test_habits.py`](../test_habits.py) — 33 standard-library tests.
- [`README.md`](../README.md) — purpose, exact quickstart, command reference, streak rules, data file, tests, limits.
- [`docs/product.md`](product.md), [`docs/design.md`](design.md), [`docs/verification.md`](verification.md), this ECR and [`EVAL.md`](../EVAL.md).

**Prerequisites, migrations, rollback:** none. There was no prior schema or consumer. Rollback is deleting the script and optionally the data file; no migration was written. The CLI only writes after a successful validation, so a bad command does not damage existing data. There is no release step and no remaining implementation blocker.

**Deviations from the design:** none in behavior. The review tightened validation (exact date shape, boolean schema version) and diagnostics (duplicate name uses the stored display name); both are consistent with the accepted design.

## 6. Verification and release

**Checked revision:** local files at [`habits.py`](../habits.py) SHA-256 `87fca0b5c6bbdb605541f14bd388a3127021509ea464a7a58b7a9f844a600bd2` and [`test_habits.py`](../test_habits.py) SHA-256 `0d965ce6f0eac4ce23b9e68992d4dac647edddee721f64f722b92a5acdc8870a`. Local-only, not published; there is no commit URL.

**Environment:** macOS (Darwin); Python 3.14.7 (`python3`) and 3.9.6 (`/usr/bin/python3`); local date 2026-11-15 for CLI runs; no network.

**Observed results:**

- `python3 -m unittest -v` → `Ran 33 tests ... OK`.
- `/usr/bin/python3 -m unittest -v` → `Ran 33 tests ... OK`.
- `python3 -m py_compile habits.py test_habits.py` → exit 0.
- CLI add/done/list/remove sequence produced the documented output; the JSON file passed `python3 -m json.tool`.
- A duplicate add and an unknown `done` exited 1 with one-line diagnostics.
- A corrupt file exited 2 and was left byte-for-byte unchanged.
- A missed-day fixture displayed streak 3 (`done`), streak 2 (`not done`, at risk) and streak 0 (`not done`).

The exact commands, transcripts and hashes are in [verification.md](verification.md).

**Failed, skipped or unavailable checks:** crash injection around `fsync`/`os.replace`, concurrent writers, Linux/Windows, Python versions outside 3.14.7 and 3.9.6, real midnight/timezone rollover, Unicode display width and long-term usability were not exercised. These remain explicit coverage gaps, not passing results.

**Documentation reconciliation:** README, product, design, verification and this ECR agree on the 33-test result, the streak rule, the exit codes, the schema and the local-only status. Stale test counts found during review were corrected.

**Release:** not performed and not applicable. There is no package, installer, deployed target or published URL; no production claim is made.

## 7. Decision history and references

| Date | Decision | Owner | Rationale |
| --- | --- | --- | --- |
| 2026-11-15 | Use a day-grace calendar streak rather than strict-today or skip-token adherence. | Author | Matches how a "current" run is described; a day is not missed until it ends; avoids punitive morning zeros. |
| 2026-11-15 | Store per-habit sorted date arrays in one versioned JSON document. | Author | Simple per-habit history, human-readable file and direct streak reads at personal scale. |
| 2026-11-15 | Use name-addressed subcommands with case-insensitive matching. | Author | The daily action needs no ID lookup; a handful of habits are memorable by name. |
| 2026-11-15 | Include `remove`; exclude backfill, undo, history and best streak. | Author | `remove` is needed to correct a typo; the rest is deferred scope. |
| 2026-11-15 | Record only the local date; reject invalid data and write atomically. | Author | One clear day model; no silent corruption or overwrite. |
| 2026-11-15 | Review fixes: exact date shape, boolean version rejection, duplicate-name diagnostic, guarded mkdir. | Author | Restore intended validation and make failures diagnosable; no behavior expansion. |

**Open questions:** backfill policy, best streak/history, timezone-aware boundaries and multi-writer support remain undecided and deferred. Owner: author. None blocks the delivered slice.

**References:**

- Request: [`IDEA.md`](../IDEA.md)
- Product intent: [product.md](product.md)
- Design decision: [design.md](design.md)
- Verification evidence: [verification.md](verification.md)
- User entry point: [README.md](../README.md)
- Process evaluation: [EVAL.md](../EVAL.md)
