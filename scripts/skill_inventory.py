#!/usr/bin/env python3
"""Print a maintainer inventory of skills and their classification metadata."""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def acquired_labels():
    data = json.loads((ROOT / 'agent-depot.json').read_text())
    artifacts = data.get('artifacts', data)
    labels = {}
    for value in artifacts.values():
        if isinstance(value, dict) and value.get('destination'):
            packaging = value.get('metadata', {}).get('packaging', {})
            labels[value['destination']] = packaging.get('labels', {})
    return labels


def frontmatter(path):
    parts = path.read_text().split('---', 2)
    if len(parts) != 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def main():
    acquired = acquired_labels()
    rows = []
    for path in sorted((ROOT / 'plugins').glob('*/skills/*/SKILL.md')):
        relative = path.parent.relative_to(ROOT).as_posix()
        metadata = frontmatter(path)
        local_labels = metadata.get('metadata', {}) or {}
        labels = acquired.get(relative, local_labels)
        origin = 'upstream' if relative in acquired else local_labels.get('origin', 'local')
        rows.append((
            metadata.get('name', path.parent.name),
            labels.get('pack', ''),
            labels.get('domain', ''),
            labels.get('kind', ''),
            labels.get('phase', ''),
            origin,
            labels.get('scope', ''),
            labels.get('invocation', ''),
            labels.get('role', ''),
            path.parents[2].name,
        ))
    print('| Skill | Pack | Domain | Kind | Phase | Origin | Scope | Invocation | Role | Plugin |')
    print('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for row in rows:
        print('| ' + ' | '.join(row) + ' |')


if __name__ == '__main__':
    main()
