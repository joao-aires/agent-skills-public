import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_plugins.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class InvocationTests(unittest.TestCase):
    def test_user_only_settings_must_agree_across_clients(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'schemas').mkdir()
            for name in ('plugin', 'mcp'):
                (root / f'schemas/{name}.schema.json').write_text('{}')
            (root / 'upstream.lock.json').write_text(json.dumps({'sources': []}))
            skill = root / 'plugins/example/skills/start-work'
            (skill / 'agents').mkdir(parents=True)
            (root / 'plugins/example/plugin.json').write_text('{"name":"example"}')
            (skill / 'SKILL.md').write_text('---\nname: start-work\ndescription: Start a workflow on request.\ndisable-model-invocation: true\n---\nStart the requested work.\n')
            settings = skill / 'agents/openai.yaml'
            settings.write_text('policy:\n  allow_implicit_invocation: false\n')
            with patch.object(validator, 'ROOT', root):
                self.assertEqual(validator.validate(), [])
                settings.write_text('policy:\n  allow_implicit_invocation: true\n')
                self.assertTrue(any('Conflicting invocation metadata' in e for e in validator.validate()))
                settings.write_text('policy:\n  allow_implicit_invocation: false\n')
                p = skill / 'SKILL.md'
                p.write_text(p.read_text().replace('invocation: true', 'invocation: "true"'))
                self.assertTrue(any('Invalid invocation flag' in e for e in validator.validate()))
