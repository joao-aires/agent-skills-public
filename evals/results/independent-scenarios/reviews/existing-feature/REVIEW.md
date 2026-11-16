# Independent review: `existing-feature` (tags for the task CLI)

**Verdict:** Pass with limitations. The change is a small, additive extension of the existing CLI; tags and tag filtering work for pending and all tasks, legacy JSON still reads, the original behaviour and the three original tests are intact, and the ECR describes the real change. Limitations are edge-case robustness and one unverifiable baseline hash, not requirement failures.

**Method.** I read `TASK.md`, `README.md`, `docs/engineering-change-record.md`, `taskcli.py` and `test_taskcli.py`; copied the source files to a throwaway directory under this review folder and ran the suite and CLI there so the actor's files were untouched. I also reconstructed the pre-change `taskcli.py` from the visible fixture structure until its SHA-256 matched the ECR's baseline hash, then diffed baseline against the delivered file and ran the three original tests against the baseline. I did not modify the actor workspace or the skill repository.

Evidence directory: `reviews/existing-feature/work.KW04dd` (copies and baseline reconstruction; not part of the actor's output).

## Expectation table

| # | Expectation | Status | Evidence |
| --- | --- | --- | --- |
| 1 | Tags and tag filtering work for pending and all tasks | **Met** | Unit suite passes 14/14; CLI run created tagged and untagged tasks, `list --tag work` returned only pending matches, `list --all --tag work` also returned the completed match with mark `x`; JSON showed `tags` only on tagged records. |
| 2 | Existing add/list/done behaviour and old JSON files remain compatible | **Met** | The baseline `taskcli.py` was reconstructed exactly (hash matches the ECR baseline) and diffed: all changes are additive. `add "write report"` still prints `added 0` and writes `{"title","done"}`; `list`/`list --all`/`done 0` output is byte-identical in shape; hand-written legacy JSON with two- and three-field records listed, filtered, completed and extended without error; `done` did not add `tags` to legacy records. |
| 3 | Tests cover the new behaviour and preserve existing tests | **Met** | 14 tests pass: the three originals (`test_add_and_list_pending`, `test_done_hides_from_pending_and_persists`, `test_unknown_index_raises`) are present verbatim and also pass against the reconstructed baseline; 11 added tests cover tag storage/dedup, empty tags, legacy record shape, legacy JSON, pending/all filtering, CLI `--tag`/`--tag=`, option placement, `--`, and missing-value errors. Gaps are disclosed (case sensitivity, repeated `list --tag`, string-API tag input). |
| 4 | The ECR and design record describe the actual change, not a rewrite | **Met** | `docs/engineering-change-record.md` has the seven ECR sections. §4 is the design record (baseline, chosen design, three rejected alternatives, seam, compatibility) and describes exactly the additive diff; the skill library permits holding the design proposal in ECR §4 for a normal change. The stated baseline behaviour ("add joined every argument", "list recognised only `--all`") matches the reconstructed baseline. One caveat: the ECR's baseline test-file hash is not independently reproducible (see below), and there is no standalone `design.md`; ECR §4 serves that role. |
| 5 | No unrelated refactor or scope expansion | **Met** | Baseline-to-current diff is confined to `normalize_tags`, optional `tags`/`tag` parameters, `_option_value`/`parse_add_args`/`parse_list_args`, and the corresponding `main` branches. No architecture, storage, command or output redesign. README and the test helper were updated for the new surface; nothing else moved. |

## Test and CLI results observed

### Test suite (temporary copy, `python3 -m unittest -v`)

```
Ran 14 tests in 0.010s
OK
```

All 14 names executed: 3 original + 11 added. `python3 -B -m py_compile taskcli.py test_taskcli.py` exited 0.

### CLI matrix (temporary `TASKCLI_DATA`)

```
add "write report"                                -> added 0      (exit 0)
add "review report" --tag work --tag urgent       -> added 1      (exit 0)
add "buy milk" --tag home                         -> added 2      (exit 0)
add "plan sprint" --tag=work                      -> added 3      (exit 0)
list                                              -> 4 pending rows, unchanged columns
list --all                                        -> 4 rows
list --tag work                                   -> rows 1 and 3 only
list --tag home                                   -> row 2 only
list --tag missing                                -> empty (exit 0)
done 0                                            -> done write report
list --tag work                                   -> rows 1 and 3 only
list --all --tag work                             -> row 1 ' ', row 3 ' '; row 0 excluded by tag
list --all                                        -> row 0 marked x
```

JSON after the run: row 0 `{"title","done"}` only; tagged rows carried `["work","urgent"]`, `["home"]`, `["work"]`. Repeated duplicate `--tag work --tag work` stored `["work"]` once. Tags were trimmed (`"  work  "` stored as `"work"`); matching is exact and case-sensitive (`Work` did not match `work`), as the README says.

### Legacy compatibility

Hand-written file `[{"title":"legacy pending","done":false},{"title":"legacy done","done":true}]`:

```
list                -> 0 legacy pending
list --all          -> 0 pending, 1 x legacy done
list --tag work     -> empty, exit 0
done 0              -> done legacy pending
add "new tagged" --tag work -> added 2
list --all --tag work -> 2 new tagged
```

The rewritten file kept the first two records as two-field objects and added `tags` only to the new record. A file with extra keys (`priority`) also survived `list`/`done` unchanged. `list --tag` did not modify the data file (SHA-256 unchanged before/after).

### Error paths

```
add "write report" --tag   -> stderr "error: --tag requires a value", exit 1, no file created
list --tag                 -> stderr "error: --tag requires a value", exit 1
add --tag work             -> stderr "error: add requires a title", exit 1
add "x" --tag=             -> stderr "error: --tag requires a value", exit 1
add "x" --tag "  "         -> stderr "error: --tag requires a value", exit 1
list --tag ""              -> stderr "error: --tag requires a value", exit 1
```

These match ECR R6 and the README/tests. `done abc` still prints a Python traceback (exit 1), which is pre-existing baseline behaviour (`done(int(argv[1]))`), not introduced here.

## Artifact consistency

- `README.md` and observed behaviour agree: `--tag`, repeated `--tag`, `--tag=work`, `--` escape, exact/case-sensitive matching, optional tags, and the unchanged `{"title","done"}` shape for untagged adds all checked out.
- ECR §3 R1–R6 and §6's 14-test/3-original claim agree with the run; the worked CLI example (indices 0 and 2 after `done 0`) is consistent with the tests.
- ECR after-change hashes are correct:
  - `taskcli.py` `d9ce3fbb…`
  - `test_taskcli.py` `9fcb18bb…`
  - `README.md` `6d961931…`
  - `docs/engineering-change-record.md` `8d384876…` (matches the EVAL's hash claim).
- Baseline `taskcli.py` hash `4472d811…` was independently reproduced by reconstructing the pre-change file; the diff is additive. This materially supports the ECR rather than treating its hash table as unverified prose.
- ECR scope statements (no tag editing/display/multi-tag filtering, no migration, no release) match the code and README.
- The ECR says the design needed no C4/sequence/ADR; that is reasonable for this local CLI change and is stated explicitly.

## Unsupported or inflated claims

1. **Baseline test-file hash.** The ECR lists `test_taskcli.py` baseline `f1f71490…`. Unlike the `taskcli.py` baseline, I could not reproduce that hash from the available material, and the workspace has no VCS or baseline copy. I therefore cannot verify it. It is not contradicted by anything; it is simply unauditable.
2. **ECR alternatives are compressed.** The design section lists three rejected options with one-line rationales but no per-option trade-off/failure-behaviour table and no explicit "decision owner" inside §4 (the owner appears in §7). The skill library's design-proposal contract is richer; the task only asked for a short record, so this is thinness, not a false claim.
3. **EVAL's reading history.** Claims such as "I did not open `evals/results/behavioral-scenarios`" and the specific list of files read are not verifiable from the workspace. They are immaterial to the delivered behaviour.
4. **"All three original tests pass unchanged."** Accurate for the three test methods; note that the shared `run_main` helper was rewritten to accept varargs and capture stderr. The original tests do not use that helper, so nothing existing broke, but the test file as a whole was not left untouched.
5. **No claim inflation about release/quality.** The ECR/EVAL explicitly say non-versioned, no release, self-review only. That is accurate.

## Defects and missing evidence

1. **`list --tag` crashes on malformed `tags` values.** With `{"tags": null}` or `{"tags": {"a":1}}`, `list` still works but `list --tag work` raises `TypeError` (`tag in task.get("tags", [])` with `None`/dict) and exits 1 with a traceback. Old files cannot contain `tags`, so this is outside the required backward-compatibility case, but the filter is less defensive than the rest of the change and has no test. Severity: low.
2. **Repeated `list --tag` silently uses the last value.** `list --tag work --tag home` returned the `home` result; `list --tag home --tag work` returned the `work` result. The README does not document this and no test covers it. The EVAL discloses it; I confirmed it.
3. **Untested documented behaviour.** Case-sensitive matching is documented and works, but only the CLI matrix exercises it; the test suite does not assert it. The same applies to single-string tags in the Python `add(title, "work")` API. Disclosed in EVAL §5.
4. **No test that filtering is read-only.** I verified the file hash is unchanged after `list --tag`, but no automated test asserts it. Minor.
5. **Pre-existing rough edge retained:** `done abc` traceback. Not a regression and not in scope; noted for completeness.
6. **Discoverability:** `README.md` does not link `docs/engineering-change-record.md` (the reference fixture README does). Cosmetic.
7. **No automated check of ledger/test hash baseline:** the ECR's baseline test hash cannot be re-derived; see above.

## Comparison with the actor's `EVAL.md`

The self-assessment is largely accurate and notably candid:

- Its claim of 14 passing tests, 3 original + 11 added, matches my run exactly.
- Its CLI smoke output is consistent with what I reproduced (same command set, same indices after `done 0`; my run used a different insertion order but the same semantics).
- Its "Met" table for every `TASK.md` requirement is consistent with my findings; I did not find a requirement it marked Met that is actually unmet.
- Its gap list is honest: red-before-green not observed, repeated `list --tag` untested, case sensitivity untested, string-tag API untested, no independent review, no linter/typechecker/coverage. I verified each of those descriptions.
- Minor overstatement: "All three original tests pass unchanged" glosses over the rewritten shared `run_main` helper; the three test bodies are unchanged and pass, so the substance holds.
- The EVAL does not claim the baseline hashes were independently verified; it calls them recorded. The ECR presents them as measured. My independent reproduction of the `taskcli.py` baseline hash supports the ECR's method, but the test-file baseline remains unverified.
- The EVAL's statement that the ECR has "the seven ECR sections, alternatives, hashes and observed commands" is true.

## Overall grade

**Pass with limitations.**

The delivered change satisfies all five expectations: tags and filtering work for pending and all tasks, legacy JSON and existing command/test behaviour are preserved, tests cover the feature while retaining the originals, the ECR describes an extension rather than a rewrite, and the diff contains no unrelated refactor. It is a clean, minimal implementation with an unusually honest self-assessment.

The limitations are real but non-blocking: unverified baseline test hash, no defensive handling of malformed `tags` values, last-wins repeated `list --tag` without documentation, and a few untested documented edge behaviours. None breaks a stated requirement or existing behaviour.
