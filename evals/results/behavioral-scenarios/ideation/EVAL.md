# EVAL: shaping the habit-tracker idea with the SDLC skills

**Scope of this evaluation:** one unattended run that took [`IDEA.md`](IDEA.md) from a rough request to a working local CLI, tests, user documentation and an engineering change record. The skill repository was read only; it was not modified. No network access or third-party dependency was used. Python 3 standard library only.

**Result:** all required outputs exist and the observed checks pass. The product and engineering claims are limited to what was actually run on macOS with Python 3.14.7 and 3.9.6.

## 1. Skills read and their effect

All paths below are under `/Users/joao/Projects/products/agent-skills-artifact-quality/plugins/sdlc/skills/`.

| Skill | What it changed in the work |
| --- | --- |
| `activity-system/SKILL.md` | Routed the request as plan → refine → design → implement → test → review, with the ECR as the coordination spine. Its "do not silently invoke a later activity" rule was overridden by the task's explicit end-to-end instruction, not ignored by accident. Kept one coherent change rather than one artifact per phase. |
| `artifact-system/SKILL.md` | Supplied the artifact model and quality bar: maturity per claim, past-tense evidence, resolvable or explicitly local-only references, one authority per concern. Drove the local-only SHA-256 revision note and the separation of product intent, design, ECR and verification. |
| `plan/SKILL.md` | Chose the smallest useful slice (add/done/list, plus remove for correction) and named what to defer. Prevented a roadmap, sync or notification platform from appearing. |
| `refine/SKILL.md` | Converted the idea into actionable behavior and observable acceptance. Because no user could answer in an unattended run, it drove explicit assumptions (grace streak, local date, one writer) rather than invented preferences. |
| `requirements-engineering/SKILL.md` | Added actor/trigger/observable-result framing, denial and failure cases (duplicate add, unknown habit, corrupt file), and quality constraints (data safety, dependency surface). Prevented invented numeric SLOs; latency is explicitly unmeasured at a stated personal scale. |
| `design/SKILL.md` | Identified the component as `library-cli` and required a command surface, compatibility, errors/exit codes and usage evidence. Forced the streak question to be treated as a consequential choice with alternatives instead of an unstated implementation detail. |
| `implement/SKILL.md` | Minimal effect: the installed skill is a 15-line stub that says to use `/tdd`, typecheck, `/code-review` and commit. Those commands and a git repository were unavailable, so I implemented directly, ran `unittest`/`py_compile`, and performed the review pass manually. |
| `test/SKILL.md` | Required a claim before implementation, checks matched to the claim, and explicit failed/skipped/unavailable evidence. Drove 33 tests plus real CLI failure-path exercises, and the coverage-gap list instead of claiming "all tested". |
| `review/SKILL.md` | Prompted tracing each behavior from CLI parsing through storage and display, with severity, impact and actionable fix. Produced six concrete findings, including a real date-validation bug caught during testing. |
| `guide-prd/SKILL.md` | Structured `docs/product.md` around problem, audience, outcome, non-goals, success signals, risks and open decisions. Kept it product intent rather than a feature inventory. |
| `guide-ecr/SKILL.md` | Structured `docs/ecr.md` with the seven required sections, current state first, separate proposed/implemented/verified/released claims, and past-tense verification. |
| `guide-design-proposal/SKILL.md` | Structured `docs/design.md`: decision first, materially different options, linked command/schema/state artifacts, trade-offs, failure behavior, one seam decision and a decision block. |
| `guide-design-spec/SKILL.md` | No UI design specification was produced because there is no graphical interface. Its state-completeness discipline was still useful: the design records the four streak display states and the CLI failure states explicitly. |
| `guide-issue/SKILL.md` | No issue was published: there is no tracker, remote or authorization to create one. Its pickup test informed the self-contained ECR/README handoff and the "what is blocked" statements. |
| `guide-pr/SKILL.md` | No PR was created: the workspace is not a git repository and has no remote. Its evidence discipline (command, result, revision; no merge-as-release claim) carried into `docs/verification.md`. |
| `guide-readme/SKILL.md` | Produced the front-door README: audience, status, prerequisites, a copyable demo quickstart that avoids the real home file, command reference, streak rules, tests, docs map and limits. |

