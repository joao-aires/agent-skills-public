# Task CLI

A tiny local task tracker with JSON persistence.

## Commands

```bash
python3 taskcli.py add "write report"
python3 taskcli.py add "write report" --tag work --tag urgent
python3 taskcli.py add "review report" --tag=work,urgent
python3 taskcli.py list
python3 taskcli.py list --all
python3 taskcli.py list --tag work
python3 taskcli.py list --all --tag work
python3 taskcli.py done 0
```

`TASKCLI_DATA` overrides the JSON file path; tests use a temporary file. Tags may be repeated or comma-separated, are lower-cased, and may be written with a leading `#`. `list` accepts one tag and keeps its existing output columns; tags are used for filtering, not printed.

## Tests

```bash
python3 -m unittest -v
```

## Current behaviour

- Tasks have a title, a `done` flag and an optional `tags` list.
- `list` shows pending tasks by default and all tasks with `--all`.
- `list --tag <tag>` restricts the result to tasks carrying that tag; add `--all` to include completed tasks.
- `done` marks a task complete.
- JSON records are stable and human-readable. Records written before tags existed remain readable and are not rewritten just to add them.

## Documentation

- [Engineering change record](docs/ecr.md) — problem, requirements, design, implementation and evidence.
- [Design](docs/design.md) — options, compatibility matrix and the accepted decision.
- [Verification](docs/verification.md) — commands, environment and observed results.
- [EVAL](EVAL.md) — evaluation notes for this change.

## Limits

The tool is a local fixture: one process, one JSON file, no schema version, no locking and no migration. Tag display and tag editing are not implemented.
