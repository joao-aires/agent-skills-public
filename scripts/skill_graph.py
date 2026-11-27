#!/usr/bin/env python3
"""Generate the skill graph from the repository's declared relationships.

Every node is one of the three node abstractions (capability, work, record);
constraints are node attributes. Every edge is one of the three moves (route,
compose, hand off) or a record link (produces, guided by). In-body links are
emitted separately as `mentions`: evidence, not structure, never counted.
"""
import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

try:
    from skill_metadata import local_skill_labels
    from skill_relationships import (
        BACKTICK_NAME, WORK_KIND, WORK_ORDER, handoff_rows, line_of,
        router_declarations, skill_links, work_targets,
    )
except ModuleNotFoundError:
    from scripts.skill_metadata import local_skill_labels
    from scripts.skill_relationships import (
        BACKTICK_NAME, WORK_KIND, WORK_ORDER, handoff_rows, line_of,
        router_declarations, skill_links, work_targets,
    )

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "docs/visualizations/skill-graph.json"
OUT_HTML = ROOT / "docs/visualizations/skill-graph.html"
CATALOG = "plugins/sdlc/skills/activity-system/references/catalog.md"
HANDOFF = "plugins/sdlc/skills/artifact-system/references/handoff.md"
REGISTRY = "plugins/sdlc/skills/artifact-system/references/artifact-registry.json"

RELATIONS = {"route", "compose", "handoff", "produces", "guided-by"}

def source_digest():
    """A stable fingerprint of the inputs, so the page does not claim a commit it was not built from."""
    digest = hashlib.sha256()
    paths = sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md"))
    paths += [ROOT / CATALOG, ROOT / REGISTRY, ROOT / HANDOFF]
    for path in paths:
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()[:8]


def acquired_labels():
    depot = json.loads((ROOT / "agent-depot.json").read_text())
    labels = {}
    for artifact in depot.get("artifacts", {}).values():
        destination = artifact.get("destination") or ""
        if "/skills/" in destination:
            labels[destination.split("/skills/")[-1]] = (
                artifact.get("metadata") or {}
            ).get("packaging", {}).get("labels", {})
    return labels


def load_skills():
    acquired = acquired_labels()
    skills = {}
    for path in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md")):
        text = path.read_text()
        parts = text.split("---", 2)
        frontmatter = yaml.safe_load(parts[1]) if len(parts) == 3 else {}
        if frontmatter is None:
            frontmatter = {}
        if not isinstance(frontmatter, dict):
            raise ValueError(f"{path.relative_to(ROOT)}: frontmatter is not a mapping")
        meta = frontmatter.get("metadata") or {}
        labels = acquired.get(path.parent.name)
        if labels is None:
            labels = local_skill_labels(frontmatter, path)

        def pick(key, default=None):
            return labels.get(key) or meta.get(key) or default

        relative = path.relative_to(ROOT)
        skills[path.parent.name] = {
            "id": path.parent.name,
            "label": path.parent.name,
            "abstraction": "capability",
            "kind": pick("kind", "method"),
            "plugin": relative.parts[1],
            "phase": pick("phase", "cross-phase"),
            "pack": pick("pack"),
            "role": pick("role"),
            "scope": pick("scope"),
            "origin": pick("origin", "local"),
            "explicit": bool(frontmatter.get("disable-model-invocation")),
            "user_invocable": frontmatter.get("user-invocable", True),
            "description": (frontmatter.get("description") or "").strip(),
            "path": str(relative),
            "body": text,
        }
    return skills


def section_range(text, heading):
    match = re.search(r"^## " + re.escape(heading) + r"\s*$", text, re.M)
    if not match:
        return None
    following = re.search(r"^## ", text[match.end():], re.M)
    end = match.end() + (following.start() if following else len(text))
    return match.start(), end


def artifact_map():
    rules = [
        ("product-feedback-analysis", "product-feedback-analysis"), ("research report", "research-report"),
        ("design proposal", "design-proposal"), ("design spec", "design-specification"), ("data model", "data-model"),
        ("compatibility matrix", "compatibility-matrix"), ("architecture set", "architecture-set"),
        ("state machine", "state-machine"), ("sequence", "sequence-view"), ("c4", "c4-view"), ("roadmap", "roadmap"),
        ("prd", "product-brief"), ("product brief", "product-brief"), ("decision record", "decision-record"),
        ("adr", "decision-record"), ("rfc", "rfc"), ("ecr", "ecr"), ("assurance", "assurance-assessment"),
        ("release note", "release-note"), ("deployment record", "deployment-record"), ("runbook", "runbook"),
        ("incident record", "incident-record"), ("postmortem", "postmortem"), ("pull request", "pull-request"),
        ("pr ", "pull-request"), ("issue", "issue"), ("work product", "work-product"), ("readme", "repository-readme"),
    ]

    def map_text(text):
        lowered = text.lower()
        return {value for key, value in rules if key in lowered}

    return map_text


