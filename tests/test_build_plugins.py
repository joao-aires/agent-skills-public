import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import yaml

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
            (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Test upstream\ndisable-model-invocation: true\nmetadata:\n  credits:\n    author: Original Author\n    url: https://example.com/source\n---\nSee references/guide.md and docs/agents/config.md and docs/adr/\n')
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
            with self.assertRaisesRegex(ValueError, 'map strings to strings'):
                installer.build(root, ['test'], output, root / 'cache')
            self.assertFalse(output.exists())
            source['adaptations'] = ['string-metadata']
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': [source]}))
            installer.build(root, ['test'], output, root / 'cache')
            self.assertEqual((output / 'test/skills/example/references/guide.md').read_text(), 'Complete reference')
            self.assertEqual((output / 'test/skills/example/UPSTREAM-LICENSE.txt').read_text(), 'Test license notice')
            self.assertFalse(any(p.is_symlink() for p in output.rglob('*')))
            metadata = yaml.safe_load((output / 'test/skills/example/SKILL.md').read_text().split('---', 2)[1])
            self.assertEqual(json.loads(metadata['metadata']['credits']),
                             {'author': 'Original Author', 'url': 'https://example.com/source'})
            self.assertEqual((output / 'test/skills/example/agents/openai.yaml').read_text(),
                             'policy:\n  allow_implicit_invocation: false\n')
            # Build adapted output without changing the pinned source or native metadata.
            source['adaptations'] = ['string-metadata', 'workflow-framing', 'documentation-paths']
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

    def test_adversarial_review_uses_packaged_inline_method(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'differential-review'
            skill.mkdir()
            (skill / 'adversarial.md').write_text('Analyze attacker paths and verify exploitability.')
            (skill / 'SKILL.md').write_text(
                '---\nname: differential-review\ndescription: Review security changes.\n---\n'
                '│  └─ Or delegate to: differential-review:adversarial-modeler agent\n'
                '│     (Autonomous attacker modeling with concrete exploit scenarios)\n'
                '\n## Agents\n\nDispatch differential-review:adversarial-modeler via subagent_type.\n'
                '\n---\n\n## Quality Checklist\nVerify the evidence.\n')
            installer.adapt_skill(skill, {'adaptations': ['inline-adversarial-review']})
            text = (skill / 'SKILL.md').read_text()
            self.assertNotIn('adversarial-modeler', text)
            self.assertNotIn('subagent_type', text)
            self.assertIn('(adversarial.md)', text)
            self.assertTrue((skill / 'adversarial.md').is_file())
            self.assertIn('## Quality Checklist', text)

    def test_built_local_skills_receive_optional_metadata_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / 'plugins/example/skills/example'
            skill.mkdir(parents=True)
            (skill.parent.parent / 'plugin.json').write_text('{"name":"example"}')
            (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Example\nallowed-tools: [Read, Bash]\n---\nGuide\n')
            (root / 'schemas').mkdir()
            (root / 'schemas/plugin.schema.json').write_text('{}')
            (root / 'upstream.lock.json').write_text('{"sources":[]}')
            output = root / 'output'
            with self.assertRaisesRegex(ValueError, 'allowed-tools'):
                installer.build(root, ['example'], output, root / 'cache')
            self.assertFalse(output.exists())
