# ECR: Task tags and tag filtering

## 1. Overview and lifecycle

**Change.** `taskcli.py` now stores an optional `tags` list on each task, `add` accepts one or more tags, `list --tag <tag>` filters pending tasks, and `list --all --tag <tag>` filters all tasks. Existing commands, list output and JSON files written before tags existed keep working.

**Current state.** Requirements accepted from [TASK.md](../TASK.md); design accepted for implementation and recorded in [design.md](design.md); implementation present in [taskcli.py](../taskcli.py); verification completed locally and recorded in [verification.md](verification.md). No release applies: this is a local evaluation fixture, not a distributed package.

| Claim | Status | Evidence |
| --- | --- | --- |
| Requirements accepted | Accepted | [TASK.md](../TASK.md) |
| Design | Accepted for implementation | [design.md](design.md) |
| Implemented | Implemented | [taskcli.py](../taskcli.py), [test_taskcli.py](../test_taskcli.py) |
| Behavior verified | Verified locally | [verification.md](verification.md): 22 tests passed; CLI scenario observed |
| Released | Not applicable | Local-only fixture; no package, deployment target, VCS revision or URL |

**Next action.** A reviewer should inspect the diff-equivalent state of `taskcli.py` and `test_taskcli.py` and confirm the acceptance cases in section 3. Owner: the requesting engineer. This run was unattended, so no separate human sign-off is claimed.

All references are local to this fixture. The directory is not a Git repository, so no commit, branch, issue or pull request exists; paths below are verified relative paths, not published URLs.

## 2. Problem and scope

**Observed baseline.** Before this change, `taskcli.py` (71 lines) appended records shaped `{"title": str, "done": bool}`, and `list` selected only on `--all`. A reader could not group or retrieve tasks by topic, and no field existed to carry that grouping. The baseline was read from the fixture at the start of the run. Because the fixture has no version control, the baseline cannot be cited at a revision; it is a local-only pre-change snapshot.

**Actor and impact.** A person using the CLI to keep local tasks cannot ask "show me the pending work tasks" without reading the whole list. The change adds that selection without altering how tasks are added, completed or printed.

**In scope.**

- Optional tags on task records.
- One or more tags on `add`, including the existing `add "title"` form with none.
- Pending-only and include-done filtering by one tag.
- Backward-compatible reading of tag-less JSON.

**Out of scope.**

- Editing, removing, renaming or bulk-tagging existing tasks.
- Printing tags in `list` output (deliberately unchanged; see section 4).
- Boolean tag expressions (`tag a AND b`, `OR`, negation) and filtering by several tags at once.
- Tag suggestions, colors, counts or a tag registry.
- Migration/backfill of old records, schema versioning, atomic writes and concurrent-writer safety.
- Any non-CLI interface, packaging or deployment.

**Existing behavior that must not change.** `add "title"` appends one record; `list` prints pending tasks as `index<TAB>mark<TAB>title`; `list --all` includes completed tasks; `done <index>` marks a task and persists it; an out-of-range index raises `IndexError`; `TASKCLI_DATA` selects the JSON file.

## 3. Requirements and acceptance

All requirements below were accepted from [TASK.md](../TASK.md). No requirement remains open.

| ID | Requirement | Status |
| --- | --- | --- |
| R1 | `add "title"` keeps working and stores an empty tag list on the new record. | Verified |
| R2 | `add` accepts one or more tags, in any argument position, via repeated `--tag`, `--tag=value` or a comma-separated value. | Verified |
| R3 | `list --tag <tag>` shows only pending tasks that carry the tag. | Verified |
| R4 | `list --all --tag <tag>` shows pending and completed tasks that carry the tag. | Verified |
| R5 | JSON files without a `tags` field remain readable; listing and `done` do not require tags. | Verified |
| R6 | Existing `list`, `list --all`, `done` and test behavior is preserved, including list output format. | Verified |
| R7 | An empty tag, a `--tag` without a value, or `list` with more than one `--tag` fails with exit code 1 and writes nothing. | Verified |
| R8 | Tags are canonical: surrounding whitespace removed, one leading `#` removed, lower-cased, and duplicates collapsed in first-seen order. | Verified |

**Named acceptance cases.**

