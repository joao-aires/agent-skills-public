#!/usr/bin/env python3
"""Generate a filterable skills map from skill metadata.

Writes docs/skills-map.html and docs/skills-map.md, or prints the
maintainer inventory matrix with --inventory. Both views are derived from the same
skill metadata and agent-depot labels, so they cannot drift from each other.
"""
import argparse
import html
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs'

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

def build_rows():
    acquired = acquired_labels()
    rows = []
    for path in sorted((ROOT / 'plugins').glob('*/skills/*/SKILL.md')):
        relative = path.parent.relative_to(ROOT).as_posix()
        metadata = frontmatter(path)
        local_labels = metadata.get('metadata', {}) or {}
        labels = acquired.get(relative, local_labels)
        origin = 'upstream' if relative in acquired else local_labels.get('origin', 'local')
        rows.append({
            'name': metadata.get('name', path.parent.name),
            'description': ' '.join((metadata.get('description') or '').split()),
            'pack': labels.get('pack', ''),
            'domain': labels.get('domain', ''),
            'kind': labels.get('kind', ''),
            'phase': labels.get('phase', ''),
            'origin': origin,
            'scope': labels.get('scope', ''),
            'invocation': labels.get('invocation', ''),
            'role': labels.get('role', ''),
            'plugin': path.parents[2].name,
            'path': relative + '/SKILL.md',
        })
    return sorted(rows, key=lambda r: (r['pack'], r['domain'], r['kind'], r['name']))

def counts(rows, key):
    result = {}
    for row in rows:
        result[row[key]] = result.get(row[key], 0) + 1
    return dict(sorted(result.items(), key=lambda item: (-item[1], item[0])))

def table_rows(rows):
    cells = []
    for row in rows:
        link = '../' + html.escape(row['path'])
        cells.append(
            '<tr data-pack="{pack}" data-domain="{domain}" data-kind="{kind}" '
            'data-phase="{phase}" data-origin="{origin}" data-invocation="{invocation}" '
            'data-role="{role}" data-search="{search}">'
            '<td><a href="{link}">{name}</a><span class="desc">{description}</span></td>'
            '<td>{pack}</td><td>{domain}</td><td>{kind}</td><td>{phase}</td>'
            '<td>{origin}</td><td>{role}</td><td>{plugin}</td></tr>'.format(
                link=link,
                name=html.escape(row['name']),
                description=html.escape(row['description']),
                search=html.escape(' '.join([row['name'], row['description'], row['plugin'],
                                             row['pack'], row['domain'], row['kind'],
                                             row['phase']]).lower()),
                pack=html.escape(row['pack']),
                domain=html.escape(row['domain']),
                kind=html.escape(row['kind']),
                phase=html.escape(row['phase']),
                origin=html.escape(row['origin']),
                invocation=html.escape(row['invocation']),
                role=html.escape(row['role']),
                plugin=html.escape(row['plugin']),
            )
        )
    return '\n'.join(cells)

def summary(rows):
    return (
        f"{len(rows)} skills · "
        f"{len({r['plugin'] for r in rows})} plugins · "
        f"{len({r['pack'] for r in rows})} packs · "
        f"{len({r['domain'] for r in rows})} domains"
    )

def pack_summary(rows):
    return ' · '.join(f"{name} {count}" for name, count in counts(rows, 'pack').items())

def kind_summary(rows):
    return ' · '.join(f"{name} {count}" for name, count in counts(rows, 'kind').items())

def write_html(rows, destination):
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skills map</title>
<style>
  :root {{ color-scheme: light dark; --fg: #0f172a; --line: #d8dee9; --muted: #5c6778; --accent: #0f766e; --bg: #ffffff; --panel: #f6f8fb; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --fg: #e2e8f0; --line: #334155; --muted: #94a3b8; --accent: #5eead4; --bg: #0f172a; --panel: #111c33; }} }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; padding: 32px; font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--fg); background: var(--bg); }}
  h1 {{ margin: 0 0 4px; font-size: 28px; letter-spacing: -.02em; }}
  h2 {{ margin: 28px 0 10px; font-size: 16px; }}
  p {{ margin: 6px 0; color: var(--muted); }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .concept {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin: 22px 0 8px; }}
  .concept div {{ padding: 10px 14px; border: 1px solid var(--line); border-radius: 10px; background: var(--panel); }}
  .concept strong {{ display: block; color: var(--fg); font-size: 13px; }}
  .concept .arrow {{ border: 0; background: transparent; color: var(--muted); padding: 0 2px; }}
  .controls {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: end; margin: 20px 0 10px; }}
  label {{ display: grid; gap: 4px; font-size: 12px; color: var(--muted); }}
  input, select {{ min-width: 130px; padding: 7px 9px; border: 1px solid var(--line); border-radius: 8px; background: var(--bg); color: var(--fg); font: inherit; }}
  input[type=search] {{ min-width: 240px; }}
  .summary {{ margin: 8px 0 14px; font-size: 13px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th, td {{ padding: 9px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
  th {{ position: sticky; top: 0; background: var(--bg); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }}
  td .desc {{ display: block; max-width: 680px; margin-top: 2px; color: var(--muted); font-size: 12px; }}
  .empty {{ padding: 24px 8px; color: var(--muted); }}
  .pill {{ display: inline-block; padding: 1px 7px; border: 1px solid var(--line); border-radius: 999px; font-size: 11px; color: var(--muted); }}
</style>
</head>
<body>
<header>
  <h1>Skills map</h1>
  <p>Generated from <code>SKILL.md</code> metadata and <code>agent-depot.json</code> labels. Do not edit by hand.</p>
  <div class="concept">
    <div><strong>Work</strong>Activities</div>
    <div class="arrow">→</div>
    <div><strong>Output</strong>Artifacts and handoffs</div>
    <div class="arrow">←</div>
    <div><strong>Guidance</strong>Methods, guides and contracts</div>
  </div>
  <p>Packs are install boundaries. Domain, phase, software type, home and evidence are filters, not extra layers.</p>
  <p class="summary">{summary(rows)}<br>Packs: {pack_summary(rows)}<br>Kinds: {kind_summary(rows)}</p>
</header>

<section class="controls">
  <label>Search<input id="search" type="search" placeholder="name, description, plugin..."></label>
  <label>Pack<select id="pack"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'pack'))}</select></label>
  <label>Domain<select id="domain"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'domain'))}</select></label>
  <label>Kind<select id="kind"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'kind'))}</select></label>
  <label>Phase<select id="phase"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'phase'))}</select></label>
  <label>Origin<select id="origin"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'origin'))}</select></label>
  <label>Invocation<select id="invocation"><option value="">All</option>{''.join(f'<option>{html.escape(k)}</option>' for k in counts(rows, 'invocation'))}</select></label>
