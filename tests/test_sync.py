import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sync_skills", ROOT / "scripts/sync_skills.py")
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class SyncTests(unittest.TestCase):
    def test_updates_legacy_links_and_preserves_unrelated_links(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            target = home / ".agents/skills"
            target.mkdir(parents=True)
            legacy = target / "business-strategy"
            legacy.symlink_to(ROOT / "skills/business-strategy")
            unrelated_source = home / "other"
            unrelated_source.mkdir()
            unrelated = target / "backend-conventions"
            unrelated.symlink_to(unrelated_source)
            with patch.object(Path, "home", return_value=home), patch("sys.argv", ["sync_skills.py", "sync"]):
                SYNC.main()
            self.assertEqual(legacy.resolve(), (ROOT / "plugins/strategy/skills/business-strategy").resolve())
            self.assertEqual(unrelated.resolve(), unrelated_source.resolve())
            with patch.object(Path, "home", return_value=home), patch("sys.argv", ["sync_skills.py", "remove"]):
                SYNC.main()
            self.assertFalse(legacy.is_symlink())
            self.assertTrue(unrelated.is_symlink())


    def test_managed_link_from_superseded_bundle_can_be_repaired(self):
        with tempfile.TemporaryDirectory() as tmp:
            link = Path(tmp) / 'business-strategy'
            link.symlink_to(ROOT / 'plugins/business-strategy/skills/business-strategy')
            current = ROOT / 'plugins/strategy/skills/business-strategy'
            self.assertTrue(SYNC.managed(link, 'business-strategy', current))
            link.unlink()
            link.symlink_to(Path(tmp) / 'other/plugins/strategy/skills/business-strategy')
            self.assertFalse(SYNC.managed(link, 'business-strategy', current))


if __name__ == "__main__":
    unittest.main()
