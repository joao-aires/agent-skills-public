# EVAL: notes CLI exercise

## 1. Skills and guides discovered and read

I inspected the skill library at `/Users/joao/Projects/products/agent-skills-artifact-quality` without modifying it. I did not read `evals/results/behavioral-scenarios` or any prior evaluation record.

Discovery started at the repository `README.md`, `AGENTS.md`, the `plugins/` directory and `plugins/sdlc/README.md`. The task is a small local Python CLI, so I followed the `sdlc` activity and artifact guidance and the `backend-python-development` package rather than the frontend, AI, database, operations or product-strategy packages.

Read in full or in the relevant sections:

| Source | Why read |
| --- | --- |
| `README.md`, `AGENTS.md`, `plugins/sdlc/README.md` | Collection structure, plugin selection and the artifact/activity model. |
| `plugins/sdlc/skills/develop/SKILL.md` | New-application flow and the implementation/verification loop. |
| `plugins/sdlc/skills/develop/references/implementation-flow.md` | Local implementation when no client commands or Git flow exist. |
| `plugins/sdlc/skills/implement/SKILL.md` | Small verified increments, local checks and handoff. |
| `plugins/sdlc/skills/test/SKILL.md` | Matching evidence to claims, persistence and failure-path coverage. |
| `plugins/sdlc/skills/change-review/SKILL.md` | Self-review of changed behavior and evidence. |
| `plugins/sdlc/skills/activity-system/references/project-fit.md` | Proportionality for a small tool; avoiding unnecessary ceremony. |
| `plugins/sdlc/skills/artifact-system/references/quality-bar.md` | Self-contained record, past-tense evidence, local-only revision form. |
| `plugins/sdlc/skills/artifact-system/references/homes.md`, `catalog.md` | Choosing the README and change-record homes. |
| `plugins/sdlc/skills/artifact-system/references/software-types.md`, `software-types/library-cli.md` | Required design evidence for a CLI: surface, compatibility, errors, packaging. |
| `plugins/sdlc/skills/artifact-system/references/contracts/ecr.md`, `repository-readme.md`, `work-product.md` | Compact ECR content, README content and work-product evidence. |
| `plugins/sdlc/skills/guide-readme/SKILL.md`, `guide-ecr/SKILL.md` | README and change-record structure and common failures. |
| `plugins/backend-python-development/skills/python-automation-engineering/SKILL.md` and `references/automation-guide.md` | CLI/config, storage/client, pure planning, atomic writes, exit codes, testing the real entrypoint. |
| `plugins/backend-python-development/skills/modern-python/SKILL.md` | Python project/tooling defaults and the conflict with this task's constraints. |
| `plugins/backend-python-development/skills/backend-conventions/SKILL.md` | Persistence, failure and verification guidance; mostly not applicable to a JSON CLI. |
| `plugins/documentation/skills/technical-writing/SKILL.md`, `humanizer/SKILL.md` | Reader fit, exact commands and prose review. |

### Which guidance changed the approach

- `project-fit.md` and the compact ECR mode stopped me from producing a PRD, ADR, issue graph or seven-section record for a one-component tool.
- `library-cli.md` made the exit-code contract, failure-path example, dependency surface and command surface explicit design evidence.
- `python-automation-engineering` changed the implementation: argparse, separate CLI/storage/search boundaries, atomic replacement of the JSON file, a documented exit-code convention, and tests through the actual `notes.py` entry point rather than only helper functions.
- `test/SKILL.md` changed verification: I exercised persistence across processes, observed deleted state by listing again, and covered corrupt data, missing ids and invalid input instead of only the happy path.
- `guide-readme` and the README contract changed the README structure: prerequisites, quickstart with expected output, data location and precedence, exit codes, docs map, limitations and an explicit no-license statement.
- The quality bar made me use a non-versioned local revision form with full SHA-256 hashes and "not published" instead of inventing a commit link.
- `modern-python` changed the approach by making the conflict explicit. I rejected its uv, Ruff and pytest defaults because the task requires standard-library tests and no third-party dependencies.
- `humanizer` shaped the prose: active voice, concrete claims, no em dashes and no staged significance.