Supporting references read to apply the artifacts honestly:

| Reference | Effect |
| --- | --- |
| `artifact-system/references/contracts/ecr.md` | Exact seven-section ECR contract and sufficiency floor. |
| `artifact-system/references/contracts/design-proposal.md` | Three-option requirement, linked-artifact and decision-block contract. |
| `artifact-system/references/software-types/library-cli.md` | Command surface, compatibility, dependency, packaging and exit-code evidence for a CLI. |
| `artifact-system/references/quality-bar.md` | Self-contained context, maturity/evidence, resolvable navigation and single-authority checks. |

## 2. Artifacts produced

| Artifact | Role |
| --- | --- |
| [`habits.py`](habits.py) | Working single-file CLI, 352 lines, standard library only. |
| [`test_habits.py`](test_habits.py) | 33 standard-library tests for streak rules, storage, CLI behavior and error paths. |
| [`README.md`](README.md) | User entry point with exact commands, streak rules, data format, exit codes, tests and limitations. |
| [`docs/product.md`](docs/product.md) | Product intent: problem, audience, scope, success signals, constraints, risks and open decisions. |
| [`docs/ecr.md`](docs/ecr.md) | Engineering change record with the required seven sections and current evidence. |
| [`docs/design.md`](docs/design.md) | Accepted design: streak, storage and command-surface options and decisions. |
| [`docs/verification.md`](docs/verification.md) | Claim, revision, environment, commands, observed results, review findings and gaps. |
| [`EVAL.md`](EVAL.md) | This evaluation. |

Ephemeral CLI fixtures were written under `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/habits-final2/` and are not part of the deliverable. The author's real `~/.habits.json` was not touched.

## 3. Commands and actual results

All commands below were run from the eval workspace. The checked revision is local-only and not published.

```sh
python3 -m unittest -v
```

Observed: `Ran 33 tests in 0.024s` / `OK`.

```sh
/usr/bin/python3 -m unittest -v
```

Observed: `Ran 33 tests in 0.032s` / `OK` (Python 3.9.6).

```sh
python3 -m py_compile habits.py test_habits.py
```

Observed: exit 0, `py_compile=ok`.

```sh
python3 habits.py --help
```

Observed: exit 0; usage, command list, `--file` help and the streak-grace explanation were printed.

```sh
python3 habits.py --file "$F" list
python3 habits.py --file "$F" add "Read 10 pages"
python3 habits.py --file "$F" add "Walk"
python3 habits.py --file "$F" done "read 10 PAGES"
python3 habits.py --file "$F" done "Read 10 pages"
python3 habits.py --file "$F" list
```

Observed:

```text
No habits yet.
Add one with: habits.py add "Read 10 pages"
Added "Read 10 pages".
Added "Walk".
Marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
Already marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
NAME           STREAK  TODAY
Read 10 pages       1  done
Walk                0  not done
```

```sh
python3 habits.py --file "$F" add "read 10 pages"
python3 habits.py --file "$F" done "Meditate"
```

Observed: duplicate add exited 1 with `habit "Read 10 pages" already exists`; unknown `done` exited 1 with a no-such-habit message and the list hint.

```sh
python3 habits.py --file "$F" remove walk
python3 habits.py --file "$F" list
python3 -m json.tool "$F" >/dev/null
```

Observed: `Removed "Walk" and 0 completions.`; list showed only the remaining habit; `json.tool` accepted the file.

```sh
printf '{ broken json' > "$D/corrupt.json"
python3 habits.py --file "$D/corrupt.json" add "Walk"
cat "$D/corrupt.json"
```

Observed: exit 2 with `is not valid JSON: line 1, column 3 ...`; the file still contained exactly `{ broken json`.

