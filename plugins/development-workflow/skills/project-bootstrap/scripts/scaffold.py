#!/usr/bin/env python3
"""Create project governance in a new/empty directory; never overwrite a project."""
import argparse
import json
from pathlib import Path
import shutil


def scaffold(destination: Path, ai: str = "none", mcp: bool = False, starter: bool = False) -> None:
    if ai not in {"none", "adk", "langchain"}:
        raise ValueError("Unsupported AI profile")
    if destination.is_symlink():
        raise ValueError("Destination must not be a symlink")
    destination = destination.resolve()
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("Destination must be a new or empty directory; adopt existing projects manually")
    assets = Path(__file__).resolve().parent.parent / "assets" / "project"
    shutil.copytree(assets, destination, dirs_exist_ok=True)
    if starter:
        shutil.copytree(assets.parent / "starter", destination, dirs_exist_ok=True)
    for folder in ("applications/api/src", "applications/api/tests", "applications/api/migrations",
                   "applications/api/ci", "applications/web/src", "applications/web/tests",
                   "applications/web/ci", "applications/tooling"):
        (destination / folder).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("check_project.py"),
                    destination / "applications/tooling/check_project.py")
    shutil.copyfile(Path(__file__).with_name("inventory_skills.py"),
                    destination / "applications/tooling/inventory_skills.py")
    path = destination / "project-profile.json"
    profile = json.loads(path.read_text())
    profile["stack"].update(ai=ai, mcp=mcp)
    path.write_text(json.dumps(profile, indent=2) + "\n")
    if ai != "none" and not starter:
        (destination / "applications/api/src/ai").mkdir()
        (destination / "documentation/verification/ai-evaluations.md").write_text(
            "# AI evaluation\n\nStatus: pending implementation\n\n"
            "## Fixtures and acceptance metrics\n\n## Live Gemini configuration\n\n"
            "Verify selected LLM/audio models, free-tier eligibility and quota. Never auto-upgrade to paid usage.\n\n"
            "## Dataset, results, limitations and review triggers\n")
        with (destination / "documentation/README.md").open("a") as index:
            index.write("\n- [AI evaluations](verification/ai-evaluations.md)\n")
    if mcp:
        (destination / "applications/api/src/mcp").mkdir()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--ai", choices=["none", "adk", "langchain"], default="none")
    parser.add_argument("--mcp", action="store_true")
    parser.add_argument("--starter", action="store_true", help="Include the runnable reference application and locked dependencies")
    args = parser.parse_args()
    try:
        scaffold(args.destination, args.ai, args.mcp, args.starter)
    except ValueError as error:
        parser.exit(2, f"{error}\n")
    print(f"Created: {args.destination.resolve()} ({'reference application; run verification' if args.starter else 'application implementation pending'})")
