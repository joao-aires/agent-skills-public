#!/usr/bin/env python3
"""Check maintained links, selected/all inventories and independently packaged resources."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def prose(text):
    """Exclude fenced examples from documentation links and headings."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker[1]
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    counts, result = Counter(), set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading).lower().replace(" ", "-")
        slug = "".join(c for c in heading if c in "-_" or unicodedata.category(c)[0] in "LN")
        number = counts[slug]
        counts[slug] += 1
        result.add(slug + (f"-{number}" if number else ""))
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return result


def maintained_documents(root):
    return sorted({root / "README.md", root / "AGENTS.md",
                   *(root / "documentation").rglob("*.md"), *root.glob("plugins/*/*.md"),
                   *root.glob("plugins/*/skills/*/SKILL.md")})


def check_links(root):
    errors, checked = [], 0
    for document in maintained_documents(root):
        body = prose(document.read_text())
        # Inline links/images and reference definitions. External URLs are not fetched.
        targets = re.findall(r"!?\[[^]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", body)
        targets += re.findall(r"^\s*\[[^]]+\]:\s*<?([^\s>]+)>?", body, re.M)
        for value in targets:
            link = urlsplit(value.strip("<>"))
            if link.scheme or link.netloc:
                continue
            target = (document.parent / unquote(link.path)).resolve() if link.path else document
            checked += 1
            if not target.exists():
                errors.append(f"{document.relative_to(root)}: missing {value}")
            elif link.fragment and target.suffix == ".md" and unquote(link.fragment) not in anchors(target.read_text()):
                errors.append(f"{document.relative_to(root)}: missing heading {value}")
    # Migration is the maintained rename map. Historical selection notes are exempt.
    migration = (root / "documentation/migration.md").read_text()
    old_names = set()
    for row in migration.splitlines():
        if row.startswith("| `") or row.startswith("| Standalone `"):
            old_names.update(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", row.split("|")[1]))
    current = {p.parent.name for p in root.glob("plugins/*/skills/*/SKILL.md")}
    for document in maintained_documents(root):
        if document.name in {"migration.md", "maintainer-reference.md"}:
            continue
        for old in old_names - current:
            if f"`{old}`" in prose(document.read_text()):
                errors.append(f"{document.relative_to(root)}: obsolete skill name {old}")
    return errors, checked


def check_package_links(package, local_names, notices):
    """Check owned Markdown resource closure without interpreting upstream examples as files."""
    errors, checked, seen = [], 0, set()
    package = package.resolve()
    queue = [*package.glob("*.md"), *(package / "skills" / n / "SKILL.md" for n in local_names)]
    framing = {
        "workflow-framing": ["../../WORKFLOW.md"],
        "composition-framing": ["../../COMPOSITION.md"],
        "frontend-framing": ["../frontend-conventions/SKILL.md"],
        "backend-framing": ["../backend-conventions/SKILL.md"],
        "ai-framing": ["../ai-conventions/SKILL.md"],
        "implementation-entrypoint": ["../../TASKS.md", "../git-contributions/SKILL.md", "../deliver-reliable-changes/SKILL.md"],
    }
    for notice in notices:
        skill = package / "skills" / notice["installed_skill"]
        for adaptation in notice.get("adaptations", []):
            for resource in framing.get(adaptation, []):
                target = (skill / resource).resolve()
                checked += 1
                if not target.is_relative_to(package) or not target.is_file():
                    errors.append(f"{package.name}: missing/escaping adaptation resource {skill.name}/{resource}")
    while queue:
        document = queue.pop()
        if document in seen or not document.is_file():
            continue
        seen.add(document)
        body = prose(document.read_text())
        targets = re.findall(r"!?\[[^]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", body)
        targets += re.findall(r"^\s*\[[^]]+\]:\s*<?([^\s>]+)>?", body, re.M)
        for value in targets:
            link = urlsplit(value.strip("<>"))
            if link.scheme or link.netloc:
                continue
            target = (document.parent / unquote(link.path)).resolve() if link.path else document
            checked += 1
            if not target.is_relative_to(package):
                errors.append(f"{package.name}: resource escapes package: {document.relative_to(package)} -> {value}")
            elif not target.exists():
                errors.append(f"{package.name}: missing resource: {document.relative_to(package)} -> {value}")
            elif target.suffix == ".md":
                if link.fragment and unquote(link.fragment) not in anchors(target.read_text()):
                    errors.append(f"{package.name}: missing resource heading: {document.relative_to(package)} -> {value}")
                queue.append(target)
    return errors, checked


def check_built(root, built, selected=None):
    errors = []
    packages = {p.name for p in (root / "plugins").iterdir() if (p / "plugin.json").exists()}
    if selected is not None:
        unknown = set(selected) - packages
        if unknown:
            errors.append(f"Unknown selected plugins: {sorted(unknown)}")
        packages = set(selected)
    actual = {p.name for p in built.iterdir() if p.is_dir()}
    if actual != packages:
        errors.append(f"Built plugins differ: missing={sorted(packages-actual)}, extra={sorted(actual-packages)}")
    sources = json.loads((root / "upstream.lock.json").read_text())["sources"]
    names = []
    for plugin in sorted(packages & actual):
        source, target = root / "plugins" / plugin, built / plugin
        for path in source.rglob("*"):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
                continue
            copy = target / path.relative_to(source)
            if path.name == "plugin.json":
                expected = json.loads(path.read_text())
                if any(s["plugin"] == plugin for s in sources):
                    expected["license"] = "LicenseRef-Mixed"
                if not copy.exists() or json.loads(copy.read_text()) != expected:
                    errors.append(f"{plugin}: changed/missing plugin manifest")
            elif not copy.exists() or copy.read_bytes() != path.read_bytes():
                errors.append(f"{plugin}: changed/missing local resource {path.relative_to(source)}")
        notice_path = target / "UPSTREAM-NOTICES.json"
        if not notice_path.exists():
            errors.append(f"{plugin}: missing upstream notices")
            continue
        notices = json.loads(notice_path.read_text())
        expected_sources = [s for s in sources if s["plugin"] == plugin]
        recorded_sources = [{k: v for k, v in n.items() if k != "installed_skill"} for n in notices]
        if Counter(map(lambda s: json.dumps(s, sort_keys=True), expected_sources)) != Counter(map(lambda s: json.dumps(s, sort_keys=True), recorded_sources)):
            errors.append(f"{plugin}: notices differ from lockfile")
        local = {p.parent.name for p in source.glob("skills/*/SKILL.md")}
        upstream = {n["installed_skill"] for n in notices}
        expected_names = local | upstream
        actual_names = {p.name for p in (target / "skills").iterdir() if p.is_dir()}
        if expected_names != actual_names or local & upstream or len(upstream) != len(notices):
            errors.append(f"{plugin}: skill inventory differs or collides")
        for notice in notices:
            skill = target / "skills" / notice["installed_skill"]
            record = skill / "UPSTREAM.json"
            if not (skill / "SKILL.md").exists() or not record.exists() or json.loads(record.read_text()) != notice:
                errors.append(f"{plugin}: incomplete upstream skill {skill.name}")
            if notice["license_path"] and not (skill / "UPSTREAM-LICENSE.txt").is_file():
                errors.append(f"{plugin}: missing upstream license {skill.name}")
        package_errors, _ = check_package_links(target, local, notices)
        errors.extend(package_errors)
        names.extend(actual_names)
    duplicates = [name for name, count in Counter(names).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate installed skill names: {sorted(duplicates)}")
    return errors, len(names)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--built", type=Path, help="Fresh build to check against source; all plugins unless --plugin is supplied")
    parser.add_argument("--plugin", action="append", help="Expected plugin in a selected build; repeatable, requires --built")
    args = parser.parse_args()
    if args.plugin and not args.built:
        parser.error('--plugin requires --built')
    errors, count = check_links(ROOT)
    print(f"Checked {count} maintained relative links/anchors and migration names")
    if args.built:
        build_errors, skills = check_built(ROOT, args.built.resolve(), args.plugin)
        errors.extend(build_errors)
        print(f"Checked built inventory, local resources and package closure: {skills} skills")
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    main()
