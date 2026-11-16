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

    def run_main(self, argv):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = taskcli.main(argv)
        return code, output.getvalue()

    def write_legacy(self, tasks):
        Path(os.environ["TASKCLI_DATA"]).write_text(json.dumps(tasks))

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

    def test_add_without_tags_persists_empty_tag_list(self):
        taskcli.add("write report")
        self.assertEqual(taskcli.load()[0]["tags"], [])

    def test_add_with_tags_persists_them(self):
        taskcli.add("write report", tags=["work", "urgent"])
        self.assertEqual(taskcli.load()[0]["tags"], ["work", "urgent"])

    def test_tags_are_normalized_and_deduplicated(self):
        taskcli.add("write report", tags=[" Work ", "#URGENT", "work"])
        self.assertEqual(taskcli.load()[0]["tags"], ["work", "urgent"])

    def test_string_tags_are_accepted(self):
        taskcli.add("write report", tags="work")
        self.assertEqual(taskcli.load()[0]["tags"], ["work"])

    def test_list_filters_pending_tasks_by_tag(self):
        taskcli.add("write report", tags=["work"])
        taskcli.add("buy milk", tags=["home"])
        taskcli.add("review report", tags=["work", "urgent"])
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks(tag="work")],
            ["write report", "review report"],
        )

    def test_list_tag_filter_includes_done_only_when_asked(self):
        taskcli.add("write report", tags=["work"])
        taskcli.done(0)
        self.assertEqual(taskcli.list_tasks(tag="work"), [])
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks(include_done=True, tag="work")],
            ["write report"],
        )

    def test_tag_filter_is_case_insensitive(self):
        taskcli.add("write report", tags=["Work"])
        self.assertEqual(len(taskcli.list_tasks(tag="WORK")), 1)

    def test_unknown_tag_returns_no_tasks(self):
        taskcli.add("write report", tags=["work"])
        self.assertEqual(taskcli.list_tasks(tag="home"), [])

    def test_legacy_json_without_tags_is_readable(self):
        self.write_legacy(
            [
                {"title": "old pending", "done": False},
                {"title": "old done", "done": True},
            ]
        )
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks()],
            ["old pending"],
        )
        self.assertEqual(
            [task["title"] for _, task in taskcli.list_tasks(include_done=True)],
            ["old pending", "old done"],
        )
        self.assertEqual(taskcli.list_tasks(tag="work"), [])

    def test_done_on_legacy_record_keeps_legacy_shape(self):
        self.write_legacy([{"title": "old pending", "done": False}])
        taskcli.done(0)
        record = taskcli.load()[0]
        self.assertTrue(record["done"])
        self.assertNotIn("tags", record)

    def test_new_record_json_has_tags_and_existing_fields(self):
        taskcli.add("write report", tags=["work"])
        record = json.loads(Path(os.environ["TASKCLI_DATA"]).read_text())[0]
        self.assertEqual(record, {"title": "write report", "done": False, "tags": ["work"]})

    def test_main_add_with_tags_and_filter(self):
        code, output = self.run_main(["add", "write report", "--tag", "work", "--tag", "urgent"])
        self.assertEqual((code, output), (0, "added 0\n"))
        self.run_main(["add", "buy milk", "--tag", "home"])
        code, output = self.run_main(["list", "--tag", "work"])
        self.assertEqual((code, output), (0, "0\t \twrite report\n"))

    def test_main_add_accepts_tag_before_title(self):
        code, output = self.run_main(["add", "--tag", "work", "write report"])
        self.assertEqual((code, output), (0, "added 0\n"))
        self.assertEqual(taskcli.load()[0]["title"], "write report")
        self.assertEqual(taskcli.load()[0]["tags"], ["work"])

    def test_main_add_accepts_equals_and_comma_tags(self):
        self.run_main(["add", "write report", "--tag=work,urgent"])
        self.assertEqual(taskcli.load()[0]["tags"], ["work", "urgent"])

    def test_main_list_all_with_tag_includes_done(self):
        self.run_main(["add", "write report", "--tag", "work"])
        self.run_main(["add", "buy milk", "--tag", "home"])
        self.run_main(["done", "0"])
        code, output = self.run_main(["list", "--all", "--tag", "work"])
        self.assertEqual((code, output), (0, "0\tx\twrite report\n"))
        code, output = self.run_main(["list", "--tag", "work"])
        self.assertEqual((code, output), (0, ""))

    def test_main_list_preserves_untagged_output_format(self):
        self.run_main(["add", "write report"])
        code, output = self.run_main(["list"])
        self.assertEqual((code, output), (0, "0\t \twrite report\n"))

    def test_main_list_rejects_multiple_tags(self):
        code, output = self.run_main(["list", "--tag", "work", "--tag", "home"])
        self.assertEqual(code, 1)
        self.assertIn("single --tag", output)

    def test_main_add_requires_a_title(self):
        code, output = self.run_main(["add", "--tag", "work"])
        self.assertEqual(code, 1)
        self.assertIn("usage", output)

    def test_main_rejects_empty_tag(self):
        code, output = self.run_main(["add", "write report", "--tag", "  "])
        self.assertEqual(code, 1)
        self.assertIn("invalid tag", output)
        self.assertEqual(taskcli.load(), [])


if __name__ == "__main__":
    unittest.main()
