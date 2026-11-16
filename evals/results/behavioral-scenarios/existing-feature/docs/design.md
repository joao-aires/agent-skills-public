# Design: tag storage and tag filtering for taskcli

## Question and constraints

**Decision.** How should `taskcli.py` carry tags on tasks and expose tag filtering without breaking the existing single-file JSON format, the `add "title"` form, the `list` output or the three existing tests?

**Accepted outcome.** From [TASK.md](../TASK.md): `add` takes one or more tags; `list --tag <tag>` shows pending tasks with the tag; `list --all --tag <tag>` shows all such tasks; old JSON stays readable; existing `list`, `list --all`, `done` and test behavior is preserved.

**Constraints.**

- One JSON file selected by `TASKCLI_DATA`; the file's current top level is a JSON array of task objects.
- No network, no third-party dependencies, Python 3 standard library only.
- No rewrite of the application and no unrelated features.
- Existing list output is `index<TAB>mark<TAB>title`; there is no schema version and no migration mechanism.
- Task identity is the array index, which is also what `done` uses.

**Current state.** The fixture has no version control, so the baseline is the local-only pre-change `taskcli.py` (71 lines, read at the start of the run): `add` writes `{"title", "done"}`, `list_tasks` filters only on `done`, and `main` joins every argument after `add` into the title. Not published; no URL. The authoritative implementation after the change is [taskcli.py](../taskcli.py).

**Authority.** The feature requester via [TASK.md](../TASK.md). This design was produced and accepted in the same unattended run; no separate design-review signature is claimed.

## Affected software types

| Component | Type | Status | Reason |
| --- | --- | --- | --- |
| `taskcli.py` command surface | library/CLI | Designed | Argument grammar, exit codes, persistence and filtering all change here. |
| Task JSON file | library/CLI data | Designed | Records gain an optional `tags` array; old records must remain valid. |
| Test module | library/CLI verification | Designed | Needs tag, filter, CLI and legacy-data coverage. |
| Frontend / UI | — | Not affected | There is no rendered interface. |
| Backend service / API | — | Not affected | There is no server, network call, tenancy or authorization boundary. |
| AI behavior | — | Not affected | There is no model, prompt or evaluation surface. |
| Deployment / architecture | — | Not affected | Single local process; no topology, queue, datastore or release target. |

The seam is therefore internal to one process: **CLI argument parsing → tag canonicalization → record persistence → list selection → unchanged text output**. It is decided once in "Seam decisions" below.

## Options

### Option A — Optional `tags` array on each task, repeated `--tag` flags (chosen)

Store tags beside the task they describe:

```json
[
  {"title": "write report", "done": false, "tags": ["work", "urgent"]}
]
```

Add surface: `add "write report" --tag work --tag urgent`, also `--tag=work` or `--tag work,urgent`. List surface: `list --tag work`, `list --all --tag work`.

- **Optimizes:** one authority, one file, atomic-enough single `save`, stable indices, no migration, old readers that ignore unknown keys still work.
- **Sacrifices:** filtering scans every record; there is no tag index or tag registry; tags are not human-visible in `list`; old records remain heterogeneous until edited.

### Option B — Versioned document wrapper with a tag index

Change the top level to `{"version": 2, "tasks": [...], "tag_index": {"work": [0, 2]}}`.

- **Optimizes:** fast lookup and a natural place for future schema evolution.
- **Sacrifices:** breaks every current reader of the top-level array, requires reading/migrating version 1, duplicates truth between records and index, and the index can drift after `done` or any future delete. Rejected as disproportionate for a fixture and contrary to "existing JSON remains readable" without a migration layer.

### Option C — Sidecar `tags.json` keyed by task index or title

Keep `tasks.json` untouched and store `{"0": ["work"], "buy milk": ["home"]}` in a second file.

- **Optimizes:** zero change to the existing record shape and to existing readers.
- **Sacrifices:** two authorities that can disagree, non-atomic updates across files, fragile keys (indices shift; titles are not unique), and `done` or any future delete silently corrupts the mapping. Rejected.

### Option D — `#tag` tokens inside title arguments

Parse `add "write report #work #urgent"` and strip `#...` tokens from the title.

- **Optimizes:** short, familiar chat-style syntax; no new flag.
- **Sacrifices:** changes the title grammar, makes `#` unrepresentable in a title, needs quoting/escaping rules, and silently reinterprets existing titles that happen to contain `#`. Rejected because it breaks the strongest compatibility constraint.

## Linked design artifacts

The affected type is library/CLI, so the evidence is the command surface, a compatibility matrix and usage/failure examples. No C4, sequence or state-machine view is needed: there is one process, one file and no asynchronous or multi-actor state.

**Command surface.**

| Command | Meaning |
| --- | --- |
| `add <title> [--tag <tag> ...]` | Append a task; tags optional, repeatable, any position. |
| `add <title> --tag=<tag>[,<tag>...]` | Same, with inline or comma-separated values. |
| `list [--all] [--tag <tag>]` | List pending (or all) tasks, optionally restricted to one tag. |
| `done <index>` | Unchanged. |

**Compatibility matrix.**

