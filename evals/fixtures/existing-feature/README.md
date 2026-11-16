# Task CLI

A tiny local task tracker with JSON persistence.

## Commands

```bash
python3 taskcli.py add "write report"
python3 taskcli.py list
python3 taskcli.py list --all
python3 taskcli.py done 0
```

`TASKCLI_DATA` overrides the JSON file path; tests use a temporary file.

## Tests

```bash
python3 -m unittest -v
```

## Current behaviour

- Tasks have a title and a `done` flag.
- `list` shows pending tasks by default and all tasks with `--all`.
- `done` marks a task complete.
- JSON records are stable and human-readable.
