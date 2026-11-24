"""Read consumer packaging metadata and verify committed Agent Depot skill snapshots.

Agent Depot owns acquisition, formats, plans and recovery. This consumer-side reader
checks the declared snapshots before packaging; it never fetches or repairs files.
"""
import hashlib
import json
from pathlib import Path
import re

try:
    from skill_schema import DOMAINS, INVOCATIONS, KINDS, ORIGINS, PACKS, PHASES, ROLES, SCOPES
except ModuleNotFoundError:
    from scripts.skill_schema import DOMAINS, INVOCATIONS, KINDS, ORIGINS, PACKS, PHASES, ROLES, SCOPES


def load_sources(root, selected=None, verify=True):
    root = Path(root)
    manifest = json.loads((root / 'agent-depot.json').read_text())
    lock = json.loads((root / 'agent-depot.lock.json').read_text())
    if manifest.get('schemaVersion') != 2 or lock.get('schemaVersion') != 2:
        raise ValueError('Expected Agent Depot schema version 2')
    if manifest['sources'] != lock['sources'] or set(manifest['artifacts']) != set(lock['artifacts']):
        raise ValueError('Depot declarations differ from lock; use Agent Depot plan/update')
    if 'packaging' in manifest.get('metadata', {}):
        raise ValueError('Packaging records belong in each artifact metadata.packaging')
    result = []
    destinations = set()
    for artifact_id, artifact in manifest['artifacts'].items():
        accepted = lock['artifacts'][artifact_id]
        declaration = {k: v for k, v in accepted.items() if k not in {'files', 'digest', 'inspection'}}
        if declaration != artifact:
            raise ValueError('Depot artifact differs from lock: ' + artifact_id)
        annotations = artifact.get('metadata', {})
        metadata = annotations.get('packaging') if isinstance(annotations, dict) else None
        if not isinstance(metadata, dict):
            raise ValueError('Each managed skill needs an artifact metadata.packaging record: ' + artifact_id)
        plugin = metadata.get('plugin')
        if not isinstance(plugin, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', plugin):
            raise ValueError('Invalid owning plugin')
        if not isinstance(metadata.get('license'), str) or not metadata['license'].strip():
            raise ValueError('Packaging license attribution is required: ' + artifact_id)
        license_path = metadata.get('license_path')
        if license_path is not None and (not isinstance(license_path, str) or not license_path):
            raise ValueError('Invalid packaging license path: ' + artifact_id)
        adaptations = metadata.get('adaptations', [])
        if not isinstance(adaptations, list) or any(not isinstance(a, str) for a in adaptations):
            raise ValueError('Packaging adaptations must be a list of names: ' + artifact_id)
        labels = metadata.get('labels', {})
        if not isinstance(labels, dict) or any(not isinstance(v, str) for v in labels.values()):
            raise ValueError('Packaging labels must map strings to strings: ' + artifact_id)
        vocabularies = {
            'scope': SCOPES, 'invocation': INVOCATIONS, 'kind': KINDS,
            'origin': ORIGINS, 'pack': PACKS, 'phase': PHASES,
            'domain': DOMAINS, 'role': ROLES,
        }
        for field, allowed in vocabularies.items():
            value = labels.get(field)
            if value is not None and value not in allowed:
                raise ValueError(f'Invalid packaging {field} label {value!r}: {artifact_id}')
        destination = Path(artifact['destination'])
        if (artifact['kind'] != 'skill' or len(destination.parts) != 4 or
                destination.parts[:3] != ('plugins', plugin, 'skills') or
                not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', destination.name) or '\\' in str(destination)):
            raise ValueError('Managed skills must live in their owning plugin: ' + artifact_id)
        if destination in destinations:
            raise ValueError('Duplicate managed destination')
        destinations.add(destination)
        if selected is not None and plugin not in selected:
            continue
        target = root / destination
        if verify:
            verify_snapshot(root, target, accepted['files'])
        result.append(dict(metadata, artifact=artifact_id, destination=artifact['destination'],
                           repository=manifest['sources'][artifact['source']]['repository'],
                           commit=artifact['commit'], path=artifact['path']))
    return result


def verify_snapshot(root, target, files):
    # Follow no managed symlink, including an ancestor of the snapshot root.
    for path in [target, *target.parents]:
        if path == root.parent:
            break
        if path.is_symlink():
            raise ValueError('Managed snapshot contains a symlink: ' + str(path))
    if not target.is_dir():
        raise ValueError('Missing committed snapshot: ' + str(target))
    actual = {}
    for path in target.rglob('*'):
        if path.is_symlink():
            raise ValueError('Managed snapshot contains a symlink: ' + str(path))
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError('Unsupported snapshot entry: ' + str(path))
        relative = path.relative_to(target).as_posix()
        mode = '100755' if path.stat().st_mode & 0o111 else '100644'
        actual[relative] = dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(), mode=mode)
    import os
    if os.name == 'nt':
        actual = {p: v['sha256'] for p, v in actual.items()}
        files = {p: v['sha256'] for p, v in files.items()}
    if actual != files:
        raise ValueError('Committed snapshot differs from Depot lock: ' + str(target))
