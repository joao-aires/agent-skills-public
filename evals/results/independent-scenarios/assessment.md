# Independent scenario results

Four end-to-end scenarios were run again with **independent actor and reviewer agents**. Unlike the first battery, the actor prompts did not name skills or guides: each actor had to inspect the library and discover what applied. Reviewers then graded the delivered result in a separate context.

- Skills revision: `3d4f3e3`
- Scenario specification: `evals/behavioral-scenarios.json`
- Recorded: 2026-11-15
- Actor workspaces: retained under this directory
- Reviewer reports: [`reviews/`](reviews/)

## Method

**Actors**

- Fresh context and separate temp directory per scenario.
- Prompt contained the fixture and the task, plus one instruction: inspect the skill library and use what applies.
- No skill list, no guide list, no expected artifacts beyond the task.
- Instructed not to read the prior evaluation results.

**Reviewers**

- Separate context from the actor.
- Received the actor workspace, task, expectations and failure signals.
- Reran tests, exercised the application and inspected artifacts.
- Graded each expectation before reading the actor's `EVAL.md`.
- Wrote a separate `REVIEW.md`; did not modify the actor workspace.

## Results

| Scenario | Actor tests | Reviewer verdict | Expectations |
| --- | ---: | --- | ---: |
| [New application](new-app/EVAL.md) | 34/34 | [Pass with limitations](reviews/new-app/REVIEW.md) | 5/5 |
| [Existing feature](existing-feature/EVAL.md) | 14/14 | [Pass with limitations](reviews/existing-feature/REVIEW.md) | 5/5 |
| [Bug fix](bug-fix/EVAL.md) | 8/8 | [Pass](reviews/bug-fix/REVIEW.md) | 5/5 |
| [Idea to implementation](ideation/EVAL.md) | 44/44 | [Pass](reviews/ideation/REVIEW.md) | 5/5 |

**Total: 100/100 tests, 20/20 expectations met** in the recorded runs.

## Discovery results

The independent actors found the guidance without a supplied list:

| Scenario | Notable discovery |
| --- | --- |
| New application | Local `implement`, `develop/references/implementation-flow.md`, `test`, `change-review`, `guide-readme`, `guide-ecr`, compact ECR, software-type evidence, local-only revision form |
| Existing feature | `python-automation-engineering`, `test`, `tdd`, `guide-ecr`, `develop`, `implement`, `change-review`, compact ECR |
| Bug fix | `fix`, `diagnosing-bugs`, `test`, `tdd`, `property-based-testing`, `guide-ecr`, quality bar, compact ECR |
| Idea to implementation | `develop`, `design`, option set, design validation, software types, design proposal, ECR, README guide, assurance, `test`, `change-review`, `code-review`, `python-automation-engineering` |

The new flow changes were used in practice:

- local `implement` was discovered and applied;
- `change-review` was used as the in-review step;
- `test` was invoked as part of the flow, not as an explicit-only skill;
- compact ECR was used by the bug fix and existing feature;
- the non-versioned local revision form was used in all non-git workspaces;
- `guide-readme` produced no-license statements.

## Reviewer findings

### Bug fix — pass

All five expectations met. The reviewer independently restored the original expression and reproduced the failures. Non-blocking issues:

- one added boundary test was not red before the fix;
- no raw pre-fix log is preserved;
- the module docstring still says “deliberate off-by-one bug.”

### Existing feature — pass with limitations

All five expectations met. The reviewer reconstructed the baseline CLI, reproduced its hash, and confirmed the diff is additive. Non-blocking issues:

- `list --tag` raises `TypeError` on malformed `tags` values (`null` or non-list);
- repeated `list --tag` silently uses the last value;
- the ECR’s baseline **test-file** hash cannot be independently reconstructed;
- case sensitivity and the single-string `add` tag API are documented but not directly tested;
- the shared test helper was rewritten, though the three original test bodies were unchanged.

### New application — pass with limitations

All five expectations met. The reviewer reran 34 tests on Python 3.14.7 and 3.9.6, and verified all 11 hashes. Non-blocking issues:

- `EVAL.md` claims generated `__pycache__` directories were removed, but two remain;
- a whitespace-only JSON file is treated as an empty notebook, contradicting the record’s “non-empty malformed JSON is an error” claim;
- the record calls the interpreter “the system Python” although `python3` is Homebrew Python 3.14.7.

