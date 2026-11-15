#!/usr/bin/env python3
"""Small local task tracker used as an existing-feature evaluation fixture."""
import json
import os
import sys
from pathlib import Path


def data_path() -> Path:
    return Path(os.environ.get("TASKCLI_DATA", "tasks.json"))


def load():
    path = data_path()
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save(tasks):
    data_path().write_text(json.dumps(tasks, indent=2))


def _normalize_tag(tag: str) -> str:
    """Return the canonical form of one tag or raise ValueError."""
    if not isinstance(tag, str):
        raise ValueError("tag must be text")
    value = tag.strip()
    if value.startswith("#"):
        value = value[1:].strip()
    value = value.lower()
    if not value:
        raise ValueError("tag cannot be empty")
    return value


def _normalize_tags(tags) -> list:
    """Normalize one tag, an iterable of tags or a comma-separated value."""
    if tags is None:
        return []
    if isinstance(tags, str):
        tags = [tags]
    normalized = []
    for raw in tags:
        if not isinstance(raw, str):
            raise ValueError("tag must be text")
        for part in raw.split(","):
            tag = _normalize_tag(part)
            if tag not in normalized:
                normalized.append(tag)
    return normalized


def task_tags(task) -> list:
    """Read tags from a task, tolerating records written before tags existed."""
    tags = task.get("tags", [])
    if not isinstance(tags, list):
        return []
    return [tag for tag in tags if isinstance(tag, str)]


def _task_tag_set(task) -> set:
    result = set()
    for tag in task_tags(task):
        try:
            result.add(_normalize_tag(tag))
        except ValueError:
            continue
    return result


def add(title: str, tags=None):
    tasks = load()
    tasks.append({"title": title, "done": False, "tags": _normalize_tags(tags)})
    save(tasks)
    return len(tasks) - 1


def list_tasks(include_done: bool = False, tag=None):
    tasks = load()
    wanted = _normalize_tag(tag) if tag is not None else None
    selected = []
    for index, task in enumerate(tasks):
        if not include_done and task["done"]:
            continue
        if wanted is not None and wanted not in _task_tag_set(task):
            continue
        selected.append((index, task))
    return selected


def done(index: int):
    tasks = load()
    if index < 0 or index >= len(tasks):
        raise IndexError(index)
    tasks[index]["done"] = True
    save(tasks)
    return tasks[index]


def _parse_tag_args(argv):
    """Split arguments into positional values and --tag/--tag= values."""
    positional = []
    tags = []
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--tag":
            if index + 1 >= len(argv):
                return positional, tags, "option --tag requires a value"
            tags.append(argv[index + 1])
            index += 2
        elif arg.startswith("--tag="):
            tags.append(arg[len("--tag="):])
            index += 1
        else:
            positional.append(arg)
            index += 1
    return positional, tags, None


def main(argv):
    if not argv:
        print("usage: taskcli.py add|list|done ...")
        return 1
    command = argv[0]
    if command == "add":
        positional, tag_values, error = _parse_tag_args(argv[1:])
        if error:
            print(error)
            return 1
        if not positional:
            print("usage: taskcli.py add <title> [--tag <tag> ...]")
            return 1
        try:
            index = add(" ".join(positional), tag_values)
        except ValueError as exc:
            print(f"invalid tag: {exc}")
            return 1
        print(f"added {index}")
    elif command == "list":
        positional, tag_values, error = _parse_tag_args(argv[1:])
        if error:
            print(error)
            return 1
        if len(tag_values) > 1:
            print("list accepts a single --tag")
            return 1
        try:
            tag = _normalize_tag(tag_values[0]) if tag_values else None
        except ValueError as exc:
            print(f"invalid tag: {exc}")
            return 1
        for index, task in list_tasks("--all" in positional, tag):
            mark = "x" if task["done"] else " "
            print(f"{index}\t{mark}\t{task['title']}")
    elif command == "done" and len(argv) >= 2:
        task = done(int(argv[1]))
        print(f"done {task['title']}")
    else:
        print("unknown command")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
