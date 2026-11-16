# Notes CLI

A small local command-line notes tool for one person on one machine. It stores plain-text notes in a JSON file, lists them, searches them by substring and deletes them by id. Status: working local tool, not a production or multi-user service.

## Quickstart

Prerequisites: Python 3.9 or newer. The tool uses only the Python standard library. It was verified with Python 3.14.7 on macOS.

From this directory:

```bash
python3 notes.py add "Buy milk"
```

Output:

```text
1
```

```bash
python3 notes.py add "Call the dentist"
python3 notes.py list
```

Output:

```text
1: Buy milk
2: Call the dentist
```

```bash
python3 notes.py search "DENTIST"
```

Output:

```text
2: Call the dentist
```

```bash
python3 notes.py delete 1
```

Output:

```text
Deleted note 1.
```

No install step and no virtual environment are required.

## Commands

| Command | Behavior | Output |
| --- | --- | --- |
| `python3 notes.py add "text"` | Stores a note and allocates the next id. | The new integer id, one line. |
| `python3 notes.py list` | Lists every note by ascending id. | `id: text` per note. |
| `python3 notes.py search "term"` | Finds notes containing the case-insensitive literal substring `term`. | Matching notes as `id: text`, or `No matches.` on stderr. |
| `python3 notes.py delete <id>` | Deletes one note. | `Deleted note <id>.` |
| `python3 notes.py --help` | Shows usage and commands. | Help text. |

Search treats the term as text, not a regular expression. Outer whitespace in a note is preserved. A whitespace-only note or search term is rejected.

## Where notes are stored

The default data file is `notes.json` in this directory, beside `notes.py`.

Set `NOTES_DATA` to use another file:

```bash
NOTES_DATA=/tmp/my-notes.json python3 notes.py add "Stored elsewhere"
```

`NOTES_DATA` is used as supplied, after expanding `~`. If it is set to an empty or whitespace-only value, the command fails with exit code 2 instead of silently falling back to the default file. Parent directories for the data file are created when a note is written.

The file is UTF-8 JSON with this shape:

```json
{
  "version": 1,
  "next_id": 2,
  "notes": [
    {
      "id": 1,
      "text": "Buy milk",
      "created_at": "2026-11-15T22:37:23Z"
    }
  ]
}
```

Writes go to a temporary file in the same directory and replace the data file with `os.replace`, so a failed write does not leave a partly written JSON file. The store does not lock the file; do not run writers concurrently.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Success. A search with no matches also returns 0, with no stdout and `No matches.` on stderr. |
| `1` | Operation or data failure, such as a missing note id, unreadable file or invalid JSON. |
| `2` | Usage, input or configuration error, such as a missing argument, a non-positive id, blank note text, a blank search term or an empty `NOTES_DATA`. |

Errors are printed to stderr as `error: ...` except for argparse usage errors, which use its standard format.

## Tests

Run the standard-library test suite from this directory:

```bash
python3 -m unittest -v
```

The suite covers storage, search and the actual `notes.py` entry point through subprocesses. It uses temporary `NOTES_DATA` paths and does not touch the default `notes.json`.

## Documentation map

| Document | Contents |
| --- | --- |
| [docs/change-record.md](docs/change-record.md) | Change record: scope, acceptance, design decisions, verification evidence and limits. |
| [EVAL.md](EVAL.md) | Skill discovery record and self-assessment for this exercise. |
| `notes_app/storage.py` | JSON persistence, schema validation, id allocation and atomic writes. |
| `notes_app/search.py` | Pure case-insensitive literal substring search. |
| `notes_app/cli.py` | Argument parsing, output and exit-code mapping. |
| `notes.py` | Thin entry point. |
| `tests/` | Standard-library unit and CLI tests. |

## Status and limits

- Single-user, single-process local use. There is no file locking, so concurrent writers can lose an update.
- No edit command, tags, reminders, sync, backup, import or export.
- Notes are stored unencrypted. Do not store secrets in them.
- Timestamps are stored but not displayed.
- Search reads the whole data file; this is intended for small note collections.
- Verified on macOS with Python 3.14.7 only. Windows and older Python versions were not exercised.

## Support and contribution

This is a self-contained exercise with no tracker, repository or support commitment. There is no external contribution route.

## License

No license is declared for this exercise. Do not redistribute it as a licensed project.
