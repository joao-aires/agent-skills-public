#!/usr/bin/env python3
"""Check the seven-section Markdown ECR shape; not semantic correctness."""
import argparse
import json
from pathlib import Path
import re
import sys

SECTIONS = (
    "Overview and lifecycle",
    "Problem and scope",
    "Requirements and acceptance",
    "Solution design",
    "Implementation strategy",
    "Verification and release",
    "Decision history and references",
)
HEADING = re.compile(r"^#{2,4}\s+([1-7])\.\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*('''|\`\`\`|~~~)")
DISPOSITION = re.compile(r"^\s*(not applicable|blocked)\s*[:\u2014\u2013-]\s*(.*)$", re.I)


def normalize(value):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower().replace("&", "and"))).strip()


def validate(markdown):
    """Return diagnostics for shape only. No authorization/quality claims."""
    found = []
    active = None
    fenced = None
    for line_no, line in enumerate(markdown.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            tag = marker.group(1)
            if fenced is None:
                fenced = tag
            elif fenced == tag:
                fenced = None
            continue
        if fenced is not None:
            continue
        match = HEADING.match(line)
        if match:
            if active is not None:
                found.append(active)
            active = {"number": int(match.group(1)), "name": match.group(2),
                      "line": line_no, "body": []}
        elif active is not None:
            active["body"].append(line)
    if active is not None:
        found.append(active)

    diagnostics = []
    numbers = [section["number"] for section in found]
    if numbers != list(range(1, 8)):
        diagnostics.append(
            f"Expected seven unique numbered sections 1-7 in order; got {numbers!r}."
        )
    for section in found:
        number = section["number"]
        expected = SECTIONS[number - 1]
        if normalize(section["name"]) != normalize(expected):
            diagnostics.append(
                f"Line {section['line']}: section {number} should be '{expected}'."
            )
        body = "\n".join(section["body"]).strip()
        if not body:
            diagnostics.append(f"Line {section['line']}: section {number} is empty.")
            continue
        if body.lower().strip(" .:\u2014\u2013-") in ("todo", "tbd", "n/a", "[todo]", "[tbd]"):
            diagnostics.append(
                f"Line {section['line']}: section {number} needs content or an explicit Pending/Not applicable disposition."
            )
        disposition = DISPOSITION.match(body)
        if disposition and not disposition.group(2).strip():
            diagnostics.append(
                f"Line {section['line']}: {disposition.group(1)} needs a reason."
            )
    return diagnostics


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ecr", type=Path, help="Path to an authorized Markdown ECR")
    parser.add_argument("--json", action="store_true", help="Print machine-readable diagnostics")
    args = parser.parse_args(argv)
    try:
        content = args.ecr.read_text(encoding="utf-8")
    except OSError as exc:
        diagnostics = [f"Cannot read ECR: {exc}"]
    else:
        diagnostics = validate(content)
    if args.json:
        print(json.dumps({"ok": not diagnostics, "diagnostics": diagnostics}, indent=2))
    elif diagnostics:
        for problem in diagnostics:
            print(problem, file=sys.stderr)
    else:
        print(f"ECR shape OK: {args.ecr} (seven sections; not a semantic check)")
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
