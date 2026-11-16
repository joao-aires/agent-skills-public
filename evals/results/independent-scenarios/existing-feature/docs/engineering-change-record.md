# Task tags and tag filtering

## 1. Overview and lifecycle

Added optional tags to tasks and a `--tag` filter to `list`. The change is **implemented and verified locally** in the working directory; it is not committed, published or deployed.

- Workspace: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/existing-feature`
- Revision: non-versioned local tree, 2026-11-15. Not published; no URL. Content hashes, not commits:

| File | Baseline SHA-256 | After change SHA-256 |
| --- | --- | --- |
| `taskcli.py` | `4472d811dd11eccf4f25bbca8dffec731914f213c3dd5bebfe164397f391d28b` | `d9ce3fbbf85594bd3d084ca3d92df887e235463826d8afc9bba83e9a87dd6a38` |
| `test_taskcli.py` | `f1f71490183fdef1fa59cf7a0a09142f319832937aaa6144ca5044e0b0e09063` | `9fcb18bb48a5e57d80374a4432c21a0feab02d157f66977289335e3f15074e5b` |
| `README.md` | `6089727e737097322c86824773088086e7ad076cf73e936d72f6ed1f01b93fd2` | `6d96193165a04307ea01308a8873dbccd4722472de27a983615ce8f9370d14e3` |

Status by claim: requirements accepted from `TASK.md`; implementation present; behavior verified by the tests and CLI run below; release not applicable.

## 2. Problem and scope

The tracker stored only a title and a `done` flag, so related tasks could not be grouped. The intended outcome is to attach zero or more tags to a task and list tasks by one exact tag, without changing the existing title-only command, output format, `done` behaviour or readable JSON records.

In scope: CLI parsing, task records, pending/all tag filtering, tests and user-facing usage notes. Out of scope: tag editing or removal, tag listing, multi-tag filters, tag display in `list` output, migrations, remote storage and release.

## 3. Requirements and acceptance

| ID | Observable acceptance | Status |
| --- | --- | --- |
| R1 | `add "title"` still creates `{"title", "done"}` and prints `added <index>`. | Passed: unit test and CLI run |
| R2 | `add "title" --tag a --tag b` stores both tags once each and preserves a multiword title. | Passed: unit test, CLI run and JSON inspection |
| R3 | `list --tag a` shows pending tasks with tag `a` only. | Passed: unit test and CLI run |
| R4 | `list --all --tag a` includes completed tasks with tag `a`. | Passed: unit test and CLI run |
| R5 | A pre-existing JSON file with no `tags` keys remains readable; `done` still works on it. | Passed: unit test |
| R6 | A missing `--tag` value exits 1, reports the error on stderr and writes no task. | Passed: unit test and CLI run |

Matching is exact and case-sensitive. Tags are trimmed; empty tags are rejected; duplicates are removed while preserving first-seen order. Untagged tasks have no `tags` key, so R1 and R5 keep the original record shape.

## 4. Solution design

Baseline: `taskcli.py` joined every argument after `add` into the title and `list` recognised only `--all`.

The chosen approach keeps the existing functions and adds an optional second parameter: `add(title, tags=None)` and `list_tasks(include_done=False, tag=None)`. The CLI uses repeatable `--tag` options, so title words are not reinterpreted as tags. `--tag=value`, `--` (end of options) and options before or after the title are supported. Tagged records add `"tags": [...]` after the existing fields; untagged records are unchanged.

Alternatives considered:

- Positional tags (`add "title" work urgent`) were rejected because they would break the existing unquoted multiword title form.
- A comma-separated `--tags a,b` option was rejected because a bare list (`--tags a b`) is ambiguous about which words are tags; repeatable `--tag` is unambiguous.
- Always writing `"tags": []` was rejected because it would change the JSON shape of existing title-only adds.

No architecture, data ownership, network or deployment boundary changed. A tag filter over local JSON needed no C4, sequence diagram, ADR or migration.

## 5. Implementation strategy

Implemented in one small increment in `taskcli.py`: tag normalisation and storage, tag-aware filtering, a shared option-value check, `add`/`list` argument parsing, and error handling in `main`. The tests were added immediately after the implementation in the same increment; strict red-before-green order was not observed. `README.md` was updated with the new commands and compatibility note. There were no dependent increments, migrations or rollout steps.

## 6. Verification and release

Environment: macOS, Python 3.14.7, standard library only, no network. Revision: the content hashes above.

- `python3 -m unittest -v` → 14 tests ran, all `ok`: 3 original tests and 11 added tests covering tagged storage, deduplication, empty tags, option placement, legacy record shape, legacy JSON, pending/all filtering, CLI title preservation, `--tag` parsing, missing values and `--`.
- A temporary-directory CLI run exercised `add` with repeated `--tag`, `add --tag=work`, legacy `add write report`, `list`, `list --tag work`, `done 0`, `list --tag work`, `list --all --tag work` and `list --all`. Outputs were as expected; the JSON showed `tags` only on tagged tasks. For example, after `done 0`, `list --all --tag work` printed `0\tx\twrite report` and `2\t \treview report`.
- `add "write report" --tag` and `list --tag` each returned exit 1 with `error: --tag requires a value` on stderr; no data file was created.
- `python3 -m py_compile taskcli.py test_taskcli.py` completed without output.
- Not run: a linter, type checker, coverage measurement or Git checks; none is configured in this directory. No release or deployment was performed.

## 7. Decision history and references

- 2026-11-15: chose repeatable `--tag` over positional tags and `--tags`, because it preserves the existing unquoted title form and avoids ambiguous parsing. Owner: implementation agent for this evaluation.
- 2026-11-15: chose exact, case-sensitive matching and order-preserving deduplication. Rationale: predictable filtering for a small local CLI; no locale or normalisation policy is established.
- 2026-11-15: omitted `tags` from untagged records and from `list` output. Rationale: preserve the documented JSON shape and existing output contract.
- Open: none required by `TASK.md`. Displaying tags in `list` and editing tags remain deliberately unimplemented.

References: `TASK.md`, `README.md`, `taskcli.py`, `test_taskcli.py` in this workspace.
