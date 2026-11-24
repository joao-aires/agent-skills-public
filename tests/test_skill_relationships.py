import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("relationships", ROOT / "scripts/skill_relationships.py")
relationships = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(relationships)


def write_skill(root, name, body, frontmatter=(), plugin="example"):
    lines = ["---", f"name: {name}", "description: Placeholder skill."]
    lines.extend(frontmatter)
    lines.extend(["---", "", body, ""])
    path = root / "plugins" / plugin / "skills" / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "SKILL.md").write_text("\n".join(lines))


class RouterTests(unittest.TestCase):
    def validate(self, skills):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, (body, frontmatter) in skills.items():
                write_skill(root, name, body, frontmatter)
            return relationships.validate_routers(root, relationships.load_skills(root))

    def test_explicit_router_to_model_invoked_skill_passes(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", ()),
                "alias": (
                    'Call the Skill tool with "alpha".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertEqual(failures, [])

    def test_router_must_be_explicit_only(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", ()),
                "alias": ('Call the Skill tool with "alpha".', ()),
            }
        )
        self.assertTrue(any("must set disable-model-invocation" in failure for failure in failures))

    def test_router_must_stay_user_invocable(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", ()),
                "alias": (
                    'Call the Skill tool with "alpha".',
                    ("disable-model-invocation: true", "user-invocable: false"),
                ),
            }
        )
        self.assertTrue(any("must stay user-invocable" in failure for failure in failures))

    def test_router_target_must_exist(self):
        failures = self.validate(
            {
                "alias": (
                    'Call the Skill tool with "missing".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertTrue(any("targets unknown skill missing" in failure for failure in failures))

    def test_router_target_must_be_model_invoked(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", ("disable-model-invocation: true",)),
                "alias": (
                    'Call the Skill tool with "alpha".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertTrue(any("targets explicit-only skill alpha" in failure for failure in failures))

    def test_router_cannot_chain(self):
        failures = self.validate(
            {
                "gamma": ("Do the work.", ()),
                "beta": (
                    'Call the Skill tool with "gamma".',
                    ("disable-model-invocation: true",),
                ),
                "alpha": (
                    'Call the Skill tool with "beta".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertTrue(any("chains to router beta" in failure for failure in failures))

    def test_router_cannot_target_itself(self):
        failures = self.validate(
            {
                "alpha": (
                    'Call the Skill tool with "alpha".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertTrue(any("targets itself" in failure for failure in failures))

    def test_two_targets_are_both_checked(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", ()),
                "beta": ("Do other work.", ()),
                "alias": (
                    'Call the Skill tool twice, for "alpha" and "missing".',
                    ("disable-model-invocation: true",),
                ),
            }
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("targets unknown skill missing", failures[0])

    def test_quoted_text_outside_the_router_call_is_ignored(self):
        failures = self.validate(
            {
                "alpha": ('Say "missing" in the output, but do the work.', ()),
            }
        )
        self.assertEqual(failures, [])


class CompositionTests(unittest.TestCase):
    def validate(self, skills):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, (body, plugin) in skills.items():
                write_skill(root, name, body, plugin=plugin)
            return relationships.validate_compositions(root, relationships.load_skills(root))

    def test_named_capability_resolves(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", "example"),
                "beta": ("## Composition\n\nUse `alpha` when relevant.", "example"),
            }
        )
        self.assertEqual(failures, [])

    def test_unknown_capability_is_reported(self):
        failures = self.validate(
            {"beta": ("## Composition\n\nUse `missing-capability` when relevant.", "example")}
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("names unknown capability missing-capability", failures[0])

    def test_lone_word_is_not_a_capability(self):
        failures = self.validate(
            {"beta": ("## Composition\n\nRun `pytest` before finishing.", "example")}
        )
        self.assertEqual(failures, [])

    def test_cross_package_link_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_skill(root, "alpha", "Do the work.", plugin="other")
            path = root / "plugins/example/skills/beta"
            path.mkdir(parents=True)
            (path / "SKILL.md").write_text(
                "---\nname: beta\ndescription: Placeholder.\n---\n\n"
                "## Composition\n\nUse [alpha](../../other/skills/alpha/SKILL.md).\n"
            )
            failures = relationships.validate_compositions(root, relationships.load_skills(root))
            self.assertTrue(any("composition links cross-package capability alpha" in f for f in failures))

    def test_cross_package_name_is_reported(self):
        failures = self.validate(
            {
                "alpha": ("Do the work.", "other"),
                "beta": ("## Composition\n\nUse `alpha` when relevant.", "example"),
            }
        )
        self.assertEqual(len(failures), 1)
        self.assertIn("cross-package capability alpha", failures[0])

    def test_token_outside_composition_is_ignored(self):
        failures = self.validate(
            {"beta": ("## Other\n\nUse `missing` when relevant.", "example")}
        )
        self.assertEqual(failures, [])

    def test_non_kebab_token_is_ignored(self):
        failures = self.validate(
            {"beta": ("## Composition\n\nRead the `ECR` and `PR` first.", "example")}
        )
        self.assertEqual(failures, [])

    def test_self_reference_is_allowed(self):
        failures = self.validate(
            {"beta": ("## Composition\n\nThis extends `beta` for larger work.", "example")}
        )
        self.assertEqual(failures, [])


class HandoffCoverageTests(unittest.TestCase):
    def matrix(self, root, rows):
        path = root / "plugins/sdlc/skills/artifact-system/references/handoff.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = ["## Phase handoff matrix", "", "| From | To |", "| --- | --- |"]
        body.extend(f"| {row} | Testing |" for row in rows)
        path.write_text("\n".join(body) + "\n")

    def test_repository_covers_every_phase(self):
        self.assertEqual(relationships.validate_handoff_coverage(ROOT), [])

    def test_missing_phase_row_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.matrix(root, ["Planning"])
            failures = relationships.validate_handoff_coverage(root)
            self.assertTrue(any("phase requirements has no row" in failure for failure in failures))

    def test_unmapped_row_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.matrix(
                root,
                [
                    "Planning",
                    "Requirements",
                    "Design",
                    "Implementation preparation",
                    "Implementation",
                    "Testing",
                    "Deployment",
                    "Maintenance",
                    "Incident",
                    "Postmortem",
                    "Any reopen",
                    "Nonsense boundary",
                ],
            )
            failures = relationships.validate_handoff_coverage(root)
            self.assertEqual(len(failures), 1)
            self.assertIn("is not a work state or wildcard", failures[0])

    def test_unknown_handoff_target_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.matrix(root, ["Planning"])
            path = root / "plugins/sdlc/skills/artifact-system/references/handoff.md"
            path.write_text(
                "## Phase handoff matrix\n\n| From | To |\n| --- | --- |\n"
                "| Planning | Nonsense target |\n"
            )
            failures = relationships.validate_handoff_coverage(root)
            self.assertTrue(any("Nonsense target" in failure and "not a work state" in failure for failure in failures))

    def test_missing_matrix_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "plugins/sdlc/skills/artifact-system/references/handoff.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Handoff\n\nNo matrix here.\n")
            self.assertEqual(
                relationships.validate_handoff_coverage(root),
                ["handoff matrix not found or empty"],
            )


if __name__ == "__main__":
    unittest.main()
