"""Guard the validation boundary of the privileged marketplace publisher."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('publication_validator', ROOT / 'scripts/validate_plugins.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PublicationTests(unittest.TestCase):
    def test_two_publications_keep_update_history_and_remove_stale_files(self):
        publication = yaml.load(
            (ROOT / '.github/workflows/publish-claude-marketplace.yml').read_text(),
            Loader=yaml.BaseLoader)
        command = publication['jobs']['publish']['steps'][-1]['run']
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote, workspace = root / 'remote.git', root / 'workspace'
            env = dict(os.environ, GITHUB_WORKSPACE=str(workspace), GITHUB_SHA='synthetic-source',
                       GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1',
                       GIT_AUTHOR_NAME='Fixture', GIT_AUTHOR_EMAIL='fixture@example.invalid',
                       GIT_COMMITTER_NAME='Fixture', GIT_COMMITTER_EMAIL='fixture@example.invalid')
            def git(*args, cwd=root):
                return subprocess.run(['git', *args], cwd=cwd, env=env, check=True,
                                      capture_output=True, text=True).stdout.strip()
            git('init', '--bare', str(remote))
            git('clone', str(remote), str(workspace))
            heads = []
            for generation in (1, 2):
                output = root / f'generation-{generation}'
                output.mkdir()
                (output / 'current.txt').write_text(f'Generation {generation}')
                if generation == 1:
                    (output / 'removed-next-time.txt').write_text('stale')
                subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', command], cwd=output,
                               env=env, check=True, capture_output=True, text=True)
                heads.append(git('rev-parse', 'refs/heads/claude-marketplace', cwd=remote))
                if generation == 1:
                    git('clone', '--branch', 'claude-marketplace', str(remote), str(root / 'consumer'))
            self.assertEqual(git('rev-parse', heads[1] + '^', cwd=remote), heads[0])
            git('pull', '--ff-only', cwd=root / 'consumer')
            self.assertEqual((root / 'consumer/current.txt').read_text(), 'Generation 2')
            self.assertFalse((root / 'consumer/removed-next-time.txt').exists())
            # Re-publishing identical output should not add an empty commit.
            output = root / 'unchanged'
            output.mkdir()
            (output / 'current.txt').write_text('Generation 2')
            subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', command], cwd=output,
                           env=env, check=True, capture_output=True, text=True)
            self.assertEqual(git('rev-parse', 'refs/heads/claude-marketplace', cwd=remote), heads[1])

    def test_publisher_requires_the_same_revision_validation_workflow(self):
        publication = yaml.load(
            (ROOT / '.github/workflows/publish-claude-marketplace.yml').read_text(),
            Loader=yaml.BaseLoader)
        validation = publication['jobs']['validate']
        self.assertEqual(validation['uses'], './.github/workflows/validate.yml')
        self.assertEqual(validation['if'], "github.ref == 'refs/heads/main'")
        publish = publication['jobs']['publish']
        self.assertEqual(publish['needs'], 'validate')
        self.assertEqual(publish['if'], "github.ref == 'refs/heads/main'")
        self.assertEqual(publication['permissions']['contents'], 'read')
        self.assertEqual(publish['permissions']['contents'], 'write')
        required = yaml.load((ROOT / '.github/workflows/validate.yml').read_text(), Loader=yaml.BaseLoader)
        self.assertIn('workflow_call', required['on'])
        steps = required['jobs']['validate']['steps']
        commands = '\n'.join(step.get('run', '') for step in steps)
        self.assertIn('python scripts/validate_plugins.py', commands)
        self.assertIn('python -m unittest discover -s tests -v', commands)
        self.assertIn('node .agent-depot/tool/dist/cli.js --json verify', commands)

    def test_source_validation_blocks_an_escaping_resource(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'schemas').mkdir()
            for name in ('plugin', 'mcp'):
                (root / f'schemas/{name}.schema.json').write_text('{}')
            package = root / 'plugins/example'
            package.mkdir(parents=True)
            (package / 'plugin.json').write_text(json.dumps({'name': 'example'}))
            (package / 'LICENSE').write_text('Synthetic fixture license')
            # A marker outside the distributable must never be accepted for publication.
            outside = root / 'private-marker.txt'
            outside.write_text('synthetic non-package content')
            (package / 'outside.txt').symlink_to(outside)
            with patch.object(validator, 'ROOT', root), patch.object(validator, 'load_sources', return_value=[]):
                failures = validator.validate()
            self.assertTrue(any('Escaping package path' in failure for failure in failures), failures)


if __name__ == '__main__':
    unittest.main()
