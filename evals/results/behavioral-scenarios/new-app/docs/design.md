# Design: notes persistence, identity and command surface

Status: **accepted** (implemented in the local working tree).
Scope: the whole application — a small local CLI with no service or network boundary.
Related: [ECR](ecr.md) · [Verification](verification.md) · [README](../README.md)

## Question and constraints

Which persistence shape and command contract should a small single-user notes
CLI use, so that `add`, `list`, `search` and `delete` are predictable, survive
process restarts, and keep a clear boundary between CLI, storage and search?

Constraints, from `TASK.md` and the operating environment:

- Standard library only; no third-party packages and no network.
- Notes persist in a local JSON file; `NOTES_DATA` overrides the path.
- The four commands and their argument forms are fixed by the request.
- One user, one machine, one process at a time is the realistic workload. No
  service, daemon or multi-user coordination is requested.
- Data loss is the expensive failure: a note the user typed must not disappear
  because a write was interrupted.
- The code must keep CLI, storage and search separable.

Current state: **greenfield; no implementation existed** at the time the
decision was fixed. Python 3.14.7 was present on the target machine; no other
runtime was available or required.

## Affected software types

| Component | Type | Status | Reason |
| --- | --- | --- | --- |
| `notes.py` + `notes_store.py` + `notes_search.py` | `library-cli` | designed | Consumed through a terminal surface; judged by command surface, file format, errors, exit codes and dependency surface. |
| User interface | `frontend` | not affected | Text output on a terminal and shell argument input; no graphical surface, layout or interaction design. |
| Service | `backend` | not affected | No server, API, queue, tenancy or network boundary. The store is a local file, not a service-owned record. |
| Model behaviour | `ai` | not affected | No model call, retrieval, evaluation set or prompt surface. |

The only type that changes the evidence is `library-cli`, so the design record
shows the command surface, file format, error contract and dependency surface.
No C4, sequence or state-machine view is produced: there is one process, no
external dependency and no note lifecycle beyond exists/deleted. Architecture
boundaries are not at stake, so `system-design` is applied only through its
"small change, brief assessment" path.

## Options

### Option A — one JSON document, read-modify-write, atomic replace (chosen)

- **Lens:** packaging and dependency surface.
- **Shape:** `notes.json` holds `{"version", "next_id", "notes": [...]}`. Each
  mutation reads the document, changes it in memory, writes a sibling temp
  file, `fsync`s it, then `os.replace`s it over the original.
- **Optimizes:** one human-readable file; no dependencies or lock files; a
  crash during a write leaves the previous complete document; installation is
  "copy three `.py` files"; the whole format is inspectable and hand-editable.
- **Sacrifices:** every mutation rewrites the whole file and re-parses it, so
  cost grows with the number of notes. There is no cross-process lock, so two
  simultaneous writers can lose one update. Deleted ids leave gaps.
- **Failure behaviour:** interrupted write → old document intact; concurrent
  write → last replacer wins; unreadable/corrupt JSON → every command that
  needs the store exits 1 and the file is not modified.
- **Linked artifact:** command surface and file-format sketch below, plus the
  failure transcript.

### Option B — append-only JSON Lines journal with compaction

- **Lens:** durability and recovery.
- **Shape:** each mutation appends one record (`{"op": "add", ...}`,
  `{"op": "delete", ...}`) to `notes.jsonl`; `list`/`search` replay the journal;
  a compaction rewrite happens when tombstones dominate.
- **Optimizes:** appends are cheap and a torn final line can be discarded while
  earlier records stay readable; an audit trail and undo come almost free.
- **Sacrifices:** replay logic, tombstone semantics, compaction as a second
  write path, and a growing file. Two crash-retried appends can create duplicate
  ids unless an explicit id allocator is added. Considerably more code and more
  failure modes for a personal notes file.
- **Failure behaviour:** truncated last line → tolerated by dropping it; a
  corrupt record in the middle → manual repair, since later ops depend on
  earlier state; compaction crash → must be re-runnable.
- **Linked artifact:** journal record sequence (add, delete, add) and the replay
  rule; not produced because the option was rejected before that fidelity was
  needed.

