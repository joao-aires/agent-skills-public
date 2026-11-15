# Independent review: new-app notes CLI

## Verdict

The delivered application is functional, persistent, framework-free and well documented. I reproduced the test suite and the CLI behavior in a temporary copy, and the implementation matches the README and the change record. All five grading expectations are met.

The overall grade is **pass with limitations** only because of two accuracy problems in the delivered narrative: `EVAL.md` claims generated `__pycache__` directories were removed, but they are present in the delivered workspace, and the storage docstring/change record say that all non-empty malformed JSON is an error while a whitespace-only file is silently treated as an empty notebook. Neither affects the requested commands or persistence.

## Expectation table

| Expectation | Status | Evidence |
| --- | --- | --- |
| 1. Working CLI with requested commands and persistence | Met | `python3 notes.py add/list/search/delete` all worked. Two adds produced ids 1 and 2; a separate `list` process showed both; `search DENT` found note 2; `delete 1` removed it; a following `list` showed only note 2; a later add produced id 3. `NOTES_DATA` persistence and the default `notes.json` path both worked. |
| 2. Standard-library tests covering add/list/search/delete and persistence | Met | `python3 -m unittest -v` ran 34 tests, all `ok`, no skips. The suite contains 13 subprocess CLI tests, 16 storage/data-path tests and 5 pure search tests. CLI tests exercise all four commands and persistence across separate processes using temporary `NOTES_DATA` paths. |
| 3. ECR or compact change record with scope, acceptance, design decision, implementation and verification | Met | `docs/change-record.md` contains Overview/scope, Change and acceptance (R1-R8), Design decisions (layers, data format, writes, search, configuration, alternatives), Implementation (file list), Verification (test command/result, CLI table, environment, limits) and Decisions/limits/open items. |
| 4. README with exact commands and a stated limitation | Met | `README.md` gives exact `python3 notes.py ...` commands, expected output, `NOTES_DATA` usage, exit codes, test command, and explicit limits including single-user/no file locking, no edit/tags/sync, unencrypted storage, and macOS/Python 3.14.7 verification only. |
| 5. No invented implementation or deployment evidence | Met, with minor caveats | The 11 SHA-256 hashes in `docs/change-record.md` all match the delivered files. The 34-test result, test-count breakdown and CLI outputs are reproducible. No deployment, package, release or commit is claimed. The false `__pycache__` cleanup claim and the whitespace-only JSON overstatement are accuracy defects, not invented implementation or deployment evidence. |

## Test and CLI results observed

Environment: macOS, `python3` = Python 3.14.7 (Homebrew on PATH); `/usr/bin/python3` = Python 3.9.6.

### Test suite

```text
$ python3 -m unittest -v
...
Ran 34 tests in 1.684s
OK
```

I also ran the suite with `/usr/bin/python3` (3.9.6):

```text
Ran 34 tests in 1.525s
OK
```

This independently validates the README's "Python 3.9 or newer" prerequisite, which the actor had described as an unverified inference.

### CLI exercise in a temporary copy

The workspace was copied to a temporary directory so the actor's files were not used as a write target.

| Action | Observed result | Exit |
| --- | --- | --- |
| `notes.py add "Buy milk"` | `1` | 0 |
| `notes.py add "Call the dentist"` | `2` | 0 |
| `notes.py list` | `1: Buy milk` then `2: Call the dentist` | 0 |
| `notes.py search "DENT"` | `2: Call the dentist` | 0 |
| `notes.py search "missing"` | empty stdout; `No matches.` on stderr | 0 |
| `notes.py delete 99` | `error: No note with id 99.` on stderr | 1 |
| `notes.py delete abc` | argparse error: `id must be a positive integer` | 2 |
| `notes.py delete 0` | argparse error: `id must be a positive integer` | 2 |
| `notes.py delete 1` | `Deleted note 1.` | 0 |
| `notes.py list` after delete | `2: Call the dentist` | 0 |
| `notes.py add "Third note"` | `3` | 0 |
| `notes.py --help` | usage listing add, list, search, delete | 0 |
| `notes.py add "   "` | `error: note text must not be empty.` | 2 |
| `notes.py search "   "` | `error: search term must not be empty.` | 2 |
| `notes.py` with no command | argparse usage error | 2 |
| `NOTES_DATA=.../custom/nested/notes.json notes.py add "Stored elsewhere"` | `1`; nested parent created; valid JSON | 0 |
| default-path run from another cwd | created `notes.json` beside `notes.py` | 0 |
| `NOTES_DATA="" notes.py list` | `error: NOTES_DATA is set but empty; ...` | 2 |
| `NOTES_DATA="~/tmp-review-notes.json" notes.py add "tilde"` | `1`; file created in home | 0 |
| corrupt JSON file, `notes.py list` | `error: Invalid JSON ...`; file unchanged | 1 |
| data path is a directory | `error: Cannot read ... Is a directory` | 1 |
| schema version 2 | `error: Unsupported notes data version 2; expected 1.` | 1 |

After add 1, add 2, delete 1, add 3, the JSON was:

