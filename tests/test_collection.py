from depot_fixture import write_depot
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("collection", Path(__file__).resolve().parents[1] / "scripts/check_collection.py")
collection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collection)


class CollectionTests(unittest.TestCase):
    def fixture(self, root):
        (root / "documentation").mkdir()
        (root / "README.md").write_text("[Start](documentation/usage.md#start)\n")
        (root / "AGENTS.md").write_text("Instructions\n")
        (root / "documentation/usage.md").write_text("# Start\n")
        (root / "documentation/migration.md").write_text("| `old-name` | `new-name` |\n")

    def test_broken_heading_and_stale_name_fail_but_fenced_examples_do_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_depot(root)
            self.fixture(root)
            self.assertFalse(collection.check_links(root)[0])
            (root / "README.md").write_text("[Start](documentation/usage.md#missing)\nUse `old-name`.\n```md\n[Example](missing.md)\n```\n")
            errors, _ = collection.check_links(root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("missing heading" in error for error in errors))
            self.assertTrue(any("obsolete skill" in error for error in errors))
            nested = root / "documentation/maintainers"
            nested.mkdir()
            (nested / "sources.md").write_text("[Missing](absent.md)\n")
            errors, _ = collection.check_links(root)
            self.assertTrue(any("maintainers/sources.md: missing absent.md" in error for error in errors))

    def test_retired_skill_names_in_prose_and_link_labels_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_depot(root)
            self.fixture(root)
            current = root / 'plugins/example/skills/new-name'
            current.mkdir(parents=True)
            (current / 'SKILL.md').write_text('# New method\n')
            (root / 'documentation/migration.md').write_text(
                '| `old-name` | `new-name` |\n'
            )
            (root / 'documentation/usage.md').write_text(
                '# Start\nOld-name is available.\n'
                '[Old name](../plugins/example/skills/new-name/SKILL.md)\n'
            )
            errors, _ = collection.check_links(root)
            self.assertTrue(any('obsolete skill name old-name' in x for x in errors))
            self.assertTrue(any('obsolete skill link label Old name' in x for x in errors))

            # Historical migration mappings remain intentionally exempt.
            (root / 'documentation/usage.md').write_text(
                '# Start\nSee [reference](https://example.com/something/old-name/guide).\n'
            )
            self.assertFalse(collection.check_links(root)[0])

    def test_missing_resource_and_extra_skill_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plugins/example"
            skill = source / "skills/local"
            skill.mkdir(parents=True)
            (source / "plugin.json").write_text('{}')
            (skill / "SKILL.md").write_text('Local')
            (skill / "resource.txt").write_text('Keep this resource')
            write_depot(root)
            built = root / "built"
            shutil.copytree(root / "plugins", built)
            (built / "example/UPSTREAM-NOTICES.json").write_text('[]')
            self.assertFalse(collection.check_built(root, built)[0])
            (built / "example/skills/local/resource.txt").unlink()
            (built / "example/skills/old-name").mkdir()
            errors, _ = collection.check_built(root, built)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("resource.txt" in error for error in errors))
            self.assertTrue(any("inventory" in error for error in errors))

    def test_selected_build_checks_only_requested_packages_but_rejects_extras(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('workflow', 'technical'):
                skill = root / 'plugins' / name / 'skills' / name
                skill.mkdir(parents=True)
                (skill.parent.parent / 'plugin.json').write_text('{}')
                (skill / 'SKILL.md').write_text('# Self-contained method\n')
            write_depot(root)
            built = root / 'built'
            shutil.copytree(root / 'plugins/workflow', built / 'workflow')
            (built / 'workflow/UPSTREAM-NOTICES.json').write_text('[]')
            self.assertFalse(collection.check_built(root, built, ['workflow'])[0])
            self.assertTrue(collection.check_built(root, built)[0])
            shutil.copytree(root / 'plugins/technical', built / 'technical')
            self.assertTrue(any('extra=' in error for error in collection.check_built(root, built, ['workflow'])[0]))

    def test_package_resources_reject_cross_package_and_missing_transitive_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package = root / 'workflow'
            skill = package / 'skills/method'
            (skill / 'references').mkdir(parents=True)
            (skill / 'SKILL.md').write_text('[Details](references/guide.md)\n')
            (skill / 'references/guide.md').write_text('[Required](absent.md)\n')
            errors, _ = collection.check_package_links(package, {'method'}, [])
            self.assertTrue(any('missing resource' in error for error in errors))
            (skill / 'references/guide.md').write_text('[Shared](../../../../outside.md)\n')
            (root / 'outside.md').write_text('Exists, but is not packaged.\n')
            errors, _ = collection.check_package_links(package, {'method'}, [])
            self.assertTrue(any('escapes package' in error for error in errors))
            (skill / 'references/guide.md').write_text('# Detail\n[Local](#detail)\n')
            self.assertFalse(collection.check_package_links(package, {'method'}, [])[0])

    def test_acquired_framing_requires_its_local_resources(self):
        cases = {'ai-framing': ['ai-conventions'],
                 'frontend-framing': ['frontend-conventions']}
        for adaptation, resources in cases.items():
            with self.subTest(adaptation=adaptation), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp)
                notices = [{'installed_skill': 'specialist', 'adaptations': [adaptation]}]
                self.assertTrue(collection.check_package_links(package, set(), notices)[0])
                for index, resource in enumerate(resources):
                    conventions = package / 'skills' / resource
                    conventions.mkdir(parents=True)
                    (conventions / 'SKILL.md').write_text('# Local implementation\n')
                    errors, _ = collection.check_package_links(package, set(), notices)
                    self.assertEqual(bool(errors), index < len(resources) - 1)
