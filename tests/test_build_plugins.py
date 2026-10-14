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
    def test_support_visibility_preserves_explicit_native_controls(self):
        for explicit in (None, True, False):
            with self.subTest(explicit=explicit), tempfile.TemporaryDirectory() as tmp:
                skill = Path(tmp) / 'example'
                skill.mkdir()
                metadata = {'name': 'example', 'description': 'Example',
                            'disable-model-invocation': True, 'metadata': {'author': 'Upstream'}}
                if explicit is not None:
                    metadata['user-invocable'] = explicit
                (skill / 'SKILL.md').write_text('---\n' + yaml.safe_dump(metadata) + '---\nOriginal body\n')
                (skill / 'resource.txt').write_text('Original resource')
                installer.adapt_skill(skill, {'adaptations': ['support-visibility']})
                text = (skill / 'SKILL.md').read_text()
                result = yaml.safe_load(text.split('---', 2)[1])
                self.assertEqual(result['user-invocable'], explicit if explicit is not None else False)
                self.assertTrue(result['disable-model-invocation'])
                self.assertEqual(result['metadata']['author'], 'Upstream')
                self.assertTrue(text.endswith('\nOriginal body\n'))
                self.assertEqual((skill / 'resource.txt').read_text(), 'Original resource')

    def test_implementation_entrypoint_retains_upstream_body_and_control(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'implement'
            skill.mkdir()
            (skill / 'SKILL.md').write_text('---\nname: implement\ndescription: Original\ndisable-model-invocation: true\n---\nOriginal implementation workflow\n')
            installer.adapt_skill(skill, {'adaptations': ['implementation-entrypoint']})
            text = (skill / 'SKILL.md').read_text()
            metadata = yaml.safe_load(text.split('---', 2)[1])
            self.assertEqual(metadata['name'], 'implement')
            self.assertTrue(metadata['user-invocable'])
            self.assertTrue(metadata['disable-model-invocation'])
            self.assertIn('../../TASKS.md', text)
            self.assertTrue(text.endswith('\nOriginal implementation workflow\n'))

    def test_frontend_framing_preserves_metadata_and_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'tailwind-design-system'
            skill.mkdir()
            original = '---\nname: tailwind-design-system\ndescription: Example\ndisable-model-invocation: true\n---\n# Version-specific guidance\nKeep original content.\n'
            (skill / 'SKILL.md').write_text(original)
            installer.adapt_skill(skill, {'adaptations': ['frontend-framing']})
            result = (skill / 'SKILL.md').read_text()
            self.assertEqual(yaml.safe_load(result.split('---', 2)[1]), yaml.safe_load(original.split('---', 2)[1]))
            self.assertIn('../frontend-conventions/SKILL.md', result)
            self.assertIn('not authorization to migrate or redesign', result)
            self.assertTrue(result.endswith(original.split('---', 2)[2]))

    def test_backend_framing_preserves_metadata_resources_and_examples(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'mcp-builder'
            skill.mkdir()
            original = '---\nname: mcp-builder\ndescription: Example\nuser-invocable: false\n---\n# Original\nfrom mcp.server.fastmcp import FastMCP\n'
            (skill / 'SKILL.md').write_text(original)
            (skill / 'reference.md').write_text('Original resource')
            installer.adapt_skill(skill, {'adaptations': ['backend-framing']})
            result = (skill / 'SKILL.md').read_text()
            self.assertEqual(yaml.safe_load(result.split('---', 2)[1]), yaml.safe_load(original.split('---', 2)[1]))
            self.assertIn('../backend-conventions/SKILL.md', result)
            self.assertIn('from fastmcp import FastMCP', result)
            self.assertIn('Do not migrate existing tooling', result)
            self.assertTrue(result.endswith(original.split('---', 2)[2]))
            self.assertEqual((skill / 'reference.md').read_text(), 'Original resource')

    def test_root_skill_acquisition_preserves_resources_and_checks_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            upstream = root / 'upstream'
            upstream.mkdir()
            subprocess.run(['git', 'init', '-q', str(upstream)], check=True)
            (upstream / 'SKILL.md').write_text('---\nname: root-skill\ndescription: Root fixture\n---\nRead references/guide.md\n')
            (upstream / 'references').mkdir()
            (upstream / 'references/guide.md').write_text('Complete reference')
            subprocess.run(['git', '-C', str(upstream), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(upstream), '-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-qm', 'Fixture'], check=True)
            commit = installer.git(upstream, 'rev-parse', 'HEAD').decode().strip()
            tree = installer.git(upstream, 'rev-parse', 'HEAD^{tree}').decode().strip()
            source = dict(repository=str(upstream), commit=commit, tree=tree, path='.')
            _, archive = installer.acquire(source, root / 'cache')
            output = root / 'skill'
            installer.extract_skill(archive, '.', output)
            self.assertTrue((output / 'SKILL.md').exists())
            self.assertEqual((output / 'references/guide.md').read_text(), 'Complete reference')
            source['tree'] = '0' * 40
            with self.assertRaisesRegex(ValueError, 'tree mismatch'):
                installer.acquire(source, root / 'cache')

    def test_usage_labels_preserve_native_controls_and_attribution(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'example'
            skill.mkdir()
            path = skill / 'SKILL.md'
            path.write_text('---\nname: example\ndescription: Example\ndisable-model-invocation: true\nmetadata:\n  author: Original Author\n---\nOriginal body\n')
            installer.adapt_skill(skill, {'adaptations': ['usage-labels'], 'labels': {'scope': 'generic', 'invocation': 'user'}})
            result = path.read_text()
            data = yaml.safe_load(result.split('---', 2)[1])
            self.assertTrue(data['disable-model-invocation'])
            self.assertEqual(data['metadata']['author'], 'Original Author')
            self.assertEqual(data['metadata']['scope'], 'generic')
            self.assertTrue(result.endswith('\nOriginal body\n'))
            with self.assertRaisesRegex(ValueError, 'Invalid usage labels'):
                installer.adapt_skill(skill, {'adaptations': ['usage-labels'], 'labels': {'scope': 'universal', 'invocation': 'user'}})

    def test_tracker_neutral_adaptation_and_upstream_drift_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'implement-spec'
            skill.mkdir()
            path = skill / 'SKILL.md'
            path.write_text('---\nname: implement-spec\ndescription: Implement /to-tickets\ndisable-model-invocation: true\n---\nThe issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.\nUnchanged implementation steps.\n')
            installer.adapt_skill(skill, {'adaptations': ['tracker-neutral']})
            result = path.read_text()
            self.assertNotIn('setup-matt-pocock-skills', result)
            self.assertNotIn('/to-tickets', result)
            self.assertIn('Unchanged implementation steps.', result)
            self.assertTrue(yaml.safe_load(result.split('---', 2)[1])['disable-model-invocation'])
            with self.assertRaisesRegex(ValueError, 'Unexpected tracker prerequisite'):
                installer.adapt_skill(skill, {'adaptations': ['tracker-neutral']})

    def test_ai_framing_points_within_ai_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'mcp-builder'
            skill.mkdir()
            path = skill / 'SKILL.md'
            path.write_text('---\nname: mcp-builder\ndescription: Example\n---\nOriginal SDK guidance\n')
            installer.adapt_skill(skill, {'adaptations': ['ai-framing']})
            result = path.read_text()
            self.assertIn('../build-evaluated-ai/SKILL.md', result)
            self.assertIn('not an LLM', result)
            self.assertNotIn('../backend-conventions', result)
            self.assertTrue(result.endswith('\nOriginal SDK guidance\n'))

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

    def test_local_script_resources_exclude_runtime_bytecode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / 'plugins/example/skills/example'
            skill.mkdir(parents=True)
            (skill.parent.parent / 'plugin.json').write_text('{"name":"example"}')
            (skill / 'SKILL.md').write_text('---\nname: example\ndescription: Example\n---\nGuide\n')
            scripts = skill / 'scripts'
            scripts.mkdir()
            (scripts / 'render.py').write_text('print("example")\n')
            (scripts / '__pycache__').mkdir()
            (scripts / '__pycache__/render.cpython-313.pyc').write_bytes(b'local cache')
            (root / 'schemas').mkdir()
            (root / 'schemas/plugin.schema.json').write_text('{}')
            (root / 'upstream.lock.json').write_text('{"sources":[]}')
            output = root / 'output'
            installer.build(root, ['example'], output, root / 'cache')
            installed = output / 'example/skills/example/scripts'
            self.assertEqual((installed / 'render.py').read_text(), 'print("example")\n')
            self.assertFalse((installed / '__pycache__').exists())
