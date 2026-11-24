"""Validate the declared relationships between skills.

Three checks, all decidable from the files:

- routers: explicit-only, user-invocable, targets exist, targets are model-invoked,
  and no router points at another router;
- composition: backticked capability names and skill links under `## Composition`
  resolve, and names stay inside their package;
- handoff coverage: every lifecycle phase has a row in the phase handoff matrix,
  and every label in that matrix resolves to a work state or a declared wildcard.

`skill_graph.py` reuses the parsers here so the validator and the generated graph
cannot disagree about what a declaration means.
"""
import re
from pathlib import Path

import yaml

try:
    from skill_schema import PHASES
except ModuleNotFoundError:
    from scripts.skill_schema import PHASES

ROUTER_CALL = re.compile(r"Call the Skill tool[^\n]*")
QUOTED = re.compile(r'"([A-Za-z0-9][A-Za-z0-9-]*)"')
BACKTICK_NAME = re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)*)`")
SKILL_LINK = re.compile(r"\]\(([^)\s]+)")

WORK_ORDER = [
    "planning", "requirements", "design", "implementation",
    "testing", "deployment", "maintenance", "incident", "postmortem",
]
WORK_KIND = {name: ("phase" if index < 7 else "boundary") for index, name in enumerate(WORK_ORDER)}

# Matrix label -> work state. Compound cells are split on "/".
WORK_LABELS = {
    "planning": "planning",
    "project planning": "planning",
    "requirements": "requirements",
    "requirements analysis": "requirements",
    "design": "design",
    "design validation": "design",
    "implementation preparation": "implementation",
    "implementation": "implementation",
    "testing": "testing",
    "verification and review": "testing",
    "deployment": "deployment",
    "release": "deployment",
    "maintenance": "maintenance",
    "operations": "maintenance",
    "operate": "maintenance",
    "incident": "incident",
    "incident / learning": "incident",
    "postmortem": "postmortem",
}

# Labels that are deliberately not a work state: a wildcard boundary.
WORK_WILDCARDS = {"any reopen", "earlier phase"}


def line_of(text, position):
    return text[:position].count("\n") + 1


def load_skills(root):
    skills = {}
    for path in sorted((root / "plugins").glob("*/skills/*/SKILL.md")):
        text = path.read_text()
        parts = text.split("---", 2)
        body = parts[2] if len(parts) == 3 else ""
        frontmatter = {}
        error = None
        if len(parts) == 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError as problem:
                error = f"{path.relative_to(root)}: invalid frontmatter ({problem})"
        if not isinstance(frontmatter, dict):
            error = error or f"{path.relative_to(root)}: frontmatter is not a mapping"
            frontmatter = {}
        skills[path.parent.name] = {
            "path": path,
            "package": path.relative_to(root).parts[1],
            "frontmatter": frontmatter,
            "body": body,
            "error": error,
        }
    return skills


def router_targets(body):
    """Return every skill named after "Call the Skill tool" in the body."""
    targets = []
    for match in ROUTER_CALL.finditer(body):
        for target in QUOTED.findall(match.group(0)):
            if target not in targets:
                targets.append(target)
    return targets


def router_declarations(body):
    """Return (target, line) for each router target, for provenance."""
    found = []
    for match in ROUTER_CALL.finditer(body):
        for target in QUOTED.findall(match.group(0)):
            found.append((target, line_of(body, match.start())))
    return found


def composition_section(body):
    """Return the text under `## Composition`, or an empty string."""
    lines = body.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == "## Composition":
            start = index + 1
            break
    if start is None:
        return ""
    collected = []
    for line in lines[start:]:
        if re.match(r"^##\s", line):
            break
        collected.append(line)
    return "\n".join(collected)


def composition_names(body):
    return BACKTICK_NAME.findall(composition_section(body))


def skill_links(text, base, known):
    """Resolve relative SKILL.md links to skill ids, excluding self-links."""
    found = []
    for match in SKILL_LINK.finditer(text):
        link = match.group(1).split("#")[0].strip("<>")
        if not link or link.startswith(("http", "mailto", "file:")):
            continue
        target = (base / link).resolve()
        if target.name == "SKILL.md" and target.parent.name in known:
            if target.parent.name != base.name:
                found.append((target.parent.name, line_of(text, match.start())))
    return found


