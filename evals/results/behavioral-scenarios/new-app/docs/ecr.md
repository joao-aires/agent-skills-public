# ECR: local notes CLI

Status: **implemented and verified locally; not released** (there is no package, install step or deployment target).
Change identity: the working tree at
`/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/new-app`,
not a Git repository, no commit; file hashes identify the checked revision.
Next action: none within the request. If the tool is adopted, put the directory
under version control and record a commit so later evidence has a stable link.

## 1. Overview and lifecycle

This change adds a small, dependency-free command-line notes application:
`add`, `list`, `search` and `delete`, backed by one local JSON file. It is a
single-user, single-process tool for capturing short notes from a terminal.

Current state, by claim:

| Claim | State | Evidence |
| --- | --- | --- |
| Requirements accepted | Yes | `TASK.md` plus this section; assumptions A1–A3 below |
| Design accepted | Yes | [design.md](design.md), decision block |
| Implemented | Yes | `notes.py`, `notes_store.py`, `notes_search.py`; SHA-256 list in [verification.md](verification.md) |
| Verified | Yes, locally | 56 unit/integration tests passed; CLI transcript in [verification.md](verification.md) |
| Released | No | no package, no distribution, no deployment target |

Scope: the four commands, JSON persistence with `NOTES_DATA`, standard-library
tests, README and the three docs. Non-goals: editing a note, tags, ranking or
fuzzy search, multi-user or concurrent use, sync, encryption, undo, packaging.

The application has no issue, PRD or ticket. The request itself is the scope;
none was invented to fill a field.

## 2. Problem and scope

The person using this repository wants to record a short note, find it again by
a word they remember, and remove it, without standing up a database, service or
third-party dependency. Today there is no such tool in the directory. A note
that survives the terminal session is the whole value; losing one silently is
the failure that matters most.

In scope:

- four commands over one local JSON file;
- a path override through `NOTES_DATA`;
- restart-safe persistence and a readable, hand-inspectable format;
- clear separation of CLI, storage and matching, with tests that observe each.

Out of scope, and why:

- **editing** — not requested; `delete` plus `add` covers the need at this size;
- **concurrency and multi-user access** — one local user is the stated context;
- **ranking, fuzzy or tokenised search** — "notes containing the term" is a
  substring statement, not a relevance requirement;
- **packaging, install and versioned distribution** — `python3 notes.py` is the
  requested entry point;
- **UI, service, AI** — no affected component of those types.

Assumptions (reversible, stated because they shape the result):

- **A1 — text on one line.** Input whitespace collapses to single spaces, so a
  note is one output line and one searchable string. Multi-line prose is not a
  stated need and would break the `<id>\t<text>` line contract.
- **A2 — no locking.** Two simultaneous writers may lose one update. Accepted
  for a personal tool rather than adding an untested lock protocol.
- **A3 — default location `~/.notes.json`.** Keeps notes out of the project
  directory; `NOTES_DATA` exists for scoping and tests.

Feasibility: Python 3.14.7 with `argparse`, `json`, `tempfile`, `os.replace`,
`pathlib` and `datetime` covers every requirement without a dependency. The
target filesystem supports atomic same-directory rename, which the write path
relies on.

## 3. Requirements and acceptance

Requirement labels are local to this record. All functional requirements are
**accepted** (from `TASK.md`) except where marked as a design assumption.

