"""Validate the end-to-end behavioral scenario battery."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / 'evals/behavioral-scenarios.json'
SKILLS = ROOT / 'plugins/sdlc/skills'


class BehavioralScenarioTests(unittest.TestCase):
    def test_scenarios_reference_existing_skills_and_have_expectations(self):
        data = json.loads(SPEC.read_text())
        scenarios = data['scenarios']
        self.assertEqual(len({s['id'] for s in scenarios}), len(scenarios))
        for scenario in scenarios:
            with self.subTest(scenario=scenario['id']):
                for field in ('id', 'name', 'fixture', 'fixture_path', 'prompt', 'skills', 'expectations', 'failure_signals'):
                    self.assertIn(field, scenario)
                self.assertTrue(scenario['skills'])
                self.assertTrue(scenario['expectations'])
                self.assertTrue(scenario['failure_signals'])
                for skill in scenario['skills']:
                    self.assertTrue((SKILLS / skill / 'SKILL.md').is_file(), skill)
                self.assertTrue((ROOT / scenario['fixture_path']).is_dir(), scenario['fixture_path'])


if __name__ == '__main__':
    unittest.main()
