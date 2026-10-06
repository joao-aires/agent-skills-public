import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('installer', Path(__file__).resolve().parents[1] / 'scripts/build_plugins.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def test_pinned_build_references_notices_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            upstream = root / 'upstream'
            upstream.mkdir()
            subprocess.run(['git', 'init', '-q', str(upstream)], check=True)
            skill = upstream / 'skills/example'
            (skill / 'references').mkdir(parents=True)
            (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Test upstream\n---\nSee references/guide.md\n')
            (skill / 'references/guide.md').write_text('Complete reference')
            (upstream / 'LICENSE').write_text('Test license notice')
            subprocess.run(['git', '-C', str(upstream), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(upstream), '-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-qm', 'Fixture'], check=True)
            commit = installer.git(upstream, 'rev-parse', 'HEAD').decode().strip()
            tree = installer.git(upstream, 'rev-parse', 'HEAD:skills/example').decode().strip()
            source = dict(plugin='test', repository=str(upstream), commit=commit, tree=tree, path='skills/example', license='MIT', license_path='LICENSE')
            package = root / 'plugins/test'
            package.mkdir(parents=True)
            (package / 'plugin.json').write_text('{"name":"test","version":"0.1.0","description":"Test"}')
            (root / 'schemas').mkdir(exist_ok=True)
            (root / 'schemas/plugin.schema.json').write_text('{}')
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': [source]}))
            output = root / 'installed'
            installer.build(root, ['test'], output, root / 'cache')
            self.assertEqual((output / 'test/skills/example/references/guide.md').read_text(), 'Complete reference')
            self.assertEqual((output / 'test/skills/example/UPSTREAM-LICENSE.txt').read_text(), 'Test license notice')
            self.assertFalse(any(p.is_symlink() for p in output.rglob('*')))
            with self.assertRaises(ValueError):
                installer.build(root, ['test'], output, root / 'cache')
            source['tree'] = '0' * 40
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': [source]}))
            with self.assertRaises(ValueError):
                installer.build(root, ['test'], root / 'tampered', root / 'cache')
            self.assertFalse((root / 'tampered').exists())