| Case | Action | Observable result | Status |
| --- | --- | --- | --- |
| A1 | `add "write report"` | `added 0`; record is `{"title": "write report", "done": false, "tags": []}`; `list` prints `0<TAB><TAB>write report` | Verified |
| A2 | `add "write report" --tag Work --tag urgent` | Record tags are `["work", "urgent"]` | Verified |
| A3 | Two pending tasks tagged `work` and one tagged `home`; `list --tag work` | Exactly the two `work` tasks, with original indices and unchanged columns | Verified |
| A4 | Complete one `work` task; `list --tag work` then `list --all --tag work` | First command omits it; second prints it with mark `x` | Verified |
| A5 | Start from `[{"title": "old pending", "done": false}, {"title": "old done", "done": true}]`; run `list`, `list --all`, `list --tag work`, `done 0` | Same output as before the feature; tag filter returns nothing; `done` succeeds and the record keeps its two-field shape | Verified |
| A6 | `python3 -m unittest -v` | 22 tests run, 0 failures, 0 errors, 0 skips; includes the three original tests unchanged | Verified |
| A7 | `add "write report" --tag "  "`; `add "x" --tag`; `list --tag work --tag home` | Each exits 1 with a usage/invalid-tag message; no task is added | Verified |
| A8 | `add "x" --tag=work,urgent`; `list --tag WORK` | Record tags are `["work", "urgent"]`; filter matches case-insensitively | Verified |

**Denied/failure paths.** Tag selection is read-only, so there is no authorization decision. Invalid input is rejected before `save`, so a rejected `add` leaves the file unchanged. Filtering by an unknown tag returns an empty result rather than an error.

## 4. Solution design

**Baseline implementation.** At the pre-change state, `add` appended `{"title": title, "done": False}`; `list_tasks(include_done)` iterated every record and filtered only on `done`; `main` joined all arguments after `add` into the title and passed `"--all" in argv` for `list`. `load` and `save` handled a top-level JSON array, and `done` indexed that array directly.

**Affected software type.** Library/CLI only: one local command-line entry point, a JSON file and a Python API used by tests. Frontend, backend/service, AI and distributed-architecture concerns are not affected; there is no network, account, tenant, deployment topology or rendered UI, so no C4, sequence, state-machine or design-specification artifact is warranted.

**Chosen design.** An optional per-record `tags` array, written on every new record, plus repeated `--tag` arguments. The full option set, compatibility matrix and rejection rationale are in [design.md](design.md). In brief:

1. **Optional array on the existing record (chosen).** `{"title", "done", "tags": [...]}` inside the existing top-level list. Old readers that ignore unknown keys still parse it; old records need no migration.
2. **Versioned document wrapper with a tag index.** Rejected: it breaks the current top-level-array contract, needs a migration and allows the index to drift from the records.
3. **Sidecar `tags.json` keyed by index or title.** Rejected: two authorities, unstable keys, non-atomic updates.
4. **`#tag` tokens inside the title arguments.** Rejected: changes the title grammar and collides with legitimate titles containing `#`.

**Seam decisions (single place).**

- **CLI grammar:** `--tag VALUE` in any position; `--tag=VALUE`; comma-separated values on `add`. Everything else is title text. On `list`, only one `--tag` is accepted; several would require an undefined AND/OR rule.
- **Canonical tag form:** strip whitespace, strip one leading `#`, lower-case, split on commas for `add`, deduplicate preserving first-seen order, reject empty results. The same function is used by `add` and by filtering, so stored and queried spellings agree.
- **Storage:** `tags` is a JSON array of canonical strings on the task object. New records always carry it; old records are left untouched, including when `done` rewrites the file.
- **Filter semantics:** tag match is exact on canonical form and is combined with the existing `done` visibility rule (`AND`).
- **Output:** `list` columns remain `index<TAB>mark<TAB>title`; tags are not printed. This is the strictest reading of "preserve existing list behavior" and avoids a format change for consumers.

**Failure behavior.** `--tag` without a following value, an empty tag, or multiple `--tag` flags on `list` print a message and return 1 without saving. Legacy records whose `tags` is absent, not a list, or contains non-text entries are treated as untagged by the filter instead of crashing. Concurrent writers and partial-write recovery are unchanged pre-existing limitations, not introduced here.

## 5. Implementation strategy

Delivered in one small increment, in this order:

