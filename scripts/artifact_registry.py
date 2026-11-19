#!/usr/bin/env python3
"""Validate the artifact/contract/guide registry and its files."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / 'plugins/sdlc/skills/artifact-system/references'
REGISTRY = ARTIFACTS / 'artifact-registry.json'
CONTRACTS = ARTIFACTS / 'contracts'
GUIDES = ROOT / 'plugins/sdlc/skills'
OUTPUT = ARTIFACTS / 'guide-registry.md'

NAMES = {
    'product-brief': 'Product brief / PRD',
    'roadmap': 'Roadmap',
    'ecr': 'ECR',
    'research-report': 'Research report',
    'rfc': 'RFC',
    'design-proposal': 'Design proposal',
    'design-specification': 'Design specification',
    'issue': 'Issue',
    'pull-request': 'Pull request',
    'architecture-set': 'Architecture set',
    'c4-view': 'C4 view',
    'sequence-view': 'Sequence view',
    'state-machine': 'State machine',
    'compatibility-matrix': 'Compatibility matrix',
    'decision-record': 'Decision record',
    'assurance-assessment': 'Assurance assessment',
    'runbook': 'Runbook',
    'api-reference': 'API reference',
    'work-product': 'Work product',
    'release-note': 'Release note',
    'deployment-record': 'Deployment record',
    'incident-record': 'Incident record',
    'postmortem': 'Postmortem',
    'repository-readme': 'Repository README',
    'guide': 'Guide',
    'glossary': 'Glossary',
}


def load():
    return json.loads(REGISTRY.read_text())['artifacts']


def guide_kind(path):
    parts = path.read_text().split('---', 2)
    if len(parts) < 3:
        return None
    for line in parts[1].splitlines():
        key, _, value = line.partition(':')
        if key.strip() == 'kind':
            return value.strip().strip('"\'')
    return None


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
            elif guide_kind(path) != 'guide':
                errors.append(f'{name}: {guide} is not declared kind: guide')
            guide_names.add(guide)
    known_contracts = {p.name for p in CONTRACTS.glob('*.md') if p.name not in {'README.md', 'TEMPLATE.md'}}
    for missing in sorted(known_contracts - contract_paths):
        errors.append(f'contract has no registry entry: {missing}')
    known_guides = {p.parent.name for p in GUIDES.glob('*/SKILL.md') if guide_kind(p) == 'guide'}
    for missing in sorted(known_guides - guide_names):
        errors.append(f'guide has no registry entry: {missing}')
    for extra in sorted(guide_names - known_guides):
        errors.append(f'registry points to missing guide: {extra}')
    return errors


def display(entry):
    return NAMES.get(entry['type'], entry['type'].replace('-', ' ').title())


def generate():
    rows = []
    for entry in load():
        contract = entry.get('contract')
        contract_cell = f'[{Path(contract).name}]({contract})' if contract else entry.get('guidance', 'No Markdown contract')
        guide = entry.get('guide')
        guide_cell = f'[{guide}](../../{guide}/SKILL.md)' if guide else entry.get('guidance', 'No dedicated guide')
        rows.append(f'| {display(entry)} | {contract_cell} | {guide_cell} |')
    return (
        '# Artifact guide registry\n\n'
        'Generated from `artifact-registry.json` by `python scripts/artifact_registry.py --write`.\n'
        'Do not edit by hand.\n\n'
        '| Artifact | Contract | Guide |\n'
        '| --- | --- | --- |\n'
        + '\n'.join(rows) + '\n'
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='write the generated guide registry')
    parser.add_argument('--check', action='store_true', help='fail if the generated registry is stale')
    args = parser.parse_args()
    errors = validate()
    if errors:
        raise SystemExit('\n'.join(errors))
    entries = load()
    if args.write:
        OUTPUT.write_text(generate())
        print(f'Wrote {OUTPUT}')
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != generate():
            raise SystemExit(f'{OUTPUT} is stale; run python scripts/artifact_registry.py --write')
        print('Guide registry is current')
    print(f'Artifact registry valid: {len(entries)} artifacts, '
          f'{sum(1 for e in entries if e.get("contract"))} contracts, '
          f'{sum(1 for e in entries if e.get("guide"))} guides')


if __name__ == '__main__':
    main()