```sh
HABITS_FILE="$D/env.json" python3 habits.py add "Stretch"
HABITS_FILE="$D/env.json" python3 habits.py list
```

Observed: `Added "Stretch".` and a one-row list with streak 0.

Missed-day fixture (hand-built dates relative to 2026-11-15: Journal today/yesterday/two days ago; Stretch yesterday/two days ago; Meditate three days ago):

```text
NAME      STREAK  TODAY
Journal        3  done
Stretch        2  not done
Meditate       0  not done

At risk (not done today): Stretch
```

This is the observed evidence for the three visible streak states. A completion two days old with yesterday missed is covered by the unit test `test_one_fully_missed_day_resets_streak`.

Revision hashes observed with `shasum -a 256`:

```text
87fca0b5c6bbdb605541f14bd388a3127021509ea464a7a58b7a9f844a600bd2  habits.py
0d965ce6f0eac4ce23b9e68992d4dac647edddee721f64f722b92a5acdc8870a  test_habits.py
```

## 4. Key product and design decisions

| Decision | Choice | Why |
| --- | --- | --- |
| Streak and missed days | **Day-grace calendar streak.** Today done → count from today; today open but yesterday done → run stays current and is marked at risk; a fully elapsed missed day resets to 0. | It matches "I'm on day 3, I haven't done today's yet" and avoids showing 0 for most of the day. Strict-today and skip-token/weekly-quota options were compared and rejected. |
| Meaning of "done" | One completion per habit per **local calendar date**; repeat is idempotent. | The request is daily, not interval-based. No backfill or undo in this slice. |
| Storage | One versioned JSON object with per-habit `name`, `created` and sorted unique `completions` dates. | Readable by hand, direct per-habit streaks, easy add/remove. Date-indexed map and event log were rejected as poorer fits at this scale. |
| Identity | Name-addressed commands; whitespace-collapsed, case-insensitive matching; first display name kept. | One short daily command; no ID lookup. Duplicate adds are rejected rather than merged. |
| Surface | `add`, `done`, `remove`, `list`; `--file` before the command; `HABITS_FILE` and `~/.habits.json` fallbacks. | The smallest surface that can be corrected and used from a terminal. No TUI, flags matrix or config file. |
| Data safety | Validate before write; exit 2 and leave invalid data untouched; write a temp file, `fsync`, then `os.replace`. | Prevents a typo or corrupt file from silently destroying the user's history. |
| Error contract | 0 success, 1 input/domain, 2 data/usage; one diagnostic line for expected errors. | Scriptable and predictable; tracebacks are reserved for unexpected bugs. |
| Scope | One file, no dependencies, no packaging, no sync. | Keeps it a personal tool rather than a platform. |

**Assumptions made explicit (not validated with a user):**

- One person, one writer at a time; no locking or conflict resolution.
- A few habits, not hundreds; whole-file rewrites are acceptable.
- The machine's local calendar date is the day boundary; timezone travel is not handled.
- Python 3.9+ on macOS; Linux/Windows are plausible but untested.
- Grace-before-midnight is motivating rather than a loophole. The "at risk" line makes the open state visible.
- `remove` is destructive without confirmation, acceptable for a personal CLI.

## 5. Gaps and friction

**Skill/procedure friction**

- `implement` is a stub that assumes `/tdd`, `/code-review` and a commit flow that this environment does not provide. I followed its intent (narrow increments, frequent tests, final full suite, review) but could not execute its literal commands. This is the largest mismatch between the skill library and the actual environment.
- `test` and `review` declare `disable-model-invocation: true`; they were readable and applicable, but an agent could not select them autonomously. This run used them because the task explicitly requested them.
- The ECR, design-proposal and quality-bar contracts are heavy for a 352-line personal script. I kept the records compact, but the seven-section ECR and three-option design still feel like more ceremony than the change's risk warrants. The streak decision genuinely benefited from the option comparison; the storage and command-surface sections were shorter for proportionality.
- The skills link to many optional methods (`project-conventions`, `git-contributions`, `system-design`, C4/sequence guides, Python automation guidance) that were not installed in the required list. I read the core contracts and library/CLI reference instead. A broader library might have changed the design details, especially Python packaging and compatibility evidence.
- There is no git repository, tracker or remote, so no issue, PR, commit link or CI evidence exists. The quality bar's link requirement was met with explicit local-only hashes and paths, not with URLs. A process that requires issues/PRs would need those homes authorized before this activity.
- No stakeholder was available. Product choices (grace streak, today-only, name addressing) were made autonomously and recorded as assumptions. They are defensible but are not user-validated.