| ID | Requirement | Status |
| --- | --- | --- |
| R1 | `add` stores one note from one or more words, prints only the new id on stdout, exits 0. Empty or missing text is a usage error (exit 2) and writes nothing. | accepted |
| R2 | `list` prints `<id>\t<text>` per note, ascending id; a missing or empty store prints nothing and exits 0. | accepted |
| R3 | `search` matches a case-insensitive, whitespace-insensitive substring of note text and prints matches in id order; no match prints nothing and exits 0; an empty term is a usage error (exit 2). | accepted |
| R4 | `delete <id>` removes that note, prints `deleted <id>`, exits 0; an unknown id exits 1 and leaves the file unchanged; a non-integer or non-positive id is a usage error (exit 2). | accepted |
| R5 | Notes persist in one JSON file at `~/.notes.json`, overridden by a non-empty `NOTES_DATA`; `~` expands; a relative override resolves against the working directory; a missing parent directory is created on first write; a missing file reads as an empty store without being created. | accepted |
| R6 | Every mutation writes a sibling temp file, flushes and `fsync`s it, then `os.replace`s it over the store, so an interrupted write leaves the previous document. An unreadable, empty, corrupt or schema-invalid file is refused with exit 1 and left byte-identical. No temp files remain after a successful or failed write. | accepted (atomicity observed for the success/failure paths; a real crash between `fsync` and `replace` was not injected) |
| R7 | Ids are positive integers, increase monotonically and are never reused after a delete. | accepted (design decision D2) |
| R8 | Expected failures print one diagnostic line to stderr with no traceback; stdout carries only data and confirmations. | accepted |
| R9 | Standard library only; no network; the entry point is `python3 notes.py`. | accepted |
| R10 | CLI, storage and matching are separate modules: the store imports neither the CLI nor search; search imports neither. | accepted |
| R11 | Tests use `unittest` and run with `python3 -m unittest -v`; the README gives exact commands. | accepted |

Observable acceptance cases and their status at the checked revision:

| Case | Action and condition | Observable result | Status |
| --- | --- | --- | --- |
| A1 | `add "buy milk"` on a fresh store | stdout `1`, exit 0, note present in the JSON file | verified |
| A2 | `add "buy" "milk"` and `add "  buy\nmilk  "` | stored text `buy milk` in both cases | verified |
| A3 | `add "   "` or `add` with no words | stderr diagnostic, exit 2, store file not created | verified |
| A4 | `list` after two adds | `1\tbuy milk` then `2\tcall Ana`, exit 0 | verified |
| A5 | `list` on a store that does not exist | empty stdout, empty stderr, exit 0 | verified |
| A6 | `search BUY` over `Buy milk` and `buy bread` | both notes, id order | verified |
| A7 | `search ana` over `call Ana` | that note only | verified |
| A8 | `search zebra` | empty stdout, exit 0 | verified |
| A9 | `search ""` | stderr `search term is empty`, exit 2 | verified |
| A10 | `delete 2` | stdout `deleted 2`, exit 0, note absent from file | verified |
| A11 | `delete 99` | stderr `no note with id 99`, exit 1, file byte-identical | verified |
| A12 | `delete abc`, `delete 0`, `delete -1` | usage diagnostic mentioning the invalid id, exit 2 | verified |
| A13 | `NOTES_DATA=/tmp/x/notes.json add …` with `/tmp/x` absent | parent created, note stored there, no `~/.notes.json` written | verified |
| A14 | `NOTES_DATA` unset, `HOME` redirected | file created at `$HOME/.notes.json` with mode `0600` | verified |
| A15 | store file containing `{"notes": [` | every command exits 1 with the file path and `invalid JSON`, no traceback, file unchanged | verified |
| A16 | delete the newest note, then add | the new note gets a higher id | verified |
| A17 | 56 tests via `python3 -m unittest -v` | `OK` | verified |
| A18 | kill the process between `fsync` and `os.replace` | previous document intact | **not exercised**; code inspection only, residual risk recorded |

Open decisions that would block implementation: none. Decisions that could
change promised behavior in future (locking, rich text, ranking) are listed as
non-goals rather than open blockers.

## 4. Solution design

Baseline: greenfield; no implementation existed. Design record:
[design.md](design.md) — full option set, tradeoffs, seam decisions and decision
block. Summary:

- **Affected type:** `library-cli` only. Frontend, backend and AI: not affected
  (terminal surface, no service, no model).
- **Chosen option:** one JSON document, read-modify-write with temp-file +
  `fsync` + atomic `os.replace`. Rejected: an append-only JSON Lines journal
  (needs replay, compaction and duplicate-id handling) and one JSON file per
  note (turns the override into a directory and adds a shared id counter).
- **Record shape:** `{"version": 1, "next_id": n, "notes": [{id, text, created_at}]}`.
- **Seam:** the store returns plain dicts and raises `StoreError` (with
  `NoteNotFound`); search raises `EmptySearchTerm`; the CLI owns stream choice,
  line formatting and exit codes `0/1/2`; `NOTES_DATA` takes precedence over
  `~/.notes.json`.
