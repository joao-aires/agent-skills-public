# habits

A small local command-line habit tracker for one person. It records daily completions in one JSON file and shows each habit's current streak without a server, account or third-party package.

Status: **first slice, implemented and verified locally** on macOS 27.0.1 with Python 3.14.7. It is a personal tool, not a released product. There has been no real-use trial.

## Quickstart

Prerequisite: Python 3 on the machine. The verified interpreter is CPython 3.14.7; other versions were not tested.

From this directory:

```bash
python3 habits.py list
python3 habits.py add "Read 30 minutes"
python3 habits.py done read-30-minutes
python3 habits.py list
```

Expected result after the last command (the date is today's local date):

```text
ID               NAME             STREAK  TODAY  LAST DONE
read-30-minutes  Read 30 minutes       1  yes    2026-11-15
```

Data defaults to `~/.local/share/habits/habits.json`. To try it without touching that file:

```bash
python3 habits.py --file /tmp/habits-demo.json add "Walk"
python3 habits.py --file /tmp/habits-demo.json done walk
python3 habits.py --file /tmp/habits-demo.json list
```

Global options must come before the command: `python3 habits.py --file PATH --today 2026-11-15 list`.

## What it does

You can add a few habits, mark one done for today, and see the streak and today's status for all of them in one table. You can also backfill a missed day, undo a mark, inspect the last seven days for one habit, and remove a habit with confirmation.

```text
$ python3 habits.py list
ID               NAME             STREAK  TODAY  LAST DONE
read-30-minutes  Read 30 minutes       2  yes    2026-11-15
walk             Walk                  0  no     2026-11-13
```

| Command | What it does |
| --- | --- |
| `python3 habits.py add "Read 30 minutes"` | Add a habit; prints its generated id. Names must be unique, ignoring case. |
| `python3 habits.py list` | Show id, name, current streak, whether today is done, and the last completion. |
| `python3 habits.py done HABIT` | Mark today done. Repeating it is harmless. |
| `python3 habits.py done HABIT --date YYYY-MM-DD` | Backfill a past date. Future dates are refused. |
| `python3 habits.py undo HABIT` | Remove today's completion. |
| `python3 habits.py undo HABIT --date YYYY-MM-DD` | Remove a specific completion, including a future entry from hand-edited data. |
| `python3 habits.py show HABIT` | Show created date, current and longest streak, today, last done, and the last seven days. |
| `python3 habits.py remove HABIT --yes` | Permanently delete the habit and its history. Without `--yes`, it refuses. |

`HABIT` can be the id, the id in any case, or the habit name in any case. Names with spaces work as a quoted reference; the id is the shortest option. `add` accepts unquoted words too: `add Read 30 minutes` creates `read-30-minutes`.

## Streak and missed days

A **current streak** is a run of consecutive calendar days that ends **today**, or ends **yesterday** when today has not been marked yet.

- Done today and yesterday: streak 2, `TODAY yes`.
- Done yesterday but not today: streak stays 2, `TODAY no`. The run is still alive until the end of today.
- Done two days ago but not yesterday or today: streak 0. A missed calendar day breaks the run.
- Miss a day, then mark today: streak 1. The new run starts today.
- A future date never counts. A completion is one local calendar date; there is no time of day.
- The streak is recalculated from stored dates on every read, so undo or a hand edit cannot leave a stale number.

The full case table is in [docs/design/streak-cases.md](docs/design/streak-cases.md). `show` makes the grace day explicit: `2 days (through 2026-11-14; today not marked)`.

## Data file

The file is selected in this order:

1. `--file PATH`
2. `$HABITS_FILE`
3. `$XDG_DATA_HOME/habits/habits.json`
4. `~/.local/share/habits/habits.json`

The file is created on the first write, with parent directories. Writes replace the file atomically. It is plaintext JSON:

```json
{
  "version": 1,
  "habits": [
    {
      "id": "read-30-minutes",
      "name": "Read 30 minutes",
      "created_on": "2026-11-15",
      "completions": ["2026-11-14", "2026-11-15"]
    }
  ]
}
```

A corrupt file or an unsupported `version` is reported and **not overwritten**. Back it up if the history matters. Removal is permanent.

## Documentation map

- [Documentation index and artifact homes](docs/README.md)
- [Product outcome](docs/product/prd.md) — audience, scope, non-goals, success signal
- [Design proposal](docs/design/design-proposal.md) — streak options, tradeoffs, command surface, exit codes
- [Streak cases](docs/design/streak-cases.md) — worked expected results
- [Engineering change record](docs/change/ecr.md) — requirements, implementation, verification, decisions
- [Verification evidence](docs/evidence/verification.md) — commands, actual results, review findings, limits
- [CLI transcript](docs/evidence/cli-transcript.md) and [test output](docs/evidence/test-output.txt) — raw observed evidence

## Development

```bash
python3 -m unittest -v
python3 -m py_compile habits.py test_habits.py
```

The suite has 44 tests: pure streak/date rules, data-path precedence, and the shipped CLI exercised as a subprocess with an isolated data file. The captured run passed (`Ran 44 tests in 4.332s`, `OK`); wall time varies slightly by run; see [verification](docs/evidence/verification.md).

Reset a default data file (permanent):

```bash
rm ~/.local/share/habits/habits.json
```

If you use `--file`, `HABITS_FILE` or `XDG_DATA_HOME`, remove that path instead.

## Support and contribution

This is a personal artifact. There is no public issue tracker, contribution process or support commitment. The owner maintains it locally.

## Status and limits

- **Maturity:** first slice, verified locally; not released, packaged or deployed.
- **Platform:** exercised only on macOS 27.0.1 with CPython 3.14.7.
- **Concurrency:** atomic per write, but no file lock; two simultaneous processes can lose one update.
- **Scope:** daily habits only. No reminders, sync, multi-user access, weekly targets, planned rest days, charts, import/export or encryption.
- **Data:** plaintext; the owner is responsible for backups and machine access.
- **Real use:** not measured. Tests prove the defined behavior, not that the tool improves consistency.
- **License:** no license is declared, so no reuse rights are granted by default.
