#!/usr/bin/env python3
"""Validate packages using bundled official 1.0.0 schemas, skill metadata and containment."""
import json
from pathlib import Path
import re
import sys

import jsonschema
import yaml

try:
    from skill_metadata import validate_skill_metadata
except ModuleNotFoundError:
    from scripts.skill_metadata import validate_skill_metadata

ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[str]:
    failures = []
    manifests = sorted((ROOT / "plugins").glob("*/plugin.json"))
    if not manifests:
        failures.append("No plugin packages found")
    schemas = {name: json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
               for name in ("plugin", "mcp")}
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
                frontmatter = validate_skill_metadata(skill)
                skill_name = frontmatter['name']
                if skill_name in skill_names:
                    raise ValueError(f"Skill folder/name mismatch or duplicate: {skill}")
                manual = frontmatter.get("disable-model-invocation", False)
                client_metadata = skill.parent / "agents/openai.yaml"
                if client_metadata.exists():
                    settings = yaml.safe_load(client_metadata.read_text())
                    implicit = settings.get("policy", {}).get("allow_implicit_invocation", True)
                    if not isinstance(implicit, bool) or (manual and implicit):
                        raise ValueError(f"Conflicting invocation metadata: {skill}")
                skill_names.add(skill_name)
        except (ValueError, TypeError, KeyError, jsonschema.ValidationError, yaml.YAMLError) as error:
            failures.append(f"{manifest.relative_to(ROOT)}: {error}")
    lock = json.loads((ROOT / "upstream.lock.json").read_text())
    for source in lock["sources"]:
        if source["plugin"] not in names:
            failures.append("Unknown upstream plugin")
        for field in ("commit", "tree"):
            if not re.fullmatch(r"[0-9a-f]{40}", source[field]):
                failures.append("Unpinned upstream " + field)
        for field in ("path", "license_path"):
            value = source.get(field)
            if value and (Path(value).is_absolute() or ".." in Path(value).parts):
                failures.append("Escaping upstream " + field)
        if not source.get("license"):
            failures.append("Missing upstream license")
    return failures


if __name__ == "__main__":
    failures = validate()
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Plugin manifests, skill metadata, upstream pins and package containment passed.")