1. Add tag canonicalization helpers and the optional `tags` argument to `add`.
2. Extend `list_tasks` with an optional `tag` filter while keeping the existing two-argument behavior.
3. Add `_parse_tag_args` and wire `add`/`list` in `main`; preserve the `done` branch.
4. Add regression coverage for tags, filtering, CLI parsing, errors and legacy JSON; keep the original three tests unchanged.
5. Write the ECR, design and verification artifacts; update the README command surface.

**Actual changes.**

- [taskcli.py](../taskcli.py): `_normalize_tag`, `_normalize_tags`, `task_tags`, `_task_tag_set`, `add(title, tags=None)`, `list_tasks(include_done=False, tag=None)`, `_parse_tag_args`, updated `main`.
- [test_taskcli.py](../test_taskcli.py): 19 added tests, 3 original tests retained verbatim in behavior.
- [docs/design.md](design.md), [docs/verification.md](verification.md), this ECR and [EVAL.md](../EVAL.md).
- [README.md](../README.md): command examples and current-behavior notes for tags.

**Compatibility and migration.** No migration runs. New records gain the field; old records remain valid and are not rewritten by `list` or `done`. A consumer that reads only `title`/`done` is unaffected. Rollback is a code revert; existing files stay readable in both directions because the field is additive and optional.

**Ready/blocked.** All planned increments are complete. No dependency or decision blocks the change. Tag display, tag editing and OR-filtering are deliberately deferred to a future change.

## 6. Verification and release

**Environment.** macOS 27.0.1 (Darwin 27.0.0), arm64, Python 3.14.7. No network access, no third-party dependencies, standard library only. Working directory: the local fixture directory; not a Git repository. Full observations are in [verification.md](verification.md).

**Observed results.**

- `python3 -m unittest -v` ran 22 tests: `OK`, 0 failures, 0 errors, 0 skips, in 0.011s. The three original tests (`test_add_and_list_pending`, `test_done_hides_from_pending_and_persists`, `test_unknown_index_raises`) passed unchanged.
- A scripted CLI run used a temporary `TASKCLI_DATA` file, added four tasks (three tagged, one untagged), listed, filtered, completed index 0, filtered again and printed the JSON. `add` returned `added 0`…`added 3`; `list --tag work` returned records 0 and 2 while pending and only record 2 after `done 0`; `list --all --tag work` returned records 0 (`x`) and 2; the JSON held canonical tags.
- A legacy run started from a two-record file with no `tags` keys. `list`, `list --all`, `list --tag work` and `done 0` behaved as before; the file after `done` still had no `tags` keys.
- Failure checks: multiple `list --tag` flags, a missing `--tag` value and a whitespace-only tag each returned exit code 1 and produced no record.

**Failed, skipped or unavailable checks.** None failed or were skipped. Not exercised: concurrent writers, non-POSIX shells, installation as a package, a JSON schema validator, and any external consumer of the file. No CI, VCS diff or pull request exists in this fixture.

**Release.** Not performed and not applicable. No deployment, publication or distribution claim is made.

## 7. Decision history and references

| Date | Decision | Owner / rationale |
| --- | --- | --- |
| 2026-11-15 | Use an optional per-record `tags` array with repeated `--tag` flags. | Feature requester via [TASK.md](../TASK.md); it preserves the existing top-level array and needs no migration. |
| 2026-11-15 | Reject the versioned wrapper, sidecar index and `#tag` title tokens. | Feature requester; reasons in [design.md](design.md) (compatibility, dual authority, title ambiguity). |
| 2026-11-15 | Canonicalize tags with trim, one leading `#`, lower-case, comma split on add and order-preserving dedupe. | Implementer; makes stored and queried spellings identical and avoids duplicates. |
| 2026-11-15 | Keep `list` output unchanged; do not print tags. | Implementer; strict preservation of existing output, as required by TASK.md. |
| 2026-11-15 | Accept only one `--tag` on `list`; several is a usage error. | Implementer; avoids inventing an AND/OR semantic not requested. |

**Open items.** Tag display, tag editing/removal, OR/AND filtering, backfilling tags on old records, atomic writes, and a documented JSON schema remain future work with no owner assigned in this run.

**References (all local-only; not published; no URL).**

- [TASK.md](../TASK.md) — accepted requirements.
- [taskcli.py](../taskcli.py) — implemented source.
- [test_taskcli.py](../test_taskcli.py) — automated checks.
- [design.md](design.md) — option set, compatibility matrix and decision block.
- [verification.md](verification.md) — commands, environment and observed output.
- [README.md](../README.md) — current command surface.
