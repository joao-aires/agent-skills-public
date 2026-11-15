# EVAL: existing-feature task tags

This report records the behavioral evaluation of the `sdlc` skill library on the `existing-feature` fixture. It states what was read, what changed, what was run, what was observed and where the skills helped or fit poorly. All results below were observed in this run; nothing is projected.

## 1. Skills read and their effect

The following skills were read in full before implementation. Their supporting contracts and quality references were read where the skill required them.

| Skill | What it changed in this run |
| --- | --- |
| `activity-system` | Routed the request as one bounded change: refine → design → implement → test/review, stopping at local verification. Prevented inventing a release, PR or architecture activity. Established that the ECR is the coordination spine and that a local fix needs proportionate evidence. |
| `artifact-system` | Selected the artifact types (`ecr`, `design-proposal`, verification record), resolved their home to `docs/`, and imposed the quality bar: self-contained context, explicit maturity per claim, past-tense evidence, resolvable or explicitly local-only references, one authority. Also justified *not* producing C4/sequence/ADR artifacts for a single-process CLI. |
| `system-documentation` | Supplied the feature-trace method: start at `main`, follow `add`/`list_tasks`/`done` through the JSON file and tests, then separate observed current behavior from the proposed extension. Its architecture-set guidance was intentionally not applied because there are no services, topology or runtime interfaces. |
| `refine` | Converted the request into R1–R8 with observable acceptance, explicit non-goals and a compatibility statement for old JSON. Made the "preserve existing behavior" constraint concrete (list output shape, index identity, `done` persistence) instead of leaving it as a slogan. |
| `design` | Chose the library/CLI evidence path, forced materially different options rather than cosmetic syntax variants, and produced the compatibility matrix and one seam decision. Its proportionality rule kept the design short: no C4, no RFC, no state machine. |
| `implement` | Set the working order: implement against the accepted behavior, test at the seams as code is added, run the full suite at the end. Its instructions to commit and to invoke `/code-review` could not be followed literally (no VCS, no slash command); the equivalent inline steps were taken and are noted as friction. |
| `test` | Turned acceptance into checks before coding: original behavior, new filtering, legacy JSON, normalization and failure paths. Required past-tense evidence with command, environment and result. Kept the original three tests and added 19 focused ones rather than replacing them. |
| `review` | Drove the final self-review: read the changed path from caller to stored result, check the changed behavior against existing callers and the accepted requirements, and report remaining limits instead of claiming review approval. Since the skill is explicit-only and no separate reviewer exists, this is a self-review, not independent review. |
| `guide-ecr` | Fixed the seven-section structure, current-state-first ordering, status-versus-claim separation, and the "commands without results" failure that the verification section had to avoid. |
| `guide-design-proposal` | Fixed the section order (question, affected types, options, linked artifacts, tradeoffs, seam, recommendation, evidence), the decision block, and the review question "are the options materially different?" |
| `guide-issue` | Used its pickup test to check that the ECR requirements stand alone. No issue was created: the fixture has no tracker and the task did not authorize publishing one. |
| `guide-pr` | Used its reader questions (why, what changed, what is preserved, validation, risk) to shape the ECR and verification. No PR was created because the directory is not a Git repository; no PR claim is made. |
| `guide-readme` | Drove the README update: exact copyable commands, current behavior, a documentation map and an explicit limits section, without duplicating the design or ECR. |

Additional references read because the skills pointed to them: `artifact-system/references/contracts/ecr.md`, `contracts/design-proposal.md`, `references/quality-bar.md`.

## 2. Artifacts produced

| Artifact | State | Purpose |
| --- | --- | --- |
| `taskcli.py` | Modified, 167 lines | Tag storage, canonicalization, `add(title, tags=None)`, `list_tasks(..., tag=None)`, CLI parsing for `--tag`. |
| `test_taskcli.py` | Modified, 164 lines, 22 tests | Original 3 tests retained; 19 added for tags, filtering, CLI, legacy JSON and failures. |
| `docs/ecr.md` | New | Seven-section change record with requirements, design, implementation and evidence. |
| `docs/design.md` | New | Design proposal: question, affected type, four options, compatibility matrix, tradeoffs, seam, decision block. |
| `docs/verification.md` | New | Environment, exact commands, observed CLI/legacy/failure output, limits. |
| `README.md` | Updated | Tag commands, current behavior, docs map, limits. |
| `EVAL.md` | New | This report. |

