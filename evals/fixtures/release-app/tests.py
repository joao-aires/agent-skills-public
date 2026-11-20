import unittest
import app


class AppTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(app.status()["version"], "1.3.0")


if __name__ == "__main__":
    unittest.main()
