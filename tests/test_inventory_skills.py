import importlib.util
from pathlib import Path
import tempfile
import unittest
spec = importlib.util.spec_from_file_location('inventory', Path(__file__).resolve().parents[1] / 'scripts/inventory_skills.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InventoryTests(unittest.TestCase):
    def test_active_metadata_without_body_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ['active', 'uninstalled/disabled']:
                p = root / folder
                p.mkdir(parents=True)
                (p / 'SKILL.md').write_text('---\nname: design\ndescription: UI guidance\n---\nPRIVATE BODY')
            data = module.inventory([root])
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['name'], 'design')
            self.assertNotIn('PRIVATE BODY', str(data))
            self.assertEqual(len(data[0]['sha256']), 64)