## 2. Artifacts produced

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

Generated `__pycache__` directories and the temporary `.cli-demo/` data directory were removed before delivery. No `notes.json` was left in the workspace.

## 3. Commands run and actual results

### Environment

```text
$ python3 --version
Python 3.14.7
```

### Test suite

```text
$ python3 -m unittest -v
...
Ran 34 tests in 1.577s

OK
```

All 34 tests passed. The suite contains 13 subprocess tests of `notes.py`, 16 storage and data-path tests, and 5 search tests. No test was skipped.

### CLI exercise

The first manual exercise used `NOTES_DATA="$PWD/.cli-demo/notes.json"`, so it did not touch the default file. A later run of the README quickstart did exercise the default path. The table below omits the environment prefix for readability.

| Command | Actual result |
| --- | --- |
| `python3 notes.py add "Buy milk"` | stdout `1` |
| `python3 notes.py add "Call the dentist"` | stdout `2` |
| `python3 notes.py list` | stdout `1: Buy milk`, then `2: Call the dentist` |
| `python3 notes.py search "DENT"` | stdout `2: Call the dentist` |
| `python3 notes.py search "missing"` | empty stdout, stderr `No matches.` |
| `python3 notes.py delete 99` | stderr `error: No note with id 99.`, exit 1 |
| `python3 notes.py delete abc` | argparse error `id must be a positive integer`, exit 2 |
| `python3 notes.py delete 1` | stdout `Deleted note 1.` |
| `python3 notes.py list` after delete | stdout `2: Call the dentist` |
| `python3 notes.py add "Third note"` | stdout `3` |
| `python3 notes.py --help` | usage text listing add, list, search and delete |

The JSON file after the two adds contained `"version": 1`, the two notes and `"next_id": 3`, with timestamps such as `2026-11-15T22:37:23Z`. After the third add, `"next_id"` was 4. In a separate `NOTES_DATA` file, I added ids 1 and 2, deleted id 2 and added again; the new id was 3, and a list showed notes 1 and 3. The highest deleted id was not reused.

The first attempt to print an exit code used `status=$?` in zsh, where `status` is a read-only special variable. That shell attempt failed before printing the captured code. I reran with `code=$?`; the observed codes in the table above come from that rerun and from the subprocess tests.

A concurrent `cat` during the `add "Third note"` command printed a file state that did not yet include the third note. That observation is consistent with the documented lack of locking; it is not evidence of a partial JSON write.

### README quickstart with the default path

I ran the quickstart commands exactly as written, with no `NOTES_DATA` override. They created `notes.json` beside `notes.py` and produced:

- `add "Buy milk"` printed `1`.
- `add "Call the dentist"` printed `2`.
- `list` printed both notes.
- `search "DENTIST"` printed `2: Call the dentist`.
- `delete 1` printed `Deleted note 1.`

A following `list` printed only `2: Call the dentist`. I then deleted note 2 and removed the default data file so the delivered workspace has no note data.

### Revision hashes

`shasum -a 256` was run over the implementation, tests and README. The full values are in `docs/change-record.md`. No Git commit exists, and no publication occurred.

## 4. Decisions and assumptions

