# EVAL: habit tracker CLI

Evaluation workspace: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/ideation`

Deliverable status: implemented and verified locally on 2026-11-15; not released or packaged; real-use value unmeasured.

## 1. Skills and guides discovered and read

I inspected the library root, the plugin inventory, the SDLC skill inventory and the artifact-workflow entry page, then followed links by capability. The library's `AGENTS.md` arrived as repository instructions; I treated it as maintainer guidance for the library, did not modify the library, and did not apply its packaging/build rules to this artifact. I did not open the evaluation results directory or any prior evaluation record.

### Read

| Guidance | Why I opened it | Effect on the work |
| --- | --- | --- |
| `README.md` (library), `documentation/artifact-workflow.md` | Find the entry path, artifact model and SDLC coverage | Established the artifact set and the ECR-as-spine approach; pointed to software types, homes, quality bar and contracts |
| `plugins/sdlc/skills/develop/SKILL.md` and `references/new-application-flow.md` | Shape a rough idea into a useful first slice | Turned "build a habit tracker" into a bounded slice with explicit assumptions instead of every imagined feature; confirmed a personal tool needs a short purpose/constraints assessment, not a business plan |
| `plugins/sdlc/skills/design/SKILL.md` | Decide how much design the change needs | Required a consequential choice to have materially different options and a linked artifact; moved the missed-day rule from an implementation detail to the central design decision |
| `plugins/sdlc/skills/design/references/option-set.md` | Check the option-set minimum | Caused a revision: added a Decision column per option and a single cross-option comparison artifact. The first draft had the directions but no per-option decision status and no shared comparison artifact, which was weaker |
| `plugins/sdlc/skills/design/references/design-validation.md` | Decide whether to claim design validation | Clarified that a probe after implementation is **verification**, not design validation. I removed any implication that the design had been validated before building and stated the limit |
| `plugins/sdlc/skills/artifact-system/SKILL.md` | Understand authority, maturity, homes and handoff | Kept product intent, design, change and evidence as distinct authorities rather than one blended report |
| `.../references/software-types.md` and `software-types/library-cli.md` | Classify the component and know what evidence it needs | Set the evidence bar: public surface, consumer task, compatibility, dependency surface, packaging, errors/exit codes, usage plus failure example. This drove the command table, exit-code contract and CLI subprocess tests |
| `.../references/contracts/design-proposal.md` and `plugins/sdlc/skills/guide-design-proposal/SKILL.md` | Structure the design decision | Gave the question/constraints/options/tradeoffs/seam/recommendation structure and the decision block |
| `.../references/contracts/ecr.md` and `plugins/sdlc/skills/guide-ecr/SKILL.md` | Structure the change record | Produced seven headings, per-claim maturity, past-tense verification, explicit release status and decision history |
| `.../references/contracts/prd.md` | Separate product intent from engineering claims | Caught and removed an implementation claim from the PRD during the assurance pass |
| `.../references/contracts/repository-readme.md` and `plugins/sdlc/skills/guide-readme/SKILL.md` | Make the README the front door | Added quickstart with expected result, command reference, docs map, development/reset commands, support boundary, status/limits and an explicit no-license statement |
| `.../references/quality-bar.md` | Check reader sufficiency and navigation | Required full SHA-256 local revision identity because the workspace is not a Git repository; no fake commit or bare SHA. Also drove the cold-reader and link checks |
| `.../references/assurance.md` | Check cross-artifact consistency | Found the PRD claiming implementation status; corrected it. Added a readiness disposition ("ready with limitations") and checked the artifact home map and links |
| `.../references/homes.md` and `catalog.md` | Resolve where records live | Chose `docs/product/`, `docs/design/`, `docs/change/`, `docs/evidence/` and recorded the map in `docs/README.md`, rather than inventing a competing authority |
| `.../references/contracts/work-product.md` | Check code/test identity, relations and evidence | Linked implementation to requirements and recorded the exact checked revision and limits |
| `plugins/sdlc/skills/requirements-engineering/SKILL.md` | Derive observable acceptance | Forced actor/action/observable-result/denial-path cases; prevented inventing a usage metric or SLO |
| `plugins/sdlc/skills/tdd/SKILL.md` | Build the behavior test-first | Started red with streak tests before the module existed; kept seams at the pure rule and the shipped CLI rather than private helpers. I did not follow one-test-at-a-time for every later CLI test (see gaps) |
| `plugins/sdlc/skills/test/SKILL.md` | Select and report verification evidence | Matched evidence to claims, exercised the real CLI boundary, covered failure/denial paths and recorded unverified limits |
| `plugins/sdlc/skills/change-review/SKILL.md` | Review the integrated change | Drove the review findings table and the requirement/evidence convergence check |
| `plugins/sdlc/skills/code-review/SKILL.md` | Code-diff review axes | Supplied the standards/spec separation; its Git fixed-point and parallel-subagent procedure was unavailable, so I reviewed inline against the spec and documented that adaptation |
| `plugins/backend-python-development/skills/python-automation-engineering/SKILL.md` | Python CLI operational quality | Drove atomic writes, stdout/stderr/exit-code agreement, testing the shipped command and distinguishing configured/local/live verification. Its API-completeness and pagination material did not apply |
| `plugins/backend-python-development/skills/modern-python/SKILL.md` | Python project conventions | **Rejected** its uv/pytest/ty/ruff/pyproject recommendations because the task requires standard-library only, no third-party dependencies. Kept stdlib `unittest` and a single script |

### Not read, and why

I did not read every skill in the 73-skill SDLC bundle. I skipped `activity-system/SKILL.md` (I followed the activity instructions directly), `design/references/design-review.md` (I used the proposal contract/guide review questions and an inline change review), `git-contributions` (no Git repository or publishing authority), and specialist frontend/visual/security/database skills (no matching component). This is a selection boundary, not a claim that those guides would add nothing.

## 2. Artifacts produced

| Artifact | Path | Purpose |
| --- | --- | --- |
| CLI implementation | `habits.py` | Add/list/done/undo/show/remove, streak logic, JSON store, atomic write, errors and help |
| Standard-library tests | `test_habits.py` | 11 pure streak/date tests, 4 data-path tests, 29 CLI subprocess tests (44 total) |
| Repository entry point | `README.md` | Purpose, quickstart, command surface, streak rule, data format, docs map, development, limits |
| Documentation index and home map | `docs/README.md` | Where each record is authoritative, reading order and maturity |
| Product intent | `docs/product/prd.md` | Problem/audience, outcome, scope/non-goals, success signal, constraints, open decisions |
| Design proposal | `docs/design/design-proposal.md` | Four materially different streak directions, tradeoffs/failure, surface/compatibility, seam, recommendation and decision block |
| Streak specification | `docs/design/streak-cases.md` | Worked cases, cross-option comparison, rendering examples and boundaries |
| Engineering change record | `docs/change/ecr.md` | Seven-section change account, requirements/acceptance, implementation, verification, decisions |
| Verification evidence | `docs/evidence/verification.md` | Environment, revision hashes, commands, actual results, review findings and limits |
| Raw test output | `docs/evidence/test-output.txt` | Captured `python3 -m unittest -v` output (44 tests; a later run also passed) |
| CLI transcript | `docs/evidence/cli-transcript.md` | 18 observed commands with stdout/stderr and exit codes |
| Help text | `docs/evidence/help.txt` | Observed `--help` output |
| This record | `EVAL.md` | Discovery, commands, decisions, gaps and self-assessment |

No separate issue, PR, ADR, architecture set, runbook or release note was created: there is no tracker, no Git host, no service boundary, no durable standalone decision beyond the proposal, and no release.

## 3. Commands run and actual results

All commands ran in the evaluation workspace. No network was used.

| Command / action | Actual observed result |
| --- | --- |
| `python3 -m unittest -v test_habits.StreakTests` before `habits.py` existed | `ModuleNotFoundError: No module named 'habits'`; exit 1 (intentional red) |
| `python3 -m unittest -v test_habits` after the core streak/path implementation | `Ran 15 tests in 0.005s`; `OK` |
| First full run after adding the CLI tests | `Ran 41 tests`; 1 failure. The failure exposed a test-harness bug: the helper `fail()` shadowed `TestCase.fail()`, so the assertion message was parsed as a CLI argument. Renamed the helpers; the next run exposed a real wrong substring expectation (`not JSON` vs `not valid JSON`), which was fixed |
| `python3 -m unittest -v` after fixes | `Ran 41 tests`; `OK` |
| `python3 -m unittest -v` after adding three review/edge tests | `Ran 44 tests in 4.171s`; `OK` |
| Final `python3 -m unittest -v` (captured to `docs/evidence/test-output.txt`) | `Ran 44 tests in 4.332s`; `OK`; exit 0 |
| `python3 -m py_compile habits.py test_habits.py` | No output; exit 0 |
| `python3 habits.py --help` | Exit 0; captured to `docs/evidence/help.txt` |
| 18-command CLI session with an isolated `--file` and `--today 2026-11-15` | 15 commands exited 0; 3 expected failures exited 1 (remove without `--yes`, unknown habit, future date). Full outputs in `cli-transcript.md` |
| Real-date smoke with `HABITS_FILE` and no `--today` | `add Stretch` → id `stretch`; `done stretch` → `2026-11-15`, streak 1; `list` → `STREAK 1`, `TODAY yes`, `LAST DONE 2026-11-15`; all exit 0 |
| Permission probe on a newly created parent | File mode `0o600`, directory mode `0o755` |
| `shasum -a 256 habits.py test_habits.py` | `habits.py` `00fad9c5…b13414`; `test_habits.py` `33025bb6…6915a` (full values in the ECR/verification) |
| `pwd`, `python3 --version`, `sw_vers -productVersion` | Workspace path above; Python 3.14.7; macOS 27.0.1 |
| `grep -c` / AST-style test count | 44 test methods: 11 streak, 4 path, 29 CLI; 18 transcript commands |
| Local Markdown link/anchor check (stdlib script) | 9 Markdown files checked; 0 missing files or anchors |
| `python3 -m unittest -v` in the final delivered state | `Ran 44 tests in 4.264s`; `OK`; exit 0 |

Not run: a linter/formatter, coverage reporting, other Python versions, Linux/Windows, a clean install (there is no package), concurrent-writer stress, real daily use, and crash injection during `os.replace`.

## 4. Product and design decisions

| Decision | Choice | Reason | Status |
| --- | --- | --- | --- |
| Streak/missed-day semantics | Consecutive calendar days ending today, or yesterday when today is unmarked; a missed day resets; future dates never count | Keeps a live run visible without claiming today is done; makes the break explicit; no schedules/quotas | Accepted for slice |
| Command names | `add`, `list`, `done`, `undo`, `show`, `remove`; global `--file`, `--today`, `--version` | Small, verb-first surface; a separate `show` covers detail without bloating `list` | Implemented |
| Identity | Lowercase ASCII slug from the name, collision suffix `-2`, `-3` | Human-readable references without a separate naming step; names remain display text | Implemented |
| Data model | One versioned JSON document; completions as sorted ISO dates; streak derived, not stored | Human-editable, simple, no stale counters; version guard allows refusal rather than silent migration | Implemented |
| Persistence safety | Same-directory temp file + `fsync` + `os.replace`; corrupt/unsupported file refused | Prevents a half-written file and accidental data loss; keeps recovery honest | Implemented; crash injection untested |
| Errors | 0 success/no-op; 1 data/habit error; 2 usage error; results on stdout, diagnostics on stderr | A caller can distinguish invalid invocation from a data or habit problem | Implemented and tested |
| Date control | Local date by default; `--today` override; `done/undo --date` for a specific day | Deterministic tests and timezone/demo correction without storing timestamps | Implemented |
| Removal | Requires `--yes` | Deleting history is irreversible; a confirmation flag avoids an accidental keystroke | Implemented and tested |
| Backfill before creation | Allowed; `created_on` is metadata | Lets a user start tracking and enter recent history | Implemented |
| Concurrency | No lock; last writer wins | Single-person local tool; a lock is disproportionate for the slice | Recorded limit |
| Packaging | No package or install | The request is a small local CLI; invocation from the directory is enough | Deferred |

Assumptions stated in the records: the requester accepts the chosen semantics for this slice; one local user; plaintext data is acceptable; local calendar dates are sufficient; Python 3.14.7/macOS is the only exercised environment; no external consumers depend on the file format yet. Rejected options: strict today-required, rolling quota and per-habit schedule (reasons and failure behavior in the design proposal).

## 5. Gaps, contradictions and discovery friction

1. **Direct tooling conflict.** `modern-python` says to use uv, pytest, ruff, ty and pyproject, and treats pytest as replacing `unittest`. The task requires Python standard library only and no third-party dependencies. I followed the task constraint and used `unittest`, a single script and no project manifest. This is a real contradiction in the available guidance, resolved by the explicit request.
2. **TDD seam confirmation.** `tdd` says to agree test seams with the user before writing tests. This was an unattended subagent task with no user available. I stated the two seams myself (pure date/streak rule; shipped CLI subprocess) and recorded that assumption rather than silently claiming agreement.
3. **Code-review procedure.** `code-review` assumes a Git fixed point, a diff and two parallel subagents. The workspace is not a Git repository and no subagent facility was used. I reviewed inline using the standards/spec axes, but there is no base-to-head diff or independent review evidence. This is a weaker review than the guide describes.
4. **ECR home versus requested layout.** The artifact system defaults the ECR to an engineering workspace outside the application repository. The task explicitly asks for product/change/design/evidence records in `docs/` in this directory. I used `docs/change/ecr.md` as the authorized home and recorded that map, rather than creating a sibling workspace the task did not request.
5. **No publication or renderer.** The quality bar asks for a read-back of the rendered view. These are local Markdown files with no provider, browser or renderer in scope. I read the files back as text and ran a relative-link/anchor check; I did not verify a rendered HTML view.
6. **No clean consumer test.** `library-cli` and `design-validation` ask for a consumer/install test. There is no package, so only direct invocation from this workspace was tested. The compatibility claim is deliberately narrow.
7. **No Git identity.** The quality bar forbids bare SHAs and requires a link or an explicit local-only revision. I used the absolute workspace path and full SHA-256 values with "not published; content hash, not a commit". There is no URL, diff, PR or commit to inspect.
8. **Single-file size.** `habits.py` is 566 lines including docstrings, help text and validation. A multi-module layout might be cleaner for a larger product, but a single runnable script matches the "small local CLI" and avoids import-path complications. The tests do not require installation.
9. **`python-automation-engineering` scope mismatch.** Its API collection, pagination, resumable mutation and provenance advice largely does not apply to a local JSON file. I applied the parts that do: atomic exports, exit/output agreement, failure visibility, CLI testing and local-versus-live evidence distinctions.
10. **Discovery cost.** The library has 21 plugins and 73 SDLC skills with overlapping names (`design`, `design-system`, `guide-design-proposal`, `frontend-design`). The capability map and artifact-workflow page were necessary to avoid reading the wrong layer. A small CLI has no single obvious entry skill; `develop` plus the library/CLI software type was the useful path.
11. **No measurement of product value.** The automated tests prove the defined behavior, not that the owner uses it or benefits. The success signal is explicitly proposed and unmeasured. No claim of behavior change is made.
12. **Review limitations.** The inline review found real defects, but it was not independent, had no diff baseline, and did not use a linter/type checker. The suite has no coverage measurement.

## 6. Self-assessment against IDEA.md

| IDEA item | Result | Evidence / gap |
| --- | --- | --- |
| Track a few daily habits | Done | `add`, `list`, `show`; list rows per habit |
| Mark a habit done for today | Done | `done`, idempotent, reports streak; `--date` for backfill |
| Show the current streak for each habit | Done | `list` STREAK column; `show` current/longest and 7-day history; rule explicit in README, design and tests |
| Keep everything in a local JSON file | Done | Versioned `habits.json`; `--file`/env/XDG/home precedence; atomic replacement; corrupt file refused |
| No third-party dependencies | Done | Only Python stdlib imports; `unittest` tests; no package install |
| Decide command names, data model, missed-day handling | Done | Command table, data schema and Option A documented; alternatives and tradeoffs recorded |
| Take the idea through a useful implementation | Done for the slice | 44 tests pass; 18-command CLI transcript; README and docs; no release claim |
| Produce application, tests, README and docs/ product/change/evidence record | Done, plus a design record | Files listed in section 2; `docs/README.md` maps them |

**Scope judgment.** The result is a useful slice, not a platform: one script, one local file, six commands, no accounts, sync, reminders, schedules or UI.

**What is not done.**

- No real week of personal use; no measured reduction in manual counting or improvement in consistency.
- No packaging/install path, global command or release artifact.
- No reminders, notifications, sync, multi-user access, web/mobile UI or calendar integration.
- No weekly targets, planned rest days, per-habit schedules or freeze tokens.
- No import/export, backup automation, encryption or data migration beyond version refusal.
- No concurrency lock; no tested crash-injection around `os.replace`.
- No verification on other Python versions, Linux or Windows.
- No linter, type checker, coverage report or independent code review.
- No license granted (explicitly stated, not invented).
- No PR, issue, commit or rendered documentation view, because this workspace has none of those.

**Status statement.** Implemented and verified locally at the recorded content hashes; ready with limitations for personal local use. Not released, not production-ready, and not evidence of a real behavior change.
