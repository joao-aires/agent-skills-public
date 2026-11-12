"""Exercise the real frontend bundle, including relocated upstream search resources."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('design_builder', ROOT / 'scripts/build_plugins.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def inventory(path):
    return {p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in path.rglob('*') if p.is_file()}


class BundledDesignMethodsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.workspace = Path(cls.temp.name)
        output = cls.workspace / 'build'
        cls.before = {name: inventory(ROOT / 'plugins/frontend-development/skills' / name)
                      for name in ('impeccable', 'ui-ux-pro-max')}
        builder.build(ROOT, ['frontend-development'], output)
        # Resource resolution must survive relocation and a working directory outside the package.
        cls.package = cls.workspace / 'relocated frontend'
        (output / 'frontend-development').rename(cls.package)

    def test_mixed_license_notices_resources_and_native_controls(self):
        manifest = json.loads((self.package / 'plugin.json').read_text())
        self.assertEqual(manifest['license'], 'LicenseRef-Mixed')
        notices = json.loads((self.package / 'UPSTREAM-NOTICES.json').read_text())
        self.assertEqual({n['installed_skill'] for n in notices}, {'impeccable', 'ui-ux-pro-max'})
        declarations = json.loads((ROOT / 'agent-depot.json').read_text())['artifacts']
        for notice in notices:
            name = notice['installed_skill']
            with self.subTest(skill=name):
                acquired = ROOT / 'plugins/frontend-development/skills' / name
                installed = self.package / 'skills' / name
                pin = declarations['frontend-development--' + name]
                self.assertEqual(notice['commit'], pin['commit'])
                self.assertEqual(json.loads((installed / 'UPSTREAM.json').read_text()), notice)
                self.assertEqual((installed / 'UPSTREAM-LICENSE.txt').read_bytes(),
                                 (acquired / 'UPSTREAM-LICENSE.txt').read_bytes())
                source_text = (acquired / 'SKILL.md').read_text()
                installed_text = (installed / 'SKILL.md').read_text()
                # Only declared metadata adaptation; original specialist method stays intact.
                self.assertEqual(source_text.split('---', 2)[2], installed_text.split('---', 2)[2])
                native = yaml.safe_load(source_text.split('---', 2)[1])
                built = yaml.safe_load(installed_text.split('---', 2)[1])
                for control in ('user-invocable', 'disable-model-invocation'):
                    if control in native:
                        self.assertEqual(native[control], built[control])
                self.assertEqual(self.before[name], inventory(acquired))
        impeccable = self.package / 'skills/impeccable'
        self.assertTrue((impeccable / 'UPSTREAM-NOTICE.md').is_file())
        self.assertTrue((impeccable / 'scripts/engine-checksums.txt').is_file())
        self.assertEqual(len(list((impeccable / 'agents').glob('*.md'))), 4)

    def test_relocated_local_search_uses_its_own_data_without_mutation(self):
        skill = self.package / 'skills/ui-ux-pro-max'
        before = inventory(skill)
        for query, mode, expected in [
            ('creative portfolio gallery', '--design-system', 'RECOMMENDED DESIGN SYSTEM'),
            ('keyboard focus visible', '--domain', 'Focus States'),
        ]:
            args = [sys.executable, '-B', str(skill / 'scripts/search.py'), query, mode]
            if mode == '--domain':
                args.append('ux')
            with self.subTest(mode=mode):
                result = subprocess.run(args, cwd=self.workspace, capture_output=True, text=True,
                                        timeout=30, check=True)
                self.assertIn(expected, result.stdout)
                self.assertNotIn('Traceback', result.stderr)
        self.assertEqual(before, inventory(skill))
        self.assertFalse((self.workspace / 'design-system').exists())