### Option C — one JSON file per note in a directory

- **Lens:** isolation and concurrency.
- **Shape:** `${NOTES_DATA dir}/0001.json`, `0002.json`, … plus a counter file
  for id allocation. `list` and `search` scan the directory.
- **Optimizes:** a write touches exactly one note, so unrelated notes cannot be
  lost by a failed write; deleting is unlinking one file; files are easy to
  inspect and back up individually.
- **Sacrifices:** `NOTES_DATA` would name a directory although the request says
  "a local JSON file"; the id counter becomes the only shared mutable state and
  therefore the new consistency point; listing costs a directory scan; partial
  multi-file states (orphans, duplicate ids after a failed counter update)
  replace one atomic swap.
- **Failure behaviour:** failed write → one stale/orphan file; failed counter
  update → duplicate ids on the next add; interrupted delete → note still
  present, which is safe but surprising.
- **Linked artifact:** directory layout and id-allocation rule; not produced
  because the option was rejected.

## Linked design artifacts

The surface a reviewer needs to judge this CLI, at comparable fidelity for the
chosen option. A command-surface table, file-format sketch and a main-path plus
failure-path transcript are the `library-cli` evidence; wireframes and C4 views
are explicitly not applicable.

**Command surface**

| Command | Arguments | stdout | Exit |
| --- | --- | --- | --- |
| `notes.py add <text…>` | one or more words, joined by a space | the new integer id | 0 |
| `notes.py list` | none | `<id>\t<text>` per note, ascending id | 0 |
| `notes.py search <term…>` | one or more words, joined by a space | matching notes, `<id>\t<text>`, ascending id | 0 |
| `notes.py delete <id>` | positive integer | `deleted <id>` | 0 |
| `notes.py --help` | | usage and command list | 0 |

Words may be quoted or passed separately; both forms store one space-joined
text. All diagnostics go to stderr. Exit codes: `0` success (including an empty
result), `1` runtime or data error, `2` usage error.

**File format**

```json
{
  "version": 1,
  "next_id": 3,
  "notes": [
    {"id": 1, "text": "buy milk", "created_at": "2026-11-15T04:12:11Z"},
    {"id": 2, "text": "call Ana", "created_at": "2026-11-15T04:12:11Z"}
  ]
}
```

`version` is the schema marker (only `1` accepted). `next_id` is the next
unused positive integer and is never lowered by a delete. `created_at` is a
UTC ISO 8601 string with second precision, stored as provenance. `notes` is
ordered by `id` when read, even if the file was hand-edited out of order.

**Main path and one failure path (observed, not projected)**

```text
$ python3 notes.py add "buy milk"
1
$ python3 notes.py list
1	buy milk
$ python3 notes.py delete 99
notes.py: error: no note with id 99
[exit 1]
```

**Compatibility and dependency surface**

| Item | Claim |
| --- | --- |
| Runtime | CPython 3.8+ syntax and APIs; exercised only on 3.14.7 |
| Platforms | macOS exercised; path handling is `pathlib`-based and expected to work on Linux/Windows, unverified there |
| Dependencies | none outside the standard library (`argparse`, `sys`, `json`, `os`, `tempfile`, `datetime`, `pathlib`) |
| Packaging | plain files; `python3 notes.py` from the project directory; no wheel, entry point or install step |
| Breaking-change policy | the command surface and JSON keys are the contract; a breaking change requires a new `version` field value |

## Tradeoffs and failure behaviour

| Event | A (chosen) | B | C |
| --- | --- | --- | --- |
| Process killed mid-write | old file intact; temp file may remain | journal keeps prior records; last line possibly torn | one note file possibly stale |
| Two processes write at once | one update lost, no corruption | interleaved records, replay order matters | lost counter update → duplicate ids |
| File hand-edited badly | command exits 1, file untouched | partial replay or dropped tail | some notes unreadable, others fine |
| Disk full / read-only directory | exit 1 with path and OS reason, old file intact | append fails, earlier data intact | individual file fails |
| Note deleted by mistake | gone; no undo | tombstone could be reversed | file gone from trash-less unlink |
| Cost per mutation | O(n) read + O(n) write | O(1) append | O(1) write + O(1) counter |
| Implementation size | smallest | largest | medium |

