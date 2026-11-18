import unittest

from app.search import filter_notes


class SearchTests(unittest.TestCase):
    def test_filters_by_term(self):
        notes = [{"id": 1, "body": "queue export"}, {"id": 2, "body": "billing"}]
        self.assertEqual([note["id"] for note in filter_notes(notes, "export")], [1])


if __name__ == "__main__":
    unittest.main()
