#!/usr/bin/env python3
"""Check structural conventions only; semantic review and application tests remain necessary."""
import argparse
import json
from pathlib import Path
import re

REQUIRED = (
    "AGENTS.md", "README.md", "project-profile.json", "applications/AGENTS.md",
    "applications/api/AGENTS.md", "applications/web/AGENTS.md", "documentation/AGENTS.md",
    "documentation/README.md", "documentation/product/prd.md", "documentation/product/roadmap.md",
    "documentation/plans/feature-template.md", "documentation/architecture/overview.md",
    "documentation/architecture/c4/context.md", "documentation/architecture/c4/containers.md",
    "documentation/architecture/data-model.md", "documentation/architecture/schemas/README.md",
    "documentation/decisions/decision-log.md", "documentation/decisions/adr/template.md",
    "documentation/ux/design-system.md", "documentation/operations/runbook.md",
    "documentation/verification/strategy.md", "documentation/verification/traceability.md",
    "applications/tooling/check_project.py",
    "documentation/engineering/agent-harness.md", "documentation/engineering/lessons.md",
    "documentation/verification/e2e.md", "documentation/operations/delivery.md",
    "documentation/operations/observability.md", "documentation/architecture/security.md",
)


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing file: {relative}")
        elif not path.resolve().is_relative_to(root):
            errors.append(f"File escapes project: {relative}")
    try:
        profile = json.loads((root / "project-profile.json").read_text())
        if not isinstance(profile, dict) or profile.get("profile_version") != 1:
            raise ValueError("expected profile_version 1")
        if profile.get("layout") != {"applications": "applications", "documentation": "documentation"}:
            errors.append("Profile must use applications/ and documentation/")
        stack = profile.get("stack")
        if not isinstance(stack, dict):
            raise ValueError("stack must be an object")
        for key, required in {
            "backend": {"python", "fastapi", "uvicorn", "sqlalchemy", "alembic", "postgresql"},
            "frontend": {"nextjs", "typescript", "shadcn", "tailwind"},
        }.items():
            values = stack.get(key)
            if not isinstance(values, list) or not all(isinstance(x, str) for x in values):
                errors.append(f"stack.{key} must be a string array")
            elif not required.issubset(values):
                errors.append(f"stack.{key} is missing approved defaults; record and review a profile change")
        if stack.get("ai") not in {"none", "adk", "langchain"}:
            errors.append("Invalid AI framework selection")
        if not isinstance(stack.get("mcp"), bool):
            errors.append("stack.mcp must be boolean")
        if stack.get("ai") in {"adk", "langchain"} and not (root / "documentation/verification/ai-evaluations.md").is_file():
            errors.append("AI profile requires ai-evaluations.md")
        checks = profile.get("checks")
        if not isinstance(checks, dict) or not checks:
            errors.append("checks must be a nonempty object")
        else:
            for name, command in checks.items():
                if not isinstance(command, list) or not command or not all(isinstance(x, str) and x for x in command):
                    errors.append(f"Check {name} must be a nonempty argument array")
        readiness = profile.get("readiness")
        if readiness not in {"scaffold", "implemented", "deployed", "production"}:
            errors.append("readiness must be scaffold, implemented, deployed or production")
        testing = profile.get("testing")
        if not isinstance(testing, dict):
            errors.append("testing must describe the E2E contract")
        else:
            expected = {"e2e_runner": "playwright", "internal_api": "real", "database": "postgresql"}
            for key, value in expected.items():
                if testing.get(key) != value:
                    errors.append(f"testing.{key} must be {value} for this full-stack profile")
            journeys = testing.get("critical_journeys")
            if not isinstance(journeys, list) or not all(isinstance(x, str) and x.strip() for x in journeys):
                errors.append("testing.critical_journeys must be a string array")
            elif readiness in {"implemented", "deployed", "production"} and not journeys:
                errors.append("Implemented applications require explicit critical E2E journeys")
        if readiness in {"implemented", "deployed", "production"}:
            required_checks = {"setup", "dev", "e2e-critical", "api-tests", "web-build"}
            if readiness in {"deployed", "production"}:
                required_checks.add("deploy-smoke")
            configured = set(checks) if isinstance(checks, dict) else set()
            for missing in sorted(required_checks - configured):
                errors.append(f"Readiness {readiness} requires configured check: {missing}")
    except (OSError, ValueError, TypeError) as error:
        errors.append(f"Invalid project profile: {error}")
    docs = root / "documentation"
    for path in docs.rglob("*.md") if docs.is_dir() else []:
        if not path.resolve().is_relative_to(root):
            errors.append(f"Document escapes project: {path.relative_to(root)}")
            continue
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = link.split("#", 1)[0]
            resolved = (root / target.lstrip("/") if target.startswith("/") else path.parent / target).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"Broken or escaping local link: {path.relative_to(root)} -> {link}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()
    failures = check(args.root)
    for failure in failures:
        print(failure)
    if failures:
        raise SystemExit(1)
    print("Structural conventions passed. Application checks and semantic documentation review still required.")
