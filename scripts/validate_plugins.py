#!/usr/bin/env python3
"""Validate packages using bundled official 1.0.0 schemas, skill metadata and containment."""
import json
from pathlib import Path
import re
import sys

import jsonschema
import yaml

try:
    from upstream_sources import load_sources
    from skill_metadata import validate_skill_metadata
except ModuleNotFoundError:
    from scripts.upstream_sources import load_sources
    from scripts.skill_metadata import validate_skill_metadata

ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[str]:
    failures = []
    manifests = sorted((ROOT / "plugins").glob("*/plugin.json"))
    if not manifests:
        failures.append("No plugin packages found")
    schemas = {name: json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
               for name in ("plugin", "mcp")}
    sources = load_sources(ROOT)
    managed = {source['destination'] for source in sources}
    names = set()
    for manifest in manifests:
        package = manifest.parent.resolve()
        try:
            metadata = json.loads(manifest.read_text())
            jsonschema.validate(metadata, schemas["plugin"])
            name = metadata["name"]
            if name in names:
                raise ValueError(f"Duplicate plugin name {name}")
            names.add(name)
            if not (package / "LICENSE").is_file():
                raise ValueError("Missing package LICENSE for local material")
            for path in package.rglob("*"):
                if not path.resolve().is_relative_to(package):
                    raise ValueError(f"Escaping package path: {path}")
            mcp = package / "mcp.json"
            if mcp.exists():
                config = json.loads(mcp.read_text())
                jsonschema.validate(config, schemas["mcp"])
                for name, server in config["mcpServers"].items():
                    if {"PLUGIN_ROOT", "PLUGIN_DATA"} & set(server.get("env", {})):
                        raise ValueError(f"Reserved MCP environment variable: {name}")
                    for field in ("command", "cwd"):
                        value = server.get(field, "")
                        if value.startswith("./") and not (package / value).resolve().is_relative_to(package):
                            raise ValueError(f"Escaping MCP {field}: {name}")
            skill_names = set()
            for skill in sorted((package / "skills").glob("*/SKILL.md")):
                if skill.parent.relative_to(ROOT.resolve()).as_posix() in managed:
                    # Raw upstream metadata is preserved; validate the adapted result at build time.
                    continue
                frontmatter = validate_skill_metadata(skill)
                skill_name = frontmatter['name']
                if skill_name in skill_names:
                    raise ValueError(f"Skill folder/name mismatch or duplicate: {skill}")
                skill_names.add(skill_name)
        except (ValueError, TypeError, KeyError, jsonschema.ValidationError, yaml.YAMLError) as error:
            failures.append(f"{manifest.relative_to(ROOT)}: {error}")
    for source in sources:
        if source['plugin'] not in names:
            failures.append('Unknown upstream plugin')
        if not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
            failures.append('Unpinned upstream commit')
        if not source.get('license'):
            failures.append('Missing upstream license')
    return failures


if __name__ == "__main__":
    failures = validate()
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Plugin manifests, licenses, skill metadata, upstream pins and package containment passed.")
