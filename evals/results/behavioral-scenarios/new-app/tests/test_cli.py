import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT / "notes.py"


class CliTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.data = self.root / "notes.json"
        self.home = self.root / "home"
        self.home.mkdir()
        self.env = {
            **os.environ,
            "NOTES_DATA": str(self.data),
            "HOME": str(self.home),
        }

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            env=self.env,
            cwd=str(PROJECT),
            timeout=30,
        )

    def stored(self):
        return json.loads(self.data.read_text(encoding="utf-8"))


class AddTests(CliTestCase):
    def test_add_prints_id_and_persists(self):
        first = self.run_cli("add", "buy milk")
        second = self.run_cli("add", "call Ana")
        self.assertEqual(first.returncode, 0)
        self.assertEqual(first.stdout, "1\n")
        self.assertEqual(first.stderr, "")
        self.assertEqual(second.stdout, "2\n")
        self.assertEqual(
            [n["text"] for n in self.stored()["notes"]], ["buy milk", "call Ana"]
        )

    def test_add_accepts_unquoted_words(self):
        result = self.run_cli("add", "buy", "milk")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.stored()["notes"][0]["text"], "buy milk")

    def test_add_collapses_whitespace_into_one_line(self):
        result = self.run_cli("add", "  buy\nmilk\tnow  ")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.stored()["notes"][0]["text"], "buy milk now")

    def test_add_empty_text_is_a_usage_error(self):
        result = self.run_cli("add", "   ")
        self.assertEqual(result.returncode, 2)
        self.assertIn("note text is empty", result.stderr)
        self.assertFalse(self.data.exists())

    def test_add_without_text_is_a_usage_error(self):
        result = self.run_cli("add")
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage:", result.stderr)
        self.assertFalse(self.data.exists())


class ListTests(CliTestCase):
    def test_list_prints_id_tab_text_in_order(self):
        self.run_cli("add", "buy milk")
        self.run_cli("add", "call Ana")
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1\tbuy milk\n2\tcall Ana\n")

    def test_list_on_missing_store_prints_nothing(self):
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


class SearchTests(CliTestCase):
    def setUp(self):
        super().setUp()
        self.run_cli("add", "Buy milk")
        self.run_cli("add", "buy bread")
        self.run_cli("add", "call Ana")

    def test_search_is_case_insensitive(self):
        result = self.run_cli("search", "BUY")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1\tBuy milk\n2\tbuy bread\n")

    def test_search_matches_a_mid_word_substring(self):
        result = self.run_cli("search", "ana")
        self.assertEqual(result.stdout, "3\tcall Ana\n")

    def test_search_without_matches_exits_zero_and_prints_nothing(self):
        result = self.run_cli("search", "zebra")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_search_empty_term_is_a_usage_error(self):
        result = self.run_cli("search", "")
        self.assertEqual(result.returncode, 2)
        self.assertIn("search term is empty", result.stderr)


class DeleteTests(CliTestCase):
    def test_delete_removes_the_note(self):
        self.run_cli("add", "keep")
        self.run_cli("add", "remove")
        result = self.run_cli("delete", "2")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "deleted 2\n")
        self.assertEqual([n["text"] for n in self.stored()["notes"]], ["keep"])

    def test_delete_unknown_id_exits_one_and_keeps_the_file(self):
        self.run_cli("add", "keep")
        before = self.data.read_text(encoding="utf-8")
        result = self.run_cli("delete", "99")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no note with id 99", result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(self.data.read_text(encoding="utf-8"), before)

    def test_delete_rejects_non_integer_and_non_positive_ids(self):
        for value in ("abc", "0", "-1"):
            with self.subTest(value=value):
                result = self.run_cli("delete", value)
                self.assertEqual(result.returncode, 2)
                self.assertIn("invalid note id", result.stderr)


class FailureModeTests(CliTestCase):
    def test_unknown_command_is_a_usage_error(self):
        result = self.run_cli("frobnicate")
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_no_command_is_a_usage_error(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage:", result.stderr)

    def test_corrupt_store_exits_one_without_a_traceback(self):
        broken = '{"notes": ['
        self.data.write_text(broken, encoding="utf-8")
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid JSON", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.data.read_text(encoding="utf-8"), broken)

    def test_corrupt_store_blocks_writes(self):
        broken = '{"notes": ['
        self.data.write_text(broken, encoding="utf-8")
        result = self.run_cli("add", "would overwrite")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_text(encoding="utf-8"), broken)

    def test_override_keeps_notes_out_of_the_default_location(self):
        self.run_cli("add", "scoped")
        self.assertFalse((self.home / ".notes.json").exists())
        self.assertTrue(self.data.exists())

    def test_help_lists_the_commands(self):
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0)
        for command in ("add", "list", "search", "delete"):
            self.assertIn(command, result.stdout)


if __name__ == "__main__":
    unittest.main()
