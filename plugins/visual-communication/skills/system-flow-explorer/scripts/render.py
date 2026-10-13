#!/usr/bin/env python3
"""Render validated JSON into a standalone HTML; Python stdlib only."""
import argparse
import json
from pathlib import Path
from validate import ModelError, load, validate


def render(data):
    validate(data)
    template = (Path(__file__).resolve().parents[1] / "assets" / "explorer.html").read_text(encoding="utf-8")
    marker = "__FLOW_MODEL_JSON__"
    if template.count(marker) != 1:
        raise ModelError("template must have exactly one data marker")
    encoded = json.dumps(data, ensure_ascii=True, allow_nan=False, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return template.replace(marker, encoded)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model")
    parser.add_argument("output")
    args = parser.parse_args()
    try:
        model_path, output = Path(args.model), Path(args.output)
        if model_path.resolve() == output.resolve():
            raise ModelError("output must differ from input")
        if not output.parent.is_dir():
            raise ModelError("output parent directory must already exist")
        artifact = render(load(model_path))
        output.write_text(artifact, encoding="utf-8")
    except (ModelError, json.JSONDecodeError, OSError) as error:
        parser.exit(1, f"RENDER FAILED: {error}\n")
    print(f"RENDERED: {output} ({len(artifact.encode('utf-8'))} bytes; model validated)")


if __name__ == "__main__":
    main()
