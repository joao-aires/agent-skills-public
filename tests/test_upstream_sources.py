from depot_fixture import write_depot
from pathlib import Path
import json
import copy
import tempfile
import unittest
from scripts.upstream_sources import load_sources
from scripts.build_plugins import build


class SnapshotTests(unittest.TestCase):
    def fixture(self, root):
        upstream = root / 'upstream'
        (upstream / 'references').mkdir(parents=True)
        (upstream / 'SKILL.md').write_text('---\nname: example\ndescription: Committed fixture\nlicense: MIT\n---\nRead references/guide.md\n')
        (upstream / 'references/guide.md').write_text('Preserve these bytes.\n')
        package = root / 'plugins/example'
        package.mkdir(parents=True)
        (package / 'plugin.json').write_text('{"name":"example"}')
        (root / 'schemas').mkdir()
        (root / 'schemas/plugin.schema.json').write_text('{}')
        record = dict(plugin='example', repository=str(upstream), commit='a'*40, path='.', license='MIT', license_path=None)
        write_depot(root, [record])
        return package / 'skills/example'

    def test_build_uses_committed_root_resources_without_an_upstream(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = self.fixture(root)
            import shutil
            shutil.rmtree(root / 'upstream')
            build(root, ['example'], root / 'output')
            self.assertEqual((root / 'output/example/skills/example/references/guide.md').read_bytes(), (target / 'references/guide.md').read_bytes())
            self.assertFalse((target / 'UPSTREAM.json').exists())

    def test_build_refuses_modified_missing_or_extra_managed_content(self):
        for mutation in ('modified', 'missing', 'extra'):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                target = self.fixture(root)
                if mutation == 'modified':
                    (target / 'references/guide.md').write_text('Changed')
                elif mutation == 'missing':
                    (target / 'references/guide.md').unlink()
                else:
                    (target / 'personal.md').write_text('Keep')
                with self.assertRaisesRegex(ValueError, 'differs from Depot lock'):
                    build(root, ['example'], root / 'output')
                self.assertFalse((root / 'output').exists())

    def test_commit_changes_need_a_matching_lock_and_metadata_requires_an_owner(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            path = root / 'agent-depot.json'
            value = json.loads(path.read_text())
            artifact = next(iter(value['artifacts']))
            value['artifacts'][artifact]['commit'] = 'b'*40
            path.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, 'differs from lock'):
                load_sources(root)
            value['artifacts'][artifact]['commit'] = 'a'*40
            del value['artifacts'][artifact]['metadata']['packaging']
            lock_path = root / 'agent-depot.lock.json'
            lock = json.loads(lock_path.read_text())
            del lock['artifacts'][artifact]['metadata']['packaging']
            lock_path.write_text(json.dumps(lock))
            path.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, 'metadata.packaging record'):
                load_sources(root)

    def test_built_acquired_skills_keep_client_invocation_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = self.fixture(root)
            (target / 'agents').mkdir()
            (target / 'agents/openai.yaml').write_text('policy:\n  allow_implicit_invocation: true\n')
            text = (target / 'SKILL.md').read_text().replace('license: MIT', 'license: MIT\ndisable-model-invocation: true')
            (target / 'SKILL.md').write_text(text)
            source = dict(plugin='example', repository=str(root / 'upstream'), commit='a'*40, path='.', license='MIT', license_path=None)
            write_depot(root, [source])
            with self.assertRaisesRegex(ValueError, 'Conflicting invocation metadata'):
                build(root, ['example'], root / 'output')
            self.assertFalse((root / 'output').exists())

    def test_consumer_validates_packaging_fields(self):
        mutations = [
            ('plugin', None, 'owning plugin'),
            ('license', '', 'license attribution'),
            ('license_path', [], 'license path'),
            ('adaptations', 'usage-labels', 'list of names'),
            ('labels', {'scope': 42}, 'strings to strings'),
        ]
        for field, invalid, error in mutations:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root)
                manifest_path = root / 'agent-depot.json'
                lock_path = root / 'agent-depot.lock.json'
                manifest = json.loads(manifest_path.read_text())
                lock = json.loads(lock_path.read_text())
                artifact = next(iter(manifest['artifacts']))
                annotations = manifest['artifacts'][artifact]['metadata']
                annotations['packaging'][field] = invalid
                lock['artifacts'][artifact]['metadata'] = copy.deepcopy(annotations)
                manifest_path.write_text(json.dumps(manifest))
                lock_path.write_text(json.dumps(lock))
                with self.assertRaisesRegex(ValueError, error):
                    load_sources(root)

    def test_unrelated_annotations_do_not_change_packaged_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            build(root, ['example'], root / 'before')
            manifest_path = root / 'agent-depot.json'
            lock_path = root / 'agent-depot.lock.json'
            manifest = json.loads(manifest_path.read_text())
            lock = json.loads(lock_path.read_text())
            artifact = next(iter(manifest['artifacts']))
            manifest['metadata'] = {'review': {'owner': 'maintainer'}}
            annotations = manifest['artifacts'][artifact]['metadata']
            annotations['review'] = {'checks': [True, None, {'notes': 'consumer annotation'}]}
            lock['artifacts'][artifact]['metadata'] = copy.deepcopy(annotations)
            manifest_path.write_text(json.dumps(manifest))
            lock_path.write_text(json.dumps(lock))
            build(root, ['example'], root / 'after')
            def files(folder):
                return {p.relative_to(folder).as_posix(): (p.read_bytes(), p.stat().st_mode & 0o777)
                        for p in folder.rglob('*') if p.is_file()}
            self.assertEqual(files(root / 'before'), files(root / 'after'))

    def test_packaging_metadata_controls_effective_labels_and_notices(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            source = dict(plugin='example', repository=str(root / 'upstream'), commit='a'*40,
                          path='.', license='MIT', license_path=None, adaptations=['usage-labels'],
                          labels={'scope': 'generic', 'invocation': 'both', 'role': 'support', 'kind': 'method', 'origin': 'upstream'})
            write_depot(root, [source])
            build(root, ['example'], root / 'output')
            target = root / 'output/example/skills/example'
            import yaml
            labels = yaml.safe_load((target / 'SKILL.md').read_text().split('---', 2)[1])['metadata']
            self.assertEqual(labels, source['labels'])
            provenance = json.loads((target / 'UPSTREAM.json').read_text())
            self.assertEqual(provenance['labels'], source['labels'])
            self.assertEqual(provenance['adaptations'], ['usage-labels'])

    def test_root_packaging_map_is_rejected_instead_of_used_as_a_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            path = root / 'agent-depot.json'
            manifest = json.loads(path.read_text())
            manifest['metadata'] = {'packaging': {}}
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, 'belong in each artifact'):
                load_sources(root)
