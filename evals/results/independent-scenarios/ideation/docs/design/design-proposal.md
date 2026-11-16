# Design proposal: streak and missed-day semantics

Status: **accepted for the first slice**; the requester delegated the choice in the implementation request. Implementation and verification are recorded in the [ECR](../change/ecr.md); this proposal does not claim behavior by itself.

## Question and constraints

How should a daily habit's **current streak** behave when today is not marked yet, and what should a missed calendar day do?

The accepted outcome from [IDEA.md](../../IDEA.md): track a few daily habits, mark one done for today, show the current streak for each habit, and keep state in a local JSON file with no third-party dependencies. The requester explicitly left the command names, data model and missed-day handling undecided.

Constraints:

- One local, human-editable JSON file; no database or service.
- Standard-library Python; no network, credentials or third-party packages.
- A short, scriptable command surface for one person.
- A missed day must be explicit, not hidden by a forgiving display.
- Greenfield: no implementation existed at decision time.

## Affected software types

| Component | Type | Status | Reason |
| --- | --- | --- | --- |
| `habits.py` | library/CLI | designed | Command surface, local persistence, exit codes and help are the product |
| Service/API | backend | not affected | No server, API, worker or remote store |
| Screen | frontend | not affected | Terminal text only; no graphical interaction |
| Model behavior | AI | not affected | No model, inference or evaluation set |

No seam exists between components. The only external boundary is the local filesystem.

## Options

| Option | Lens | Behavior | Optimizes | Sacrifices | Decision |
| --- | --- | --- | --- | --- | --- |
| **A. Calendar run, active through yesterday** | Daily consistency | Streak counts consecutive completed calendar days ending today, or ending yesterday when today is unmarked. Any earlier gap yields 0. Marking today extends it. | A morning check shows the run the owner still has; today is clearly "not done" without pretending the run is already broken. | A user who does not mark today sees a nonzero streak that will break tomorrow; the display needs "today not marked" wording. | **Recommended** |
| **B. Strict today-required run** | Immediate urgency | Streak counts only if today is completed; otherwise it is 0, even if yesterday was completed. | Unambiguous "streak only counts when today is done"; no grace interpretation. | Every early-day check looks like failure; users may mark before doing the habit just to keep the number. | Rejected |
| **C. Rolling weekly quota** | Flexible cadence | Replace the day streak with "n of the last 7 days" against a per-habit target. Missed individual days do not break anything; the quota does. | Realistic for habits that need frequency, not daily perfection. | Does not provide the requested current day-streak; needs targets and a different display; a missed day is easier to overlook. | Rejected for this slice |
| **D. Per-habit planned schedule** | Realistic routine | Each habit declares scheduled weekdays; only scheduled days count, and unscheduled days are neutral. A missed scheduled day breaks the run. | Handles gym/commute-style routines and planned rest days honestly. | Adds schedule configuration, migration and a policy for off-schedule completions; a daily habit still needs the same missed-day decision as A. | Rejected for this slice |

### Worked comparison and linked artifacts

