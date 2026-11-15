#!/usr/bin/env python3
"""habits: a small, local daily-habit tracker.

Streak rule: a current streak is a run of consecutive calendar days ending
today, or ending yesterday when today has not been marked yet. A missed
calendar day breaks the run. Future dates never count.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import unicodedata
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, Sequence

VERSION = "1.0.0"
SCHEMA_VERSION = 1
DEFAULT_FILENAME = "habits.json"
RECENT_DAYS = 7


class HabitError(Exception):
    """A user-facing data or habit error (exit code 1)."""


@dataclass
class Habit:
    id: str
    name: str
    created_on: date
    completions: set[date] = field(default_factory=set)

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "created_on": self.created_on.isoformat(),
            "completions": sorted(day.isoformat() for day in self.completions),
        }


# ---------------------------------------------------------------------------
# Date and streak rules
# ---------------------------------------------------------------------------


def parse_date(value: str, label: str = "date") -> date:
    """Parse a strict YYYY-MM-DD date, with a clear error for the CLI."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise HabitError(f"invalid {label} {value!r}; use YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise HabitError(f"invalid {label} {value!r}; use YYYY-MM-DD") from None


def current_streak(completions: Iterable[date], today: date) -> int:
    """Count the run ending today, or yesterday when today is unmarked."""
    days = {day for day in completions if day <= today}
    if today in days:
        cursor = today
    elif today - timedelta(days=1) in days:
        cursor = today - timedelta(days=1)
    else:
        return 0

    streak = 0
    while cursor in days:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def longest_streak(completions: Iterable[date], today: date | None = None) -> int:
    """Count the longest consecutive run, optionally ignoring future dates."""
    days = sorted({day for day in completions if today is None or day <= today})
    best = 0
    run = 0
    previous: date | None = None
    for day in days:
        if previous is not None and day == previous + timedelta(days=1):
            run += 1
        else:
            run = 1
        best = max(best, run)
        previous = day
    return best


def plural_days(count: int) -> str:
    return f"{count} day" if count == 1 else f"{count} days"


def plural_completions(count: int) -> str:
    return f"{count} completion" if count == 1 else f"{count} completions"


def _argument_date(value: str) -> date:
    """Argparse type: malformed dates are usage errors (exit 2)."""
    try:
        return parse_date(value)
    except HabitError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from None


# ---------------------------------------------------------------------------
# Data file
# ---------------------------------------------------------------------------


def resolve_data_path(explicit: str | None) -> Path:
    """Resolve the data file: --file, HABITS_FILE, XDG data home, home."""
    if explicit:
        return Path(explicit).expanduser()
    env_path = os.environ.get("HABITS_FILE")
    if env_path:
        return Path(env_path).expanduser()
    xdg = os.environ.get("XDG_DATA_HOME")
    base = Path(xdg).expanduser() if xdg else Path.home() / ".local" / "share"
    return base / "habits" / DEFAULT_FILENAME


def _error(path: Path, message: str) -> HabitError:
    return HabitError(f"{path}: {message}")


def load_store(path: Path) -> list[Habit]:
    if not path.exists():
        return []

    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise _error(path, f"cannot read data file ({exc.strerror or exc})") from None

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise _error(
            path,
            f"not valid JSON ({exc.msg} at line {exc.lineno} column {exc.colno})",
        ) from None

    if not isinstance(data, dict):
        raise _error(path, "expected a JSON object at the top level")

    version = data.get("version")
    if version != SCHEMA_VERSION:
        raise _error(
            path,
            f"unsupported data version {version!r}; this tool reads version "
            f"{SCHEMA_VERSION}",
        )

    raw_habits = data.get("habits")
    if not isinstance(raw_habits, list):
        raise _error(path, "'habits' must be a list")

    habits: list[Habit] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(raw_habits, start=1):
        if not isinstance(item, dict):
            raise _error(path, f"habit {index} must be an object")

        habit_id = item.get("id")
        name = item.get("name")
        created = item.get("created_on")
        completions = item.get("completions", [])

        if not isinstance(habit_id, str) or not habit_id.strip():
            raise _error(path, f"habit {index} has no valid id")
        if habit_id in seen_ids:
            raise _error(path, f"duplicate habit id {habit_id!r}")
        if not isinstance(name, str) or not name.strip():
            raise _error(path, f"habit {habit_id!r} has no valid name")
        if not isinstance(created, str):
            raise _error(path, f"habit {habit_id!r} has no valid created_on")
        if not isinstance(completions, list) or not all(
            isinstance(day, str) for day in completions
        ):
            raise _error(path, f"habit {habit_id!r} has invalid completions")

        try:
            created_date = parse_date(created, "created_on")
            completion_dates = {
                parse_date(day, "completion date") for day in completions
            }
        except HabitError as exc:
            raise _error(path, f"habit {habit_id!r}: {exc}") from None

        seen_ids.add(habit_id)
        habits.append(
            Habit(
                id=habit_id,
                name=name,
                created_on=created_date,
                completions=completion_dates,
            )
        )

    return habits


