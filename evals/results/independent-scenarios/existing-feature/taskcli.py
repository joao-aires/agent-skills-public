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


def normalize_tags(tags):
    if tags is None:
        return []
    if isinstance(tags, str):
        tags = [tags]
    normalized = []
    for tag in tags:
        tag = tag.strip()
        if not tag:
            raise ValueError("tags cannot be empty")
        if tag not in normalized:
            normalized.append(tag)
    return normalized


def add(title: str, tags=None):
    tasks = load()
    task = {"title": title, "done": False}
    normalized = normalize_tags(tags)
    if normalized:
        task["tags"] = normalized
    tasks.append(task)
    save(tasks)
    return len(tasks) - 1


def list_tasks(include_done: bool = False, tag=None):
    if tag is not None:
        tag = tag.strip()
        if not tag:
            raise ValueError("tag cannot be empty")
    tasks = load()
    return [
        (index, task)
        for index, task in enumerate(tasks)
        if (include_done or not task["done"])
        and (tag is None or tag in task.get("tags", []))
    ]


def done(index: int):
    tasks = load()
    if index < 0 or index >= len(tasks):
        raise IndexError(index)
    tasks[index]["done"] = True
    save(tasks)
    return tasks[index]


def _option_value(args, index, option):
    if index >= len(args):
        raise ValueError(f"{option} requires a value")
    value = args[index].strip()
    if not value:
        raise ValueError(f"{option} requires a value")
    return value


def parse_add_args(args):
    """Split add arguments into a title and tags; non-option words stay in the title."""
    title_parts = []
    tags = []
    options = True
    index = 0
    while index < len(args):
        arg = args[index]
        if options and arg == "--":
            options = False
        elif options and arg == "--tag":
            index += 1
            tags.append(_option_value(args, index, "--tag"))
        elif options and arg.startswith("--tag="):
            tags.append(_option_value([arg.split("=", 1)[1]], 0, "--tag"))
        else:
            title_parts.append(arg)
        index += 1
    if not title_parts:
        raise ValueError("add requires a title")
    return " ".join(title_parts), normalize_tags(tags)


def parse_list_args(args):
    include_done = False
    tag = None
    index = 0
    while index < len(args):
        arg = args[index]
        if arg == "--all":
            include_done = True
        elif arg == "--tag":
            index += 1
            tag = _option_value(args, index, "--tag")
        elif arg.startswith("--tag="):
            tag = _option_value([arg.split("=", 1)[1]], 0, "--tag")
        index += 1
    return include_done, tag


def main(argv):
    if not argv:
        print("usage: taskcli.py add|list|done ...")
        return 1
    command = argv[0]
    if command == "add" and len(argv) >= 2:
        try:
            title, tags = parse_add_args(argv[1:])
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        index = add(title, tags)
        print(f"added {index}")
    elif command == "list":
        try:
            include_done, tag = parse_list_args(argv[1:])
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        for index, task in list_tasks(include_done, tag):
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
