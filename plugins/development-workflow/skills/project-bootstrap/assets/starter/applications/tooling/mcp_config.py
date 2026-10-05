#!/usr/bin/env python3
"""Render opt-in client MCP configuration; never start servers or store credentials."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--project', type=Path, default=Path(__file__).resolve().parents[2])
args = parser.parse_args()
project = args.project.resolve()
api = project / 'applications/api'
web = project / 'applications/web'
if not (web / 'components.json').is_file() or not (api / 'pyproject.toml').is_file():
    parser.error('Expected the full-stack application layout')
print(json.dumps({'mcpServers': {
    'shadcn': {'command': 'npx', 'args': ['--yes', 'shadcn@4.21.2', 'mcp', '--cwd', str(web)]},
    'project-notes': {'command': 'uv', 'args': ['run', '--frozen', '--directory', str(api), '--group', 'mcp', 'python', '-m', 'notes.mcp'],
                      'env': {'PYTHONPATH': str(api / 'src'), 'NOTES_API_URL': 'http://127.0.0.1:8000'}},
}}, indent=2))