def save_store(path: Path, habits: Sequence[Habit]) -> None:
    """Write atomically so a crash cannot leave a half-written data file."""
    payload = {
        "version": SCHEMA_VERSION,
        "habits": [habit.to_dict() for habit in habits],
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise _error(
            path, f"cannot create data directory ({exc.strerror or exc})"
        ) from None

    temp_name: str | None = None
    try:
        fd, temp_name = tempfile.mkstemp(
            prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
        )
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
        temp_name = None
    except OSError as exc:
        raise _error(path, f"cannot write data file ({exc.strerror or exc})") from None
    finally:
        if temp_name is not None:
            try:
                os.unlink(temp_name)
            except OSError:
                pass


# ---------------------------------------------------------------------------
# Habit helpers
# ---------------------------------------------------------------------------


def slugify(name: str) -> str:
    ascii_name = (
        unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    )
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")
    return slug or "habit"


def unique_id(name: str, habits: Sequence[Habit]) -> str:
    base = slugify(name)
    existing = {habit.id for habit in habits}
    if base not in existing:
        return base
    suffix = 2
    while f"{base}-{suffix}" in existing:
        suffix += 1
    return f"{base}-{suffix}"


def find_habit(habits: Sequence[Habit], reference: str) -> Habit:
    """Find by exact id, then case-insensitive id, then name."""
    reference = reference.strip()
    if not reference:
        raise HabitError("habit reference cannot be empty")

    for habit in habits:
        if habit.id == reference:
            return habit

    matches = [
        habit
        for habit in habits
        if habit.id.casefold() == reference.casefold()
        or habit.name.casefold() == reference.casefold()
    ]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise HabitError(f"no habit matches {reference!r}; run 'list' to see ids")
    raise HabitError(f"{reference!r} matches more than one habit; use its id")


def require_name(raw_parts: Sequence[str]) -> str:
    name = " ".join(part.strip() for part in raw_parts).strip()
    name = re.sub(r"\s+", " ", name)
    if not name:
        raise HabitError("habit name cannot be empty")
    if len(name) > 80:
        raise HabitError("habit name is too long (maximum 80 characters)")
    return name


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def cmd_add(args: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    name = require_name(args.name)
    if any(habit.name.casefold() == name.casefold() for habit in habits):
        raise HabitError(f"a habit named {name!r} already exists")

    habit = Habit(id=unique_id(name, habits), name=name, created_on=today)
    habits.append(habit)
    save_store(path, habits)
    print(f'Added "{habit.name}" with id {habit.id}.')
    return 0


def cmd_list(_: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    if not habits:
        print('No habits yet. Add one with: python3 habits.py add "Read"')
        return 0

    header = ("ID", "NAME", "STREAK", "TODAY", "LAST DONE")
    rows: list[tuple[str, str, str, str, str]] = []
    for habit in habits:
        past = [day for day in habit.completions if day <= today]
        rows.append(
            (
                habit.id,
                habit.name,
                str(current_streak(habit.completions, today)),
                "yes" if today in habit.completions else "no",
                max(past).isoformat() if past else "-",
            )
        )

    widths = [
        max(len(header[column]), *(len(row[column]) for row in rows))
        for column in range(len(header))
    ]
    print("  ".join(header[column].ljust(widths[column]) for column in range(5)).rstrip())
    for row in rows:
        cells = [
            row[0].ljust(widths[0]),
            row[1].ljust(widths[1]),
            row[2].rjust(widths[2]),
            row[3].ljust(widths[3]),
            row[4].ljust(widths[4]),
        ]
        print("  ".join(cells).rstrip())
    return 0


def _streak_description(habit: Habit, today: date) -> str:
    streak = current_streak(habit.completions, today)
    if streak == 0:
        past = [day for day in habit.completions if day <= today]
        if past:
            return f"0 days (broken; last done {max(past).isoformat()})"
        return "0 days (no completions yet)"
    if today in habit.completions:
        return f"{plural_days(streak)} (through {today.isoformat()})"
    anchor = today - timedelta(days=1)
    return (
        f"{plural_days(streak)} (through {anchor.isoformat()}; "
        "today not marked)"
    )


def cmd_show(args: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    habit = find_habit(habits, args.habit)
    past = [day for day in habit.completions if day <= today]

    print(f"{habit.name} ({habit.id})")
    print(f"  Created:        {habit.created_on.isoformat()}")
    print(f"  Current streak: {_streak_description(habit, today)}")
    print(f"  Longest streak: {plural_days(longest_streak(habit.completions, today))}")
    print(f"  Today:          {'done' if today in habit.completions else 'not done'}")
    print(f"  Last done:      {max(past).isoformat() if past else '-'}")
    print("  Recent:")
    for offset in range(RECENT_DAYS - 1, -1, -1):
        day = today - timedelta(days=offset)
        marker = "done" if day in habit.completions else "-"
        label = "today" if offset == 0 else day.strftime("%a")
        print(f"    {day.isoformat()}  {label:<5}  {marker}")
    return 0


def _mark(habit: Habit, day: date) -> bool:
    if day in habit.completions:
        return False
    habit.completions.add(day)
    return True


def cmd_done(args: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    habit = find_habit(habits, args.habit)
    day = args.date or today
    if day > today:
        raise HabitError(
            f"cannot mark a future date ({day.isoformat()}) as done; today is "
            f"{today.isoformat()}"
        )

    if _mark(habit, day):
        save_store(path, habits)
        action = "Marked"
    else:
        action = "Already marked"
    streak = current_streak(habit.completions, today)
    print(
        f'{action} "{habit.name}" done on {day.isoformat()}. '
        f"Current streak: {plural_days(streak)}."
    )
    return 0


def cmd_undo(args: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    habit = find_habit(habits, args.habit)
    day = args.date or today
    if day not in habit.completions:
        raise HabitError(
            f'"{habit.name}" was not marked done on {day.isoformat()}'
        )

    habit.completions.remove(day)
    save_store(path, habits)
    streak = current_streak(habit.completions, today)
    print(
        f'Removed "{habit.name}" from {day.isoformat()}. '
        f"Current streak: {plural_days(streak)}."
    )
    return 0


def cmd_remove(args: argparse.Namespace, habits: list[Habit], path: Path, today: date) -> int:
    habit = find_habit(habits, args.habit)
    if not args.yes:
        raise HabitError(
            f'refusing to remove "{habit.name}" without --yes '
            "(this deletes its history)"
        )
    habits.remove(habit)
    save_store(path, habits)
    count = len(habit.completions)
    print(
        f'Removed habit "{habit.name}" ({habit.id}) with '
        f"{plural_completions(count)}."
    )
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    examples = """examples:
  python3 habits.py add "Read 30 minutes"
  python3 habits.py done read-30-minutes
  python3 habits.py list
  python3 habits.py show read-30-minutes
  python3 habits.py undo read-30-minutes
  HABITS_FILE=~/my-habits.json python3 habits.py list

data file:
  --file PATH, else $HABITS_FILE, else $XDG_DATA_HOME/habits/habits.json,
  else ~/.local/share/habits/habits.json

streak rule:
  consecutive calendar days ending today, or ending yesterday when today is
  not marked yet. A missed day resets the streak. Future dates never count.

exit codes:
  0 success, 1 data/habit error, 2 usage error
"""
    parser = argparse.ArgumentParser(
        prog="habits.py",
        description="Track a few daily habits in a local JSON file.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="data file to use (default: see below)",
    )
    parser.add_argument(
        "--today",
        metavar="YYYY-MM-DD",
        type=_argument_date,
        help="override today's date (for tests, demos or timezone correction)",
    )
    parser.add_argument(
        "--version", action="version", version=f"habits.py {VERSION}"
    )
    subparsers = parser.add_subparsers(dest="command", metavar="command")

    add = subparsers.add_parser("add", help="add a habit")
    add.add_argument("name", nargs="+", metavar="NAME", help="habit name")
    add.set_defaults(handler=cmd_add)

    listing = subparsers.add_parser("list", help="list habits and current streaks")
    listing.set_defaults(handler=cmd_list)

    done = subparsers.add_parser("done", help="mark a habit done for today")
    done.add_argument("habit", metavar="HABIT", help="habit id or name")
    done.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        type=_argument_date,
        help="mark a different date instead of today (backfill)",
    )
    done.set_defaults(handler=cmd_done)

    undo = subparsers.add_parser("undo", help="remove a completion for today")
    undo.add_argument("habit", metavar="HABIT", help="habit id or name")
    undo.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        type=_argument_date,
        help="undo a different date instead of today",
    )
    undo.set_defaults(handler=cmd_undo)

    show = subparsers.add_parser("show", help="show one habit and its recent days")
    show.add_argument("habit", metavar="HABIT", help="habit id or name")
    show.set_defaults(handler=cmd_show)

    remove = subparsers.add_parser("remove", help="delete a habit and its history")
    remove.add_argument("habit", metavar="HABIT", help="habit id or name")
    remove.add_argument(
        "--yes", action="store_true", help="confirm permanent deletion"
    )
    remove.set_defaults(handler=cmd_remove)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    if not arguments:
        parser.print_help()
        return 0

    args = parser.parse_args(arguments)
    if not getattr(args, "handler", None):
        parser.print_help()
        return 0

    try:
        today = args.today or date.today()
        path = resolve_data_path(args.file)
        habits = load_store(path)
        return args.handler(args, habits, path, today)
    except HabitError as exc:
        print(f"habits: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
