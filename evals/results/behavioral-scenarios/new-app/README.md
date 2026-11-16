# notes.py

A small local command-line notes application. One JSON file holds your notes;
`add`, `list`, `search` and `delete` read and write it. It uses only the Python
standard library — no install step, no service, no network, no account. The code
is split so the command line, the storage and the search rules can be read and
tested separately.

## Status and audience

Working and tested locally on macOS with CPython 3.14.7. It is a personal,
single-user tool: one process at a time, one machine, no sync and no
concurrency control. It is not packaged, published or production-hardened.

Intended for someone who wants to capture short one-line notes from a terminal
and find them again by a word they remember.

## Prerequisites

- Python 3.8 or newer (verified only on 3.14.7). No packages to install.
- A POSIX-like shell for the examples below. On this machine the interpreter is
  `python3`; `python` is not on `PATH`. If your system provides `python`, the
  same commands work with it.

## Quickstart

Run from this directory. These commands are the shortest path that works from a
fresh copy; none of them writes to your real notes file, because `NOTES_DATA`
points at a scratch file.

```sh
export NOTES_DATA="$PWD/demo-notes.json"
rm -f "$NOTES_DATA"

python3 notes.py add "buy milk"          # prints 1
python3 notes.py add "call Ana about the roof"   # prints 2
python3 notes.py list
python3 notes.py search milk
python3 notes.py delete 1
python3 notes.py list
```

Expected output of the quickstart:

```text
$ python3 notes.py add "buy milk"
1
$ python3 notes.py add "call Ana about the roof"
2
$ python3 notes.py list
1	buy milk
2	call Ana about the roof
$ python3 notes.py search milk
1	buy milk
$ python3 notes.py delete 1
deleted 1
$ python3 notes.py list
2	call Ana about the roof
```

Delete the scratch file when you are done:

```sh
rm -f "$NOTES_DATA"
```

To use your real notes file, unset the override for this shell; the default is
`~/.notes.json`:

```sh
unset NOTES_DATA
python3 notes.py add "buy milk"
python3 notes.py list
```

## Commands

| Command | What it does | stdout | Exit |
| --- | --- | --- | --- |
| `python3 notes.py add <text…>` | Stores one note and prints its id. Words may be quoted or separate. | the id, for example `3` | 0 |
| `python3 notes.py list` | Lists every note, oldest id first. | `<id>\t<text>` per line | 0 |
| `python3 notes.py search <term…>` | Finds notes whose text contains the term. | matching `<id>\t<text>` lines | 0 |
| `python3 notes.py delete <id>` | Deletes the note with that id. | `deleted <id>` | 0 |
| `python3 notes.py --help` | Shows usage and the command list. | usage text | 0 |

Examples:

```sh
python3 notes.py add "buy milk"                  # 1
python3 notes.py add buy bread                   # 2 — quoting is optional
python3 notes.py search "BUY"                    # case-insensitive
python3 notes.py search milk                     # 1	buy milk
python3 notes.py delete 2                        # deleted 2
python3 notes.py delete 99                       # error, exit 1
python3 notes.py search ""                       # error, exit 2
```

## Notes file

- Default path: `~/.notes.json`. `NOTES_DATA` overrides it.
- A non-empty `NOTES_DATA` is used as given: `~` is expanded, and a relative path
  is resolved from the directory you run the command in. An empty `NOTES_DATA`
  is treated as unset.
- Missing parent directories are created on the first write. A missing file is
  an empty store; `list` does not create it.
- The file is one JSON object:

  ```json
  {
    "version": 1,
    "next_id": 4,
    "notes": [
      {"id": 1, "text": "buy milk", "created_at": "2026-11-15T04:12:11Z"},
      {"id": 3, "text": "buy bread", "created_at": "2026-11-15T04:12:11Z"}
    ]
  }
  ```

- Writes replace the whole file atomically (temp file, `fsync`, rename), so an
  interrupted write leaves the previous version. The file is created with mode
  `0600`.
