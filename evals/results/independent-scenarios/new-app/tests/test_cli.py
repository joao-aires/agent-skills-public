"""End-to-end tests for the notes.py command-line entry point."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "notes.py"


class CliTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.working_directory = Path(self.temporary_directory.name)
        self.data_path = self.working_directory / "data" / "notes.json"
        self.environment = os.environ.copy()
        self.environment["NOTES_DATA"] = str(self.data_path)

    def run_cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=self.working_directory,
            env=self.environment,
            capture_output=True,
            text=True,
            timeout=15,
        )

    def test_add_prints_id_and_persists_across_processes(self):
        added = self.run_cli("add", "Buy milk")
        self.assertEqual(added.returncode, 0)
        self.assertEqual(added.stdout, "1\n")
        self.assertEqual(added.stderr, "")

        second = self.run_cli("add", "Call the dentist")
        self.assertEqual(second.stdout, "2\n")

        listed = self.run_cli("list")
        self.assertEqual(listed.returncode, 0)
        self.assertEqual(listed.stdout, "1: Buy milk\n2: Call the dentist\n")

        payload = json.loads(self.data_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["next_id"], 3)
        self.assertEqual(len(payload["notes"]), 2)

    def test_search_is_case_insensitive_and_literal(self):
        self.run_cli("add", "Alpha Beta")
        self.run_cli("add", "literal [draft] .*")

        searched = self.run_cli("search", "ALPHA")
        self.assertEqual(searched.returncode, 0)
        self.assertEqual(searched.stdout, "1: Alpha Beta\n")

        literal = self.run_cli("search", "[draft]")
        self.assertEqual(literal.stdout, "2: literal [draft] .*\n")

    def test_search_without_matches_exits_zero(self):
        self.run_cli("add", "Buy milk")
        searched = self.run_cli("search", "missing")

        self.assertEqual(searched.returncode, 0)
        self.assertEqual(searched.stdout, "")
        self.assertEqual(searched.stderr, "No matches.\n")

    def test_blank_search_term_exits_two(self):
        result = self.run_cli("search", "   ")

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "error: search term must not be empty.\n")

    def test_delete_removes_note_and_does_not_reuse_its_id(self):
        self.run_cli("add", "one")
        self.run_cli("add", "two")

        deleted = self.run_cli("delete", "2")
        self.assertEqual(deleted.returncode, 0)
        self.assertEqual(deleted.stdout, "Deleted note 2.\n")

        listed = self.run_cli("list")
        self.assertEqual(listed.stdout, "1: one\n")

        added = self.run_cli("add", "three")
        self.assertEqual(added.stdout, "3\n")

    def test_delete_missing_note_exits_one(self):
        result = self.run_cli("delete", "99")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "error: No note with id 99.\n")

    def test_invalid_id_exits_two(self):
        for value in ("abc", "0", "-1"):
            with self.subTest(value=value):
                result = self.run_cli("delete", value)
                self.assertEqual(result.returncode, 2)
                self.assertIn("id must be a positive integer", result.stderr)

    def test_blank_note_exits_two_without_creating_data(self):
        result = self.run_cli("add", "   ")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr, "error: note text must not be empty.\n")
        self.assertFalse(self.data_path.exists())

    def test_corrupt_json_exits_one_and_preserves_file(self):
        self.data_path.parent.mkdir(parents=True)
        self.data_path.write_text("{not json", encoding="utf-8")

        result = self.run_cli("list")

        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Invalid JSON", result.stderr)
        self.assertEqual(
            self.data_path.read_text(encoding="utf-8"), "{not json"
        )

    def test_help_lists_the_commands(self):
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0)
        for command in ("add", "list", "search", "delete"):
            self.assertIn(command, result.stdout)

    def test_unicode_round_trip(self):
        added = self.run_cli("add", "Café ☕")
        self.assertEqual(added.stdout, "1\n")

        listed = self.run_cli("list")
        self.assertEqual(listed.stdout, "1: Café ☕\n")

        searched = self.run_cli("search", "café")
        self.assertEqual(searched.stdout, "1: Café ☕\n")

    def test_empty_data_file_is_an_empty_notebook(self):
        self.data_path.parent.mkdir(parents=True)
        self.data_path.write_text("", encoding="utf-8")

        listed = self.run_cli("list")
        self.assertEqual(listed.returncode, 0)
        self.assertEqual(listed.stdout, "")

        added = self.run_cli("add", "first")
        self.assertEqual(added.stdout, "1\n")

    def test_empty_notes_data_environment_variable_is_rejected(self):
        self.environment["NOTES_DATA"] = ""
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 2)
        self.assertIn("NOTES_DATA is set but empty", result.stderr)


if __name__ == "__main__":
    unittest.main()
