# Personal habit tracker: product outcome

Status: **proposed** first slice. This record owns product intent only; implementation and verification are recorded in the [ECR](../change/ecr.md). The implementation request is the only product authority; no separate product review or real-use evidence exists.

## Problem and audience

The audience is one person tracking a small set of daily habits on a local machine. Today the owner has to remember what was done, count consecutive days by hand, or keep an unstructured note. That makes two questions expensive to answer at the moment they matter:

- Did I do this today?
- Is the run still alive, or did I miss a day?

The supplied request (`IDEA.md`, 2026-11-15) describes this need. No interviews, usage data or retention evidence were supplied. This is a personal tool, not a commercial product.

## Desired outcome

The owner can add a few daily habits, mark one done for today with one command, and see each habit's current streak and today's status without opening the JSON file. The state survives restarts in one local file. A missed day is visible in the result rather than silently ignored.

The useful outcome is a **correct daily answer**, not a dashboard: a short list that distinguishes "done today", "run still alive from yesterday", and "run broken".

## Scope and non-goals

In scope for this slice:

- 3–10 daily habits with human names and generated ids.
- One completion per local calendar day per habit.
- Current streak, longest streak, today's status and last completion.
- Backfill and undo for a specific date.
- One plaintext JSON file, atomic replacement, stdlib-only Python.
- A small command surface with explicit errors and exit codes.

Non-goals:

- Accounts, sync, multi-user access, sharing, mobile or a web UI.
- Reminders, notifications, scheduling or calendar integration.
- Weekly quotas, planned rest days, freeze tokens or per-habit schedules.
- Time-of-day tracking, timezone conversion, durations or notes per completion.
- Analytics, charts, gamification, import/export, encryption or backup automation.
- Packaging, installation as a global command or a release channel.

## Success signal

Proposed, not yet measured in real use:

- The owner can answer both questions from one `list` command without manual date counting.
- After a simulated four-day journey (two consecutive completions, a missed day, then today), `list` reports the expected streak and `TODAY` value. This is encoded in the automated acceptance suite.
- A week of real use requires no manual inspection of the JSON file and no manual date counting. **Not measured.**

A passing test suite proves the defined behavior, not that the habit tracker changes the owner's behavior.

## Constraints and dependencies

- Python 3 standard library only. No network access, credentials or third-party packages.
- One local JSON file at `--file`, `HABITS_FILE`, `$XDG_DATA_HOME/habits/habits.json`, or `~/.local/share/habits/habits.json`, in that precedence order.
- Target environment: macOS 27.0.1 with Python 3.14.7. Other platforms and interpreter versions are outside the verified scope; see [verification](../evidence/verification.md).
- The file is plaintext and created with user-only permissions by the temporary-file path. The owner is responsible for backups and access to the machine.
- The tool uses the machine's local calendar date. `--today` overrides it for tests, demos or timezone correction.
- A missed day is defined as a calendar date with no completion. The chosen semantics are recorded in the [design proposal](../design/design-proposal.md).

## Open decisions

| Decision | Owner | Evidence that would settle it | Current disposition |
| --- | --- | --- | --- |
| Whether planned rest days or weekly targets are needed | Requester | A repeated need during real use, or a habit that is not daily | Deferred; current rule treats every missed day as a break |
| Whether to install as a `habits` command | Requester | Friction from typing `python3 habits.py` | Deferred; run from the repository |
| Whether real use improves consistency | Requester | One week of personal use | Not measured |
| Whether to support non-daily schedules | Requester | A habit whose intended cadence is not daily | Out of scope for this slice |

## Links

- [Design proposal: streak and missed-day semantics](../design/design-proposal.md)
- [Streak cases and worked timeline](../design/streak-cases.md)
- [Engineering change record](../change/ecr.md)
- [Verification evidence](../evidence/verification.md)
- [Repository entry point](../../README.md)