- An unreadable or invalid file is refused with exit 1 and is not modified. If
  you edit it by hand, keep `id`s unique and positive; a missing or stale
  `next_id` is raised above the largest existing id on the next write.

## Behaviour details

- **Input text.** Words are joined with one space and every whitespace run is
  collapsed, so a note is one line. `add "  buy\nmilk  "` stores `buy milk`.
- **Ids.** Positive integers that increase and are never reused; deleting note
  2 leaves the next new note at 4 if 3 existed.
- **Search.** Case-insensitive substring match with whitespace collapsed, so
  `search "BUY   milk"` matches `buy milk` and `search ana` matches `call Ana`.
  There is no ranking, AND/OR syntax, fuzzy matching or prefix operator.
  Results keep id order. No matches prints nothing and exits 0.
- **Output.** stdout carries only ids, note lines and the `deleted <id>`
  confirmation. Diagnostics go to stderr as `notes.py: error: …`, without a
  traceback for expected failures.
- **Exit codes.** `0` success (including an empty result), `1` runtime or data
  error (unknown id, unreadable/corrupt file, write failure), `2` usage error
  (missing command, empty note text, empty search term, invalid id).
- **Encoding.** UTF-8; non-ASCII text is stored unescaped.

## Documentation

| Need | Read |
| --- | --- |
| Why the change exists, requirements, acceptance and decisions | [docs/ecr.md](docs/ecr.md) |
| Persistence and command-surface design, options and tradeoffs | [docs/design.md](docs/design.md) |
| Commands run, observed results, review findings and gaps | [docs/verification.md](docs/verification.md) |
| Evaluation of the process used to build this | [EVAL.md](EVAL.md) |
| The original request | [TASK.md](TASK.md) |

## Development

Run the whole suite from this directory:

```sh
python3 -m unittest -v
```

Expected tail of the output (`<elapsed>` varies; the count and `OK` should match):

```text
----------------------------------------------------------------------
Ran 56 tests in <elapsed>

OK
```

Run one module while working:

```sh
python3 -m unittest -v tests.test_store
python3 -m unittest -v tests.test_search
python3 -m unittest -v tests.test_cli
```

`tests/test_cli.py` invokes `notes.py` as a subprocess with a temporary
`NOTES_DATA` and `HOME`, so it does not touch your notes. No linter, formatter
or third-party test tool is required or configured.

## Layout

| File | Responsibility |
| --- | --- |
| `notes.py` | Argument parsing, input normalisation, output formatting, exit codes |
| `notes_store.py` | JSON file format, path resolution, schema validation, atomic writes |
| `notes_search.py` | Case/whitespace folding and substring matching |
| `tests/test_store.py` | Storage, validation and path rules (25 tests) |
| `tests/test_search.py` | Matching rules (11 tests) |
| `tests/test_cli.py` | End-to-end command behaviour and exit codes (20 tests) |

## Limitations and unsupported paths

- **No concurrency control.** Two processes writing at the same time can lose
  one update. There is no lock file.
- **No editing, tags, priorities, due dates, undo, import or export.** Delete is
  permanent.
- **Single-line notes only.** Multi-line input is collapsed to one line.
- **No ranking or query syntax.** Search is a substring test.
- **Untested platforms.** macOS was exercised; Linux and Windows are expected to
  work but were not run.
- **Crash between `fsync` and the rename** was not injected; the previous file
  is intact by design, but that specific interruption is unverified.
- **Piped output** into a reader that closes early (for example `head -1`) can
  produce a `BrokenPipeError` traceback.

## Support and contributing

There is no issue tracker, release or support channel; this is a local
evaluation project. Do not expect compatibility guarantees across edits. See
[docs/design.md](docs/design.md) for the decision to revisit before changing the
file format or command surface.

## License

No license is declared for this local project. It is not published for reuse.
