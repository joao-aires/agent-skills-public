# Product brief: habits.py

**Status:** Accepted product intent. The implementation and local verification are recorded in [the ECR](ecr.md); this document owns *why* the tool exists, not its build status.

## Problem and audience

The author wants to track a few daily habits without an account, a cloud service, notifications or a dependency tree. The request is recorded in [`IDEA.md`](../IDEA.md): mark a habit done for today, see the current streak, keep everything in a local JSON file, and use no third-party packages. The command names, data model and missed-day behavior were explicitly left open.

The primary audience is **one person at a terminal on their own machine**. A secondary audience is anyone who wants to copy a single Python file and own their data. This is not a team tool, a mobile app or a hosted service. There is no user research beyond the request; claims here are about a personal utility, not a market.

Today the author has no tracker in this workspace. The alternative is ad-hoc memory or a notes file. Doing nothing is acceptable; this tool is worth building only if it is faster than that ad-hoc habit.

## Desired outcome

A person can add a small set of habits once, then spend one short command per day marking one done and one command seeing where every habit stands. The stored file stays human-readable and portable.

The smallest useful slice is **add, done, list, with an explicit streak rule**. `remove` is included because a mistyped habit otherwise cannot be corrected from the CLI. Everything else is deferred.

## In scope

- `add`, `done`, `list` and `remove` commands over a local JSON document.
- One completion per habit per local calendar day; `done` is idempotent for today.
- A current streak per habit, including a defined rule for the current day and for missed days.
- A default data file at `~/.habits.json`, overridable by `--file` or `HABITS_FILE`.
- Clear domain errors (exit 1), data errors (exit 2) and safe refusal to overwrite an invalid file.
- Python standard library only; one runnable file.

## Non-goals

- Accounts, sync, sharing, cloud storage or multi-device behavior.
- Reminders, notifications, a GUI, a TUI or a mobile app.
- Backfilling or editing past dates, undo, skip tokens, streak freezes or weekly quotas.
- Best-streak, history views, charts, export or machine-readable output.
- Multi-user access, file locking or conflict resolution.
- Packaging, publishing, installers or a service.
- Encryption, secrets management or regulatory data handling.
- Timezone-aware instants or localization; the tool records a **local calendar date**.

## Success signals

These are observable product outcomes, not adoption metrics. Evidence for each is in [verification](verification.md).

| # | Signal |
| --- | --- |
| S1 | From an empty file, adding two habits and marking one done makes `list` show one habit as `done` with streak 1 and the other as `not done` with streak 0. |
| S2 | Running `done` twice for the same habit and day stores one completion and exits 0 both times. |
| S3 | A habit completed yesterday but not yet today still shows its streak as current, with `not done` and an at-risk hint. |
| S4 | A habit whose most recent completion is two or more days old shows streak 0. |
| S5 | Adding a duplicate name that differs only by case or spacing exits 1 and does not create a second habit. |
| S6 | A corrupt or unsupported data file exits 2 with a diagnostic and is left byte-for-byte unchanged. |
| S7 | The data file is valid, indented JSON that a person can read and back up. |

## Constraints and assumptions

- **Runtime:** Python 3.9 or newer syntax; only the standard library. Verified on Python 3.14.7 and 3.9.6 on macOS. Other platforms are unverified.
- **Form:** one `habits.py` file, no package layout, no install step.
- **Storage:** one local JSON document. The user is assumed to be the only writer and to run one command at a time.
- **Clock:** `date.today()` in the machine's local timezone. A completion belongs to the local date on which it was recorded.
- **Authority:** the user owns the file and may hand-edit it; the tool validates it before writing.
- **Exit codes:** 0 success, 1 input/domain error, 2 data or usage error.

## Risks and trade-offs

| Risk | Disposition |
| --- | --- |
| Streak pressure can feel punitive. | The current day stays open until midnight; no notifications or loss framing beyond a factual reset and an "at risk" line. |
| Travel or a timezone change can attribute a completion to the "wrong" day. | Accepted for a personal tool; local date is the explicit model. Revisit only if it causes real loss. |
| Hand-editing can corrupt the file. | Full validation, a precise error, exit 2 and no overwrite; README recommends copying the file before editing. |
| Two simultaneous commands can lose one write. | Accepted; no locking. Documented as a single-user assumption. |
| A global default file can surprise a user trying a demo. | The README's quickstart uses an explicit `--file ./demo.json`; the real path is stated. |
| A missed day erases visible progress. | That is the chosen semantic; history remains in the file, so a future "best streak" feature can use it. |

## Open decisions and owner

Owner for all product decisions is the author, who is also the sole user.

| Decision | Status | Revisit trigger |
| --- | --- | --- |
| Allow backfilling a missed day? | Not in this slice. | The author misses marking because of travel or a late night often enough that the data feels wrong. |
| Show best streak or full history? | Deferred. | The current streak alone stops being motivating, or the stored history feels wasted. |
| Add skip days, freezes or weekly targets? | Deferred; would change the streak definition. | Daily adherence proves too rigid for the habits actually tracked. |
| Timezone-aware day boundaries? | Deferred; local date accepted. | Travel causes a completion to land on the wrong day in practice. |

## Links

- Source request: [`IDEA.md`](../IDEA.md)
- Change record: [docs/ecr.md](ecr.md)
- Design decision: [docs/design.md](design.md)
- Local verification: [docs/verification.md](verification.md)
- User entry point: [README.md](../README.md)