```json
{
  "version": 1,
  "next_id": 4,
  "notes": [
    {"id": 2, "text": "Call the dentist", "created_at": "..."},
    {"id": 3, "text": "Third note", "created_at": "..."}
  ]
}
```

This matches the change record's claim that a deleted highest id is not reused.

## Artifact consistency findings

- `notes.py` is a thin entry point calling `notes_app.cli.main`; the CLI, storage, search and shared errors are separate modules. No framework and no third-party imports.
- No `pyproject.toml`, `requirements*.txt`, `setup.py`, lockfile or virtual-environment dependency exists.
- The README's quickstart outputs, command table, `NOTES_DATA` behavior, exit-code table and JSON shape match observed behavior.
- The change record's R1-R8 evidence and CLI table match observed behavior.
- The change record's revision hashes all match the delivered files (verified with `shasum -a 256`).
- `docs/change-record.md` is a compact record that covers more than the four headings in the skill library's compact template; this is consistent with the task's request for a short change/evidence record.
- The workspace has no `notes.json`, no `.cli-demo/` directory, no `.git` repository, and no leftover `*.tmp` files.
- The workspace does contain `notes_app/__pycache__/` and `tests/__pycache__/` with `.pyc` files timestamped 22:46, after `EVAL.md` was written at 22:44.

## Unsupported or inflated claims

1. **False cleanup claim in `EVAL.md`.** Section 2 says: "Generated `__pycache__` directories and the temporary `.cli-demo/` data directory were removed before delivery." The `.cli-demo/` part is true, but `notes_app/__pycache__/` and `tests/__pycache__/` are still present. Their `.pyc` files predate my review run (22:46 vs. my run at 22:57), so they came from the actor's own final test run. This is a concrete false statement, although harmless to functionality.
2. **Overstated JSON strictness.** `notes_app/storage.py` says: "A zero-byte file is treated as an empty notebook. Any non-empty content must be valid JSON with the expected shape." The change record and EVAL say non-empty malformed JSON is an error. In fact, a file containing only spaces/newlines is non-empty malformed JSON but `_read()` returns an empty notebook (`if not raw.strip(): return [], 1`). I observed `NOTES_DATA=<whitespace-only-file> python3 notes.py list` exit 0 with no output. This is a minor code/comment and record mismatch; it does not damage real note data because a whitespace-only file has none.
3. **"System Python" wording.** The change record says the suite ran with the system Python. In this environment `python3` resolves to Homebrew Python 3.14.7, while `/usr/bin/python3` is Apple's 3.9.6. If "system Python" means the OS-provided interpreter, the phrase is imprecise. The suite runs under both; this is only a wording issue.
4. **Historical quickstart run.** The change record says the README quickstart was run exactly as written and exercised the default `notes.json` path. I cannot verify the historical run, but I reproduced the same commands successfully in a copy, and no default `notes.json` remains. This is credible, not contradicted.
5. **Skill-reading inventory.** `EVAL.md` lists many skill files as read. All cited paths exist, and the claimed counts (21 plugins, 73 sdlc skills) are correct. Reading itself is not independently verifiable, but the artifacts are consistent with the cited guidance. This is not a substantive concern.

No invented deployment, release, commit, package or production evidence was found. The revision identity is explicitly non-versioned and the hashes are genuine.

## Defects and missing evidence

- **Minor:** EVAL's `__pycache__` cleanup claim is false.
- **Minor:** The storage docstring and change record overstate strictness for whitespace-only files. No test covers that input; adding one test would either lock in the behavior or expose the mismatch.
- **Minor:** No test exercises an invalid schema version or a whitespace-only data file, though both are reachable through `NOTES_DATA`. The main acceptance paths are covered.
- **Minor:** The test suite does not write through the default path; that path is covered by a unit test of `default_data_path()` and by the actor's manual quickstart, which I reproduced separately.
- **Documented, not a defect:** No file locking, no concurrent-writer protection, no edit command, no encryption, and verification limited to macOS/Python 3.14.7 by the actor (I added a 3.9.6 check).
- **Documented, not a defect:** `NOTES_DATA` relative paths are resolved against the process working directory; the README says the value is used as supplied and only documents `~` expansion.

## Comparison with the actor's `EVAL.md`

`EVAL.md` is substantially accurate and not inflated. Its test count (34), test breakdown (13 CLI, 16 storage/data-path, 5 search), environment (Python 3.14.7), CLI observations, revision-hash statement, no-Git/no-publication statement, and no-deployment statement all match what I observed. Its self-assessment that all TASK.md requirements are met is correct.

The one clear inaccuracy is the claim that generated `__pycache__` directories were removed before delivery. The claim that Python 3.9 compatibility was inferred rather than executed was accurate at authoring time, and my 3.9.6 run now confirms the inference. The storage-strictness overstatement appears in both the code comment and the change record, so it is a small consistency issue rather than an EVAL-only inflation.

## Overall grade

**pass with limitations**

All five expectations are met, the CLI and persistence work, the tests pass on both Python 3.14.7 and 3.9.6, and the README/change record match observed behavior. The limitations are evidence hygiene and minor documentation accuracy, not missing functionality or invented implementation evidence.