| Surface | Before | After | Compatibility |
| --- | --- | --- | --- |
| `add "write report"` | record without tags | record with `"tags": []` | Additive field only; title semantics unchanged. |
| `add "write report" #note` | title contains `#note` | title contains `#note` (only `--tag` is special) | Unchanged. |
| `list` | `index<TAB>mark<TAB>title` | identical | Preserved exactly. |
| `list --all` | all tasks | identical | Preserved exactly. |
| `done 0` | marks and saves | identical | Preserved. |
| Old JSON record | `{"title", "done"}` | still valid; treated as untagged | Read without migration; `done` does not add keys. |
| New JSON record | n/a | `{"title", "done", "tags": [...]}` | Unknown-key-tolerant readers unaffected. |
| Tag filter | n/a | `list [--all] --tag t` | New, additive. |
| Exit code on bad input | 1 for unknown command/index | 1 for unknown command/index and invalid tag usage | Existing failures unchanged; new failures are explicit. |

**Usage and failure examples.**

```text
$ python3 taskcli.py add "write report" --tag Work --tag urgent
added 0
$ python3 taskcli.py add "buy milk" --tag home
added 1
$ python3 taskcli.py list --tag work
0	 	write report
$ python3 taskcli.py done 0
done write report
$ python3 taskcli.py list --all --tag work
0	x	write report
$ python3 taskcli.py list --tag work --tag home
list accepts a single --tag        # exit 1
$ python3 taskcli.py add "x" --tag
option --tag requires a value      # exit 1
```

## Tradeoffs and failure behavior

| Concern | Option A (chosen) | Option B | Option C | Option D |
| --- | --- | --- | --- | --- |
| Old file readable with no migration | Yes | No, needs version dispatch | Yes | Yes |
| Single source of truth | Yes | No, record and index can drift | No, two files | Yes |
| Index/title changes safe | Yes | Index must be maintained | Fragile keys | Yes |
| Title containing `#` | Safe | Safe | Safe | Ambiguous |
| Read cost | O(tasks) scan | O(1) index lookup | O(tasks) + second read | O(tasks) |
| Failure mode | Bad file still fails as before | Partial migration / divergent index | Orphaned or wrong tags | Silent title rewrite |
| Implementation size | Small | Large (migration + dual write) | Medium (two-file atomicity) | Medium (escaping) |

**Failure behavior of the chosen option.**

- Empty or whitespace-only tag: rejected before save; exit 1; file unchanged.
- `--tag` with no following value: rejected before save; exit 1.
- More than one `--tag` on `list`: rejected; exit 1. Supporting several would require choosing AND vs OR, which the request does not define.
- Unknown tag: empty result, exit 0. This matches "filter", not "validate".
- Legacy record with missing, non-list or non-text `tags`: treated as untagged; no crash.
- Comma inside a tag: treated as a separator on `add`; a literal comma in a tag is therefore unsupported.
- Case: `Work` and `work` are the same tag by design; the first spelling is not preserved, the canonical lower-case form is stored.
- Crash between `load` and `save` or concurrent writers: unchanged pre-existing limitation of the whole CLI, not made worse; no locking was added.

**Evidence and limits.** The behavior above was observed with the standard library on macOS/Python 3.14.7 only. No concurrent-writer, filesystem-quota or non-POSIX test was run.

## Seam decisions

Decided once and used by both the CLI and the data layer:

1. **Grammar:** `--tag VALUE` and `--tag=VALUE` are recognized anywhere after the subcommand; all other tokens are positional. On `add`, comma-separated tag values are split. On `list`, exactly one tag is allowed.
2. **Canonical form:** `strip()` → remove one leading `#` → `strip()` → `lower()`; reject empty; deduplicate preserving first-seen order. The same `_normalize_tag` function is used for writes and queries.
3. **Storage:** optional `tags` array of canonical strings on the task object. New records always include it; old records are never rewritten just to add it.
4. **Selection:** `tag` is an `AND` with the existing pending/all rule, and matching is exact on the canonical form.
5. **Presentation:** list output stays byte-for-byte the same shape; tags are metadata for selection, not a new column. This is the conservative reading of the preservation requirement.

## Recommendation and decision

**Recommendation.** Option A. It is the only option that satisfies every constraint at once: the file remains a top-level array, old records need no migration, title parsing is unchanged, there is one source of truth, and the code change stays local to the existing helper functions.

**Rejected alternatives.** B (breaks the file contract and duplicates truth), C (dual authority and unstable keys), D (title-grammar ambiguity).

```text
Decision: optional per-record tags array + repeatable --tag flags
Options considered: A record array, B versioned wrapper+index, C sidecar, D #tokens
Chosen because: no migration, one authority, unchanged title grammar, additive JSON
Rejected because: B breaks readers and can drift; C splits authority and uses fragile keys;
                  D reinterprets existing titles
Accepted/delegated by: feature requester via TASK.md (unattended run; no separate sign-off)
Status: accepted; implemented and verified locally
Revisit if: tag display/editing, multi-tag boolean filters, tag counts, or a real
             migration/versioning need appears; also if concurrent writers become real
```

## Evidence and open questions

**Inspected.** Pre-change [taskcli.py](../taskcli.py) and [test_taskcli.py](../test_taskcli.py); the fixture [README.md](../README.md); [TASK.md](../TASK.md). Implemented behavior and legacy-file behavior were exercised with temporary files; results are in [verification.md](verification.md).

**Unknown or undecided.**

- Whether users need tags shown in `list` (deliberately excluded here).
- Whether multiple tags should mean AND or OR if ever supported.
- Whether old records should be backfilled or a schema version added.
- Whether a future delete/reorder command would need stable task IDs; today the index is the identity.
- Whether the comma convention should be documented as reserved rather than merely accepted.
