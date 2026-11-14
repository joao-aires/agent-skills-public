from pathlib import Path
import tempfile
import unittest

import yaml

from scripts.skill_metadata import validate_local_skill_classification, validate_skill_metadata


class SkillMetadataTests(unittest.TestCase):
    def test_optional_standard_fields_and_native_invocation_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'example'
            skill.mkdir()
            path = skill / 'SKILL.md'
            metadata = dict(name='example', description='Example guidance', license='MIT',
                            compatibility='Requires Git', metadata={'author': 'Author'},
                            **{'allowed-tools': 'Read Bash(git:*)', 'disable-model-invocation': True})
            path.write_text('---\n' + yaml.safe_dump(metadata) + '---\nGuide\n')
            self.assertEqual(validate_skill_metadata(path), metadata)

    def test_invalid_optional_fields_are_rejected(self):
        cases = [
            {'metadata': {'credits': {'author': 'Author'}}},
            {'metadata': {'version': 1}},
            {'metadata': {'scope': 'anything'}},
            {'metadata': {'invocation': 'auto-magic'}},
            {'metadata': {'role': 'dispatcher'}},
            {'metadata': {'kind': 'other'}},
            {'metadata': {'origin': 'elsewhere'}},
            {'metadata': {'scope': 'stack-specific'}},
            {'metadata': ['author']},
            {'allowed-tools': ['Read', 'Bash']},
            {'license': ['MIT']},
            {'compatibility': ''},
            {'compatibility': 'x' * 501},
            {'disable-model-invocation': 'true'},
            {'user-invocable': 'false'},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'example'
            skill.mkdir()
            path = skill / 'SKILL.md'
            for fields in cases:
                with self.subTest(fields=fields):
                    path.write_text('---\n' + yaml.safe_dump(dict(name='example', description='Example', **fields)) + '---\nGuide\n')
                    with self.assertRaises(ValueError):
                        validate_skill_metadata(path)

    def test_local_classification_requires_kind_and_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / 'example'
            skill.mkdir()
            path = skill / 'SKILL.md'
            metadata = dict(name='example', description='Example', metadata={
                'scope': 'generic', 'invocation': 'agent', 'role': 'support', 'pack': 'sdlc', 'domain': 'development', 'phase': 'cross-phase'})
            path.write_text('---\n' + yaml.safe_dump(metadata) + '---\nGuide\n')
            with self.assertRaises(ValueError):
                validate_local_skill_classification(path)
            metadata['metadata'].update({'kind': 'method', 'origin': 'local'})
            path.write_text('---\n' + yaml.safe_dump(metadata) + '---\nGuide\n')
            self.assertEqual(validate_local_skill_classification(path), metadata)
