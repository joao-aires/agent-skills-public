# Evaluation record

Date: 2026-11-15
Workspace: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/existing-feature`
Task: `TASK.md` — add tags and tag filtering to the existing task CLI.
Constraints applied: work only in this directory, no skill-library changes, no network or third-party dependencies, Python 3 standard library only.

## 1. Skills, guides and discovery

### What I inspected

- Listed the workspace and the skill-library root and plugin directories.
- Enumerated `plugins/sdlc/**/SKILL.md` and `plugins/backend-python-development/**/SKILL.md` to find candidate guidance rather than assuming a fixed list.
- Read these library files (paths relative to `/Users/joao/Projects/products/agent-skills-artifact-quality`):
  - `README.md`, `AGENTS.md`
  - `plugins/sdlc/skills/develop/SKILL.md`
  - `plugins/sdlc/skills/implement/SKILL.md`
  - `plugins/sdlc/skills/test/SKILL.md`
  - `plugins/sdlc/skills/tdd/SKILL.md`
  - `plugins/sdlc/skills/change-review/SKILL.md`
  - `plugins/sdlc/skills/guide-ecr/SKILL.md`
  - `plugins/sdlc/skills/project-conventions/SKILL.md`
  - `plugins/sdlc/skills/artifact-system/SKILL.md`
  - `plugins/sdlc/skills/artifact-system/references/quality-bar.md`
  - `plugins/sdlc/skills/artifact-system/references/homes.md`
  - `plugins/sdlc/skills/artifact-system/references/storage/coordination.md`
  - `plugins/sdlc/skills/artifact-system/references/contracts/ecr.md`
  - `plugins/backend-python-development/skills/backend-conventions/SKILL.md`
  - `plugins/backend-python-development/skills/python-automation-engineering/SKILL.md`
  - `plugins/backend-python-development/skills/modern-python/SKILL.md`

I did not open `evals/results/behavioral-scenarios` or any prior evaluation record.

### What changed my approach

- **`python-automation-engineering`** was the strongest fit. Its emphasis on a CLI's exit status, stdout/stderr and mutation result agreeing, and on testing the packaged command rather than only helpers, led to CLI-level tests, stderr for option errors, exit 1, and a test proving a failed `add` writes nothing.
- **`test`** shaped the acceptance and evidence: test the changed behavior plus preserved behavior and failure paths, run the full relevant suite, and report unavailable checks. It led to the legacy-JSON test and the explicit “not run” list.
- **`tdd`** supplied the public-seam and anti-tautology criteria. I used the existing function seam (`add`, `list_tasks`) and added `main()` as the CLI seam, with literal expected output. I did **not** follow its red-before-green rule; see gaps.
- **`guide-ecr` + `ecr.md` + `quality-bar.md`** determined the `docs/` record: seven compact sections, past-tense evidence, explicit maturity, alternatives and the non-versioned-local revision form with full SHA-256 hashes and “not published”.
- **`project-conventions`** reinforced preserving the existing one-file layout, `unittest` runner and command style instead of restructuring the fixture.
- **`develop` / `implement`** shaped the small-slice approach: preserve existing architecture, keep unrelated cleanup out, run the suite, and distinguish implemented from verified and released.
- **`change-review`** shaped the closing self-review and the requirement to label it as self-review, not independent assurance.

### Read but not applied, or applied only partly

- **`backend-conventions`** mostly targets FastAPI/SQLAlchemy services and was not applicable. Its general “preserve accepted choices and verify observable behavior” points were applied.
- **`modern-python`** recommends `uv`, `ruff`, `ty` and `pytest`. Its own “When NOT to use” section and the project's existing `unittest`/stdlib setup meant I did not migrate tooling. The task also forbids third-party dependencies.
- **`artifact-system` homes/coordination** normally put an ECR in an engineering workspace and require a storage-choice question. `TASK.md` explicitly requests a short `docs/` record, which answered the storage question and overrode the default home.
- **`AGENTS.md`** is maintainer guidance for the skill repository, not for this fixture. I read it for artifact/verification principles but did not run its plugin-repository checks or edit the library.

## 2. Artifacts produced

- `taskcli.py` — optional tags on `add`, tag filtering on `list_tasks`, `--tag` parsing for `add`/`list`, stderr errors for missing values, unchanged `done`.
- `test_taskcli.py` — 14 tests: 3 original tests preserved and 11 added for tags, filtering, legacy JSON, CLI behavior and failure paths.
- `README.md` — updated commands and current-behaviour notes. (Not explicitly required, but the usage changed.)
- `docs/engineering-change-record.md` — compact seven-section ECR with baseline/current hashes and observed verification.
- `EVAL.md` — this record.

No files in the skill library were modified. No temporary data files remain; CLI checks used `tempfile.TemporaryDirectory()`.

## 3. Commands run and observed results

### Discovery

- `ls -la` in the workspace → showed `README.md`, `TASK.md`, `taskcli.py`, `test_taskcli.py`, `__pycache__`.
- `ls -la` and `ls plugins` in the skill library → showed the plugin set, including `sdlc` and `backend-python-development`.
- `find .../plugins/sdlc -name SKILL.md | sort` → returned the SDLC skill inventory (activities, guides, methods and support skills).
- `find .../plugins/backend-python-development -name SKILL.md | sort` → returned `backend-conventions`, `modern-python` and `python-automation-engineering`.

### Baseline

- `python3 --version` → `Python 3.14.7`.
- `python3 -m unittest -v` → 3 tests ran, all `ok`.
- `shasum -a 256 taskcli.py test_taskcli.py README.md` → baseline hashes recorded in the ECR.

### Final verification

- `python3 -m unittest -v` → **14 tests ran, all `ok`**:
  - original: add/list pending, done persistence, unknown index
  - added: tag persistence/deduplication, legacy record shape, empty tag rejection, tag filtering with `done`, legacy JSON readability, CLI legacy title/output, CLI add/filter/done, missing `--tag` value, missing list tag value, `--` escape, option before title.
- CLI smoke run in a temporary directory using `python3 taskcli.py ...`:
  - `add "write report" --tag work --tag urgent` → exit 0, `added 0`
  - `add "buy milk" --tag home` → exit 0, `added 1`
  - `add "review report" --tag=work` → exit 0, `added 2`
  - `add "legacy style title"` → exit 0, `added 3`
  - `list` → `0\t \twrite report`, `1\t \tbuy milk`, `2\t \treview report`, `3\t \tlegacy style title`
  - `list --tag work` → `0\t \twrite report`, `2\t \treview report`
  - `done 0` → exit 0, `done write report`
  - `list --tag work` → `2\t \treview report`
  - `list --all --tag work` → `0\tx\twrite report`, `2\t \treview report`
  - `list --all` → all four tasks, with task 0 marked `x`
  - JSON inspection → tagged records had `tags`; the legacy-style record had no `tags` key.
- Invalid-input run:
  - `add "write report" --tag` → exit 1, stdout empty, stderr `error: --tag requires a value`; no data file created.
  - `list --tag` → exit 1, stdout empty, same stderr message.
  - `add` and `unknown` → exit 1, stdout `unknown command` (existing behaviour preserved).
- `python3 -m py_compile taskcli.py test_taskcli.py` → exited 0 with no output.
- Final `shasum -a 256`:
  - `taskcli.py` → `d9ce3fbbf85594bd3d084ca3d92df887e235463826d8afc9bba83e9a87dd6a38`
  - `test_taskcli.py` → `9fcb18bb48a5e57d80374a4432c21a0feab02d157f66977289335e3f15074e5b`
  - `README.md` → `6d96193165a04307ea01308a8873dbccd4722472de27a983615ce8f9370d14e3`
  - `docs/engineering-change-record.md` → `8d3848765b5badc391323fc283c987edf40e689b932c4f6ce231f118a673587c`

## 4. Decisions and assumptions

- **Tag syntax:** repeatable `--tag <tag>` for `add`, plus `--tag=<tag>`. `list` accepts one `--tag` filter. This preserves the unquoted multiword title form and matches the `list --tag` wording in the task.
- **Rejected syntax:** positional tags and a comma-separated `--tags` option. Positional tags would break `add write report`; a bare `--tags a b` is ambiguous about where the title ends. `--` remains available to keep option-like words in a title.
- **Tag identity:** exact, case-sensitive strings; trim surrounding whitespace; reject empty tags; deduplicate while preserving first-seen order. No case-folding or locale rules were specified.
- **Storage shape:** tagged tasks gain `"tags": [...]` after the existing fields. Untagged tasks and existing files keep the original shape; no migration is needed.
- **Output:** `list` keeps its existing columns and does not print tags, to preserve the output contract. Filtering is the requested addition.
- **Errors:** new option-value errors go to stderr with exit 1 and do not write data. Existing “unknown command” text and exit 1 were preserved.
- **Parser looseness:** unrecognised `add` words still join the title, and unrecognised `list` arguments are still ignored, preserving the old CLI's permissive behavior. Recognised `--tag` options are the only new exception to title joining.
- **Artifact home:** the ECR is in `docs/` because `TASK.md` explicitly asked for it, even though the library's default ECR home is an engineering workspace.
- **No tag display/editing:** not requested; left out to keep scope and output stable.

Assumptions a different reviewer might challenge: the expected CLI spelling was not specified by `TASK.md`; an evaluator expecting `--tags`, positional tags or `@tag` syntax would exercise a different interface. I chose repeatable `--tag` as the least disruptive form and documented it.

## 5. Gaps, contradictions and discovery friction

- **TDD seam confirmation vs. unattended task:** `tdd` says to confirm test seams with the user before writing tests. The task says not to ask the user. I used the existing, visible seams (`add`, `list_tasks`, `main`) and treated that as the confirmation substitute.
- **TDD red-before-green not followed:** I implemented the behavior in `taskcli.py` and then wrote the tests in the same increment. The tests fail if the tag behavior is removed, but I did not observe a red state first. This is a real process gap.
- **Storage-choice question:** `artifact-system/references/storage/coordination.md` says to ask which storage to use. `TASK.md` already designated `docs/`, so asking would have contradicted the task. I treated the task as the answer.
- **ECR default home:** `homes.md` defaults ECRs to an engineering workspace; the task explicitly requested `docs/`. I followed the task and recorded the deviation.
- **Injected repository instructions:** the skill library's `AGENTS.md` arrived as repository instructions. It is about maintaining the skill collection, not this fixture. Applying it literally would have meant editing `plugins/` or running collection checks, which the task forbids. I separated its principles from its maintainer commands.
- **`modern-python` vs. existing project:** its default stack (uv/ruff/ty/pytest) conflicts with the fixture's `unittest` and the stdlib-only constraint. Preserving the project won.
- **`guide-ecr` ownership:** the ECR asks for decision owners. In an unattended evaluation the only owner is the implementation agent; there was no external product or design signoff.
- **No configured lint/type/coverage checks:** none exist in the directory, so I did not invent or install them. `py_compile` is not a linter.
- **Self-review only:** no independent reviewer or second agent reviewed the diff. The `change-review` guidance explicitly distinguishes this from independent assurance.
- **Untested edge behaviours:** repeated `list --tag` currently uses the last value and has no test; case-sensitive matching is documented but not separately tested; `add(title, "work")` accepts a single string through `normalize_tags` but only list inputs are tested. These are low-risk, but they are not claimed as verified.
- **Single environment:** all checks ran on macOS with Python 3.14.7. No other Python version, platform or data file with unusual encoding was tried.

## 6. Self-assessment against `TASK.md`

| Requirement | Assessment |
| --- | --- |
| `add` accepts one or more tags without breaking `add "title"` | **Met.** Repeatable `--tag`; legacy title joining and record shape tested; CLI run confirmed. |
| `list --tag <tag>` shows pending tasks with that tag | **Met.** Unit and CLI checks passed. |
| `list --all --tag <tag>` shows all tasks with that tag | **Met.** Unit and CLI checks passed, including a completed tagged task. |
| Existing JSON without tags remains readable | **Met.** Hand-written legacy JSON was listed, filtered, marked done, and extended with a tagged task. |
| Existing `list`, `list --all`, `done` and test behavior preserved | **Met.** All three original tests pass unchanged; CLI output for `list --all` and `done` was observed. `list` output columns are unchanged. |
| Tests for tags, filtering and backward compatibility | **Met.** 11 tests added; full suite of 14 passes. |
| `docs/` record of change, decisions and verification | **Met.** `docs/engineering-change-record.md` has the seven ECR sections, alternatives, hashes and observed commands. |
| `EVAL.md` with discovery, artifacts, commands, decisions, gaps and self-assessment | **Met** by this file. |

**Not done or deliberately out of scope:** tag editing/removal, showing tags in `list`, multi-tag filtering, a migration, a linter/typechecker/coverage run, a Git commit/PR, and release or deployment. There is no claim of independent review or production readiness. Within the requested scope, the implementation and observed verification are complete.
