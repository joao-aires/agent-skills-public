"""Checks for the generated skills map and its maintainer inventory view."""
import subprocess
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HEADER = '| Skill | Pack | Domain | Kind | Phase | Origin | Scope | Invocation | Role | Plugin |'


class SkillMapTests(unittest.TestCase):
    def run_map(self, *args):
        return subprocess.run([sys.executable, 'scripts/skill_map.py', *args], cwd=ROOT,
                              capture_output=True, text=True, check=False)

    def test_inventory_view_prints_the_classification_matrix(self):
        result = self.run_map('--inventory')
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(lines[0], HEADER)
        expected = len(list((ROOT / 'plugins').glob('*/skills/*/SKILL.md')))
        self.assertEqual(len(lines) - 2, expected)
        for line in lines[2:]:
            self.assertEqual(line.count('|'), HEADER.count('|'))


if __name__ == '__main__':
    unittest.main()
