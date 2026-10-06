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
            (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Test upstream\ndisable-model-invocation: true\n---\nSee references/guide.md and docs/agents/config.md and docs/adr/\n')
            (skill / 'references/guide.md').write_text('Complete reference')
            (skill / 'agents').mkdir()
            (skill / 'agents/openai.yaml').write_text('policy:\n  allow_implicit_invocation: false\n')
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
            self.assertEqual((output / 'test/skills/example/agents/openai.yaml').read_text(),
                             'policy:\n  allow_implicit_invocation: false\n')
            # Build adapted output without changing the pinned source or native metadata.
            source['adaptations'] = ['workflow-framing', 'documentation-paths']
            (package / 'WORKFLOW.md').write_text('Project workflow guidance')
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': [source]}))
            adapted = root / 'adapted'
            installer.build(root, ['test'], adapted, root / 'cache')
            skill_text = (adapted / 'test/skills/example/SKILL.md').read_text()
            self.assertIn('../../WORKFLOW.md', skill_text)
            self.assertIn('documentation/engineering/config.md', skill_text)
            self.assertIn('documentation/decisions/adr/', skill_text)
            self.assertIn('disable-model-invocation: true', skill_text)
            self.assertTrue((adapted / 'test/WORKFLOW.md').exists())
            self.assertEqual((adapted / 'test/skills/example/agents/openai.yaml').read_text(),
                             (skill / 'agents/openai.yaml').read_text())
            self.assertNotIn('workflow framing', (skill / 'SKILL.md').read_text())
            notices = json.loads((adapted / 'test/skills/example/UPSTREAM.json').read_text())
            self.assertEqual(notices['adaptations'], source['adaptations'])

            with self.assertRaises(ValueError):
                installer.build(root, ['test'], output, root / 'cache')
            source['tree'] = '0' * 40
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': [source]}))
            with self.assertRaises(ValueError):
                installer.build(root, ['test'], root / 'tampered', root / 'cache')
            self.assertFalse((root / 'tampered').exists())