The same history is applied to all four directions in [streak cases § Cross-option comparison](streak-cases.md#cross-option-comparison): A reports a 3-day live run, B reports 0 until today is marked, C reports a five-of-seven quota, and D reports one scheduled day with an unresolved off-schedule policy. That table is the shared artifact used to compare the directions at comparable fidelity.

- [Streak cases and worked timeline](streak-cases.md) — the chosen rule, every edge case and the cross-option comparison used to write the tests.
- [CLI evidence transcript](../evidence/cli-transcript.md) — observed outputs after implementation, including a missed-day reset and the active-through-yesterday case. This is verification, not design validation.
- No design specification, C4, sequence or state-machine view applies: this is one local command with no service or interaction surface. A compatibility matrix is reduced to the [surface and compatibility](#surface-and-compatibility) section below.

## Tradeoffs and failure behavior

| Concern | A (chosen) | B | C | D |
| --- | --- | --- | --- | --- |
| Missed one day | Streak 0 immediately after the missed day; history remains and backfill can repair it | Same | May still meet quota; no day-level signal | Breaks only if the missed day was scheduled |
| Today unmarked | Shows the live run through yesterday, labeled "today not marked" | Shows 0 | Shows quota status | Shows the scheduled run |
| Backfill | A past date can restore a run; `current_streak` recalculates | Same | Recalculates quota | Recalculates scheduled run |
| Bad input | Reject future completion dates; reject unknown habit; refuse corrupt JSON without overwriting | Same | Needs target validation | Needs schedule validation and off-schedule policy |
| Data loss risk | Atomic replace; no lock against concurrent processes | Same | Same | Same plus schema migration |
| User misread | Nonzero streak may be read as "done today"; separate `TODAY` column and show wording prevent this | Zero may be read as "all prior work lost" | Quota may hide a lapse | Rest days may look like missing data |

Additional chosen-option failure behavior:

- A corrupt or unsupported data file is **refused**; the tool does not silently start empty or overwrite it.
- Future dates are rejected on write. They are ignored by streak calculation so a clock change cannot inflate a streak; `undo` can still remove an existing future entry for recovery.
- Duplicate habit names are rejected case-insensitively. Duplicate ids in a hand-edited file are rejected at load.
- Removing a habit requires `--yes` and deletes its history.
- A timezone change can make a local calendar date repeat or disappear. The tool stores dates, not timestamps, and offers `--today` for correction; it does not attempt timezone conversion.
- Two concurrent processes can lose one process's update because there is no file lock. This is acceptable for one-person local use and is recorded as a limit.

## Surface and compatibility

| Surface | Contract |
| --- | --- |
| `add NAME...` | Create a habit; id is a lowercase ASCII slug, suffixed on collision; names are unique case-insensitively |
| `list` | One row per habit: id, name, current streak, today yes/no, last completion |
| `done HABIT [--date YYYY-MM-DD]` | Idempotent for an already-marked day; rejects future dates; default is today |
| `undo HABIT [--date YYYY-MM-DD]` | Removes an existing completion; errors if the day is not marked; also cleans future entries |
| `show HABIT` | Created date, current and longest streak, today, last done, last seven days |
| `remove HABIT --yes` | Permanently deletes a habit and its history; refuses without `--yes` |
| `--file PATH` / `HABITS_FILE` / XDG / home | Precedence in that order; parent directories are created |
| `--today YYYY-MM-DD` | Overrides the local date used for streak evaluation and defaults |
| Exit codes | `0` success or harmless no-op; `1` data/habit error; `2` usage error |
| Dependencies | Python standard library only |
| Compatibility | Exercised on Python 3.14.7 / macOS 27.0.1; no other interpreter or platform was tested |
| Packaging | Single executable script; no install, package or release claim |

## Seam decisions

There is no multi-component seam. The filesystem boundary is decided once:

- Configuration precedence is `--file`, `HABITS_FILE`, `XDG_DATA_HOME`, home.
- Normal output goes to stdout; diagnostics go to stderr.
- The file is replaced atomically through a same-directory temporary file.
- A missing file is an empty store; an unreadable, corrupt or unsupported file is an error.
- No network, credential or permission boundary exists.

## Recommendation and decision

Recommend **Option A**. It keeps the requested day-streak meaning, preserves a run the owner can still extend today, and makes the missed-day break explicit without inventing schedules or quotas. Option B was rejected because it makes an ordinary morning check look like failure. Option C was rejected because it removes the requested current streak and needs per-habit targets. Option D was rejected for this slice because schedule configuration and off-schedule policy add a data migration and a larger surface than the request justifies.

The requester owns the product choice; this slice was implemented on their behalf and the semantics are stated in the README and help output. Real-use acceptance is not recorded.

Decision:
Options considered: A, B, C, D above.
Chosen because: it preserves a live run through yesterday, keeps today's incompletion visible, and adds no schedule or quota model.
Rejected because: B treats an unmarked morning as failure; C loses the requested day streak; D adds configuration and policy beyond the slice.
Accepted/delegated by: requester (implementation request); no separate product review.
Status: accepted for the first slice.
Revisit if: the owner repeatedly needs planned rest days or weekly targets, reports that a nonzero streak reads as "already done today", or wants more than one local writer.

## Evidence and open questions

- The rule was encoded in 11 pure streak tests and exercised through the CLI for consecutive days, an unmarked today, a missed day, backfill, undo, corrupt data, future dates and removal.
- No design validation preceded implementation. The command probe and test run happened after implementation, so they are verification. Only the implemented surface was exercised; no independent consumer or clean-install test exists.
- Observed evidence is recorded in [verification](../evidence/verification.md); design intent alone is not a behavior claim.
- Open: real-use value, the need for planned rest days, and whether an installed command reduces friction. Owners and triggers are recorded in the [PRD](../product/prd.md#open-decisions).
