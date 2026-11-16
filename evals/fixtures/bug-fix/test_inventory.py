import unittest

import inventory


class PaginationTests(unittest.TestCase):
    def setUp(self):
        self.items = ["a", "b", "c", "d", "e"]

    def test_first_page(self):
        self.assertEqual(inventory.paginate(self.items, 1, 2), ["a", "b"])

    def test_second_page(self):
        self.assertEqual(inventory.paginate(self.items, 2, 2), ["c", "d"])

    def test_last_page(self):
        self.assertEqual(inventory.paginate(self.items, 3, 2), ["e"])

    def test_page_count(self):
        self.assertEqual(inventory.page_count(self.items, 2), 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            inventory.paginate(self.items, 0, 2)


if __name__ == "__main__":
    unittest.main()
