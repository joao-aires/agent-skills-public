import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'plugins/development-workflow/skills/project-bootstrap/scripts/scaffold.py'
spec = importlib.util.spec_from_file_location('scaffold_starter', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class StarterTests(unittest.TestCase):
    def test_reference_is_self_contained_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / 'reference'
            module.scaffold(project, starter=True)
            for file in ['applications/api/uv.lock', 'applications/api/migrations/versions/0001_notes.py',
                         'applications/web/pnpm-lock.yaml', 'applications/web/components.json',
                         'applications/web/tests/e2e/notes.spec.ts', 'documentation/architecture/schemas/openapi.json',
                         'applications/tooling/inventory_skills.py']:
                self.assertTrue((project / file).is_file(), file)
            self.assertFalse(any(p.is_symlink() for p in project.rglob('*')))
            subprocess.run(['python', str(project / 'applications/tooling/check_project.py'), str(project)], check=True, capture_output=True)
            with self.assertRaises(ValueError):
                module.scaffold(project, starter=True)
