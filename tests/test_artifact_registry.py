"""Consistency checks for the artifact registry, contracts, guides and activities."""
import importlib.util
import json
import re
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / 'plugins/sdlc/skills/artifact-system/references'
CONTRACTS = ARTIFACTS / 'contracts'
SKILLS = ROOT / 'plugins/sdlc/skills'
ACTIVITY_CATALOG = SKILLS / 'activity-system/references/catalog.md'


def load_registry_module():
    spec = importlib.util.spec_from_file_location('artifact_registry', ROOT / 'scripts/artifact_registry.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def metadata(path):
    parts = path.read_text().split('---', 2)
    return yaml.safe_load(parts[1]) if len(parts) == 3 else {}


def acquired_labels():
    data = json.loads((ROOT / 'agent-depot.json').read_text())
    labels = {}
    for value in data.get('artifacts', data).values():
        if isinstance(value, dict) and value.get('destination'):
            packaging = value.get('metadata', {}).get('packaging', {})
            labels[value['destination']] = packaging.get('labels', {})
    return labels


def skill_labels(path):
    relative = path.parent.relative_to(ROOT).as_posix()
    return acquired_labels().get(relative) or (metadata(path).get('metadata', {}) or {})


class ArtifactConsistencyTests(unittest.TestCase):
    def test_artifact_registry_is_valid(self):
        self.assertEqual(load_registry_module().validate(), [])

    def test_contracts_have_required_headings(self):
        for path in sorted(CONTRACTS.glob('*.md')):
            if path.name in {'README.md', 'TEMPLATE.md'}:
                continue
            text = path.read_text()
            with self.subTest(contract=path.name):
                for heading in ('## Reader questions', '## Contract', '## Handoff'):
                    self.assertIn(heading, text)

    def activity_names(self):
        text = ACTIVITY_CATALOG.read_text()
        start = text.index('## Core activities')
        end = text.index('## Assure')
        names = set()
        for line in text[start:end].splitlines():
            if not line.startswith('| ['):
                continue
            first = line.split('|')[1].strip()
            match = re.match(r'\[[^\]]+\]\(\.\./\.\./([^/]+)/SKILL\.md\)', first)
            if match:
                names.add(match.group(1))
        return names

    def test_activity_tables_do_not_list_guides_as_activities(self):
        self.assertTrue(self.activity_names())
        for name in sorted(self.activity_names()):
            self.assertFalse(name.startswith('guide-'), name)

    def test_activity_rows_point_to_activity_skills(self):
        names = self.activity_names()
        self.assertTrue(names)
        for name in sorted(names):
            path = SKILLS / name / 'SKILL.md'
            with self.subTest(activity=name):
                self.assertTrue(path.is_file(), path)
                labels = skill_labels(path)
                self.assertEqual(labels.get('kind'), 'activity', name)

    def test_guides_are_self_contained(self):
        for path in sorted(SKILLS.glob('guide-*/SKILL.md')):
            text = path.read_text()
            with self.subTest(guide=path.parent.name):
                for forbidden in ('artifact-system', 'activity-system', '/contracts/', 'software-types', 'handoff.md'):
                    self.assertNotIn(forbidden, text)

    def test_every_guide_has_a_registry_entry(self):
        registry = load_registry_module().load()
        registered = {entry['guide'] for entry in registry if entry.get('guide')}
        guides = {p.parent.name for p in SKILLS.glob('guide-*/SKILL.md')}
        self.assertEqual(guides, registered)


if __name__ == '__main__':
    unittest.main()
