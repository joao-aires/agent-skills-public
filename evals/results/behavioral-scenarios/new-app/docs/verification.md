# Verification: local notes CLI

Result: **verified locally for the tested acceptance cases; not released; one
acceptance case not exercised.**
Checked on 2026-11-15. Requirements and cases are labelled in the
[ECR](ecr.md#3-requirements-and-acceptance); design evidence is in
[design.md](design.md).

## Revision and environment

| Item | Value |
| --- | --- |
| Working tree | `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/new-app` |
| Version control | none — not a Git repository, no commit, nothing published |
| Revision identifier | SHA-256 of the checked files, below |
| OS | macOS (`Darwin arm64`) |
| Runtime | CPython 3.14.7 (`/Users/joao/homebrew/bin/python3`) |
| `python` on PATH | absent; every command below uses `python3` |
| Data file for manual checks | `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/notes-demo.json` (scratch) |

```text
04ac7946bcd1b940e2a12a14af30fc0de5d89bc3b3a83908514fbb2c3b353795  notes.py
e4c391c2a3d47a836059ccce94a6cd9759349198e2f91737e6362ca708600380  notes_store.py
a85798bcc55f8a7e8255c6e1168805e0e3df7a6861e9af2f3763249701cba125  notes_search.py
69372bf2e92244637378c4665354925c1dd94ad96f273bb8a012af14c14cbc24  tests/test_store.py
8d7d2c9bec7eaf8984f27afdbbe469c195fd8bee522b9023637d4dc281f45764  tests/test_search.py
f51b86aab2ccb4b188375c3d341817a4bc05a5ca710f5fb771c570b90c34fe88  tests/test_cli.py
```

Expected output of `shasum -a 256 notes.py notes_store.py notes_search.py
tests/test_*.py` at this revision is the list above. Any edit invalidates it.

## Automated checks

| Command | Observed result |
| --- | --- |
| `python3 -m unittest -v` | `Ran 56 tests in 2.044s` — `OK`, exit 0 (repeated runs ranged 1.978–2.044 s, same result) |
| `python3 -m py_compile notes.py notes_store.py notes_search.py tests/test_store.py tests/test_search.py tests/test_cli.py` | exit 0, no output |
| `grep -nE '^(import\|from) ' notes.py notes_store.py notes_search.py` | only `argparse`, `sys`, `json`, `os`, `tempfile`, `datetime`, `pathlib` and the three local modules — no third-party import |

Per-module counts at this revision:

| Module | Tests | Observed |
| --- | --- | --- |
| `tests.test_store` | 25 | `Ran 25 tests in 0.013s`, OK |
| `tests.test_search` | 11 | `Ran 11 tests in 0.000s`, OK |
| `tests.test_cli` | 20 | `Ran 20 tests in 2.177s`, OK |

`tests.test_cli` runs the real entry point as a subprocess with a scoped
`NOTES_DATA` and a redirected `HOME`, so it observes stdout, stderr, exit codes
and the stored file rather than calling functions in-process.

## Manual CLI exercise

Commands were run from the working tree with
`NOTES_DATA=/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/notes-demo.json`,
after removing that scratch file. Output and exit codes are observed; `[exit n]`
marks the shell status.

```text
$ python3 notes.py add "buy milk"
1
[exit 0]
$ python3 notes.py add "call Ana about the roof"
2
[exit 0]
$ python3 notes.py add "buy bread"
3
[exit 0]
$ python3 notes.py list
1	buy milk
2	call Ana about the roof
3	buy bread
[exit 0]
$ python3 notes.py search milk
1	buy milk
[exit 0]
$ python3 notes.py search BUY
1	buy milk
3	buy bread
[exit 0]
$ python3 notes.py search zebra
[exit 0]
$ python3 notes.py delete 2
deleted 2
[exit 0]
$ python3 notes.py delete 99
notes.py: error: no note with id 99
[exit 1]
$ python3 notes.py delete abc
usage: notes.py delete [-h] id
notes.py delete: error: argument id: invalid note id 'abc': expected an integer
[exit 2]
$ python3 notes.py add ""
notes.py: error: note text is empty
[exit 2]
$ python3 notes.py list
1	buy milk
3	buy bread
[exit 0]
$ python3 notes.py search ""
notes.py: error: search term is empty
[exit 2]
$ python3 notes.py
usage: notes.py [-h] command ...
notes.py: error: the following arguments are required: command
[exit 2]
```

Stored file after the session (`cat "$NOTES_DATA"`), confirming deletion,
unreused ids and the recorded format:

```json
{
  "version": 1,
  "next_id": 4,
  "notes": [
    {
      "id": 1,
      "text": "buy milk",
      "created_at": "2026-11-15T04:12:11Z"
    },
    {
      "id": 3,
      "text": "buy bread",
      "created_at": "2026-11-15T04:12:11Z"
    }
  ]
}
```

Default path and configuration checks, run separately:

| Scenario | Command | Observed |
| --- | --- | --- |
| Default location with redirected home | `env -u NOTES_DATA HOME=<scratch>/home python3 notes.py add "default-location"` | id `1`, exit 0, `<scratch>/home/.notes.json` created, mode `-rw-------` (0600) |
| Relative override | `cd <scratch>/work && NOTES_DATA=relative/notes.json python3 <tree>/notes.py add "relative-path"` | id `1`, exit 0, `<scratch>/work/relative/notes.json` created (parent directories made) |
| Corrupt store | `NOTES_DATA=<scratch>/broken.json python3 notes.py list` with contents `{"notes": [` | exit 1, stderr `notes.py: error: …/broken.json: invalid JSON: Expecting value: line 1 column 12 (char 11)`, no traceback, file unchanged |

## Acceptance status

| Case | Status | Evidence |
| --- | --- | --- |
| A1, A2, A4, A6–A14, A16, A17 | verified | tests above and the transcript |
| A3, A5, A15 | verified | CLI tests and the corrupt-store scenario |
| A18 (crash between `fsync` and `os.replace`) | **not exercised** | atomic-replace design is inspected and successful/failed writes are tested, but no crash was injected; residual risk remains |

No evidence is claimed for Windows, Linux, concurrent writers, large note
counts or piped output. Those are stated as limits, not as passing checks.

## Review findings and disposition

The review compared the actual tree against the accepted requirements and the
design record, reading every changed file and the test assertions.

| # | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| 1 | medium (data safety) | The write path cleaned up its temp file only for `OSError`; a `KeyboardInterrupt` during the write would leave a `.notes-*.tmp` file behind (the store stayed intact). | Fixed: cleanup now runs for `BaseException`, `OSError` is still wrapped as `StoreError`, others re-raise. |
| 2 | low | An unused `import notes_search` in `tests/test_search.py`. | Fixed: import removed. |
| 3 | low | `_search` normalises the term, then `search()` normalises it again. | Accepted: keeps the usage-error path ahead of opening the store; cost is negligible and the behaviour is tested. |
| 4 | low | `NOTES_DATA=""` silently falls back to `~/.notes.json` instead of erroring. | Accepted and documented in the README; empty usually means unset. |
| 5 | low | Output piped into a closing reader (for example `head -1`) can raise `BrokenPipeError` with a traceback. | Not fixed; unexercised scenario, recorded here and in the ECR open items. |
| 6 | medium (accepted limitation) | Two concurrent writers can lose one update; no lock. | Accepted in design option A and assumed in the ECR (A2); no test claims otherwise. |
| 7 | low | `created_at` is stored but never displayed, so a reviewer cannot see it through the CLI. | Accepted: the file is inspectable and the value is documented; displaying it would change the output contract. |

No finding contradicted an accepted requirement. Finding 1 was repaired before
the final test run whose hashes are recorded above; the remaining findings are
scope decisions, not hidden defects.

This review was performed by the same agent that wrote the code, so it is a
self-review, not independent verification. No CI, linter or type checker beyond
`py_compile` was available.

## What remains

- Release: none attempted; no package, install or deployment exists.
- Known gaps: A18 crash injection, cross-platform claims, concurrency, large
  note counts, broken-pipe handling.
- Documentation reconciliation: README, ECR, design and this record describe the
  same command surface, file format, exit codes and limits.
