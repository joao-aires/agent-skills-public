"""Standard-library tests for habits.py.

Run with: python3 -m unittest -v
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

import habits

TODAY = date(2026, 11, 15)


class StreakTests(unittest.TestCase):
    def test_three_consecutive_days_ending_today(self):
        completions = ["2026-11-13", "2026-11-14", "2026-11-15"]
        self.assertEqual(habits.current_streak(completions, TODAY), 3)

    def test_today_not_marked_yet_keeps_yesterdays_streak_current(self):
        completions = ["2026-11-13", "2026-11-14"]
        self.assertEqual(habits.current_streak(completions, TODAY), 2)

    def test_one_fully_missed_day_resets_streak(self):
        completions = ["2026-11-13"]
        self.assertEqual(habits.current_streak(completions, TODAY), 0)

    def test_no_completions_is_zero(self):
        self.assertEqual(habits.current_streak([], TODAY), 0)

    def test_yesterday_only_is_a_one_day_streak(self):
        self.assertEqual(habits.current_streak(["2026-11-14"], TODAY), 1)

    def test_future_dates_are_ignored(self):
        self.assertEqual(habits.current_streak(["2026-11-16"], TODAY), 0)
        self.assertEqual(
            habits.current_streak(["2026-11-15", "2026-11-16"], TODAY), 1
        )

    def test_duplicates_and_order_do_not_change_the_streak(self):
        completions = ["2026-11-14", "2026-11-15", "2026-11-14"]
        self.assertEqual(habits.current_streak(completions, TODAY), 2)

    def test_malformed_entries_are_ignored_by_the_pure_helper(self):
        completions = ["not-a-date", "2026-11-14", "2026-11-15"]
        self.assertEqual(habits.current_streak(completions, TODAY), 2)

    def test_compact_iso_dates_are_not_accepted_by_the_pure_helper(self):
        self.assertEqual(habits.current_streak(["20261115"], TODAY), 0)

    def test_older_gap_after_a_long_recent_run(self):
        completions = ["2026-11-09", "2026-11-13", "2026-11-14", "2026-11-15"]
        self.assertEqual(habits.current_streak(completions, TODAY), 3)


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.path = Path(self.tempdir.name) / "habits.json"

    def run_cli(self, *args, today=TODAY):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = habits.main(["--file", str(self.path), *args], today=today)
        return code, stdout.getvalue(), stderr.getvalue()

    def write_db(self, habits_list):
        self.path.write_text(
            json.dumps({"version": 1, "habits": habits_list}), encoding="utf-8"
        )

    def read_db(self):
        return json.loads(self.path.read_text(encoding="utf-8"))

    def test_add_creates_a_versioned_file_with_normalized_name(self):
        code, out, err = self.run_cli("add", "  Read   10 pages  ")
        self.assertEqual(code, 0, err)
        self.assertEqual(out, 'Added "Read 10 pages".\n')
        db = self.read_db()
        self.assertEqual(db["version"], 1)
        self.assertEqual(
            db["habits"],
            [
                {
                    "name": "Read 10 pages",
                    "created": "2026-11-15",
                    "completions": [],
                }
            ],
        )

    def test_add_duplicate_is_case_insensitive_and_keeps_one_habit(self):
        self.assertEqual(self.run_cli("add", "Read 10 pages")[0], 0)
        code, _, err = self.run_cli("add", " read   10 PAGES ")
        self.assertEqual(code, 1)
        self.assertIn('habit "Read 10 pages" already exists', err)
        self.assertEqual(len(self.read_db()["habits"]), 1)

    def test_add_rejects_a_whitespace_only_name(self):
        code, _, err = self.run_cli("add", "   ")
        self.assertEqual(code, 1)
        self.assertIn("must not be empty", err)
        self.assertFalse(self.path.exists())

    def test_done_is_idempotent_for_the_same_day(self):
        self.run_cli("add", "Walk")
        code, out, _ = self.run_cli("done", "walk")
        self.assertEqual(code, 0)
        self.assertEqual(
            out, 'Marked "Walk" done for 2026-11-15. Current streak: 1.\n'
        )
        code, out, _ = self.run_cli("done", "WALK")
        self.assertEqual(code, 0)
        self.assertIn("Already marked", out)
        self.assertEqual(
            self.read_db()["habits"][0]["completions"], ["2026-11-15"]
        )

    def test_done_unknown_habit_fails_without_creating_a_file(self):
        code, _, err = self.run_cli("done", "Walk")
        self.assertEqual(code, 1)
        self.assertIn('no habit named "Walk"', err)
        self.assertFalse(self.path.exists())

    def test_list_empty_does_not_create_the_file(self):
        code, out, err = self.run_cli("list")
        self.assertEqual(code, 0, err)
        self.assertIn("No habits yet.", out)
        self.assertFalse(self.path.exists())

    def test_list_shows_streak_today_status_and_risk_hint(self):
        self.write_db(
            [
                {
                    "name": "Read 10 pages",
                    "created": "2026-11-13",
                    "completions": ["2026-11-14", "2026-11-15"],
                },
                {
                    "name": "Walk",
                    "created": "2026-11-13",
                    "completions": ["2026-11-14"],
                },
                {"name": "Write", "created": "2026-11-15", "completions": []},
            ]
        )
        code, out, err = self.run_cli("list")
        self.assertEqual(code, 0, err)
        lines = [line for line in out.splitlines() if line.strip()]
        self.assertEqual(
            lines[0].split(), ["NAME", "STREAK", "TODAY"]
        )
        self.assertIn("Read 10 pages", lines[1])
        self.assertTrue(lines[1].endswith("2  done"))
        self.assertTrue(lines[2].endswith("1  not done"))
        self.assertTrue(lines[3].endswith("0  not done"))
        self.assertIn("At risk (not done today): Walk", out)

    def test_list_ignores_future_completions(self):
        self.write_db(
            [
                {
                    "name": "Walk",
                    "created": "2026-11-15",
                    "completions": ["2026-11-16"],
                }
            ]
        )
        code, out, _ = self.run_cli("list")
        self.assertEqual(code, 0)
        self.assertIn("0  not done", out)
        self.assertNotIn("At risk", out)

    def test_remove_deletes_the_habit_and_its_history(self):
        self.write_db(
            [
                {
                    "name": "Walk",
                    "created": "2026-11-14",
                    "completions": ["2026-11-14", "2026-11-15"],
                }
            ]
        )
        code, out, err = self.run_cli("remove", "walk")
        self.assertEqual(code, 0, err)
        self.assertEqual(out, 'Removed "Walk" and 2 completions.\n')
        self.assertEqual(self.read_db()["habits"], [])

    def test_remove_unknown_habit_fails(self):
        code, _, err = self.run_cli("remove", "Nope")
        self.assertEqual(code, 1)
        self.assertIn("no habit named", err)

    def test_corrupt_json_is_reported_and_not_overwritten(self):
        original = "{ this is not json"
        self.path.write_text(original, encoding="utf-8")
        code, _, err = self.run_cli("add", "Walk")
        self.assertEqual(code, 2)
        self.assertIn("is not valid JSON", err)
        self.assertEqual(self.path.read_text(encoding="utf-8"), original)

    def test_unsupported_schema_version_is_reported(self):
        self.write_db([])
        db = self.read_db()
        db["version"] = 99
        self.path.write_text(json.dumps(db), encoding="utf-8")
        before = self.path.read_text(encoding="utf-8")
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 2)
        self.assertIn("unsupported schema version 99", err)
        self.assertEqual(self.path.read_text(encoding="utf-8"), before)

    def test_boolean_schema_version_is_rejected(self):
        self.write_db([])
        db = self.read_db()
        db["version"] = True
        self.path.write_text(json.dumps(db), encoding="utf-8")
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 2)
        self.assertIn("unsupported schema version True", err)

    def test_invalid_completion_date_is_reported(self):
        self.write_db(
            [
                {
                    "name": "Walk",
                    "created": "2026-11-15",
                    "completions": ["2026-13-01"],
                }
            ]
        )
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 2)
        self.assertIn("invalid date", err)

    def test_duplicate_names_in_the_file_are_reported(self):
        self.write_db(
            [
                {"name": "Walk", "created": "2026-11-15", "completions": []},
                {"name": " walk ", "created": "2026-11-15", "completions": []},
            ]
        )
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 2)
        self.assertIn("duplicate habit name", err)

    def test_load_normalizes_duplicate_and_unsorted_completions(self):
        self.write_db(
            [
                {
                    "name": "Walk",
                    "created": "2026-11-13",
                    "completions": ["2026-11-15", "2026-11-14", "2026-11-15"],
                }
            ]
        )
        db = habits.load(self.path)
        self.assertEqual(
            db["habits"][0]["completions"], ["2026-11-14", "2026-11-15"]
        )

    def test_add_creates_missing_parent_directories(self):
        nested = Path(self.tempdir.name) / "a" / "b" / "habits.json"
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = habits.main(
                ["--file", str(nested), "add", "Walk"], today=TODAY
            )
        self.assertEqual(code, 0)
        self.assertTrue(nested.exists())

    def test_successful_write_leaves_no_temporary_file(self):
        self.run_cli("add", "Walk")
        self.assertEqual(list(self.path.parent.glob("*.tmp")), [])

    def test_habits_file_environment_variable_is_used(self):
        env_path = Path(self.tempdir.name) / "env.json"
        with mock.patch.dict(os.environ, {"HABITS_FILE": str(env_path)}):
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                code = habits.main(["add", "Walk"], today=TODAY)
        self.assertEqual(code, 0)
        self.assertTrue(env_path.exists())
        self.assertFalse(self.path.exists())

    def test_default_file_is_created_under_the_home_directory(self):
        home = Path(self.tempdir.name) / "home"
        home.mkdir()
        with mock.patch.dict(os.environ, {"HOME": str(home)}):
            os.environ.pop("HABITS_FILE", None)
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                code = habits.main(["add", "Walk"], today=TODAY)
        self.assertEqual(code, 0)
        self.assertTrue((home / ".habits.json").exists())

    def test_explicit_file_wins_over_the_environment_variable(self):
        env_path = Path(self.tempdir.name) / "env.json"
        with mock.patch.dict(os.environ, {"HABITS_FILE": str(env_path)}):
            code = self.run_cli("add", "Walk")[0]
        self.assertEqual(code, 0)
        self.assertTrue(self.path.exists())
        self.assertFalse(env_path.exists())

    def test_unknown_command_is_a_usage_error(self):
        stderr = io.StringIO()
        with self.assertRaises(SystemExit) as raised, contextlib.redirect_stderr(
            stderr
        ):
            habits.main(["bogus"])
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("invalid choice", stderr.getvalue())

    def test_help_exits_zero_and_explains_streak_grace(self):
        stdout = io.StringIO()
        with self.assertRaises(SystemExit) as raised, contextlib.redirect_stdout(
            stdout
        ):
            habits.main(["--help"])
        self.assertEqual(raised.exception.code, 0)
        self.assertIn("still current until the day ends", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
