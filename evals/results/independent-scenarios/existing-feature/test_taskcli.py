import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

import taskcli


class TaskCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        os.environ["TASKCLI_DATA"] = str(Path(self.temp.name) / "tasks.json")

    def run_main(self, *args):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = taskcli.main(list(args))
        return code, stdout.getvalue(), stderr.getvalue()

    def test_add_and_list_pending(self):
        taskcli.add("write report")
        taskcli.add("review report")
        pending = taskcli.list_tasks()
        self.assertEqual([task["title"] for _, task in pending], ["write report", "review report"])

    def test_done_hides_from_pending_and_persists(self):
        taskcli.add("write report")
        taskcli.done(0)
        self.assertEqual(taskcli.list_tasks(), [])
        self.assertEqual([task["title"] for _, task in taskcli.list_tasks(include_done=True)], ["write report"])
        self.assertTrue(taskcli.load()[0]["done"])

    def test_unknown_index_raises(self):
        with self.assertRaises(IndexError):
            taskcli.done(5)

    def test_add_with_tags_persists_and_deduplicates(self):
        index = taskcli.add("write report", ["work", "urgent", "work"])
        self.assertEqual(index, 0)
        self.assertEqual(
            taskcli.load()[0],
            {"title": "write report", "done": False, "tags": ["work", "urgent"]},
        )

    def test_add_without_tags_keeps_legacy_record_shape(self):
        taskcli.add("write report")
        self.assertEqual(taskcli.load()[0], {"title": "write report", "done": False})

    def test_empty_tag_is_rejected(self):
        with self.assertRaises(ValueError):
            taskcli.add("write report", [" "])
        self.assertEqual(taskcli.load(), [])

    def test_cli_option_can_precede_title(self):
        code, stdout, stderr = self.run_main("add", "--tag", "work", "write report")
        self.assertEqual((code, stdout, stderr), (0, "added 0\n", ""))
        self.assertEqual(taskcli.load()[0], {"title": "write report", "done": False, "tags": ["work"]})

    def test_list_filters_by_tag_and_respects_done(self):
        taskcli.add("write report", ["work"])
        taskcli.add("buy milk", ["home"])
        taskcli.add("review report", ["work", "urgent"])
        taskcli.done(0)

        self.assertEqual([task["title"] for _, task in taskcli.list_tasks(tag="work")], ["review report"])
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks(include_done=True, tag="work")],
            ["write report", "review report"],
        )
        self.assertEqual(taskcli.list_tasks(tag="missing"), [])

    def test_legacy_json_without_tags_remains_readable(self):
        taskcli.data_path().write_text(
            json.dumps(
                [
                    {"title": "legacy pending", "done": False},
                    {"title": "legacy done", "done": True},
                ]
            )
        )

        self.assertEqual([task["title"] for _, task in taskcli.list_tasks()], ["legacy pending"])
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks(include_done=True)],
            ["legacy pending", "legacy done"],
        )
        self.assertEqual(taskcli.list_tasks(tag="work"), [])

        taskcli.done(0)
        taskcli.add("new tagged task", ["work"])
        self.assertTrue(taskcli.load()[0]["done"])
        self.assertEqual([task["title"] for _, task in taskcli.list_tasks(tag="work")], ["new tagged task"])

    def test_cli_keeps_legacy_add_title_and_list_output(self):
        code, stdout, stderr = self.run_main("add", "write", "report")
        self.assertEqual((code, stdout, stderr), (0, "added 0\n", ""))
        self.assertNotIn("tags", taskcli.load()[0])

        code, stdout, stderr = self.run_main("list")
        self.assertEqual((code, stdout, stderr), (0, "0\t \twrite report\n", ""))

    def test_cli_add_tags_then_filter_and_done(self):
        self.run_main("add", "write report", "--tag", "work", "--tag", "urgent")
        self.run_main("add", "buy milk", "--tag", "home")
        self.run_main("add", "review report", "--tag=work")
        self.assertEqual(taskcli.load()[0]["tags"], ["work", "urgent"])

        self.assertEqual(self.run_main("done", "0")[0], 0)

        code, stdout, stderr = self.run_main("list", "--tag", "work")
        self.assertEqual((code, stdout, stderr), (0, "2\t \treview report\n", ""))

        code, stdout, stderr = self.run_main("list", "--all", "--tag=work")
        self.assertEqual((code, stdout, stderr), (0, "0\tx\twrite report\n2\t \treview report\n", ""))

    def test_cli_add_tag_without_value_does_not_write(self):
        code, stdout, stderr = self.run_main("add", "write report", "--tag")
        self.assertEqual(code, 1)
        self.assertEqual(stdout, "")
        self.assertIn("--tag requires a value", stderr)
        self.assertEqual(taskcli.load(), [])

    def test_cli_list_tag_without_value(self):
        code, stdout, stderr = self.run_main("list", "--tag")
        self.assertEqual(code, 1)
        self.assertEqual(stdout, "")
        self.assertIn("--tag requires a value", stderr)

    def test_cli_double_dash_keeps_tag_words_in_title(self):
        code, stdout, stderr = self.run_main("add", "--", "deploy --tag work")
        self.assertEqual((code, stdout, stderr), (0, "added 0\n", ""))
        self.assertEqual(taskcli.load()[0], {"title": "deploy --tag work", "done": False})


if __name__ == "__main__":
    unittest.main()
