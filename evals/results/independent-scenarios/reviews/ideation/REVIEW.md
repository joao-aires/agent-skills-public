# Independent review: habit tracker CLI

**Actor workspace:** `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-independent-evals/ideation`

**Review method:** inspected all source, test and `docs/` files; ran the full `unittest` suite; replayed the recorded 18-command CLI transcript against a fresh temporary data directory; independently exercised the CLI (streaks, missed days, backfill, undo, future dates, malformed dates, permissions, real-date smoke); compared the records to the code and to each other; checked hashes, test counts, help output and Markdown links. The actor's source and documentation were not edited; the recorded content hashes still match after inspection.

## Verdict

**Pass.** The vague request has been turned into a bounded, implemented and tested local CLI. Streak and missed-day semantics are explicit in the design record, README, help text, module docstring and tests, and the implemented behavior matches them. The product, design, ECR and verification records agree on the consequential facts, with only minor wording/precision nits. Open ideas are explicitly deferred rather than stubbed. No correctness defect was found in the verified scope.

This is not a claim that the product is validated in real use; the actor explicitly and correctly records that it is not.

## Expectation assessment

| # | Expectation | Status | Evidence |
| --- | --- | --- | --- |
| 1 | A bounded product outcome and observable acceptance replace the vague idea | **Met** | `docs/product/prd.md` defines one-user audience, the two questions to answer, a six-item in-scope list, explicit non-goals (accounts/sync/reminders/schedules/analytics/packaging), a success signal and open decisions. `docs/change/ecr.md` §3 turns the outcome into R1–R14 with actor/action/observable-result rows and named evidence. The simulated acceptance journey in the PRD ("two consecutive completions, a missed day, then today") is actually encoded in `test_missed_day_resets_streak_but_keeps_history`. |
| 2 | Streak and missed-day behavior are explicitly decided | **Met** | `docs/design/design-proposal.md` compares four materially different options (A calendar run through yesterday, B strict today, C rolling quota, D schedules), records A with rationale, rejected alternatives and revisit triggers. `docs/design/streak-cases.md` gives 12 worked cases plus a cross-option comparison. The rule is repeated in `habits.py`'s module docstring, `README.md`, the `--help` epilog and 11 pure streak tests. Observed CLI results matched: run through yesterday reports 2 with `TODAY no`; a two-day-old run reports 0 and retains history; marking today after a miss reports 1. |
| 3 | A useful slice is implemented and tested, not an unbounded platform | **Met** | `habits.py` is a 566-line stdlib-only script with six commands (`add`, `list`, `done`, `undo`, `show`, `remove`) and global `--file`, `--today`, `--version`. No server, network, database, UI, sync, scheduling or third-party package exists. `test_habits.py` has 44 tests: 11 pure streak, 4 data-path and 29 CLI subprocess tests. The full suite passed in my run (44 tests, `OK`, 4.456s). |
| 4 | The product, ECR, design and verification records agree | **Met** (minor nits) | SHA-256 values in `ecr.md` and `verification.md` match the current files exactly. Test counts (44 total; 11/4/29) match the source and the captured output. The 18-command transcript replayed with 0 mismatches. `help.txt` is byte-identical to current `--help`. Data-path precedence, exit codes and the six-command surface match across PRD, design, ECR, README, help and parser. All Markdown links and anchors resolve. Nits are listed below. |
| 5 | Open ideas are deferred rather than silently dropped or half-built | **Met** | PRD §Open decisions lists planned rest days/weekly targets (deferred), installed command (deferred), real-use value (not measured) and non-daily schedules (out of scope), each with an owner and evidence trigger. ECR §7 repeats the open decisions; the design proposal gives "Revisit if" triggers. Nothing in the code is a half-built stub for these items. |

## Test and CLI results observed

Full suite:

```text
$ cd <actor workspace> && python3 -m unittest -v
...
Ran 44 tests in 4.456s

OK
```

The 44 recorded names in `docs/evidence/test-output.txt` are exactly the 44 names produced by a fresh run (set comparison; no missing or extra test names).

CLI replay:

