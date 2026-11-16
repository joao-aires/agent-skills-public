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


def add(title: str):
    tasks = load()
    tasks.append({"title": title, "done": False})
    save(tasks)
    return len(tasks) - 1


def list_tasks(include_done: bool = False):
    tasks = load()
    return [
        (index, task)
        for index, task in enumerate(tasks)
        if include_done or not task["done"]
    ]


def done(index: int):
    tasks = load()
    if index < 0 or index >= len(tasks):
        raise IndexError(index)
    tasks[index]["done"] = True
    save(tasks)
    return tasks[index]


def main(argv):
    if not argv:
        print("usage: taskcli.py add|list|done ...")
        return 1
    command = argv[0]
    if command == "add" and len(argv) >= 2:
        index = add(" ".join(argv[1:]))
        print(f"added {index}")
    elif command == "list":
        for index, task in list_tasks("--all" in argv):
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
