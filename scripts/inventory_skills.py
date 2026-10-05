#!/usr/bin/env python3
"""Inspect installed skill metadata without copying skill bodies or changing installations."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml


def inventory(roots):
    result = []
    for root in roots:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob('SKILL.md')):
            if 'uninstalled' in path.relative_to(root).parts:
                continue
            text = path.read_text()
            parts = text.split('---', 2)
            if len(parts) != 3 or parts[0].strip():
                continue
            metadata = yaml.safe_load(parts[1])
            if not isinstance(metadata, dict) or not metadata.get('name'):
                continue
            result.append({'name': metadata['name'], 'description': metadata.get('description', ''),
                           'path': str(path.resolve()), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, action='append', required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps({'skills': inventory(args.root)}, indent=2) + '\n'
    if args.output:
        if args.output.exists():
            parser.error('Output exists; choose a new path')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    else:
        print(data, end='')
