import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("collection", Path(__file__).resolve().parents[1] / "scripts/check_collection.py")
collection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collection)


class CollectionTests(unittest.TestCase):
    def fixture(self, root):
        (root / "documentation").mkdir()
        (root / "README.md").write_text("[Start](documentation/usage.md#start)\n")
        (root / "AGENTS.md").write_text("Instructions\n")
        (root / "documentation/usage.md").write_text("# Start\n")
        (root / "documentation/migration.md").write_text("| `old-name` | `new-name` |\n")

    def test_broken_heading_and_stale_name_fail_but_fenced_examples_do_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            self.assertFalse(collection.check_links(root)[0])
            (root / "README.md").write_text("[Start](documentation/usage.md#missing)\nUse `old-name`.\n```md\n[Example](missing.md)\n```\n")
            errors, _ = collection.check_links(root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("missing heading" in error for error in errors))
            self.assertTrue(any("obsolete skill" in error for error in errors))

    def test_missing_resource_and_extra_skill_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plugins/example"
            skill = source / "skills/local"
            skill.mkdir(parents=True)
            (source / "plugin.json").write_text('{}')
            (skill / "SKILL.md").write_text('Local')
            (skill / "resource.txt").write_text('Keep this resource')
            (root / "upstream.lock.json").write_text('{"sources": []}')
            built = root / "built"
            shutil.copytree(root / "plugins", built)
            (built / "example/UPSTREAM-NOTICES.json").write_text('[]')
            self.assertFalse(collection.check_built(root, built)[0])
            (built / "example/skills/local/resource.txt").unlink()
            (built / "example/skills/old-name").mkdir()
            errors, _ = collection.check_built(root, built)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("resource.txt" in error for error in errors))
            self.assertTrue(any("inventory" in error for error in errors))
