#!/usr/bin/env python3
"""Build self-contained portable plugins from pinned upstream Git trees."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.DEVNULL)


def acquire(source, cache):
    key = hashlib.sha256(source['repository'].encode()).hexdigest()[:20]
    repo = cache / key
    if not repo.exists():
        subprocess.run(['git', 'init', '--bare', '-q', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', source['repository']], check=True)
    try:
        git(repo, 'cat-file', '-e', source['commit'] + '^{commit}')
    except subprocess.CalledProcessError:
        subprocess.run(['git', '-C', str(repo), 'fetch', '--depth=1', 'origin', source['commit']], check=True)
    actual = git(repo, 'rev-parse', source['commit'] + ':' + source['path']).decode().strip()
    if actual != source['tree']:
        raise ValueError('Upstream tree mismatch: ' + source['path'])
    archive = git(repo, 'archive', source['commit'], source['path'])
    return repo, archive


def extract_skill(archive, source_path, destination):
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar.getmembers():
            path = Path(member.name)
            if path == Path(source_path) or (member.isdir() and path in Path(source_path).parents):
                continue
            if not path.is_relative_to(source_path):
                raise ValueError('Unexpected archive path')
            relative = path.relative_to(source_path)
            target = destination / relative
            if '..' in relative.parts or not target.resolve().is_relative_to(destination.resolve()):
                raise ValueError('Escaping archive path')
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(tar.extractfile(member).read())
                target.chmod(0o755 if member.mode & 0o111 else 0o644)
            else:
                raise ValueError('Upstream links/devices are not portable: ' + member.name)


def build(root, selected, destination, cache):
    if destination.exists():
        raise ValueError('Destination must not exist; existing installations are never overwritten')
    lock = json.loads((root / 'upstream.lock.json').read_text())
    cache.mkdir(parents=True, exist_ok=True)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as temp:
        output = Path(temp) / 'output'
        output.mkdir()
        for name in selected:
            package = root / 'plugins' / name
            if not package.is_dir() or name != package.name or '/' in name or '..' in name:
                raise ValueError('Unknown plugin: ' + name)
            shutil.copytree(package, output / name)
        acquired = []
        for source in lock['sources']:
            if source['plugin'] not in selected:
                continue
            repo, archive = acquire(source, cache)
            with tempfile.TemporaryDirectory() as tmp:
                unpacked = Path(tmp) / 'skill'
                extract_skill(archive, source['path'], unpacked)
                # Frontmatter is YAML; the runtime builder uses the validator's pinned dependency.
                import yaml
                metadata = yaml.safe_load((unpacked / 'SKILL.md').read_text().split('---', 2)[1])
                name = metadata['name']
                import re
                if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                    raise ValueError('Invalid upstream skill name')
                target = output / source['plugin'] / 'skills' / name
                if target.exists():
                    raise ValueError('Skill collision: ' + name)
                target.parent.mkdir(exist_ok=True)
                shutil.copytree(unpacked, target)
                notice = dict(source, installed_skill=name)
                (target / 'UPSTREAM.json').write_text(json.dumps(notice, indent=2) + '\n')
                if source['license_path']:
                    license_bytes = git(repo, 'show', source['commit'] + ':' + source['license_path'])
                    (target / 'UPSTREAM-LICENSE.txt').write_bytes(license_bytes)
                elif not metadata.get('license'):
                    raise ValueError('Missing upstream license declaration')
                acquired.append(notice)
        for name in selected:
            package = output / name
            notices = [s for s in acquired if s['plugin'] == name]
            (package / 'UPSTREAM-NOTICES.json').write_text(json.dumps(notices, indent=2) + '\n')
            # Root license covers local files only, never third-party directories.
            if notices:
                manifest = json.loads((package / 'plugin.json').read_text())
                manifest['license'] = 'LicenseRef-Mixed'
                (package / 'plugin.json').write_text(json.dumps(manifest, indent=2) + '\n')
        import jsonschema
        import yaml
        for package in output.iterdir():
            jsonschema.validate(json.loads((package / "plugin.json").read_text()),
                                json.loads((root / "schemas/plugin.schema.json").read_text()))
            for skill in package.glob("skills/*/SKILL.md"):
                metadata = yaml.safe_load(skill.read_text().split("---", 2)[1])
                if metadata.get("name") != skill.parent.name or not isinstance(metadata.get("description"), str) or len(metadata["description"]) > 1024:
                    raise ValueError("Invalid built skill metadata: " + str(skill))
        shutil.copytree(output, destination)
    return acquired


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin', action='append', help='Plugin to bundle, repeatable; default: workflow, backend, frontend')
    parser.add_argument('--destination', type=Path, required=True)
    parser.add_argument('--cache', type=Path, default=Path.home() / '.cache' / 'agent-skills-public')
    args = parser.parse_args()
    selected = list(dict.fromkeys(args.plugin or ['development-workflow', 'python-backend', 'web-frontend']))
    acquired = build(ROOT, selected, args.destination.resolve(), args.cache.resolve())
    print(f'Built {len(selected)} plugins with {len(acquired)} upstream skills at {args.destination}')


if __name__ == '__main__':
    main()
