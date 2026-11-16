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

    def test_first_page_of_size_one(self):
        self.assertEqual(inventory.paginate(self.items, 1, 1), ["a"])

    def test_page_beyond_last_page_is_empty(self):
        self.assertEqual(inventory.paginate(self.items, 4, 2), [])

    def test_pages_cover_every_item_once(self):
        pages = [
            inventory.paginate(self.items, page, 2)
            for page in range(1, inventory.page_count(self.items, 2) + 1)
        ]
        self.assertEqual(pages, [["a", "b"], ["c", "d"], ["e"]])
        self.assertEqual([item for page in pages for item in page], self.items)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            inventory.paginate(self.items, 0, 2)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            inventory.paginate(self.items, 1, 0)


if __name__ == "__main__":
    unittest.main()
