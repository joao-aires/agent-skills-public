# habits.py

A small local habit tracker for a handful of daily habits. Mark today's habit done, see its current streak, and keep everything in one readable JSON file. Standard library only; no account, server or install step.

**Status:** Implemented and locally verified on macOS with Python 3.14.7 and 3.9.6. This is a personal tool, not a published package or hosted service.

## Prerequisites

- Python 3.9 or newer (`python3 --version`).
- A terminal. No third-party packages.
- A writable home directory, or a path passed with `--file`.

Only macOS was exercised. Linux and Windows are plausible but unverified.

## Quickstart

Run these from this directory. The demo file keeps the trial away from your real data.

```sh
python3 habits.py --file ./demo.json add "Read 10 pages"
python3 habits.py --file ./demo.json add "Walk"
python3 habits.py --file ./demo.json done "Read 10 pages"
python3 habits.py --file ./demo.json list
```

Expected output (the date and streaks depend on when you run it; this was recorded on 2026-11-15):

```text
Added "Read 10 pages".
Added "Walk".
Marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
NAME           STREAK  TODAY
Read 10 pages       1  done
Walk                0  not done
```

Remove the demo file when finished:

```sh
rm ./demo.json
```

## Real use

Without `--file`, the tool uses `~/.habits.json`:

```sh
python3 habits.py add "Read 10 pages"
python3 habits.py done "Read 10 pages"
python3 habits.py list
```

To keep the file somewhere else, use either form:

```sh
python3 habits.py --file ~/Documents/habits.json list
HABITS_FILE=~/Documents/habits.json python3 habits.py list
```

`--file` is a global option and goes **before** the command. Precedence is `--file` > `HABITS_FILE` > `~/.habits.json`.

## Commands

| Command | What it does |
| --- | --- |
| `add NAME` | Create a habit. Names are unique, ignoring case and repeated spaces. |
| `done NAME` | Mark the habit done for today. Running it again the same day is harmless. |
| `list` | Show every habit with its current streak and whether it is done today. |
| `remove NAME` | Delete the habit and its completion history immediately. No confirmation. |

Names are matched case-insensitively with whitespace collapsed, so `done "read 10 PAGES"` finds `Read 10 pages`. The display name from the first `add` is kept.

Exit codes: `0` success, `1` input error (unknown or duplicate habit, empty name), `2` data or usage error (bad JSON, unsupported schema, unreadable/unwritable file, invalid arguments).

## Streak rules

A streak is the number of consecutive days completed, ending today or yesterday:

- If **today is done**, the streak counts backwards from today.
- If **today is not done but yesterday is**, the streak counts backwards from yesterday and stays current until the day ends. `list` shows that habit as `not done` and prints an at-risk line.
- If **yesterday is not done either**, the streak is `0`. One fully elapsed day without a completion resets it.
- Future dates are ignored. There is no backfill, undo, skip token or freeze in this version.

`done` records only the current **local** calendar date. Changing timezones can change which date a new completion receives.

Example with today unmarked:

```text
NAME      STREAK  TODAY
Journal        3  done
Stretch        2  not done
Meditate       0  not done

At risk (not done today): Stretch
```

`Stretch` was completed the two previous days, so its streak is still current. `Meditate` last completed three days ago, so it has reset.

## Data file

The file is indented JSON with a schema version:

```json
{
  "version": 1,
  "habits": [
    {
      "name": "Read 10 pages",
      "created": "2026-11-15",
      "completions": [
        "2026-11-15"
      ]
    }
  ]
}
```

- Completions are unique ISO dates, sorted on save.
- The file is validated before any write. Malformed JSON, a wrong `version`, invalid dates or duplicate names exit `2` and leave the file untouched.
- Writes go to a temporary file and are atomically replaced, so an interrupted command should not leave a half-written document.
- A missing file is treated as empty. `list` does not create it; `add` creates it. `done` requires an existing habit, so it cannot create a file on its own.
- There is no locking. Run one command at a time; a second concurrent writer can overwrite the first.

**Back up by copying the file** before hand-editing or experimenting:

```sh
cp ~/.habits.json ~/.habits.json.backup
```

To reset, delete the data file (after backing it up) or `remove` habits individually. There is no import or merge command.

## Tests

```sh
python3 -m unittest -v
```

Expected: 33 tests, all `ok`. The suite covers streak boundaries, idempotent marking, name matching, missing and corrupt files, schema validation, path precedence, atomic-write cleanup and usage exit codes.

## Documentation map

| Document | Purpose |
| --- | --- |
| [docs/product.md](docs/product.md) | Problem, audience, scope, success signals, risks and open decisions. |
| [docs/ecr.md](docs/ecr.md) | The change record: requirements, design summary, implementation and evidence. |
| [docs/design.md](docs/design.md) | The streak, storage and command-surface decisions with alternatives. |
| [docs/verification.md](docs/verification.md) | Exact commands, observed results and coverage gaps. |
| [EVAL.md](EVAL.md) | Evaluation of the skill-guided process that produced this tool. |

## Limitations and unsupported paths

- Today only: no backfill, editing past days, undo or history view.
- No best streak, charts, export, JSON output, reminders or notifications.
- One user and one writer; no sync, accounts or conflict handling.
- Local calendar dates only; no timezone-aware timestamps.
- No encryption. Do not put secrets in habit names.
- No package, installer, license or support commitment. `remove` is immediate and permanent.
- Display alignment is byte-count based and may look off with double-width scripts.

## Support and contribution

This is a personal utility with no issue tracker or contribution process. Copy and adapt the file for your own use. No license is granted; do not redistribute it without permission.
