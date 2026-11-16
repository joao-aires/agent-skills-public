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


if __name__ == "__main__":
    unittest.main()