- **Default data path:** `notes.json` beside `notes.py`, not the process working directory. This keeps invocation from another directory predictable. The default path was unit-tested and exercised by the README quickstart.
- **Ids:** sequential positive integers with a persisted `next_id`, so a deleted highest id is not reused. This avoids stale references without UUID typing friction.
- **Search:** case-insensitive `casefold()` over literal substrings, not regexes. No matches returns exit 0 because the search completed successfully.
- **Input:** outer whitespace in note text is preserved; whitespace-only note text and search terms are rejected. The term is not normalized beyond the case fold.
- **Storage:** UTF-8 JSON with a version field. Non-empty malformed JSON is a data error. A zero-byte file is treated as empty. Writes use a same-directory temporary file and `os.replace`.
- **Configuration:** `NOTES_DATA` is used as supplied after `~` expansion. An empty or whitespace-only value is an explicit exit-2 error.
- **Exit codes:** 0 success, 1 operation/data failure, 2 usage/input/configuration error.
- **Python version:** the code uses features available in 3.9. The claim "Python 3.9 or newer" is an assumption; only 3.14.7 was executed.
- **Scope:** no edit command, tags, backup, sync or encryption; none were requested, and adding them would widen the surface without acceptance criteria.

## 5. Gaps, contradictions and discovery friction

- **No single entry point for "small local CLI".** The root README lists 21 plugins, and the sdlc plugin has 73 skills. I had to read the root and sdlc READMEs plus the activity and software-type references to choose a proportionate path.
- **`modern-python` conflicts with the task.** It recommends uv, Ruff and pytest, and lists pytest as a replacement for unittest. The task forbids third-party dependencies and asks for standard-library tests. I followed the task and the repository instruction that technical guidance applies only to matching accepted choices. The conflict is recorded rather than hidden.
- **Automation guidance is broader than the task.** `python-automation-engineering` recommends a packaged project, lockfile, versioned structured results, dry runs and resumable mutations. I used the applicable parts (argparse, boundaries, atomic writes, exit codes, real-entrypoint tests) and left the rest out as disproportionate.
- **Artifact ceremony risk.** The ECR contract describes a full seven-section record; `project-fit` and the compact mode justify a shorter record. The task asks for a "short" docs record, so the compact form is intentional.
- **No artifact home map or `AGENTS.md` in the workspace.** I used the default homes: README at the root and the change record under `docs/`. There was no established map to follow.
- **No Git history.** The quality bar's local-only revision form was necessary. A bare hash or invented commit link would have been misleading.
- **No license.** The README guide asks for a license link or an explicit statement; I stated that no license is declared.
- **Optional skill discovery.** `python-automation-engineering` is marked `user-invocable: false`; it was found by browsing the package, not through a user-facing skill list. This is expected from the metadata, but it makes capability discovery depend on directory inspection.
- **No independent review.** I reviewed the diff and ran the checks myself. That is self-review, not independent assurance.

## 6. Self-assessment against TASK.md

| Requirement | Assessment |
| --- | --- |
| `python3 notes.py add "text"` stores a note and prints its id | Met. Observed stdout `1`, `2`, `3` in separate runs. |
| `python3 notes.py list` lists notes | Met. Observed `id: text` output in ascending id order. |
| `python3 notes.py search "term"` finds notes containing the term | Met. Case-insensitive literal substring search; observed matching and no-match behavior. |
| `python3 notes.py delete <id>` deletes a note | Met. Observed deletion, confirmation and subsequent list. |
| Notes persist in a local JSON file; `NOTES_DATA` overrides the path | Met. Persistence across subprocesses and custom path behavior were tested and exercised. |
| No third-party dependencies | Met. Standard library only; no install step. |
| Standard-library tests and README with exact commands | Met. `python3 -m unittest -v` ran 34 passing tests; README commands were exercised. |
| Clear separation between CLI, storage and search | Met. Separate modules with a thin entry point; pure search and storage tests. |
| Short docs record of change, design decisions and observed verification | Met in `docs/change-record.md`, with exact commands, results, hashes and limits. |

Not done or not fully established:

- No concurrency lock or lost-update protection. A single writer is assumed.
- No edit command, tags, export, backup or encryption.
- Python 3.9 compatibility is inferred from the syntax, not executed.
- Only macOS and Python 3.14.7 were verified.
- Symlink targets, file permission policy and disk-full write failures were not exercised.
- No independent review, deployment, packaging or release.

Overall: the requested local CLI, tests, README and evidence record are complete for the stated scope. The remaining items are explicit limits, not hidden claims.