</section>
<p class="summary"><span id="visible">{len(rows)}</span> of {len(rows)} skills shown.</p>

<table>
<thead><tr><th>Skill</th><th>Pack</th><th>Domain</th><th>Kind</th><th>Phase</th><th>Origin</th><th>Role</th><th>Plugin</th></tr></thead>
<tbody id="rows">
{table_rows(rows)}
</tbody>
</table>
<p id="empty" class="empty" hidden>No skills match the filters.</p>

<script>
const filters = {{}};
const rows = [...document.querySelectorAll('#rows tr')];
const nodes = {{}};
for (const id of ['pack','domain','kind','phase','origin','invocation']) nodes[id] = document.getElementById(id);
const search = document.getElementById('search');
function apply() {{
  const q = search.value.trim().toLowerCase();
  let shown = 0;
  for (const row of rows) {{
    const ok = (!q || row.dataset.search.includes(q)) &&
      Object.entries(nodes).every(([key, node]) => !node.value || row.dataset[key] === node.value);
    row.hidden = !ok;
    if (ok) shown++;
  }}
  document.getElementById('visible').textContent = shown;
  document.getElementById('empty').hidden = shown !== 0;
}}
search.addEventListener('input', apply);
for (const node of Object.values(nodes)) node.addEventListener('change', apply);
</script>
</body>
</html>
'''
    destination.write_text(page)

def write_markdown(rows, destination):
    packs = '\n'.join(f"| `{name}` | {count} |" for name, count in counts(rows, 'pack').items())
    kinds = '\n'.join(f"| `{name}` | {count} |" for name, count in counts(rows, 'kind').items())
    guides = '\n'.join(
        f"| [{row['name']}](../{row['path']}) | {row['domain']} | {row['description']} |"
        for row in rows if row['kind'] == 'guide'
    )
    page = f'''# Skills map

Generated from `SKILL.md` metadata and `agent-depot.json` labels. Open [skills-map.html](skills-map.html) for the filterable explorer.

## The simple model

```mermaid
flowchart LR
  P[Packs / install boundaries] --> S[Skills]
  S --> W[Activities]
  S --> G[Methods and guides]
  S --> C[Contracts]
  W --> A[Artifacts]
  G --> A
  C --> A
  A --> V[Artifact types]
  D[Dimensions: phase, role, software type, home, evidence] -.-> S
  D -.-> A
```

Two core models, a method layer, three cross-cutting dimensions:

- **Activity** — what work is requested and where it stops.
- **Artifact** — what durable output exists, with authority, home, maturity, relations and evidence.
- **Method** — how to deepen or produce the work; `kind: guide` skills own artifact craft.
- **Dimensions** — phase, role, software type, home and evidence filter the two core models.

## Counts

{summary(rows)}

| Pack | Skills |
| --- | ---: |
{packs}

| Kind | Skills |
| --- | ---: |
{kinds}

## Artifact guides

| Guide | Domain | Use for |
| --- | --- | --- |
{guides}

## Full inventory

Run `python scripts/skill_map.py` to regenerate this page and the HTML explorer. The generated HTML is the filterable view; this page is the stable summary.
'''
    destination.write_text(page)

INVENTORY_FIELDS = ('name', 'pack', 'domain', 'kind', 'phase', 'origin',
                    'scope', 'invocation', 'role', 'plugin')

def write_inventory(rows):
    print('| Skill | Pack | Domain | Kind | Phase | Origin | Scope | Invocation | Role | Plugin |')
    print('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for row in rows:
        print('| ' + ' | '.join(row[field] for field in INVENTORY_FIELDS) + ' |')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=OUTPUT)
    parser.add_argument('--inventory', action='store_true',
                        help='print the maintainer classification matrix instead of writing the map')
    args = parser.parse_args()
    rows = build_rows()
    if args.inventory:
        write_inventory(sorted(rows, key=lambda row: (row['plugin'], row['name'])))
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_html(rows, args.output_dir / 'skills-map.html')
    write_markdown(rows, args.output_dir / 'skills-map.md')
    print(f'Wrote {len(rows)} skills to {args.output_dir / "skills-map.html"} and .md')

if __name__ == '__main__':
    main()