def work_targets(label):
    """Resolve a handoff matrix label, including compound "a / b" cells."""
    normalized = label.strip().lower().strip("`")
    if normalized in WORK_LABELS:
        return [WORK_LABELS[normalized]]
    targets = []
    for part in normalized.split("/"):
        target = WORK_LABELS.get(part.strip())
        if target and target not in targets:
            targets.append(target)
    return targets


def is_explicit_only(skill):
    return skill["frontmatter"].get("disable-model-invocation") is True


def is_user_invocable(skill):
    return skill["frontmatter"].get("user-invocable", True) is not False


def validate_routers(root, skills):
    failures = [skill["error"] for skill in skills.values() if skill["error"]]
    routers = {name for name, skill in skills.items() if router_targets(skill["body"])}
    for name in sorted(routers):
        skill = skills[name]
        path = skill["path"].relative_to(root)
        if not is_explicit_only(skill):
            failures.append(f"{path}: router {name} must set disable-model-invocation: true")
        if not is_user_invocable(skill):
            failures.append(f"{path}: router {name} must stay user-invocable")
        for target in router_targets(skill["body"]):
            if target == name:
                failures.append(f"{path}: router {name} targets itself")
            elif target not in skills:
                failures.append(f"{path}: router {name} targets unknown skill {target}")
            else:
                if is_explicit_only(skills[target]):
                    failures.append(f"{path}: router {name} targets explicit-only skill {target}")
                if target in routers:
                    failures.append(f"{path}: router {name} chains to router {target}")
    return failures


def validate_compositions(root, skills):
    """Names and links under `## Composition` must resolve inside the package."""
    failures = []
    for name in sorted(skills):
        skill = skills[name]
        path = skill["path"].relative_to(root)
        for target in composition_names(skill["body"]):
            # A lone lowercase word is a tool or a command; capability ids are kebab-case.
            if "-" not in target and target not in skills:
                continue
            if target not in skills:
                failures.append(f"{path}: composition names unknown capability {target}")
            elif skills[target]["package"] != skill["package"]:
                failures.append(
                    f"{path}: composition names cross-package capability {target}; "
                    "describe the capability area instead"
                )
        section = composition_section(skill["body"])
        for target, _ in skill_links(section, skill["path"].parent, set(skills)):
            if skills[target]["package"] != skill["package"]:
                failures.append(
                    f"{path}: composition links cross-package capability {target}; "
                    "describe the capability area instead"
                )
    return failures


def handoff_rows(root):
    """Return (from, to, line) for each row of the phase handoff matrix."""
    path = root / "plugins/sdlc/skills/artifact-system/references/handoff.md"
    if not path.exists():
        return []
    rows = []
    in_matrix = False
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("## "):
            in_matrix = line.strip() == "## Phase handoff matrix"
            continue
        if not in_matrix or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] == "From" or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append((cells[0], cells[1], number))
    return rows


def validate_handoff_coverage(root):
    package = root / "plugins/sdlc/skills/artifact-system"
    if not package.exists():
        # A synthetic package fixture has no lifecycle; the real collection does.
        return []
    path = package / "references/handoff.md"
    if not path.exists():
        return [f"missing handoff matrix: {path.relative_to(root)}"]
    rows = handoff_rows(root)
    if not rows:
        return ["handoff matrix not found or empty"]
    failures = []
    reached = set()
    for source_label, target_label, number in rows:
        source = work_targets(source_label)
        target = work_targets(target_label)
        if not source and source_label.strip().lower() not in WORK_WILDCARDS:
            failures.append(
                f"handoff row {number}: {source_label!r} is not a work state or wildcard"
            )
        if not target and target_label.strip().lower() not in WORK_WILDCARDS:
            failures.append(
                f"handoff row {number}: {target_label!r} is not a work state or wildcard"
            )
        reached.update(source)
    for phase in sorted(PHASES - {"cross-phase"}):
        if phase not in reached:
            failures.append(f"phase {phase} has no row in the phase handoff matrix")
    return failures


def validate_relationships(root):
    skills = load_skills(root)
    return (
        validate_routers(root, skills)
        + validate_compositions(root, skills)
        + validate_handoff_coverage(root)
    )