Nothing under `/Users/joao/Projects/products/agent-skills-artifact-quality` was modified.

## 3. Commands and actual results

### 3.1 Environment

```text
python3 --version        → Python 3.14.7
uname -sr                → Darwin 27.0.0
uname -m                 → arm64
sw_vers                  → macOS 27.0.1, build 26A434
git rev-parse --short HEAD → fatal: not a git repository
```

### 3.2 Test suite

```bash
python3 -m unittest -v
```

Actual result: `Ran 22 tests in 0.011s` then `OK`; 0 failures, 0 errors, 0 skips. All methods reported `ok`, including the three pre-existing tests. The added tests are listed in `docs/verification.md`.

### 3.3 Add / list / filter / done

Temporary `TASKCLI_DATA`; actual output:

```text
$ python3 taskcli.py add "write report" --tag Work --tag urgent
added 0
$ python3 taskcli.py add "buy milk" --tag home
added 1
$ python3 taskcli.py add "review report" --tag=work,urgent
added 2
$ python3 taskcli.py add "legacy style"
added 3
$ python3 taskcli.py list
0	 	write report
1	 	buy milk
2	 	review report
3	 	legacy style
$ python3 taskcli.py list --tag work
0	 	write report
2	 	review report
$ python3 taskcli.py list --tag URGENT
0	 	write report
2	 	review report
$ python3 taskcli.py done 0
done write report
$ python3 taskcli.py list --tag work
2	 	review report
$ python3 taskcli.py list --all --tag work
0	x	write report
2	 	review report
```

The persisted JSON contained `["work", "urgent"]`, `["home"]`, `["work", "urgent"]`, `[]` respectively, with `done: true` on record 0.

### 3.4 Legacy JSON (no tags)

Input `[{"title":"old pending","done":false},{"title":"old done","done":true}]`.

```text
list           → 0	 	old pending
list --all     → 0	 	old pending / 1	x	old done
list --tag work→ (no output)
done 0         → done old pending
list --all     → 0	x	old pending / 1	x	old done
```

After `done`, the file still had no `tags` keys.

### 3.5 Failure paths

```text
add "write report" --tag "  "     → invalid tag: tag cannot be empty      exit 1
add "write report" --tag          → option --tag requires a value         exit 1
list --tag work --tag home        → list accepts a single --tag           exit 1
file existence check              → no
```

### 3.6 Revision pin

The fixture is not a Git repository, so revision is pinned by content hash, local-only and not published:

```text
taskcli.py       SHA-256 32f2faecb02ce76a0995a0cb00f700ca84e5735b11cfeaee7ef2841710560506
test_taskcli.py  SHA-256 0cd042660352dee2aa1b1d904aee3ba55022edf285da9a74a78b340fc411c0f5
```

## 4. Decisions and assumptions

1. **`--tag` is the tag surface.** Chosen over `#tag` title tokens (title ambiguity) and over a versioned wrapper or sidecar (breaks the file contract or splits authority). The full option set is in `docs/design.md`.
2. **`--tag` is recognized in any position**, with `--tag value` and `--tag=value`; `add` also splits commas. `add "title"` with no tag still works.
3. **Tags are canonicalized** by trimming, removing one leading `#`, lower-casing, splitting commas on add and de-duplicating in first-seen order. Stored and queried forms therefore agree.
4. **List output is unchanged** (`index<TAB>mark<TAB>title`); tags are not displayed. This is a deliberate strict reading of "existing list behavior must be preserved". It is a usability limitation, not an oversight.
5. **`list` accepts exactly one tag.** Multiple `--tag` flags return exit 1 rather than inventing an AND/OR rule the request does not define.
6. **New records always carry `tags`; old records are never backfilled.** `done` on a legacy record keeps its two-field shape.
7. **Filtering is exact on canonical form and case-insensitive.** Unknown tags return an empty result (exit 0), not an error.
8. **Defensive legacy reads:** a missing, non-list or non-text `tags` value is treated as untagged instead of crashing.
9. **Scope was not widened:** no tag display, tag editing, counts, colors, OR filters, schema version, locking or migration.
10. **No commit, issue, PR or release** was produced because the fixture has no VCS, tracker or deployment target; the task did not authorize publishing.

