#!/usr/bin/env python3
"""Validate the artifact/contract/guide registry and its files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / 'plugins/sdlc/skills/artifact-system/references'
REGISTRY = ARTIFACTS / 'artifact-registry.json'
CONTRACTS = ARTIFACTS / 'contracts'
GUIDES = ROOT / 'plugins/sdlc/skills'


def load():
    return json.loads(REGISTRY.read_text())['artifacts']


def validate():
    errors = []
    entries = load()
    types = set()
    contract_paths = set()
    guide_names = set()
    for entry in entries:
        name = entry.get('type')
        if not name:
            errors.append('registry entry missing type')
            continue
        if name in types:
            errors.append(f'{name}: duplicate artifact type')
        types.add(name)
        contract = entry.get('contract')
        if contract:
            path = ARTIFACTS / contract
            if not path.is_file():
                errors.append(f'{name}: missing contract {contract}')
            contract_paths.add(Path(contract).name)
        guide = entry.get('guide')
        if guide:
            path = GUIDES / guide / 'SKILL.md'
            if not path.is_file():
                errors.append(f'{name}: missing guide {guide}')
            guide_names.add(guide)
    known_contracts = {p.name for p in CONTRACTS.glob('*.md') if p.name not in {'README.md', 'TEMPLATE.md'}}
    for missing in sorted(known_contracts - contract_paths):
        errors.append(f'contract has no registry entry: {missing}')
    known_guides = {p.parent.name for p in GUIDES.glob('guide-*/SKILL.md')}
    for missing in sorted(known_guides - guide_names):
        errors.append(f'guide has no registry entry: {missing}')
    for extra in sorted(guide_names - known_guides):
        errors.append(f'registry points to missing guide: {extra}')
    return errors


def main():
    errors = validate()
    if errors:
        raise SystemExit('\n'.join(errors))
    entries = load()
    print(f'Artifact registry valid: {len(entries)} artifacts, '
          f'{sum(1 for e in entries if e.get("contract"))} contracts, '
          f'{sum(1 for e in entries if e.get("guide"))} guides')


if __name__ == '__main__':
    main()
