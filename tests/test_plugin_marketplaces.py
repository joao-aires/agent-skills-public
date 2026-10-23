import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('marketplace', Path(__file__).resolve().parents[1] / 'scripts/build_plugin_marketplaces.py')
marketplace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(marketplace)


class PluginMarketplaceTests(unittest.TestCase):
    def test_lists_each_built_bundle_with_its_manifest_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = Path(tmp)
            for name, version in (('strategy', '1.2.0'), ('development', '3.0.0')):
                (built / name).mkdir()
                (built / name / 'plugin.json').write_text(json.dumps(
                    {'name': name, 'version': version, 'description': f'{name} bundle'}))
            (built / 'notes').mkdir()

            count = marketplace.write_marketplaces(built, 'agent-skills-public', 'Owner')

            data = json.loads((built / '.claude-plugin' / 'marketplace.json').read_text())
            self.assertEqual(count, 2)
            self.assertEqual(data['name'], 'agent-skills-public')
            self.assertEqual(data['owner'], {'name': 'Owner'})
            self.assertEqual(data['plugins'], [
                {'name': 'development', 'source': './development', 'description': 'development bundle', 'version': '3.0.0'},
                {'name': 'strategy', 'source': './strategy', 'description': 'strategy bundle', 'version': '1.2.0'},
            ])
            codex = json.loads((built / '.agents/plugins/marketplace.json').read_text())
            self.assertEqual(codex['name'], data['name'])
            self.assertEqual([p['name'] for p in codex['plugins']], ['development', 'strategy'])
            for entry in codex['plugins']:
                self.assertEqual(entry['source'], {'source': 'local', 'path': './' + entry['name']})
                self.assertTrue((built / entry['source']['path'] / 'plugin.json').is_file())
                self.assertEqual(entry['policy'], {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'})
                self.assertEqual(entry['category'], 'Productivity')

    def test_refuses_to_overwrite_an_existing_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            built = Path(tmp)
            for relative in ('.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json'):
                with self.subTest(relative=relative):
                    target = built / relative
                    target.parent.mkdir(parents=True)
                    target.write_text('existing catalog')
                    with self.assertRaises(FileExistsError):
                        marketplace.write_marketplaces(built, 'agent-skills-public', 'Owner')
                    self.assertEqual(target.read_text(), 'existing catalog')
                    self.assertEqual(list(built.rglob('marketplace.json')), [target])
                    target.unlink()

    def test_rejects_empty_output_without_writing_catalogs(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, 'No built plugin'):
                marketplace.write_marketplaces(Path(tmp), 'test', 'Owner')
            self.assertEqual(list(Path(tmp).rglob('marketplace.json')), [])

    def test_rejects_a_source_that_does_not_match_the_plugin_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp) / 'wrong-folder'
            plugin.mkdir()
            (plugin / 'plugin.json').write_text(json.dumps({'name': 'development', 'version': '1.0.0'}))
            with self.assertRaisesRegex(ValueError, 'does not match'):
                marketplace.write_marketplaces(Path(tmp), 'test', 'Owner')
            self.assertEqual(list(Path(tmp).rglob('marketplace.json')), [])


if __name__ == '__main__':
    unittest.main()