def build():
    skills = load_skills()
    skill_ids = set(skills)
    registry = json.loads((ROOT / REGISTRY).read_text())["artifacts"]
    records = {item["type"]: item for item in registry if isinstance(item, dict) and "type" in item}
    all_ids = skill_ids | set(records) | {f"work:{name}" for name in WORK_ORDER}

    edges = []
    index = {}
    unresolved = []
    priority = {"section": 3, "alias": 3, "matrix": 3, "registry": 3, "catalog": 1}

    def add(source, target, relation, mechanism, file, line, confidence, note=None):
        if relation not in RELATIONS:
            raise ValueError(f"unknown relation {relation}")
        if source == target:
            return
        for endpoint in (source, target):
            if endpoint not in all_ids:
                unresolved.append(f"{relation} {source}->{target} uses unknown id {endpoint}")
                return
        key = (source, target, relation)
        existing = index.get(key)
        if existing:
            if priority.get(mechanism, 0) > priority.get(existing["mechanism"], 0):
                existing.update({
                    "mechanism": mechanism,
                    "confidence": confidence,
                    "provenance": {"file": file, "line": line},
                })
                if note:
                    existing["note"] = note
            return
        edge = {
            "id": f"{relation}:{mechanism}:{source}->{target}",
            "source": source,
            "target": target,
            "relation": relation,
            "mechanism": mechanism,
            "confidence": confidence,
            "provenance": {"file": file, "line": line},
            **({"note": note} if note else {}),
        }
        index[key] = edge
        edges.append(edge)

    # Route: explicit alias only. Description-based routing has no edge.
    for skill in skills.values():
        text = skill["body"]
        for target, line in router_declarations(text):
            if target in skill_ids:
                add(skill["id"], target, "route", "alias", skill["path"], line, "declared", "router skill")

        declared = section_range(text, "Composition")
        if not declared:
            continue
        segment = text[declared[0]:declared[1]]
        offset = line_of(text, declared[0]) - 1
        for target, line in skill_links(segment, (ROOT / skill["path"]).parent, skill_ids):
            add(skill["id"], target, "compose", "section", skill["path"], line + offset, "declared", "linked capability")
        for match in BACKTICK_NAME.finditer(segment):
            target = match.group(1)
            if target in skill_ids and target != skill["id"]:
                add(skill["id"], target, "compose", "section", skill["path"],
                    line_of(text, declared[0] + match.start()), "declared", "named capability")

    # Compose by catalog index: the row lists supporting expertise.
    catalog_text = (ROOT / CATALOG).read_text()
    rows = []
    for number, line in enumerate(catalog_text.splitlines(), 1):
        if not line.startswith("| ["):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        activity = re.search(r"\]\(\.\./\.\./([a-z0-9-]+)/SKILL\.md\)", cells[0])
        if not activity:
            continue
        rows.append((activity.group(1), cells, number))
        for match in re.finditer(r"\]\(\.\./\.\./([a-z0-9-]+)/SKILL\.md\)", line):
            target = match.group(1)
            if target != activity.group(1) and target in skill_ids:
                add(activity.group(1), target, "compose", "catalog", CATALOG, number, "declared")

    # Produces: work -> record, derived from the catalog's target-view column.
    map_text = artifact_map()
    for activity, cells, number in rows:
        for record in sorted(map_text(cells[4] if len(cells) > 4 else "")):
            add(activity, record, "produces", "catalog", CATALOG, number, "derived")
    for activity, produced in {
        "design": ["design-specification", "data-model", "c4-view", "sequence-view", "state-machine", "compatibility-matrix"],
        "research": ["research-report"],
        "release": ["deployment-record"],
    }.items():
        for record in produced:
            add(activity, record, "produces", "catalog", CATALOG, 0, "derived",
                "curated from the catalog target-view prose")

    # Guided by: record -> the capability that guides writing it.
    for record, item in records.items():
        if item.get("guide") and item["guide"] in skill_ids:
            add(record, item["guide"], "guided-by", "registry", REGISTRY, 0, "declared")

    # Hand off: work -> work, from the phase handoff matrix.
    for source_label, target_label, number in handoff_rows(ROOT):
        for source in work_targets(source_label):
            for target in work_targets(target_label):
                add(f"work:{source}", f"work:{target}", "handoff", "matrix",
                    HANDOFF, number, "declared")

    if unresolved:
        raise ValueError("unresolved graph ids:\n  " + "\n  ".join(unresolved))

    # Mentions: body links that are not already a declared edge.
    declared_pairs = {(edge["source"], edge["target"]) for edge in edges}
    mentions = []
    for skill in skills.values():
        text = skill["body"]
        for target, line in skill_links(text, (ROOT / skill["path"]).parent, skill_ids):
            if (skill["id"], target) in declared_pairs:
                continue
            mentions.append({"from": skill["id"], "to": target, "file": skill["path"], "line": line})

    in_degree = collections.Counter()
    out_degree = collections.Counter()
    for edge in edges:
        out_degree[edge["source"]] += 1
        in_degree[edge["target"]] += 1

    def group_for(skill):
        if skill["plugin"] == "sdlc":
            return "sdlc " + (skill["kind"] or "method")
        return skill["plugin"]

    nodes = []
    for skill in skills.values():
        nodes.append({
            k: v for k, v in skill.items() if k != "body"
        } | {
            "group": group_for(skill),
            "constraints": {"invocation": "explicit-only" if skill["explicit"] else "model-invoked"},
            "degree": in_degree[skill["id"]] + out_degree[skill["id"]],
            "in_degree": in_degree[skill["id"]],
            "out_degree": out_degree[skill["id"]],
        })

    plane = {
        "intent": "intent", "coordination": "coordination", "system-knowledge": "system",
        "implementation": "impl", "delivery": "delivery", "entry": "entry",
    }
    for record, item in records.items():
        nodes.append({
            "id": record, "label": record, "abstraction": "record", "kind": "artifact",
            "plugin": "records", "plane": plane.get(item.get("plane"), "entry"), "group": "records",
            "contract": item.get("contract"), "home": item.get("home"), "guide": item.get("guide"),
            "constraints": {},
            "degree": in_degree[record] + out_degree[record],
            "in_degree": in_degree[record], "out_degree": out_degree[record],
            "path": item.get("contract") or REGISTRY,
        })

    for index, name in enumerate(WORK_ORDER, 1):
        node_id = f"work:{name}"
        nodes.append({
            "id": node_id, "label": name, "abstraction": "work", "kind": WORK_KIND[name],
            "plugin": "work", "group": "work", "order": index,
            "constraints": {},
            "degree": in_degree[node_id] + out_degree[node_id],
            "in_degree": in_degree[node_id], "out_degree": out_degree[node_id],
            "path": HANDOFF,
        })

    groups = collections.defaultdict(list)
    for node in nodes:
        groups[node["group"]].append(node["id"])

    capabilities = [node for node in nodes if node["abstraction"] == "capability"]
    return {
        "schema": "skill-graph/2",
        "model": {
            "abstractions": ["capability", "work", "record", "constraint"],
            "moves": ["route", "compose", "handoff"],
            "record_links": ["produces", "guided-by"],
            "note": "Mentions are evidence, not edges. Constraints are node attributes.",
        },
        "generated": {
            "repository": "joao-aires/agent-skills-public",
            "digest": source_digest(),
            "sources": ["plugins/*/skills/*/SKILL.md", CATALOG, REGISTRY, HANDOFF],
        },
        "counts": {
            "capabilities": len(capabilities),
            "records": sum(1 for node in nodes if node["abstraction"] == "record"),
            "work": len(WORK_ORDER),
            "edges": len(edges),
            "by_relation": dict(collections.Counter(edge["relation"] for edge in edges)),
            "by_mechanism": dict(collections.Counter(edge["mechanism"] for edge in edges)),
            "mentions": len(mentions),
            "isolated_capabilities": sum(1 for node in capabilities if node["degree"] == 0),
            "linked_capabilities": sum(1 for node in capabilities if node["degree"] > 0),
        },
        "groups": [{"id": key, "nodes": members} for key, members in sorted(groups.items())],
        "nodes": nodes,
        "edges": edges,
        "mentions": mentions,
    }


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The skill graph</title>
<style>
  :root{--bg:#0b0e13;--panel:#11151c;--ink:#e9e6df;--muted:#8b93a0;--line:#232a34;
    --route:#f4a261;--compose:#7d9bff;--handoff:#b794f6;--produces:#e0b15c;--guided:#63c68a;--mention:#5a6472;}
  *{box-sizing:border-box}
  html,body{margin:0;background:var(--bg);color:var(--ink);font-family:ui-sans-serif,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
  header{padding:20px 24px 10px}
  .top{display:flex;justify-content:space-between;gap:20px;align-items:flex-start}
  .kicker{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
  h1{font-family:ui-serif,Georgia,serif;font-weight:600;font-size:clamp(26px,3vw,40px);line-height:1.05;margin:7px 0 6px;letter-spacing:-.02em}
  .meta{font-size:12px;color:var(--muted);margin:0}
  .meta b{color:var(--ink);font-weight:600}
  .jsonlink{font-size:11px;color:var(--muted);text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 10px;white-space:nowrap}
  .jsonlink:hover{color:var(--ink);border-color:#3a4452}
  .controls{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-top:12px}
  .chip{border:1px solid var(--line);background:var(--panel);border-radius:999px;padding:5px 10px;font-size:11.5px;color:#c5cbd4;cursor:pointer;display:inline-flex;gap:6px;align-items:center}
  .chip[aria-pressed="false"]{opacity:.35;text-decoration:line-through}
  .chip i{width:15px;height:0;border-top:2px solid var(--ink);display:inline-block}
  input[type=search],select{border:1px solid var(--line);background:var(--panel);border-radius:8px;padding:6px 9px;font:inherit;font-size:12px;color:var(--ink);outline:none}
  input[type=search]{width:190px}
  input[type=search]:focus,select:focus{border-color:#3a4452}
  select{max-width:210px}
  .hint{font-size:11px;color:var(--muted);margin-left:auto}
  .workspace{display:flex;gap:14px;padding:4px 20px 20px;height:calc(100vh - 210px);min-height:560px}
  .wrap{position:relative;flex:1;min-width:0;background:#0a0d12;border:1px solid var(--line);border-radius:14px;overflow:hidden}
  canvas{position:absolute;inset:0;width:100%;height:100%;display:block;cursor:grab;touch-action:none;-webkit-tap-highlight-color:transparent}
  canvas.grabbing{cursor:grabbing}
  .legend{position:absolute;left:14px;bottom:12px;display:flex;flex-wrap:wrap;gap:10px;font-size:10.5px;color:#93a0b0;pointer-events:none;max-width:70%}
  .legend span{display:inline-flex;align-items:center;gap:5px;background:rgba(11,14,19,.7);padding:3px 6px;border-radius:5px}
  .legend i{width:18px;height:0;border-top:2px solid var(--ink);display:inline-block}
  .hud{position:absolute;right:12px;bottom:12px;display:flex;gap:6px}
  .hud button{width:30px;height:30px;border:1px solid var(--line);background:rgba(17,21,28,.9);border-radius:7px;font:inherit;font-size:14px;color:#c5cbd4;cursor:pointer}
  aside{width:340px;flex:0 0 340px;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px;overflow:auto}
  aside h2{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 8px;font-weight:600}
  aside h3{font-family:ui-serif,Georgia,serif;font-size:22px;line-height:1.12;margin:0 0 7px;font-weight:600}
  aside p{font-size:12.5px;line-height:1.5;color:#aab2bd;margin:0 0 8px}
  aside .tag{display:inline-block;font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;border:1px solid var(--line);border-radius:999px;padding:2px 7px;color:#9aa4b2;margin:0 4px 6px 0}
  aside dl{margin:8px 0 0;font-size:12px}
  aside dt{color:var(--muted);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;margin-top:10px}
  aside dd{margin:2px 0 0;line-height:1.45;color:#c5cbd4}
  aside ul{margin:3px 0 0;padding-left:15px;font-size:11.5px;line-height:1.45;color:#c5cbd4}
  aside li{margin:1px 0}
  aside code{font-size:10.5px;background:#1a2029;padding:1px 4px;border-radius:3px;color:#c5cbd4}
  aside .edge{color:var(--muted)}
  footer{padding:0 24px 26px;color:#6f7885;font-size:10.5px;line-height:1.55;max-width:1100px}
  @media (max-width:1050px){
    .workspace{flex-direction:column;height:auto;min-height:0;padding:4px 12px 14px;gap:10px}
    .wrap{flex:0 0 auto;height:68vh;min-height:340px;order:-1}
    aside{width:auto;flex:0 0 auto;max-height:none}
    header{padding:14px 14px 6px}
    .top{flex-wrap:wrap}
    .hint{display:none}
    input[type=search]{width:100%}
    .hud button{width:40px;height:40px;font-size:16px}
  }
  @media (max-width:560px){
    .wrap{height:62vh;min-height:300px}
    h1{font-size:26px}
    .legend{font-size:9.5px;max-width:88%;bottom:58px}
  }
</style>
</head>
<body>
<header>
  <div class="top">
    <div>
      <div class="kicker">Skill interaction model · derived graph</div>
      <h1>The skill graph</h1>
      <p class="meta"><b>__CAPS__</b> capabilities (<b>__LINKED__</b> linked) · <b>__RECORDS__</b> records · <b>__WORK__</b> work states · <b>__EDGES__</b> edges · <b>__MENTIONS__</b> mentions · source <code>__COMMIT__</code></p>
    </div>
    <a class="jsonlink" href="skill-graph.json" download>Download JSON</a>
  </div>
  <div class="controls">
    <button class="chip" data-relation="route" aria-pressed="true"><i style="border-color:var(--route)"></i>Route</button>
    <button class="chip" data-relation="compose" aria-pressed="true"><i style="border-color:var(--compose)"></i>Compose</button>
    <button class="chip" data-relation="handoff" aria-pressed="true"><i style="border-color:var(--handoff)"></i>Hand off</button>
    <button class="chip" data-relation="produces" aria-pressed="true"><i style="border-color:var(--produces)"></i>Produces</button>
    <button class="chip" data-relation="guided-by" aria-pressed="true"><i style="border-color:var(--guided);border-top-style:dotted"></i>Guided by</button>
    <button class="chip" data-layer="work" aria-pressed="false"><i style="border-color:var(--handoff)"></i>Work states</button>
    <button class="chip" id="mentions" aria-pressed="false"><i style="border-color:var(--mention)"></i>Mentions</button>
    <input id="search" type="search" placeholder="Search capabilities and records">
    <select id="plugin"><option value="">All plugins</option></select>
    <select id="kind"><option value="">All kinds</option></select>
    <button class="chip" id="labels" aria-pressed="false">Always show labels</button>
    <button class="chip" id="orphans" aria-pressed="false">Show orphans</button>
    <button class="chip" id="physics" aria-pressed="true">Physics</button>
    <span class="hint">Hover to isolate · click to inspect · drag · scroll to zoom</span>
  </div>
</header>
<div class="workspace">
  <div class="wrap" id="wrap">
    <canvas id="graph"></canvas>
    <div class="legend">
      <span><i style="border-color:var(--route)"></i>route</span>
      <span><i style="border-color:var(--compose)"></i>compose</span>
      <span><i style="border-color:var(--compose);border-top-style:dashed"></i>compose · catalog</span>
      <span><i style="border-color:var(--handoff)"></i>hand off</span>
      <span><i style="border-color:var(--produces)"></i>produces</span>
      <span><i style="border-color:var(--guided);border-top-style:dotted"></i>guided by</span>
    </div>
    <div class="hud"><button id="fit">⌂</button><button id="zoomout">−</button><button id="zoomin">+</button></div>
  </div>
  <aside id="panel"></aside>
</div>
<footer>
  Derived from <code>plugins/*/skills/*/SKILL.md</code>, the activity catalog, the artifact registry and the handoff matrix. Every edge is a move or a record link; in-body links are <b>mentions</b>, drawn only on request and never counted as edges. Constraints are node attributes, not relations. A missing edge means no declared relationship was found, not that the capabilities are unrelated. The layout is a reading aid, not a resolver.
</footer>
<script>
const DATA = __DATA__;
const canvas=document.getElementById('graph');
const wrap=document.getElementById('wrap');
const panel=document.getElementById('panel');
const ctx=canvas.getContext('2d');
const edges=DATA.edges.map(e=>({...e}));
const rawMentions=DATA.mentions.map(m=>({...m}));
const state={relation:{route:true,compose:true,handoff:true,produces:true,'guided-by':true},
  layer:{capability:true,record:true,work:false},mentions:false,
  focus:null,hover:null,search:'',plugin:'',kind:'',labels:false,showOrphans:false,physics:true,
  moved:false,dragStart:null,panMoved:false,suppressClick:false,pointers:new Map(),pinch:null,
  cam:{x:0,y:0,k:1},alpha:1,dragging:null,pan:null};

const COLOR={kind:{activity:'#7d9bff',method:'#4fd1c5',guide:'#e0b15c',workflow:'#b794f6',system:'#f2f2f2',acquired:'#6b7480'},
  plane:{intent:'#e0b15c',coordination:'#7d9bff',system:'#63c68a',impl:'#4fd1c5',delivery:'#f08a5d',entry:'#8b93a0'},
  work:'#b794f6'};
const EDGE={route:['#f4a261',1.7,'none'],'compose:section':['#7d9bff',1.5,'none'],
  'compose:catalog':['#7d9bff',1.1,[5,4]],handoff:['#b794f6',1.6,'none'],
  produces:['#e0b15c',0.9,'none'],'guided-by':['#63c68a',0.9,[1,4]]};
const edgeKey=e=>e.relation==='compose'?'compose:'+e.mechanism:e.relation;
const colorOf=n=>n.abstraction==='work'?COLOR.work:n.abstraction==='record'?(COLOR.plane[n.plane]||'#8b93a0'):(COLOR.kind[n.kind]||'#6b7480');

const nodes=DATA.nodes.map(n=>({...n,x:0,y:0,vx:0,vy:0,
  r:n.abstraction==='record'?9:n.abstraction==='work'?11:7+Math.min(9,Math.sqrt(n.degree||0)*1.25)}));
// Bind edges to the laid-out nodes, not to the raw data objects.
const nodeById=new Map(nodes.map(n=>[n.id,n]));
edges.forEach(e=>{e.a=nodeById.get(e.source);e.b=nodeById.get(e.target);});
const mentions=rawMentions.map(m=>({...m,a:nodeById.get(m.from),b:nodeById.get(m.to)})).filter(m=>m.a&&m.b);

const groups=[...new Set(nodes.map(n=>n.group))];
const centers={};
const inner=groups.filter(g=>g.startsWith('sdlc')||g==='strategy'||g==='documentation');
const outer=groups.filter(g=>!inner.includes(g)&&g!=='records'&&g!=='work');
inner.forEach((g,i)=>{const a=i/inner.length*Math.PI*2;centers[g]=[Math.cos(a)*190,Math.sin(a)*190];});
outer.forEach((g,i)=>{const a=i/outer.length*Math.PI*2;centers[g]=[Math.cos(a)*430,Math.sin(a)*430];});
centers.records=[0,0];centers.work=[0,760];
let seed=1234567;const rnd=()=>{seed=(seed*1664525+1013904223)>>>0;return seed/4294967296;};
nodes.forEach(n=>{const c=centers[n.group]||[0,0];n.x=c[0]+(rnd()-.5)*110;n.y=c[1]+(rnd()-.5)*110;});

function tick(alpha){
  for(let i=0;i<nodes.length;i++){
    const a=nodes[i];
    for(let j=i+1;j<nodes.length;j++){
      const b=nodes[j];let dx=b.x-a.x,dy=b.y-a.y;let d2=dx*dx+dy*dy;
      if(d2>250000||d2===0)continue;
      const f=2300/d2*alpha;const ux=dx/Math.sqrt(d2),uy=dy/Math.sqrt(d2);
      a.vx-=ux*f;a.vy-=uy*f;b.vx+=ux*f;b.vy+=uy*f;
    }
    const c=centers[a.group]||[0,0];
    a.vx+=(c[0]-a.x)*0.004*alpha;a.vy+=(c[1]-a.y)*0.004*alpha;
    a.vx-=a.x*0.00015*alpha;a.vy-=a.y*0.00015*alpha;
  }
  edges.forEach(e=>{
    const a=e.a,b=e.b;if(!a||!b)return;
    let dx=b.x-a.x,dy=b.y-a.y;let d=Math.hypot(dx,dy)||1;
    const rest=e.relation==='handoff'?150:65;const k=e.relation==='handoff'?0.02:0.014;
    const f=(d-rest)*k*alpha;const ux=dx/d,uy=dy/d;
    a.vx+=ux*f;a.vy+=uy*f;b.vx-=ux*f;b.vy-=uy*f;
    const min=a.r+b.r+7;
    if(d<min){const push=(min-d)*0.5*alpha;a.vx-=ux*push;a.vy-=uy*push;b.vx+=ux*push;b.vy+=uy*push;}
  });
  nodes.forEach(n=>{if(n.fixed)return;n.vx*=0.86;n.vy*=0.86;n.x+=n.vx;n.y+=n.vy;});
}
for(let i=0;i<260;i++)tick(1-i/260);
nodes.forEach(n=>{if(!n.fixed)n.x*=1.55;});
// Work states are a chain, not a cloud: place them in reading order below the graph.
const workNodes=nodes.filter(n=>n.abstraction==='work').sort((a,b)=>a.order-b.order);
workNodes.forEach((n,i)=>{n.x=(i-(workNodes.length-1)/2)*240;n.y=820;n.vx=0;n.vy=0;n.fixed=true;});

// Records shown under a filter are the ones its capabilities actually connect to.
const capNeighbors=new Map();
nodes.filter(n=>n.abstraction==='capability').forEach(n=>capNeighbors.set(n.id,new Set()));
edges.forEach(e=>{
  if(e.a&&e.a.abstraction==='capability'&&e.b)capNeighbors.get(e.a.id).add(e.b.id);
  if(e.b&&e.b.abstraction==='capability'&&e.a)capNeighbors.get(e.b.id).add(e.a.id);
});
const matchesFilters=c=>(!state.plugin||c.plugin===state.plugin)&&(!state.kind||c.kind===state.kind);
const mentionIn={},mentionOut={};
DATA.mentions.forEach(m=>{mentionOut[m.from]=(mentionOut[m.from]||0)+1;mentionIn[m.to]=(mentionIn[m.to]||0)+1;});

function visibleNode(n){
  if(!state.layer[n.abstraction])return false;
  const filtered=state.plugin||state.kind;
  if(n.abstraction==='capability'){
    // A filter shows the whole matching membership, including skills with no declared edge.
    if(!matchesFilters(n))return false;
    if(n.degree===0&&!state.showOrphans&&!filtered)return false;
    return true;
  }
  if(n.abstraction==='record'&&filtered){
    for(const c of nodes){ if(c.abstraction==='capability'&&matchesFilters(c)&&capNeighbors.get(c.id).has(n.id)) return true; }
    return false;
  }
  return true;
}
function visibleEdge(e){
  if(!state.relation[e.relation])return false;
  if(!e.a||!e.b)return false;
  return visibleNode(e.a)&&visibleNode(e.b);
}
function neighbors(id){
  const s=new Set([id]);
  edges.forEach(e=>{if(!visibleEdge(e))return;if(e.source===id)s.add(e.target);if(e.target===id)s.add(e.source);});
  return s;
}
function focusSet(){return state.hover?neighbors(state.hover):state.focus?neighbors(state.focus):null;}

function fit(){
  const vis=nodes.filter(visibleNode);
  if(!vis.length)return;
  const xs=vis.map(n=>n.x),ys=vis.map(n=>n.y);
  const minx=Math.min(...xs),maxx=Math.max(...xs),miny=Math.min(...ys),maxy=Math.max(...ys);
  const w=wrap.clientWidth,h=wrap.clientHeight;
  const k=Math.min((w-80)/(maxx-minx||1),(h-80)/(maxy-miny||1));
  state.cam.k=Math.max(.15,Math.min(3,k));
  state.cam.x=-(minx+maxx)/2*state.cam.k;
  state.cam.y=-(miny+maxy)/2*state.cam.k;
}
function fitTo(ids){
  const vis=nodes.filter(n=>ids.has(n.id)&&visibleNode(n));
  if(!vis.length){fit();return;}
  const xs=vis.map(n=>n.x),ys=vis.map(n=>n.y);
  const minx=Math.min(...xs),maxx=Math.max(...xs),miny=Math.min(...ys),maxy=Math.max(...ys);
  const w=wrap.clientWidth,h=wrap.clientHeight;
  const k=Math.min((w-140)/(maxx-minx||1),(h-140)/(maxy-miny||1));
  state.cam.k=Math.max(.35,Math.min(2.4,k));
  state.cam.x=-(minx+maxx)/2*state.cam.k;
  state.cam.y=-(miny+maxy)/2*state.cam.k;
}
function resize(){
  const dpr=window.devicePixelRatio||1;
  const r=wrap.getBoundingClientRect();
  canvas.width=Math.floor(r.width*dpr);canvas.height=Math.floor(r.height*dpr);
  ctx.setTransform(dpr,0,0,dpr,0,0);
  if(state.focus)fitTo(neighbors(state.focus));else fit();draw();
}
window.addEventListener('resize',resize);

function draw(){
  const w=wrap.clientWidth,h=wrap.clientHeight;
  ctx.clearRect(0,0,w,h);
  ctx.save();
  ctx.translate(w/2+state.cam.x,h/2+state.cam.y);
  ctx.scale(state.cam.k,state.cam.k);
  const rel=focusSet();
  const q=state.search;
  const visDeg={}; nodes.forEach(n=>visDeg[n.id]=0);
  edges.forEach(e=>{if(!visibleEdge(e))return;visDeg[e.source]++;visDeg[e.target]++;});
  const rOf=n=>n.abstraction==='record'?9:n.abstraction==='work'?11:6+Math.min(9,Math.sqrt(visDeg[n.id]||0)*1.25);
  nodes.forEach(n=>{n.rr=rOf(n);});

  if(state.mentions){
    mentions.forEach(m=>{
      if(!visibleNode(m.a)||!visibleNode(m.b))return;
      ctx.strokeStyle='#5a6472';ctx.globalAlpha=.22;ctx.lineWidth=.7/state.cam.k;
      ctx.beginPath();ctx.moveTo(m.a.x,m.a.y);ctx.lineTo(m.b.x,m.b.y);ctx.stroke();
    });
    ctx.globalAlpha=1;
  }

  const rank={route:6,handoff:5,'compose:section':4,'compose:catalog':3,produces:2,'guided-by':1};
  const best=new Map();
  edges.forEach(e=>{
    if(!visibleEdge(e))return;
    const key=e.source+'|'+e.target;
    const cur=best.get(key);
    if(!cur||rank[edgeKey(e)]>rank[edgeKey(cur)])best.set(key,e);
  });
  const drawEdges=[...best.values()];
  drawEdges.forEach(e=>{
    if(rel&&!(rel.has(e.source)&&rel.has(e.target)))return;
    if(q&&!(e.source.includes(q)||e.target.includes(q)))return;
    const [c,lw,dash]=EDGE[edgeKey(e)];
    ctx.strokeStyle=c;ctx.globalAlpha=.55;ctx.lineWidth=lw/state.cam.k;
    ctx.setLineDash(Array.isArray(dash)?dash.map(x=>x/state.cam.k):[]);
    ctx.beginPath();ctx.moveTo(e.a.x,e.a.y);ctx.lineTo(e.b.x,e.b.y);ctx.stroke();
  });
  ctx.setLineDash([]);ctx.globalAlpha=1;

  const focusId=state.hover||state.focus;
  if(focusId){
    drawEdges.forEach(e=>{
      if(e.source!==focusId&&e.target!==focusId)return;
      const [c]=EDGE[edgeKey(e)];ctx.strokeStyle=c;ctx.globalAlpha=.95;ctx.lineWidth=1.6/state.cam.k;
      ctx.beginPath();ctx.moveTo(e.a.x,e.a.y);ctx.lineTo(e.b.x,e.b.y);ctx.stroke();
      const ang=Math.atan2(e.b.y-e.a.y,e.b.x-e.a.x);const tx=e.b.x-Math.cos(ang)*((e.b.rr||e.b.r)+4),ty=e.b.y-Math.sin(ang)*((e.b.rr||e.b.r)+4);
      const s=4/state.cam.k;ctx.fillStyle=c;ctx.beginPath();
      ctx.moveTo(tx,ty);ctx.lineTo(tx-Math.cos(ang-.5)*s,ty-Math.sin(ang-.5)*s);ctx.lineTo(tx-Math.cos(ang+.5)*s,ty-Math.sin(ang+.5)*s);ctx.closePath();ctx.fill();
    });
    ctx.globalAlpha=1;
  }

  nodes.forEach(n=>{
    if(!visibleNode(n))return;
    const dim=rel&&!rel.has(n.id) || (q&&!n.id.includes(q));
    ctx.globalAlpha=dim?.12:1;
    ctx.fillStyle=colorOf(n);
    const rr=n.rr||n.r;
    if(n.abstraction==='record'){
      ctx.beginPath();ctx.moveTo(n.x,n.y-rr);ctx.lineTo(n.x+rr,n.y);ctx.lineTo(n.x,n.y+rr);ctx.lineTo(n.x-rr,n.y);ctx.closePath();ctx.fill();
    }else if(n.abstraction==='work'){
      ctx.beginPath();ctx.roundRect(n.x-rr,n.y-rr,rr*2,rr*2,4);ctx.fill();
      ctx.strokeStyle='#0b0e13';ctx.lineWidth=2/state.cam.k;ctx.stroke();
    }else{
      ctx.beginPath();ctx.arc(n.x,n.y,rr,0,Math.PI*2);ctx.fill();
    }
    if(n.id===state.focus||n.id===state.hover){
      ctx.strokeStyle='#f4f1e9';ctx.lineWidth=1.6/state.cam.k;ctx.stroke();
    }
  });
  ctx.globalAlpha=1;

  nodes.forEach(n=>{
    if(!visibleNode(n))return;
    const rel2=focusSet();
    const show=state.labels||rel2&&rel2.has(n.id)||n.id===state.focus||n.id===state.hover||n.degree>=22||n.abstraction==='work'||state.cam.k>1.7;
    if(!show)return;
    if(rel2&&!rel2.has(n.id))return;
    if(q&&!n.id.includes(q))return;
    const isWork=n.abstraction==='work';
    const text=isWork?n.label:n.id;
    const fs=(isWork?13:12)/state.cam.k;
    ctx.font=`${fs}px ui-sans-serif,-apple-system,sans-serif`;
    ctx.textAlign='center';ctx.textBaseline=isWork?'bottom':'top';
    const ly=isWork?n.y-(n.rr||n.r)-5/state.cam.k:n.y+(n.rr||n.r)+3/state.cam.k;
    ctx.lineWidth=3/state.cam.k;ctx.strokeStyle='#0a0d12';
    ctx.strokeText(text,n.x,ly);
    ctx.fillStyle=n.id===state.focus||n.id===state.hover?'#ffffff':'#c5cbd4';
    ctx.fillText(text,n.x,ly);
  });
  ctx.restore();
}

// interaction
function world(e){
  const r=canvas.getBoundingClientRect();
  const mx=(e.clientX-r.left),my=(e.clientY-r.top);
  return {x:(mx-wrap.clientWidth/2-state.cam.x)/state.cam.k,y:(my-wrap.clientHeight/2-state.cam.y)/state.cam.k,mx,my};
}
function hit(e){
  const {x,y}=world(e);let best=null,bd=1e9;
  nodes.forEach(n=>{if(!visibleNode(n))return;const d=Math.hypot(n.x-x,n.y-y);if(d<(n.rr||n.r)+9/state.cam.k&&d<bd){best=n;bd=d;}});
  return best;
}
canvas.addEventListener('pointermove',e=>{
  if(state.pointers.has(e.pointerId))state.pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
  if(state.pinch&&state.pointers.size>=2){
    const [a,b]=[...state.pointers.values()];
    const r=canvas.getBoundingClientRect();
    const mx=(a.x+b.x)/2-r.left,my=(a.y+b.y)/2-r.top;
    const span=Math.hypot(a.x-b.x,a.y-b.y)||1;
    const k=Math.max(.2,Math.min(4,state.pinch.k*span/state.pinch.dist));
    const wx=(state.pinch.mx-state.pinch.w/2-state.pinch.cx)/state.pinch.k;
    const wy=(state.pinch.my-state.pinch.h/2-state.pinch.cy)/state.pinch.k;
    state.cam.k=k;
    state.cam.x=mx-state.pinch.w/2-wx*k;
    state.cam.y=my-state.pinch.h/2-wy*k;
    draw();return;
  }
  if(state.dragging){
    const dx=e.clientX-state.dragStart.x,dy=e.clientY-state.dragStart.y;
    if(!state.moved&&Math.hypot(dx,dy)>5)state.moved=true;
    if(state.moved){
      const w=world(e);state.dragging.x=w.x;state.dragging.y=w.y;state.dragging.vx=0;state.dragging.vy=0;state.alpha=Math.max(state.alpha,.15);draw();
    }
    return;
  }
  if(state.pan){
    const dx=e.clientX-state.pan.sx,dy=e.clientY-state.pan.sy;
    if(Math.hypot(dx,dy)>5)state.panMoved=true;
    state.cam.x=state.pan.cx+dx;state.cam.y=state.pan.cy+dy;draw();return;
  }
  const n=hit(e);
  if((n?n.id:null)!==state.hover){state.hover=n?n.id:null;draw();}
  canvas.style.cursor=n?'pointer':'grab';
});
canvas.addEventListener('pointerdown',e=>{
  state.pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
  if(state.pointers.size===2){
    state.dragging=null;state.pan=null;
    const [a,b]=[...state.pointers.values()];
    const r=canvas.getBoundingClientRect();
    state.pinch={dist:Math.hypot(a.x-b.x,a.y-b.y)||1,k:state.cam.k,
      mx:(a.x+b.x)/2-r.left,my:(a.y+b.y)/2-r.top,
      cx:state.cam.x,cy:state.cam.y,w:wrap.clientWidth,h:wrap.clientHeight};
    state.suppressClick=true;
    canvas.setPointerCapture(e.pointerId);
    return;
  }
  const n=hit(e);
  if(n){state.dragging=n;state.moved=false;state.dragStart={x:e.clientX,y:e.clientY};state.alpha=Math.max(state.alpha,.2);}
  else{state.pan={sx:e.clientX,sy:e.clientY,cx:state.cam.x,cy:state.cam.y};state.panMoved=false;canvas.classList.add('grabbing');}
  canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener('pointerup',e=>{
  state.pointers.delete(e.pointerId);
  if(state.pinch){
    if(state.pointers.size<2)state.pinch=null;
    state.suppressClick=true;canvas.classList.remove('grabbing');draw();return;
  }
  if(state.dragging){
    if(!state.moved){state.focus=state.dragging.id;state.suppressClick=true;fitTo(neighbors(state.focus));renderPanel();}
    else state.suppressClick=true;
    state.dragging=null;
  }
  if(state.pan){if(state.panMoved)state.suppressClick=true;state.pan=null;}
  canvas.classList.remove('grabbing');draw();
});
canvas.addEventListener('pointercancel',e=>{
  state.pointers.delete(e.pointerId);
  if(state.pointers.size<2)state.pinch=null;
  state.dragging=null;state.pan=null;canvas.classList.remove('grabbing');
});
canvas.addEventListener('click',e=>{
  if(state.suppressClick){state.suppressClick=false;return;}
  if(!hit(e)){state.focus=null;fit();renderPanel();draw();}
});
canvas.addEventListener('dblclick',e=>e.preventDefault());
canvas.addEventListener('wheel',e=>{
  e.preventDefault();
  const r=canvas.getBoundingClientRect();const mx=e.clientX-r.left,my=e.clientY-r.top;
  const wx=(mx-wrap.clientWidth/2-state.cam.x)/state.cam.k,wy=(my-wrap.clientHeight/2-state.cam.y)/state.cam.k;
  const d=Math.max(-80,Math.min(80,e.deltaY));
  const k=Math.max(.2,Math.min(4,state.cam.k*Math.exp(-d*0.0016)));
  state.cam.x=mx-wrap.clientWidth/2-wx*k;state.cam.y=my-wrap.clientHeight/2-wy*k;state.cam.k=k;draw();
},{passive:false});

function step(){
  if(state.physics&&state.alpha>.004){tick(state.alpha);state.alpha*=.985;draw();}
  requestAnimationFrame(step);
}

document.querySelectorAll('[data-relation]').forEach(b=>b.addEventListener('click',()=>{
  const key=b.dataset.relation;state.relation[key]=!state.relation[key];
  b.setAttribute('aria-pressed',String(state.relation[key]));draw();
}));
document.querySelectorAll('[data-layer]').forEach(b=>b.addEventListener('click',()=>{
  const key=b.dataset.layer;state.layer[key]=!state.layer[key];
  b.setAttribute('aria-pressed',String(state.layer[key]));
  state.focus=null;fit();renderPanel();draw();
}));
const sel=document.getElementById('plugin');
const capabilities=DATA.nodes.filter(n=>n.abstraction==='capability');
sel.options[0].textContent=`All plugins · ${capabilities.length}`;
[...new Set(capabilities.map(n=>n.plugin))].sort().forEach(p=>{
  const count=capabilities.filter(n=>n.plugin===p).length;
  const o=document.createElement('option');o.value=p;o.textContent=`${p} · ${count}`;sel.appendChild(o);
});
sel.onchange=()=>{state.plugin=sel.value;state.focus=null;fit();renderPanel();draw();};
const kindSel=document.getElementById('kind');
kindSel.options[0].textContent=`All kinds · ${capabilities.length}`;
['activity','workflow','method','guide','system'].forEach(k=>{
  const count=capabilities.filter(n=>n.kind===k).length;
  if(!count)return;
  const o=document.createElement('option');o.value=k;o.textContent=`${k} · ${count}`;kindSel.appendChild(o);
});
kindSel.onchange=()=>{state.kind=kindSel.value;state.focus=null;fit();renderPanel();draw();};
document.getElementById('search').oninput=e=>{state.search=e.target.value.toLowerCase().trim();draw();};
document.getElementById('labels').onclick=e=>{state.labels=!state.labels;e.currentTarget.setAttribute('aria-pressed',String(state.labels));draw();};
document.getElementById('orphans').onclick=e=>{state.showOrphans=!state.showOrphans;e.currentTarget.setAttribute('aria-pressed',String(state.showOrphans));fit();draw();};
document.getElementById('physics').onclick=e=>{state.physics=!state.physics;e.currentTarget.setAttribute('aria-pressed',String(state.physics));};
document.getElementById('mentions').onclick=e=>{state.mentions=!state.mentions;e.currentTarget.setAttribute('aria-pressed',String(state.mentions));draw();};
document.getElementById('fit').onclick=()=>{fit();draw();};
document.getElementById('zoomin').onclick=()=>{state.cam.k=Math.min(4,state.cam.k*1.2);draw();};
document.getElementById('zoomout').onclick=()=>{state.cam.k=Math.max(.2,state.cam.k/1.2);draw();};

function relationList(arr,dir){
  return arr.length?`<ul>${arr.map(e=>{
    const other=dir==='out'?e.target:e.source;
    const label=e.relation==='compose'?`compose · ${e.mechanism}`:e.relation==='handoff'?'hand off':e.relation;
    return `<li>${dir==='out'?'→':'←'} <b>${other}</b> <span class="edge">${label}</span></li>`;
  }).join('')}</ul>`:'<p>—</p>';
}

function renderPanel(){
  if(!state.focus){
    const c=DATA.counts.by_relation||{};
    const filters=[state.plugin,state.kind].filter(Boolean).join(' · ');
    const scoped=capabilities.filter(n=>matchesFilters(n));
    const scopedIds=new Set(scoped.map(n=>n.id));
    const scopedOrphans=scoped.filter(n=>n.degree===0).length;
    const scopedMentions=DATA.mentions.filter(m=>scopedIds.has(m.from)).length;
    const heading=filters?`${filters} · ${scoped.length} capabilities`:`${DATA.counts.capabilities} capabilities, ${DATA.counts.records} records`;
    const isolatedNote=scopedOrphans?` (${filters?'shown because a filter is active':'hidden until you show orphans'})`:'';
    panel.innerHTML=`<h2>Reading the graph</h2><h3>${heading}</h3>
      <p><b>${filters||'All plugins'}</b>: ${scoped.length} capabilities, ${scoped.length-scopedOrphans} with a declared relationship, ${scopedOrphans} isolated${isolatedNote}, ${scopedMentions} mentions among them.</p>
      <p>${DATA.counts.edges} edges — ${c.route||0} route, ${c.compose||0} compose, ${c.handoff||0} hand off, ${c.produces||0} produces, ${c['guided-by']||0} guided by. Plus ${DATA.counts.mentions} mentions, not counted.</p>
      <p><b>Route</b> is explicit entry: a user-invoked alias calling a model-invoked skill. Description-based selection has no edge.</p>
      <p><b>Compose</b> is optional expertise; a solid line is declared in the skill, a dashed line comes from the catalog index. <b>Hand off</b> moves work between phases. <b>Produces</b> and <b>guided by</b> are record links, not moves.</p>
      <p><b>Work states</b> are off by default: showing phases makes the graph look like a pipeline, which it is not. Turn them on to see the handoff chain.</p>
      <p><b>Mentions</b> are body links — evidence, not structure. They never change node size.</p>
      <p>${DATA.counts.isolated_capabilities} capabilities have no declared relationship and are hidden; use <b>Show orphans</b>. Hover to isolate, click to inspect, background click to reset.</p>`;
    return;
  }
  const n=nodeById.get(state.focus);
  const out=edges.filter(e=>e.source===n.id&&visibleEdge(e));
  const inc=edges.filter(e=>e.target===n.id&&visibleEdge(e));
  const tags=[`<span class="tag">${n.abstraction}</span>`];
  if(n.abstraction==='capability')tags.push(`<span class="tag">${n.kind}</span>`,`<span class="tag">${n.plugin}</span>`);
  if(n.abstraction==='record')tags.push(`<span class="tag">${n.plane}</span>`);
  if(n.abstraction==='work')tags.push(`<span class="tag">${n.kind}</span>`);
  if(n.explicit)tags.push('<span class="tag" style="border-color:#b45309;color:#e0b15c">explicit only</span>');
  if(n.abstraction==='capability'&&n.degree===0)tags.push('<span class="tag">no declared relationship</span>');
  const detail=n.abstraction==='record'
    ?`<dt>Contract</dt><dd>${n.contract||'—'}</dd><dt>Home</dt><dd>${n.home||'—'}</dd><dt>Guide</dt><dd>${n.guide||'—'}</dd>`
    :n.abstraction==='work'
      ?`<dt>Order</dt><dd>${n.order}</dd>`
      :`<dt>Phase</dt><dd>${n.phase}</dd><dt>Pack</dt><dd>${n.pack||'—'}</dd><dt>Invocation</dt><dd>${(n.constraints||{}).invocation||'—'}</dd>`;
  panel.innerHTML=`<h2>${n.abstraction}</h2><h3>${n.abstraction==='work'?n.label:n.id}</h3>
    <div>${tags.join('')}</div>
    ${n.description?`<p>${n.description.length>420?n.description.slice(0,417)+'…':n.description}</p>`:''}
    <dl>
      ${detail}
      <dt>Degree</dt><dd>${n.in_degree} in · ${n.out_degree} out</dd>
      <dt>Mentions</dt><dd>${mentionIn[n.id]||0} in · ${mentionOut[n.id]||0} out <span class="edge">(evidence, not edges)</span></dd>
      <dt>Outgoing (${out.length})</dt><dd>${relationList(out,'out')}</dd>
      <dt>Incoming (${inc.length})</dt><dd>${relationList(inc,'in')}</dd>
      <dt>Source</dt><dd><code>${n.path}</code></dd>
    </dl>`;
}

window.__graphNodes=nodes;window.__graphCam=state.cam;window.__graphState=state;window.__graphVisible=visibleNode;
if(nodeById.has('design'))state.focus='design';
resize();renderPanel();step();
</script>
</body>
</html>
"""


def render(document):
    html = HTML.replace("__DATA__", json.dumps(document, separators=(",", ":")).replace("</", "<\\/"))
    for token, value in {
        "__CAPS__": document["counts"]["capabilities"],
        "__LINKED__": document["counts"]["linked_capabilities"],
        "__RECORDS__": document["counts"]["records"],
        "__WORK__": document["counts"]["work"],
        "__EDGES__": document["counts"]["edges"],
        "__MENTIONS__": document["counts"]["mentions"],
        "__COMMIT__": document["generated"]["digest"],
    }.items():
        html = html.replace(token, str(value))
    return html


def comparable(document):
    """The parts a fresh generation must reproduce; provenance of the run is not one."""
    return {key: document[key] for key in ("schema", "model", "counts", "nodes", "edges", "mentions")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the committed JSON is stale")
    args = parser.parse_args()
    document = build()
    if args.check:
        if not OUT_JSON.exists() or not OUT_HTML.exists():
            print("missing generated graph files; run scripts/skill_graph.py", file=sys.stderr)
            return 1
        current = json.loads(OUT_JSON.read_text())
        if comparable(current) != comparable(document):
            print("skill-graph.json is stale; regenerate it", file=sys.stderr)
            return 1

        def normalize(html):
            return re.sub(r"source <code>[^<]*</code>", "source <code>COMMIT</code>", html)

        if normalize(OUT_HTML.read_text()) != normalize(render(document)):
            print("skill-graph.html is stale; regenerate it", file=sys.stderr)
            return 1
        print("skill graph is current")
        return 0
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(document, indent=1) + "\n")
    OUT_HTML.write_text(render(document))
    print(f"wrote {OUT_JSON.relative_to(ROOT)} ({OUT_JSON.stat().st_size:,} bytes)")
    print(f"wrote {OUT_HTML.relative_to(ROOT)} ({OUT_HTML.stat().st_size:,} bytes)")
    print(json.dumps(document["counts"], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