## 5. Gaps and friction

- **VCS-dependent guidance.** `implement` says "commit to the current branch" and `guide-pr`/`review` assume a base/head diff. The fixture is not a Git repository, so commit/PR/diff steps were skipped and local content hashes were used as a substitute pin. This is an environment limit, not a skill defect, but the skills do not offer a compact fallback for `git`-less fixtures.
- **Slash commands.** `implement` points to `/tdd` and `/code-review`; those are not callable in this harness. The equivalent behavior (small increments, tests alongside code, inline review) was applied manually.
- **Tracker assumption.** `refine` and `guide-issue` lean on an engineering workspace/tracker. The ECR home was resolved to the requested `docs/` directory and no issue was invented; a reader of the skills should see that fallback stated more directly.
- **Design proportionality vs. mandatory output.** The change is a small local feature for which the design skill allows "a short explanation beside acceptance criteria". The task required `docs/design.md`, so a full proposal with four options was produced. The options are storage/grammar alternatives, not cosmetic variants, but this is more ceremony than the change strictly needs.
- **Grammar edge.** An unquoted literal `--tag` token in a title (for example `add fix --tag bug` as separate shell words) is now parsed as an option, not title text. A fully quoted title (`add "fix --tag bug"`) is unaffected because it arrives as one argument. No escape or `--` terminator was added; this is recorded as a limitation.
- **No independent review.** `review` is explicit-only and this run is unattended. The final review was a self-review; no human approval or second reviewer is claimed.
- **Coverage limits.** No concurrent-writer, disk-full, non-POSIX or external-consumer test exists. The JSON shape is asserted in tests and observed in the CLI run, not validated against a formal schema.
- **Timing.** `0.011s` is an observation, not a performance claim.

## 6. Self-assessment against TASK.md

| TASK.md requirement | Result | Evidence |
| --- | --- | --- |
| `add` accepts one or more tags without breaking `add "title"` | Met | Scenario `added 0`–`added 3`; tests `test_main_add_with_tags_and_filter`, `test_main_add_accepts_equals_and_comma_tags`, `test_main_add_accepts_tag_before_title`; plain add test unchanged. |
| `list --tag <tag>` shows pending tasks with that tag | Met | Scenario returns records 0 and 2, then only 2 after `done 0`; test `test_list_filters_pending_tasks_by_tag`. |
| `list --all --tag <tag>` shows all tasks with that tag | Met | Scenario returns `0	x` and `2`; test `test_main_list_all_with_tag_includes_done`. |
| Existing JSON without tags remains readable | Met | Legacy scenario listed, filtered and completed old records; file kept its shape; tests `test_legacy_json_without_tags_is_readable`, `test_done_on_legacy_record_keeps_legacy_shape`. |
| Existing `list`, `list --all`, `done` and test behavior preserved | Met | Same output columns and marks; `done` still persists; original three tests pass unchanged; `test_main_list_preserves_untagged_output_format`. |
| Tests for tags, filtering and backward compatibility | Met | 19 added tests; 22 total, all pass. |
| Produce `docs/ecr.md`, `docs/design.md`, `docs/verification.md`, `EVAL.md` | Met | All four exist and are linked from the README. |
| Use installed `sdlc` skills; do not edit the skill repository | Met | 13 skills plus contracts read; only the fixture directory was written. |

**Overall.** The requested feature is complete and locally verified, with the original behavior and tests preserved. The main residual risks are deliberate scope exclusions (no tag display/editing, one tag per list, no migration) and the pre-existing single-file concurrency limit. No claim of release, deployment or independent review is made.
