#!/usr/bin/env python3
"""Compatibility skills-only installer; never replace unrelated links."""
import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def managed(destination: Path, name: str, source: Path) -> bool:
    if not destination.is_symlink():
        return False
    target = (destination.parent / os.readlink(destination)).resolve()
    return target in {source.resolve(), (ROOT / "skills" / name).resolve()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", nargs="?", default="sync")
    parser.add_argument("skill", nargs="?", default="all")
    args = parser.parse_args()
    if args.action not in {"sync", "status", "remove"}:
        args.skill, args.action = args.action, "sync"
    sources = {path.parent.name: path.parent for path in sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md"))}
    if args.skill != "all":
        if args.skill not in sources:
            parser.error(f"Unknown skill: {args.skill}")
        sources = {args.skill: sources[args.skill]}
    target = Path.home() / ".agents" / "skills"
    if args.action == "sync":
        target.mkdir(parents=True, exist_ok=True)
    for name, source in sources.items():
        destination = target / name
        owned = managed(destination, name, source)
        if args.action == "status":
            print(f"{name}: {'managed' if owned else 'unmanaged or absent'}")
        elif args.action == "remove":
            if owned:
                destination.unlink()
                print(f"Removed {name}")
        elif destination.exists() or destination.is_symlink():
            if owned:
                destination.unlink()
                destination.symlink_to(os.path.relpath(source, target))
                print(f"Updated {name}")
            else:
                print(f"Skipped {name}: unrelated path exists")
        else:
            destination.symlink_to(os.path.relpath(source, target))
            print(f"Linked {name}")


if __name__ == "__main__":
    main()
