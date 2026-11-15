# Notes CLI: initial local implementation

Status: implemented and verified locally. Not published; this workspace has no Git repository. A full seven-section ECR is not warranted for this small local tool, so this is a compact change record with the design decisions and observed evidence kept together.

- Verified: 2026-11-15 on macOS, Python 3.14.7.
- Revision: non-versioned local tree; file hashes are in [Revision identity](#revision-identity).
- Next action: none within the requested scope. Concurrency support and an edit command are explicitly deferred.

## Overview

The workspace contained only `TASK.md`. The change adds a local notes command-line application with four commands: add, list, search and delete. Notes persist in one UTF-8 JSON file selected by `NOTES_DATA` or by a default path beside `notes.py`.

The useful outcome is a person being able to record a short note, find it later by a case-insensitive substring and remove it, without a service, database or third-party package.

## Change and acceptance

| Id | Observable acceptance | Status | Evidence |
| --- | --- | --- | --- |
| R1 | `python3 notes.py add "Buy milk"` stores the note and prints its id. | Verified | CLI run printed `1`; `tests.test_cli` asserts stdout and persisted JSON. |
| R2 | `python3 notes.py list` lists stored notes. | Verified | CLI run printed `1: Buy milk` and `2: Call the dentist`; CLI test asserts order and format. |
| R3 | `python3 notes.py search "term"` finds notes containing the term. | Verified | Search for `DENT` printed note 2; unit tests cover case folding, literal metacharacters and no match. |
| R4 | `python3 notes.py delete <id>` deletes the note. | Verified | CLI run printed `Deleted note 1.`; a following list omitted it. |
| R5 | Notes persist in a local JSON file; `NOTES_DATA` overrides the path. | Verified | CLI runs used `NOTES_DATA`; the README quickstart exercised the default path; tests assert reload, schema, custom path, `~` expansion and empty-value rejection. |
| R6 | No third-party dependencies. | Verified by inspection and execution | Only standard-library imports are used; the suite ran with the system Python and no install step. |
| R7 | Standard-library tests and a README with exact commands. | Verified | `python3 -m unittest -v` ran 34 tests, all passing; README commands were run. |
| R8 | CLI, storage and search remain separate. | Verified by structure | `notes_app/cli.py` parses arguments and maps exits; `notes_app/storage.py` owns JSON and ids; `notes_app/search.py` is a pure function. |

Failure and boundary cases covered:

- Blank note and blank search term: exit 2, no data write.
- Non-positive or non-integer delete id: exit 2.
- Missing note id: exit 1 with a diagnostic.
- Corrupt JSON: exit 1, file left unchanged.
- Zero-byte data file: treated as an empty notebook.
- Duplicate ids or a `next_id` that could reuse an id: data error.
- Unicode text round trip.
- Search with no matches: exit 0, empty stdout, `No matches.` on stderr.

## Design decisions

The component is a `library-cli` software type. Its relevant design evidence is the command surface, dependency surface, error and exit-code behavior, persistence format and usage example, not UI direction or C4 views.

### Layers

| Layer | Responsibility |
| --- | --- |
| `notes.py` | Entry point; calls `notes_app.cli.main`. |
| `notes_app/cli.py` | argparse surface, output formatting and exit-code mapping. |
| `notes_app/storage.py` | Data path resolution, JSON schema validation, id allocation and atomic writes. |
| `notes_app/search.py` | Pure case-insensitive literal substring matching. |
| `notes_app/errors.py` | Shared expected errors so search does not import storage for error types. |

This split follows the Python automation guidance to separate argument handling, pure transformations and file I/O. It is four small modules rather than a framework.

### Data format and ids

The data file is a JSON object with `version`, `next_id` and `notes`. Each note has `id`, `text` and a UTC `created_at` string. `next_id` is stored rather than derived so deleting the highest note does not reuse its id. A missing `next_id` is derived as `max(id) + 1` for hand-edited files; a present value must exceed every note id.

A zero-byte file is an empty notebook. Non-empty invalid JSON or an invalid schema is an error, not an empty notebook, so corruption is not silently discarded.

### Write behavior

Writes use `tempfile.mkstemp` in the target directory, flush and `fsync`, then `os.replace`. A failed write does not leave a partly written JSON file. There is no lock. A single local user is the assumed writer; concurrent updates can overwrite one another. Adding a lock or compare-and-swap protocol was deferred because the task asks for a small local CLI and no such requirement was stated.

### Search semantics

The search term is case-insensitive through `str.casefold()` and is a literal substring, not a regular expression. Outer whitespace in stored note text is preserved; whitespace-only note text and search terms are rejected. No match is a successful search with an empty result, not an operational failure.

### Configuration and exit codes

Precedence is `NOTES_DATA` when present, otherwise `notes.json` beside the entry point. An empty `NOTES_DATA` is a configuration error rather than a silent fallback. `~` is expanded. Exit codes follow the automation guidance convention: 0 success, 2 usage/input/configuration, 1 operation or data failure. Stdout carries command results; diagnostics go to stderr.

### Alternatives considered

| Alternative | Why it was not selected |
| --- | --- |
| SQLite | The task explicitly asks for a local JSON file. A database would add state and tooling without serving this scope. |
| One `notes.py` containing every layer | Feasible, but the task asks for clear separation; separate modules make the boundaries testable without making the code large. |
| UUID note ids | Less convenient on a command line. Sequential ids are enough for a local tool, with non-reuse handled by `next_id`. |
| Case-sensitive search | Less useful for notes and not required. Case-insensitive literal matching is predictable and simple. |
| Silent fallback for empty `NOTES_DATA` | Would hide a misconfigured environment variable. An explicit exit-2 error is easier to diagnose. |
| uv, Ruff, pytest project setup from `modern-python` | The task forbids third-party dependencies, asks for a single runnable `notes.py`, and names standard-library tests. Those constraints take precedence for this exercise. |
| Full ECR with seven headings and a design proposal with three options | Disproportionate for one small component with one evident approach. The meaningful choices are recorded above instead. |

## Implementation

Created:

```text
notes.py
notes_app/__init__.py
notes_app/errors.py
notes_app/storage.py
notes_app/search.py
notes_app/cli.py
tests/__init__.py
tests/test_storage.py
tests/test_search.py
tests/test_cli.py
README.md
docs/change-record.md
EVAL.md
```

### Revision identity

This workspace is not a Git repository, so there is no commit. These are full SHA-256 content hashes of the implementation, tests and README at the verified revision. `docs/change-record.md` and `EVAL.md` are excluded because embedding their own hashes would change the files being hashed.

| File | SHA-256 |
| --- | --- |
| `notes.py` | `368c4fa2b85126bc82caffb21132ffc3d0f4bcb001c26cdaf773b965299ffe23` |
| `notes_app/__init__.py` | `c3e2b395215d17caafae3f494d6aa6c826a35f6fe12340caf70f77d7892a4b33` |
| `notes_app/errors.py` | `0f2f784302bfbd4697c08d38b9787b1fc9f3f72d8bb4b4d11ba76ca6a921dfd1` |
| `notes_app/storage.py` | `13d532f1b8a75eefa336cc6d8a4c33bd86ef379c340bdcf59be9e2cd94e0eb8d` |
| `notes_app/search.py` | `c513363b438b46bf36edbfddcf85737b061c4037ec2a69c27694e8c24bf615af` |
| `notes_app/cli.py` | `22fddb1fe3204efe65b146aa4b9bc87ea161de2163992e05ec2a60c6ae8f7eed` |
| `tests/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `tests/test_storage.py` | `a9ac7e593ebc5c1e7a3beca27de0fb1e71b39f2593f17647f69602fa7ba79315` |
| `tests/test_search.py` | `7c42278fceeda8a5538671cdb02ef8f91894279f48948f893aad5746b3b8a052` |
| `tests/test_cli.py` | `01b91c0a1128ac70edfa93cc16dc67b30da006134df9e7d039f8b336a603aedc` |
| `README.md` | `34947c5a7eac607a71c8672ff8486f2ab8d49eace7993694ceab9a271ec38079` |

Not published; content hashes, not a commit.

## Verification

Environment: macOS, Python 3.14.7, standard library only, working directory `new-app`.

### Automated tests

```text
$ python3 -m unittest -v
...
Ran 34 tests in 1.577s

OK
```

The suite includes 13 subprocess tests of `notes.py` itself, 16 storage and data-path tests, and 5 pure search tests. The CLI tests use temporary `NOTES_DATA` paths. All 34 tests passed; none were skipped.

### CLI exercise

A temporary data path at `.cli-demo/notes.json` was used, then the directory was removed. In the table, `NOTES_DATA` refers to `$PWD/.cli-demo/notes.json`.

| Command | Observed stdout | Exit |
| --- | --- | --- |
| `NOTES_DATA=... python3 notes.py add "Buy milk"` | `1` | 0 |
| `NOTES_DATA=... python3 notes.py add "Call the dentist"` | `2` | 0 |
| `NOTES_DATA=... python3 notes.py list` | `1: Buy milk` then `2: Call the dentist` | 0 |
| `NOTES_DATA=... python3 notes.py search "DENT"` | `2: Call the dentist` | 0 |
| `NOTES_DATA=... python3 notes.py search "missing"` | empty stdout; `No matches.` on stderr | 0 |
| `NOTES_DATA=... python3 notes.py delete 99` | empty stdout; `error: No note with id 99.` on stderr | 1 |
| `NOTES_DATA=... python3 notes.py delete abc` | argparse usage error: `id must be a positive integer` | 2 |
| `NOTES_DATA=... python3 notes.py delete 1` | `Deleted note 1.` | 0 |
| `NOTES_DATA=... python3 notes.py list` after delete | `2: Call the dentist` | 0 |
| `NOTES_DATA=... python3 notes.py add "Third note"` | `3` | 0 |

The JSON file after the third add contained version 1, the expected notes and `next_id: 4`, with timestamps such as `2026-11-15T22:37:23Z`. In a separate temporary file, adding ids 1 and 2, deleting id 2 and adding again produced id 3; a list then showed notes 1 and 3. A deleted id was not reused.

The README quickstart was then run exactly as written without `NOTES_DATA`, which exercised the default `notes.json` path. It printed ids 1 and 2, listed both notes, found the dentist note with `search "DENTIST"` and printed `Deleted note 1.`. A following list showed only note 2, which was then deleted and the default data file removed.

### Not exercised

- Two concurrent writers and lost-update behavior.
- Windows, Linux or Python versions older than 3.14.7.
- Invalid UTF-8 arguments from the operating system.
- Very large note collections or search performance.
- Encryption at rest or file permission policy beyond the process umask and `mkstemp` defaults.

## Decisions, limits and open items

- No file lock. This is the main known limitation; the code assumes one writer at a time.
- No edit command, tags, export, backup or sync. None were requested.
- The README claims Python 3.9 or newer based on the language features used. Only 3.14.7 was executed, so that compatibility claim is unverified.
- The default path is beside `notes.py`, not the process working directory. This makes invocation from another directory predictable, but it differs from tools that store data in the current directory.
- Self-review only. No independent reviewer or separate agent review was performed.
- No deployment, packaging or release was performed; those actions were outside the requested scope.

## References

- Task: `TASK.md`.
- README: `README.md`.
- Tests: `tests/test_storage.py`, `tests/test_search.py`, `tests/test_cli.py`.
- Skill guidance applied: `develop`, `implement`, `test`, `project-fit`, `artifact-system` quality bar and library/CLI evidence, `guide-readme`, `guide-ecr`, `python-automation-engineering`, `modern-python`, `technical-writing` and `humanizer` in the skill library at `/Users/joao/Projects/products/agent-skills-artifact-quality`.
