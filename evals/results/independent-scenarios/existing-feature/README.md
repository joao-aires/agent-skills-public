# Task CLI

A tiny local task tracker with JSON persistence.

## Commands

```bash
python3 taskcli.py add "write report"
python3 taskcli.py add "write report" --tag work --tag urgent
python3 taskcli.py list
python3 taskcli.py list --all
python3 taskcli.py list --tag work
python3 taskcli.py list --all --tag work
python3 taskcli.py done 0
```

Tags are optional. Repeat `--tag` to add more than one; `--tag=work` also works. `list --tag` matches tags exactly and is case-sensitive. Use `--` to keep option-like words in a title: `add -- "deploy --tag work"`.

`TASKCLI_DATA` overrides the JSON file path; tests use a temporary file.

## Tests

```bash
python3 -m unittest -v
```

## Current behaviour

- Tasks have a title, a `done` flag and optional `tags`.
- `list` shows pending tasks by default and all tasks with `--all`.
- `list --tag <tag>` filters by exact tag; combine it with `--all` to include completed tasks.
- `done` marks a task complete.
- JSON records are stable and human-readable. Tasks created without tags keep the older `{"title", "done"}` record shape, and older files without tags remain readable.