**Verification limits**

- Atomicity was exercised only on the success path; no kill/fault injection between `fsync` and `os.replace`, and no directory-entry durability check.
- No concurrent-writer test; last-write-wins is reasoned, not reproduced.
- Only macOS; no Linux/Windows run.
- Only Python 3.14.7 and 3.9.6; no full version matrix.
- Midnight and timezone rollover were simulated by injecting a fixed `today`, not by changing the OS clock.
- Unicode display width and long names were not tested.
- No long-term usability or motivation study; passing tests do not prove the streak rule is helpful.
- No release, packaging or install evidence, because none exists.

**Defects found and fixed during the run**

- The first date parser rejected every valid `YYYY-MM-DD` date because it required all three dash-separated parts to be two characters. The initial test run showed 7 failures and 1 error; after the fix, the suite passed.
- Duplicate-add output used the user's input casing instead of the stored name.
- Parent-directory creation sat outside the `OSError` boundary in `save()`.
- The pure streak helper accepted compact ISO dates that the file validator rejected.
- JSON `true` compared equal to schema version `1`.
- README/design test counts went stale after tests were added and were reconciled to 33.

## 6. Self-assessment against IDEA.md

The request asked for a small personal habit tracker: track a few daily habits, mark one done for today, show its current streak, keep data in local JSON, use no third-party dependencies, and decide the command names, data model and missed-day behavior. It also asked for the full idea-to-implementation path and the named documents.

| Request | Result | Honest assessment |
| --- | --- | --- |
| Track a few daily habits | `add`, `list`, `remove` over a few named habits. | Met. No upper limit is enforced, but the design assumes a small personal set. |
| Mark a habit done for today | `done NAME`, idempotent per local date. | Met, including unknown/duplicate failure paths. |
| Show the current streak for each habit | `list` shows streak, today status and an at-risk line. | Met. The grace rule is explicit in help, README, design and tests. |
| Keep everything in a local JSON file | Versioned indented JSON at `~/.habits.json`, `HABITS_FILE` or `--file`. | Met. The file was validated with `json.tool`; corrupt input is not overwritten. |
| No third-party dependencies | Standard library only. | Met; verified on two Python versions. |
| Decide command names, data model, missed days | Documented decisions with alternatives and decision blocks. | Met. The choices are defensible for a personal tool; they were not user-validated. |
| Take it from idea through a useful implementation | Working CLI, 33 tests, README, product, ECR, design, verification. | Met for a small slice. Not a platform: no sync, reminders, history, packaging or UI. |
| Small local CLI, useful slice | 352-line single file plus tests. | Mostly met. `remove`, `--file`/env overrides, validation and atomic writes are small additions that make daily use and data safety credible; they stop short of platform scope. |
| Required artifacts | All eight named outputs exist. | Met. |
| Verify, don't claim | 33 tests on two interpreters, real CLI runs, corrupt-file and missed-day evidence, explicit gaps. | Met within the stated local boundary. Cross-platform, crash and concurrency claims are deliberately absent. |

**Overall:** the run produced a usable personal tool and an inspectable decision/evidence trail. The largest weaknesses are environmental rather than product: no stakeholder validation, no issue/PR/CI homes, and no way to execute the `implement` skill's assumed workflow. The most valuable skill contributions were the streak option comparison and the refusal to turn "tests pass" into a broader verification claim.