```text
Parsed 18 command blocks from docs/evidence/cli-transcript.md
Executed each in a fresh temporary directory with DEMO set
0 mismatches in stdout/stderr or exit status
```

Independent probes in temporary directories (the actor's data file was not used):

```text
$ python3 habits.py --file "$H" --today 2026-11-15 list
No habits yet. Add one with: python3 habits.py add "Read"
[exit 0]

$ ... add Read
Added "Read" with id read.                                [exit 0]
$ ... done read --date 2026-11-13
Marked "Read" done on 2026-11-13. Current streak: 0 days.  [exit 0]
$ ... done read --date 2026-11-14
Marked "Read" done on 2026-11-14. Current streak: 2 days.  [exit 0]
$ ... list
ID    NAME  STREAK  TODAY  LAST DONE
read  Read       2  no     2026-11-14                        [exit 0]
$ ... show read
Current streak: 2 days (through 2026-11-14; today not marked)
Today:          not done
[exit 0]

$ ... done read --date 2026-11-16
habits: cannot mark a future date (2026-11-16) as done; today is 2026-11-15
[exit 1]

$ ... frobnicate
habits.py: error: argument command: invalid choice: 'frobnicate'
[exit 2]
```

Additional observations:

- `python3 -m py_compile habits.py test_habits.py` exited 0 with no output.
- `python3 habits.py --help` diffed clean against `docs/evidence/help.txt`.
- Permission probe: an application-created parent directory was `drwxr-xr-x` (0755) and the data file was `-rw-------` (0600), matching the verification record.
- Real-date smoke with `HABITS_FILE` and no `--today`: `add Stretch`, `done stretch`, `list` produced `STREAK 1`, `TODAY yes`, `LAST DONE 2026-11-15`, all exit 0, matching the record.
- Summary of the replay: 18 transcript commands, 15 exit 0 and 3 expected failures exit 1 (remove without `--yes`, unknown habit, future date), matching `EVAL.md`.

## Artifact consistency findings

Confirmed consistent:

- **Revision identity:** `habits.py` `00fad9c5e5ccfcbfbc6e072fc0eb6543509ceb7057b1e4808a2cd82694b13414` and `test_habits.py` `33025bb6a3dce43c0b83306f819cfdf0ef66a107ec6859dbed66dd772136915a` match ECR §1/§6 and verification §Revision and environment.
- **Test evidence:** 44 tests, 11/4/29 split, all named tests present; captured `Ran 44 tests in 4.332s`, `OK` is a plausible earlier run (my run was 4.456s; the record explicitly says wall time varies).
- **CLI evidence:** all 18 transcript blocks reproduced exactly, including the missed-day reset, undo, removal refusal and future-date error.
- **Surface:** parser has exactly the commands and globals described in design §Surface and compatibility, README and help.
- **Data path:** code implements `--file` → `HABITS_FILE` → `XDG_DATA_HOME/habits/habits.json` → `~/.local/share/habits/habits.json`, as documented; tests cover the resolver and the environment-variable path.
- **Streak rule:** `current_streak` and `longest_streak` match every row of `streak-cases.md`; the CLI row/status strings match the documented renderings.
- **Errors/exit codes:** observed 1 for data/habit errors and future dates, 2 for argparse/unknown-command errors, 0 for success and idempotent no-ops, as documented.
- **Links:** 10 Markdown files (including `EVAL.md`) were checked; 0 missing files or anchors.

Minor consistency nits (not enough to fail the expectation):

1. `docs/evidence/verification.md` labels the 11 pure tests "streak and date rules" and names `parse_date` among what they exercise directly. The 11 `StreakTests` do not call `parse_date`; it is exercised indirectly through the CLI malformed-date test. The count is right, the coverage description is slightly broader than the suite.
2. ECR R4 says the reported streak "becomes 1" after marking today. That is true for a fresh habit (the tested case), but marking today after a completed yesterday reports 2. The implementation is correct per the chosen rule; the requirement wording is narrower than the general behavior.
3. The 80-character name cap in `require_name` is user-visible (`habits: habit name is too long (maximum 80 characters)`, exit 1) but is not mentioned in README, help, PRD, design surface or ECR acceptance. This is an undocumented constraint, not a contradiction.
4. ECR says unknown data-file fields are "ignored"; `load_store` tolerates them, but `save_store` rewrites from the dataclass and drops them on the next write. "Ignored" is ambiguous; preservation was never claimed.
5. ECR §5 says "four presentation/contract defects", while verification lists seven review findings. The four can reasonably map to findings 2–5 (duplicate dates, malformed-date exit code, removal wording, undo of future entries), with the helper and weak-assertion items separate. The count is reconcilable but the two sections could be read as inconsistent.
6. README's quickstart shows a hard-coded `2026-11-15` result while saying the date is today's local date. It is clearly presented as a captured example, so this is cosmetic.

## Unsupported or inflated claims

- **EVAL self-assessment is accurate, not inflated.** Its concrete claims were independently checked: 44 tests pass, the 44/11/4/29 count is right, the 18-command transcript is exact, the 0600/0755 permission probe is right, the hashes are right, and the real-date smoke reproduces. It explicitly says real use, cross-platform support, concurrency safety, coverage, packaging and independent review are absent. It does not claim product benefit.
- The **historical process timeline** in EVAL (red run before `habits.py`, the 41-test failure and repair sequence, a 4.171s intermediate run) cannot be verified from the final state. It is plausible and consistent with the current helper names and suite, but should be treated as actor-reported process history, not independently observed evidence. It is not load-bearing for any deliverable claim.
- EVAL says "9 Markdown files checked"; the workspace now has 10 including `EVAL.md`, or 9 artifact Markdown files if `EVAL.md` itself is excluded. My independent check over all 10 found 0 broken links/anchors.
- No claim of a released, packaged or real-use-validated product is made anywhere; the ECR's "ready with limitations" disposition matches the evidence.

## Defects and missing evidence

No functional defect was found in the verified scope: the fresh suite passes, the transcript is exact, the rule is implemented as specified, and I could not induce a behavior that contradicts the documented contract.

Missing or weak evidence, mostly already disclosed:

- **No real-use evidence.** The PRD success signal is explicitly unmeasured; tests prove defined behavior, not behavior change.
- **One environment only.** Verified on CPython 3.14.7/macOS 27.0.1; no Linux/Windows/other interpreter run.
- **No concurrency safety.** Atomic per-file replace but no lock; concurrent writers can lose an update (disclosed).
- **Unverified failure edges.** Crash injection around `os.replace`, disk-full, permission-denied on existing paths, symlinked data files, very large histories, narrow terminals and timezone travel are not exercised (disclosed).
- **Coverage gaps.** No direct unit test for `parse_date` itself; no test for the 80-character name cap; no test for an unknown data-file field being tolerated/dropped; no test for `show` on a habit with no completions (I observed it manually); no test for `--today` malformed input. These are small and do not undermine the acceptance claims.
- **No independent review or linter/type checker/coverage report** in the actor's process (disclosed in EVAL).
- **No license, packaging or release artifact** (disclosed).

## Comparison with the actor's `EVAL.md`

`EVAL.md` is unusually honest and its numerical self-assessment holds up:

- Artifact list matches the files that exist.
- Test breakdown and transcript counts match my independent count and replay.
- Hash, permission-probe and real-date-smoke claims match.
- Gaps section correctly names the missing real-use trial, single-platform scope, no concurrency lock, no packaging, no coverage and no independent review.
- The "ready with limitations" status is consistent with the ECR and verification records; it does not overstate readiness.
- Minor discrepancies: the "9 Markdown files" count (10 now, 9 artifacts) and the "11 pure streak/date tests" label (the 11 are streak-only). Historical intermediate-run timings and the red-first sequence are unverifiable but not inflated. None of these change the verdict.

## Overall grade

**Pass.**

The deliverable meets all five expectations. The implementation is a bounded, working slice; the streak/missed-day decision is explicit, implemented and tested; the product/design/change/evidence records agree on hashes, counts, surface, data paths, exit codes and observed behavior; and deferred ideas are listed rather than half-built. The remaining issues are documentation precision nits and disclosed verification limits, not failures of the slice.
