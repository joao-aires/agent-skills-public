#!/usr/bin/env python3
"""A small, local daily-habit tracker backed by one JSON file.

Standard library only. See README.md for the command surface and
docs/design.md for the streak and storage decisions.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable

SCHEMA_VERSION = 1
DEFAULT_FILENAME = ".habits.json"


class HabitsError(Exception):
    """A failure with a user-facing message and a process exit code."""

    exit_code = 1


class InputError(HabitsError):
    """Bad user input: unknown or duplicate habit, empty name."""

    exit_code = 1


class DataError(HabitsError):
    """Unreadable, invalid or unwritable data file."""

    exit_code = 2


def normalize_name(name: str) -> str:
    """Collapse surrounding and repeated whitespace."""
    return " ".join(name.split())


def name_key(name: str) -> str:
    """Identity used for lookup; display name keeps its original case."""
    return normalize_name(name).casefold()


def new_db() -> dict:
    return {"version": SCHEMA_VERSION, "habits": []}


def find_habit(db: dict, name: str) -> dict | None:
    key = name_key(name)
    for habit in db["habits"]:
        if name_key(habit["name"]) == key:
            return habit
    return None


def _parse_date(value: object, where: str) -> date:
    if not isinstance(value, str) or len(value) != 10:
        raise DataError(f"{where}: expected a date as YYYY-MM-DD, got {value!r}")
    parts = value.split("-")
    if (
        len(parts) != 3
        or len(parts[0]) != 4
        or len(parts[1]) != 2
        or len(parts[2]) != 2
    ):
        raise DataError(f"{where}: expected a date as YYYY-MM-DD, got {value!r}")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise DataError(f"{where}: invalid date {value!r}: {exc}") from exc


def _validate_db(raw: object, path: Path) -> dict:
    if not isinstance(raw, dict):
        raise DataError(f"{path}: expected a JSON object at the top level")
    version = raw.get("version")
    if isinstance(version, bool) or version != SCHEMA_VERSION:
        raise DataError(
            f"{path}: unsupported schema version {version!r}; "
            f"expected {SCHEMA_VERSION}"
        )
    habits_raw = raw.get("habits")
    if not isinstance(habits_raw, list):
        raise DataError(f"{path}: 'habits' must be a list")

    habits: list[dict] = []
    seen: set[str] = set()
    for index, item in enumerate(habits_raw, start=1):
        where = f"{path}: habit #{index}"
        if not isinstance(item, dict):
            raise DataError(f"{where}: expected an object")
        name = item.get("name")
        if not isinstance(name, str) or not normalize_name(name):
            raise DataError(f"{where}: 'name' must be a non-empty string")
        key = name_key(name)
        if key in seen:
            raise DataError(f"{where}: duplicate habit name {name!r}")
        seen.add(key)
        created = _parse_date(item.get("created"), f"{where}: created")
        completions_raw = item.get("completions")
        if not isinstance(completions_raw, list):
            raise DataError(f"{where}: 'completions' must be a list")
        completions = {
            _parse_date(value, f"{where}: completion").isoformat()
            for value in completions_raw
        }
        habits.append(
            {
                "name": normalize_name(name),
                "created": created.isoformat(),
                "completions": sorted(completions),
            }
        )
    return {"version": SCHEMA_VERSION, "habits": habits}


def load(path: Path) -> dict:
    """Read and validate the data file. A missing file is an empty database."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return new_db()
    except OSError as exc:
        raise DataError(f"cannot read {path}: {exc.strerror or exc}") from exc

    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        raise DataError(
            f"{path} is not valid JSON: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    return _validate_db(raw, path)


def save(path: Path, db: dict) -> None:
    """Write atomically so an interrupted run cannot leave a half-written file."""
    tmp_name = None
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(
            prefix=path.name + ".", suffix=".tmp", dir=str(path.parent)
        )
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(db, handle, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except OSError as exc:
        if tmp_name is not None:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
        raise DataError(f"cannot write {path}: {exc.strerror or exc}") from exc


def add_habit(db: dict, name: str, today: date) -> dict:
    display = normalize_name(name)
    if not display:
        raise InputError("habit name must not be empty")
    existing = find_habit(db, display)
    if existing is not None:
        raise InputError(f'habit "{existing["name"]}" already exists')
    habit = {"name": display, "created": today.isoformat(), "completions": []}
    db["habits"].append(habit)
    return habit


def mark_done(db: dict, name: str, day: date) -> tuple[dict, bool]:
    """Record `day` once. Returns (habit, changed). Idempotent for one day."""
    habit = find_habit(db, name)
    if habit is None:
        raise InputError(
            f'no habit named "{normalize_name(name)}"; run "habits.py list" to see habits'
        )
    iso = day.isoformat()
    if iso in habit["completions"]:
        return habit, False
    habit["completions"] = sorted(set(habit["completions"]) | {iso})
    return habit, True


def remove_habit(db: dict, name: str) -> dict:
    habit = find_habit(db, name)
    if habit is None:
        raise InputError(
            f'no habit named "{normalize_name(name)}"; run "habits.py list" to see habits'
        )
    db["habits"] = [item for item in db["habits"] if item is not habit]
    return habit


def current_streak(completions: Iterable[str], today: date) -> int:
    """Consecutive days ending today, or ending yesterday if today is not marked.

    A day that has fully elapsed without a completion breaks the streak; the
    current day is still open. Future-dated entries are ignored.
    """
    days = {
        parsed
        for value in completions
        if (parsed := _try_parse(value)) is not None and parsed <= today
    }
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


def _try_parse(value: str) -> date | None:
    """Ignore malformed values in the pure helper; load() rejects them."""
    if (
        not isinstance(value, str)
        or len(value) != 10
        or value[4] != "-"
        or value[7] != "-"
    ):
        return None
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def default_path() -> Path:
    configured = os.environ.get("HABITS_FILE", "").strip()
    if configured:
        return Path(configured).expanduser()
    return Path.home() / DEFAULT_FILENAME


EXAMPLES = """examples:
  habits.py add "Read 10 pages"
  habits.py done "Read 10 pages"
  habits.py list
  habits.py remove "Read 10 pages"
  habits.py --file ./demo.json list

A streak counts consecutive days ending today. If today is not marked yet,
a streak ending yesterday is still current until the day ends. One fully
missed day resets the streak to zero. Marking is for the local date only.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="habits.py",
        description="Track daily habits in one local JSON file.",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="data file (default: $HABITS_FILE or ~/.habits.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    add = subparsers.add_parser("add", help="create a habit")
    add.add_argument("name", help='habit name, for example "Read 10 pages"')

    done = subparsers.add_parser("done", help="mark a habit done for today")
    done.add_argument("name", help="habit name (case-insensitive)")

    remove = subparsers.add_parser("remove", help="delete a habit and its history")
    remove.add_argument("name", help="habit name (case-insensitive)")

    subparsers.add_parser("list", help="show habits, streaks and today's status")
    return parser


def _resolve_path(args: argparse.Namespace) -> Path:
    if args.file:
        return Path(args.file).expanduser()
    return default_path()


def _print_list(db: dict, today: date) -> None:
    habits = db["habits"]
    if not habits:
        print("No habits yet.")
        print('Add one with: habits.py add "Read 10 pages"')
        return

    name_width = max(len("NAME"), *(len(habit["name"]) for habit in habits))
    print(f"{'NAME':<{name_width}}  {'STREAK':>6}  TODAY")
    at_risk: list[str] = []
    for habit in habits:
        done_today = today.isoformat() in habit["completions"]
        streak = current_streak(habit["completions"], today)
        status = "done" if done_today else "not done"
        print(f"{habit['name']:<{name_width}}  {streak:>6}  {status}")
        if streak and not done_today:
            at_risk.append(habit["name"])
    if at_risk:
        print()
        print("At risk (not done today): " + ", ".join(at_risk))


def main(argv: list[str] | None = None, today: date | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    path = _resolve_path(args)
    today = today or date.today()

    try:
        db = load(path)
        if args.command == "add":
            habit = add_habit(db, args.name, today)
            save(path, db)
            print(f'Added "{habit["name"]}".')
        elif args.command == "done":
            habit, changed = mark_done(db, args.name, today)
            if changed:
                save(path, db)
            streak = current_streak(habit["completions"], today)
            verb = "Marked" if changed else "Already marked"
            print(f'{verb} "{habit["name"]}" done for {today.isoformat()}. '
                  f'Current streak: {streak}.')
        elif args.command == "remove":
            habit = remove_habit(db, args.name)
            save(path, db)
            count = len(habit["completions"])
            noun = "completion" if count == 1 else "completions"
            print(f'Removed "{habit["name"]}" and {count} {noun}.')
        elif args.command == "list":
            _print_list(db, today)
        else:  # pragma: no cover - argparse rejects unknown commands
            parser.error(f"unknown command {args.command!r}")
        return 0
    except HabitsError as exc:
        print(f"habits: error: {exc}", file=sys.stderr)
        return exc.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