The chosen option accepts a lost-update window under concurrent use because
nothing in the request implies concurrent writers, and it rejects silent
corruption in every other case. That is a deliberate scope trade, recorded as a
known limitation rather than solved with a lock protocol that nothing tests.

## Seam decisions

Decided once, because the CLI, store and search meet in this application:

1. **Record shape.** The store returns plain `dict`s with `id` (positive `int`),
   `text` (`str`) and `created_at` (`str` or `None`). No custom note class is
   exposed, which keeps the CLI and search free of storage internals.
2. **Error mapping.** Storage raises `StoreError` (and `NoteNotFound`, a
   subclass). The CLI prints `notes.py: error: …` to stderr and exits 1.
   Search raises `EmptySearchTerm` (a `ValueError`); the CLI resolves that
   before opening the store and exits 2, so a usage error is not masked by a
   broken data file.
3. **Ownership of output.** The store and search return data; only the CLI
   formats lines (`<id>\t<text>`, `deleted <id>`) and decides streams.
4. **Configuration precedence.** Non-empty `NOTES_DATA` wins over
   `~/.notes.json`; `~` is expanded; a relative override is resolved against the
   current working directory; parent directories are created on first write; a
   missing file reads as an empty store without creating it.
5. **Text normalisation.** `add` joins its words and collapses every whitespace
   run to one space, so a note is one display line. The store preserves what it
   is given. Search folds the same way (whitespace-collapsed, `casefold()`), so
   `search "BUY   milk"` matches `buy milk` and a hand-edited note containing a
   newline still matches across the break.
6. **Identity.** Ids are positive integers, monotonic, and never reused after a
   delete; `next_id` is persisted and raised above any existing id when a
   hand-edited file has a missing or stale value.
7. **Corruption policy.** Unparseable, empty, non-object or schema-violating
   files are refused, not repaired and not overwritten. Repairs are left to the
   user with the file untouched.

## Recommendation and decision

**Option A.** It is the only option that satisfies "a local JSON file" literally,
it needs no extra consistency point, and its one real risk (a torn write) is
addressed by temp-file plus `fsync` plus `os.replace` with stdlib only. Options B
and C pay structural complexity for capabilities (history, per-note isolation)
that the request does not ask for and that no test would exercise.

`created_at` is included even though no command displays it: a note without a
creation time loses information that cannot be reconstructed later, and the key
is cheap. `version` and `next_id` exist for the same reason — they make future
format changes and id allocation explicit instead of implicit.

```text
Decision: single JSON document, read-modify-write with atomic replace
Options considered: A (single document), B (append-only journal), C (file per note)
Chosen because: one human-readable file, stdlib only, atomic replace covers the realistic failure
Rejected because: B adds replay/compaction and duplicate-id risk; C turns NOTES_DATA into a directory and needs a shared counter
Accepted/delegated by: the task's instruction to proceed autonomously; no separate human sign-off
Status: accepted
Revisit if: notes exceed roughly 5k and per-command latency is noticeable; concurrent writers become real; edit/undo/history is requested (then B); or NOTES_DATA must hold many independent notes (then C)
```

## Evidence and open questions

Inspected at decision time: `TASK.md` requirements and the empty project
directory; Python 3.14.7 availability; `argparse` subcommand support; `os.replace`
atomicity on the same filesystem. No external source, vendor claim or benchmark
was used.

Open, deliberately not resolved:

- **Concurrent writers.** No lock; last writer wins. A lock would need a
  platform-appropriate primitive and a stale-lock policy, which is more risk
  than the request justifies.
- **Very large note counts.** O(n) rewrite per mutation is untested beyond
  hand-sized files; the revisit trigger above records the threshold as an
  estimate, not a measurement.
- **`created_at` semantics.** Second precision, UTC, not displayed. If it ever
  becomes user-visible, the display format and timezone policy need a decision.
- **Multi-line note text.** Intentionally not preserved on `add`; a request to
  store prose would change both the output format and the search contract.

Verified implementation evidence and residual limits are in
[verification.md](verification.md).