- **Decision owner:** the task authorized autonomous work; no separate human
  sign-off. Status `accepted`, revisit trigger and thresholds in `design.md`.

No C4, sequence or state-machine view was produced: one process, no service
boundary, no meaningful note state beyond exists/deleted. Compatibility is
recorded as a small matrix in `design.md` rather than a separate document.

## 5. Implementation strategy

Delivered in four increments, each with its own checks (all performed):

1. **Storage.** `notes_store.py`: path resolution, schema validation, atomic
   save, add/list/delete. Checked with 25 store and path tests, including
   corrupt files, duplicate ids, stale `next_id`, UTF-8 round trip and temp-file
   cleanup.
2. **Matching.** `notes_search.py`: whitespace-collapsed `casefold` substring
   with an empty-term error. Checked with 11 search tests, including Unicode
   case folding (`STRASSE` matches `Straße`).
3. **CLI.** `notes.py`: argparse subcommands, text normalisation, output
   formatting, exit codes, stderr diagnostics. Checked with 20 subprocess tests
   that invoke the real entry point with a scoped `NOTES_DATA`.
4. **Documentation and manual exercise.** README with exact commands; this ECR;
   the design record; the verification record; a hand-run CLI session over a
   scratch data file.

There was no migration, compatibility window or rollout: the application did
not exist before, and no user data was touched. Rollback is deleting the
directory. Remaining blockers: none.

## 6. Verification and release

Full record: [verification.md](verification.md). Summary of what ran:

- `python3 -m unittest -v` → `Ran 56 tests`, `OK`, elapsed 2.044 s (repeated runs 1.978–2.044 s).
- `python3 -m py_compile …` → exit 0.
- Manual CLI session: add, list, search (match, case variant, no match), delete
  (success, unknown id, invalid id), empty add, empty search, no command,
  inspect stored JSON. Observed outputs and exit codes matched cases A1–A12; the
  stored file kept `next_id` above the deleted id, consistent with A16, which is
  covered by a unit test. Configuration cases A13–A15 were exercised separately
  with a redirected `HOME`, a relative `NOTES_DATA` and a deliberately corrupt
  file.

Not exercised: a real crash between `fsync` and `os.replace` (A18); Windows and
Linux; simultaneous writers; note counts large enough to make the O(n) rewrite
visible; `BrokenPipeError` when output is piped into a closing reader.

Release: none. No artifact was published, installed or deployed. The
application is usable only from this working tree.

## 7. Decision history and references

| Date | Decision | Status | Rationale |
| --- | --- | --- | --- |
| 2026-11-15 | D1: single JSON document with atomic replace over journal or file-per-note | accepted | One file, stdlib only, crash-safe writes; journal and per-note layouts add a consistency point without a requested capability |
| 2026-11-15 | D2: integer ids, monotonic, never reused | accepted | `delete <id>` needs a short stable handle; reuse would make a stale reference delete a different note |
| 2026-11-15 | D3: default `~/.notes.json` | accepted | Keeps notes out of the project tree; override available for scoping |
| 2026-11-15 | D4: collapse input whitespace to one line | accepted as assumption A1 | Keeps the line-oriented `<id>\t<text>` contract and search string unambiguous |
| 2026-11-15 | D5: exit codes `0` success, `1` runtime/data, `2` usage | accepted | Separates scripts' "worked", "data problem" and "you called it wrong" cases |
| 2026-11-15 | D6: persist `created_at` and `version` even though no command displays them | accepted | Irreversible information and format evolution cost almost nothing to keep |

Superseded decisions: none. Open items, deliberately not resolved:

- concurrency behaviour (A2) and a possible lock, if the tool ever gains a
  second writer;
- multi-line note text, if notes become prose;
- `BrokenPipeError` handling for piped output;
- Windows/Linux support claims, currently unverified.

References: [TASK.md](../TASK.md) (request) · [design.md](design.md) (design
proposal and seam) · [verification.md](verification.md) (commands, results,
hashes, residual limits) · [README.md](../README.md) (entry point and usage).