### Idea to implementation — pass

All five expectations met. The reviewer replayed all 18 CLI transcript commands with zero mismatches, verified hashes and test counts, and confirmed the streak semantics in design, README, help, docstring and tests. Minor issues:

- an 80-character name cap is undocumented;
- verification slightly overstates direct `parse_date` coverage;
- ECR R4’s “streak becomes 1” is only true for a fresh habit;
- `EVAL.md` says 9 Markdown files where 10 were checked.

## Cross-scenario findings

### What worked

- **Discovery without a list**: all four actors found a proportionate path. The root README, plugin README, artifact workflow and software-type files were the common entry points.
- **Compact ECR**: both the bug fix and existing feature used it. The full seven-section record was not forced onto small local changes.
- **Flow integration**: `implement`, `test` and `change-review` were discovered and used as part of the work.
- **Local-only evidence**: the quality bar’s non-versioned revision form was used consistently.
- **Guides**: `guide-ecr`, `guide-readme`, `guide-design-proposal` and the software-type files changed the artifact shape, not just the prose.

### Friction

| Finding | Severity | Evidence | Recommendation |
| --- | --- | --- | --- |
| Discovery cost is high in a 73-skill SDLC bundle | Medium | Every actor started from the root/plugin README and had to filter by capability; new-app noted “no single entry point for a small local CLI.” | Add a short “start here” path for local CLI/feature work, or a capability index that points to `develop`, `implement`, `test`, `change-review`, the compact ECR and the CLI software type. |
| Optional skills are not user-invocable and are hard to discover | Low | `python-automation-engineering` is `user-invocable: false`; the new-app actor found it only by browsing directories. | Make capability discovery explicit: either expose relevant optional methods in the plugin README or document the browsing path. |
| `tdd` expects seam confirmation from the user | Low | Unattended actors treated the task-specified seams as the substitute and recorded the deviation. | State that a task-specified seam or public interface counts as the agreed seam when no user is available. |
| `modern-python` conflicts with stdlib-only tasks | Low | Actors rejected uv/pytest/ruff because the task required no dependencies; the skill’s “when not to use” helped. | Keep the existing fit guidance; optionally add a one-line “project constraints override defaults” reminder. |
| Evidence hygiene: cleanup and coverage claims are not verified | Medium | New-app claimed `__pycache__` removal but left directories; ideation overstated `parse_date` coverage. | Add a quality-bar reminder: verify file-state, cleanup and coverage claims by inspection, not intention. |
| Baseline hashes may be unverifiable | Low | Existing-feature’s baseline test-file hash could not be reconstructed without a baseline copy. | When recording a baseline, keep a baseline copy or mark the hash as unverified. |
| Edge-case robustness is actor-specific | Low | Malformed `tags` values crash `list --tag`; repeated `--tag` is last-wins. | These are code findings, not skill defects. Keep them as reviewer signals rather than changing the skill model. |

## Comparison with the first battery

| Dimension | First battery | Independent battery |
| --- | --- | --- |
| Skill prompts | Named skills | Actor had to discover |
| Review | Author inspection | Separate reviewer context |
| Tests | 120/120 | 100/100 |
| Expectations | 20/20 | 20/20 |
| Flow changes | Pre-change | Local `implement`, `test`, `change-review`, compact ECR |
| New findings | Friction log | Evidence-hygiene and edge-case defects the self-evals missed |

The independent reviewers found real issues that the first self-evaluations did not: unremoved `__pycache__`, a whitespace-only JSON contradiction, a malformed-tag crash and an unverifiable baseline hash. That is the value of the separate review context.

## Limitations

- One model family and one run per scenario.
- Reviewers had fresh contexts but the same model family; this is not cross-model validation.
- Fixtures are local, non-git, single-machine and Python standard-library only.
- No provider, browser, native, deployment, production or independent human review.
- The actor prompts said to inspect the skill library; they did not test a fully cold agent with no mention of the library at all.

## Recommended next changes

1. Add a compact “start here” path for local CLI/feature work.
2. Add the quality-bar reminder about verifying cleanup, file-state and coverage claims.
3. Add the `tdd` note about task-specified seams in unattended runs.
4. Consider exposing or documenting optional non-user-invocable capabilities.
5. Keep the compact ECR and the local-only revision form; both reduced ceremony without weakening evidence.
6. Re-run this battery with a second model family before treating the results as stable.
