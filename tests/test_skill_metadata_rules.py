import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_metadata", ROOT / "scripts/skill_metadata.py")
skill_metadata = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(skill_metadata)


def write_skill(root, **overrides):
    fields = {
        "invocation": "agent",
        "kind": "method",
        "pack": "sdlc",
        "domain": "development",
        "phase": "design",
        "role": "support",
        "origin": "local",
        "scope": "generic",
    }
    fields.update(overrides)
    metadata = "\n".join(f"  {key}: {value}" for key, value in fields.items())
    path = root / "plugins/example/skills/example-skill"
    path.mkdir(parents=True)
    (path / "SKILL.md").write_text(
        "---\n"
        "name: example-skill\n"
        "description: Placeholder skill for metadata tests.\n"
        "user-invocable: false\n"
        f"metadata:\n{metadata}\n"
        "---\n\nExample body.\n"
    )
    return path / "SKILL.md"


class InvocationLabelTests(unittest.TestCase):
    def test_agent_label_allows_no_user_surface(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = write_skill(Path(directory), invocation="agent")
            self.assertIsNotNone(skill_metadata.validate_local_skill_classification(skill))

    def test_user_label_requires_a_user_surface(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = write_skill(Path(directory), invocation="user")
            with self.assertRaisesRegex(ValueError, "requires a user surface"):
                skill_metadata.validate_local_skill_classification(skill)

    def test_both_label_allows_no_direct_command(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = write_skill(Path(directory), invocation="both")
            self.assertIsNotNone(skill_metadata.validate_local_skill_classification(skill))


if __name__ == "__main__":
    unittest.main()
