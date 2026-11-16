"""Tests for the habits CLI.

The suite has two layers:
- pure date/streak behavior, exercised directly;
- the shipped CLI, exercised through subprocesses with an isolated data file.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest import mock

import habits

ROOT = Path(__file__).resolve().parent
CLI = ROOT / "habits.py"


class StreakTests(unittest.TestCase):
    def test_no_completions_is_zero(self) -> None:
        self.assertEqual(habits.current_streak([], date(2026, 11, 15)), 0)

    def test_today_only_is_one(self) -> None:
        self.assertEqual(
            habits.current_streak([date(2026, 11, 15)], date(2026, 11, 15)), 1
        )

    def test_today_and_yesterday_is_two(self) -> None:
        days = [date(2026, 11, 14), date(2026, 11, 15)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 2)

    def test_unmarked_today_keeps_yesterdays_streak_active(self) -> None:
        days = [date(2026, 11, 13), date(2026, 11, 14)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 2)

    def test_gap_breaks_the_streak(self) -> None:
        days = [date(2026, 11, 12), date(2026, 11, 15)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 1)

    def test_two_day_old_completion_is_zero(self) -> None:
        days = [date(2026, 11, 12), date(2026, 11, 13)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 0)

    def test_future_completions_do_not_inflate_streak(self) -> None:
        days = [date(2026, 11, 16), date(2026, 11, 17)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 0)

    def test_duplicate_days_are_counted_once(self) -> None:
        days = [date(2026, 11, 15), date(2026, 11, 15)]
        self.assertEqual(habits.current_streak(days, date(2026, 11, 15)), 1)

    def test_longest_streak_finds_the_best_run(self) -> None:
        days = [
            date(2026, 11, 1),
            date(2026, 11, 2),
            date(2026, 11, 3),
            date(2026, 11, 6),
            date(2026, 11, 7),
        ]
        self.assertEqual(habits.longest_streak(days), 3)

    def test_longest_streak_ignores_future_when_today_given(self) -> None:
        days = [date(2026, 11, 14), date(2026, 11, 15), date(2026, 11, 16)]
        self.assertEqual(habits.longest_streak(days, today=date(2026, 11, 15)), 2)

    def test_longest_streak_empty_is_zero(self) -> None:
        self.assertEqual(habits.longest_streak([]), 0)


class DataPathTests(unittest.TestCase):
    def test_explicit_path_wins(self) -> None:
        with mock.patch.dict(os.environ, {"HABITS_FILE": "/tmp/from-env.json"}):
            self.assertEqual(
                habits.resolve_data_path("/tmp/explicit.json"),
                Path("/tmp/explicit.json"),
            )

    def test_habits_file_environment_variable(self) -> None:
        with mock.patch.dict(os.environ, {"HABITS_FILE": "/tmp/from-env.json"}):
            self.assertEqual(
                habits.resolve_data_path(None), Path("/tmp/from-env.json")
            )

    def test_xdg_data_home(self) -> None:
        env = {"XDG_DATA_HOME": "/tmp/xdg", "HABITS_FILE": ""}
        with mock.patch.dict(os.environ, env, clear=False):
            os.environ.pop("HABITS_FILE", None)
            self.assertEqual(
                habits.resolve_data_path(None),
                Path("/tmp/xdg/habits/habits.json"),
            )

    def test_home_fallback(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(
                habits.resolve_data_path(None),
                Path.home() / ".local" / "share" / "habits" / "habits.json",
            )


class CliTests(unittest.TestCase):
    """Exercise the shipped command surface through subprocesses."""

    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.tmp = Path(temp.name)
        self.data = self.tmp / "state" / "habits.json"
        self.today = date(2026, 11, 15)

    def run_cli(
        self,
        *args: str,
        today: date | None = None,
        data: Path | None = None,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env.pop("HABITS_FILE", None)
        env.pop("XDG_DATA_HOME", None)
        command = [
            sys.executable,
            str(CLI),
            "--file",
            str(data if data is not None else self.data),
            "--today",
            (today or self.today).isoformat(),
        ]
        command.extend(args)
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            env=env,
            cwd=self.tmp,
        )

    def cli_ok(self, *args: str, today: date | None = None) -> subprocess.CompletedProcess[str]:
        result = self.run_cli(*args, today=today)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def cli_fail(self, *args: str, today: date | None = None) -> subprocess.CompletedProcess[str]:
        result = self.run_cli(*args, today=today)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        return result

    def load(self) -> dict:
        return json.loads(self.data.read_text(encoding="utf-8"))

    def row_for(self, listing: str, habit_id: str) -> list[str]:
        for line in listing.splitlines():
            cells = line.split()
            if cells and cells[0] == habit_id:
                return cells
        self.fail(f"no list row for {habit_id!r} in:\n{listing}")

    def test_add_creates_file_and_lists_habit(self) -> None:
        result = self.cli_ok("add", "Read 30 minutes")
        self.assertIn("read-30-minutes", result.stdout)
        store = self.load()
        self.assertEqual(store["version"], 1)
        self.assertEqual(store["habits"][0]["name"], "Read 30 minutes")
        self.assertEqual(store["habits"][0]["created_on"], "2026-11-15")

        listing = self.cli_ok("list").stdout
        self.assertIn("ID", listing)
        self.assertIn("STREAK", listing)
        self.assertIn("read-30-minutes", listing)
        self.assertIn("Read 30 minutes", listing)
        self.assertIn("no", listing)

    def test_add_accepts_unquoted_words(self) -> None:
        self.cli_ok("add", "Read", "30", "minutes")
        self.assertEqual(self.load()["habits"][0]["id"], "read-30-minutes")

    def test_duplicate_name_is_rejected_without_writing(self) -> None:
        self.cli_ok("add", "Read")
        before = self.data.read_text(encoding="utf-8")
        result = self.cli_fail("add", "read")
        self.assertIn("already exists", result.stderr)
        self.assertEqual(self.data.read_text(encoding="utf-8"), before)

    def test_colliding_slug_gets_a_suffix(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("add", "Read!")
        ids = [habit["id"] for habit in self.load()["habits"]]
        self.assertEqual(ids, ["read", "read-2"])

    def test_done_is_idempotent(self) -> None:
        self.cli_ok("add", "Read")
        first = self.cli_ok("done", "read")
        self.assertIn("Current streak: 1 day.", first.stdout)
        second = self.cli_ok("done", "read")
        self.assertIn("Already marked", second.stdout)
        self.assertIn("Current streak: 1 day.", second.stdout)
        self.assertEqual(self.load()["habits"][0]["completions"], ["2026-11-15"])

    def test_backfilled_consecutive_days_build_streak(self) -> None:
        self.cli_ok("add", "Read")
        for day in ("2026-11-13", "2026-11-14", "2026-11-15"):
            self.cli_ok("done", "read", "--date", day)
        row = self.row_for(self.cli_ok("list").stdout, "read")
        self.assertEqual(row[2], "3")
        self.assertEqual(row[3], "yes")
        self.assertEqual(row[4], "2026-11-15")

    def test_missed_day_resets_streak_but_keeps_history(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read", "--date", "2026-11-12")
        self.cli_ok("done", "read", "--date", "2026-11-13")
        row = self.row_for(self.cli_ok("list").stdout, "read")
        self.assertEqual(row[2], "0")
        self.assertEqual(row[3], "no")
        self.assertEqual(row[4], "2026-11-13")

        result = self.cli_ok("done", "read")
        self.assertIn("Current streak: 1 day.", result.stdout)

    def test_unmarked_today_keeps_yesterday_streak_active(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read", "--date", "2026-11-13")
        result = self.cli_ok("done", "read", "--date", "2026-11-14")
        self.assertIn("Current streak: 2 days.", result.stdout)
        row = self.row_for(self.cli_ok("list").stdout, "read")
        self.assertEqual(row[2], "2")
        self.assertEqual(row[3], "no")

        shown = self.cli_ok("show", "read").stdout
        self.assertIn("2 days (through 2026-11-14; today not marked)", shown)

    def test_undo_today_removes_only_that_day(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read", "--date", "2026-11-14")
        self.cli_ok("done", "read")
        result = self.cli_ok("undo", "read")
        self.assertIn("Removed", result.stdout)
        self.assertEqual(self.load()["habits"][0]["completions"], ["2026-11-14"])
        again = self.cli_fail("undo", "read")
        self.assertIn("was not marked done", again.stderr)

    def test_undo_yesterday_breaks_the_run(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read", "--date", "2026-11-14")
        self.cli_ok("done", "read")
        result = self.cli_ok("undo", "read", "--date", "2026-11-14")
        self.assertIn("Current streak: 1 day.", result.stdout)

    def test_undo_can_remove_a_future_entry_from_edited_data(self) -> None:
        self.data.parent.mkdir(parents=True)
        self.data.write_text(
            json.dumps(
                {
                    "version": 1,
                    "habits": [
                        {
                            "id": "read",
                            "name": "Read",
                            "created_on": "2026-11-01",
                            "completions": ["2026-11-16"],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        result = self.cli_ok("undo", "read", "--date", "2026-11-16")
        self.assertIn("Removed", result.stdout)
        self.assertEqual(self.load()["habits"][0]["completions"], [])

    def test_empty_name_is_rejected(self) -> None:
        result = self.cli_fail("add", "   ")
        self.assertIn("cannot be empty", result.stderr)
        self.assertFalse(self.data.exists())

    def test_unknown_command_is_a_usage_error(self) -> None:
        result = self.run_cli("frobnicate")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_unknown_habit_fails_without_creating_a_file(self) -> None:
        result = self.cli_fail("done", "nope")
        self.assertIn("no habit matches", result.stderr)
        self.assertFalse(self.data.exists())

    def test_future_date_is_rejected(self) -> None:
        self.cli_ok("add", "Read")
        result = self.cli_fail("done", "read", "--date", "2026-11-16")
        self.assertIn("future", result.stderr)
        self.assertEqual(self.load()["habits"][0]["completions"], [])

    def test_malformed_date_is_a_usage_error(self) -> None:
        result = self.run_cli("done", "read", "--date", "2026-1-1")
        self.assertEqual(result.returncode, 2)
        self.assertIn("use YYYY-MM-DD", result.stderr)

    def test_corrupt_json_is_reported_and_not_overwritten(self) -> None:
        self.data.parent.mkdir(parents=True)
        self.data.write_text("{not json\n", encoding="utf-8")
        result = self.cli_fail("list")
        self.assertIn("not valid JSON", result.stderr)
        self.assertEqual(self.data.read_text(encoding="utf-8"), "{not json\n")

        result = self.cli_fail("add", "Read")
        self.assertIn("not valid JSON", result.stderr)
        self.assertEqual(self.data.read_text(encoding="utf-8"), "{not json\n")

    def test_unsupported_data_version_is_rejected(self) -> None:
        self.data.parent.mkdir(parents=True)
        self.data.write_text(
            json.dumps({"version": 99, "habits": []}), encoding="utf-8"
        )
        result = self.cli_fail("list")
        self.assertIn("unsupported data version", result.stderr)

    def test_duplicate_ids_are_rejected(self) -> None:
        self.data.parent.mkdir(parents=True)
        habit = {
            "id": "read",
            "name": "Read",
            "created_on": "2026-11-01",
            "completions": [],
        }
        self.data.write_text(
            json.dumps({"version": 1, "habits": [habit, habit]}), encoding="utf-8"
        )
        result = self.cli_fail("list")
        self.assertIn("duplicate habit id", result.stderr)

    def test_remove_requires_yes_and_deletes_history(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read")
        refused = self.cli_fail("remove", "read")
        self.assertIn("--yes", refused.stderr)
        self.assertEqual(len(self.load()["habits"]), 1)

        removed = self.cli_ok("remove", "read", "--yes")
        self.assertIn("1 completion", removed.stdout)
        self.assertEqual(self.load()["habits"], [])
        self.assertIn("No habits yet", self.cli_ok("list").stdout)

    def test_list_shows_each_habit_independently(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("add", "Walk")
        self.cli_ok("done", "read")
        listing = self.cli_ok("list").stdout
        read_row = self.row_for(listing, "read")
        walk_row = self.row_for(listing, "walk")
        self.assertEqual(read_row[2], "1")
        self.assertEqual(read_row[3], "yes")
        self.assertEqual(walk_row[2], "0")
        self.assertEqual(walk_row[3], "no")
        self.assertEqual(walk_row[4], "-")

    def test_show_renders_recent_days_and_breakage(self) -> None:
        self.cli_ok("add", "Read")
        self.cli_ok("done", "read", "--date", "2026-11-14")
        self.cli_ok("done", "read")
        shown = self.cli_ok("show", "read").stdout
        self.assertIn("Read (read)", shown)
        self.assertIn("Current streak: 2 days (through 2026-11-15)", shown)
        self.assertIn("Longest streak: 2 days", shown)
        self.assertIn("Today:          done", shown)
        for day in ("2026-11-09", "2026-11-13", "2026-11-15"):
            self.assertIn(day, shown)

        self.cli_ok("undo", "read")
        self.cli_ok("undo", "read", "--date", "2026-11-14")
        self.cli_ok("done", "read", "--date", "2026-11-12")
        broken = self.cli_ok("show", "read").stdout
        self.assertIn("broken; last done 2026-11-12", broken)

    def test_empty_list_explains_next_step(self) -> None:
        result = self.cli_ok("list")
        self.assertIn("No habits yet", result.stdout)
        self.assertIn("add", result.stdout)

    def test_reference_by_name_and_case(self) -> None:
        self.cli_ok("add", "Read 30 minutes")
        self.cli_ok("done", "Read 30 minutes")
        self.cli_ok("done", "READ 30 MINUTES")
        self.assertEqual(self.load()["habits"][0]["completions"], ["2026-11-15"])

    def test_unicode_name_gets_ascii_slug(self) -> None:
        self.cli_ok("add", "Café")
        self.assertEqual(self.load()["habits"][0]["id"], "cafe")

    def test_write_leaves_no_temporary_files(self) -> None:
        self.cli_ok("add", "Read")
        self.assertEqual(list(self.data.parent.glob("*.tmp")), [])

    def test_habits_file_environment_variable(self) -> None:
        env = os.environ.copy()
        env["HABITS_FILE"] = str(self.data)
        env.pop("XDG_DATA_HOME", None)
        result = subprocess.run(
            [
                sys.executable,
                str(CLI),
                "--today",
                self.today.isoformat(),
                "add",
                "Read",
            ],
            capture_output=True,
            text=True,
            env=env,
            cwd=self.tmp,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.data.exists())

    def test_no_arguments_prints_help(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CLI)],
            capture_output=True,
            text=True,
            cwd=self.tmp,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("streak rule", result.stdout)
        self.assertIn("exit codes", result.stdout)

    def test_version_flag(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CLI), "--version"],
            capture_output=True,
            text=True,
            cwd=self.tmp,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("habits.py 1.0.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
