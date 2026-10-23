#!/usr/bin/env python3
"""Add Claude Code and Codex marketplace manifests to a complete build output."""
import argparse
import json
from pathlib import Path


def write_marketplaces(destination, name, owner):
    targets = [destination / folder / 'marketplace.json'
               for folder in ('.claude-plugin', '.agents/plugins')]
    # Refuse before writing either catalog, including partial prior generations.
    for target in targets:
        if target.exists():
            raise FileExistsError(target)
    plugins = []
    for manifest_path in sorted(destination.glob('*/plugin.json')):
        manifest = json.loads(manifest_path.read_text())
        if manifest['name'] != manifest_path.parent.name:
            raise ValueError(f'Plugin name does not match its directory: {manifest_path}')
        plugins.append({
            'name': manifest['name'],
            'source': './' + manifest_path.parent.name,
            'description': manifest.get('description', ''),
            'version': manifest['version'],
        })
    if not plugins:
        raise ValueError('No built plugin manifests found')
    claude = {
        'name': name,
        'owner': {'name': owner},
        'description': 'Portable SDLC, strategy and operations skill bundles built from agent-skills-public.',
        'plugins': plugins,
    }
    codex = {
        'name': name,
        'interface': {'displayName': 'Agent Skills Public'},
        'plugins': [{
            'name': plugin['name'],
            'source': {'source': 'local', 'path': plugin['source']},
            'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'},
            'category': 'Productivity',
        } for plugin in plugins],
    }
    for target, catalog in zip(targets, (claude, codex)):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + '\n')
    return len(plugins)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--built', type=Path, required=True, help='Output of build_plugins.py --all')
    parser.add_argument('--name', default='agent-skills-public')
    parser.add_argument('--owner', default='João Aires')
    args = parser.parse_args()
    built = args.built.resolve()
    count = write_marketplaces(built, args.name, args.owner)
    print(f'Added Claude Code and Codex marketplace manifests for {count} plugins at {built}')


if __name__ == '__main__':
    main()
