# Streak cases and worked timeline

This is the linked design artifact for the chosen **Option A** in the [design proposal](design-proposal.md). It is a specification of expected results, not implementation evidence. Observed results are in [verification](../evidence/verification.md).

## The rule in one paragraph

A completion is stored as a local calendar date. The **current streak** is the length of the consecutive run of completed dates that ends **today**, or ends **yesterday** when today has no completion. There is a grace window of exactly one day: if both today and yesterday are unmarked, the current streak is 0 even when earlier days were completed. Future dates never count. A missed calendar day breaks the run; the next completion starts a new run of 1. The longest streak is the longest consecutive run in the non-future history, independent of today.

## Worked cases

Today is **2026-11-15** in every row.

| Completed dates | Current streak | Today | Reader-visible explanation | Case |
| --- | --- | --- | --- | --- |
| none | 0 | no | `0 days (no completions yet)` | fresh habit |
| 15 | 1 | yes | `1 day (through 2026-11-15)` | first completion |
| 14, 15 | 2 | yes | `2 days (through 2026-11-15)` | normal extension |
| 13, 14 | 2 | no | `2 days (through 2026-11-14; today not marked)` | live run, today still open |
| 14 | 1 | no | `1 day (through 2026-11-14; today not marked)` | single live day |
| 13 | 0 | no | `0 days (broken; last done 2026-11-13)` | yesterday missing breaks it |
| 12, 13 | 0 | no | `0 days (broken; last done 2026-11-13)` | two-day-old run is not current |
| 12, 15 | 1 | yes | `1 day (through 2026-11-15)` | gap, then today restarts |
| 10, 11, 12, 13, 14, 15 | 6 | yes | `6 days (through 2026-11-15)` | longer run |
| 15, 16 | 1 | yes | `1 day (through 2026-11-15)` | future date ignored |
| 15, 15 | 1 | yes | `1 day (through 2026-11-15)` | duplicate collapses to one day |
| 13, 14, 15 | 3 | yes | `3 days (through 2026-11-15)` | backfilled run |

### Same input under strict Option B

For completion set `13, 14` with today `2026-11-15`, Option A reports **2**; Option B (today-required) reports **0** until 15 is marked. This is the visible difference that made the choice consequential.

## Cross-option comparison

The same history is used to judge each direction at comparable fidelity. Completions: Mon 9, Tue 10, Thu 12, Fri 13, Sat 14. Today is Sun 15 and is unmarked.

| Option | Reader-visible result | Why |
| --- | --- | --- |
| A: calendar run, active through yesterday | `3 days (through 2026-11-14; today not marked)` | Thu–Sat are consecutive and today can still extend the run |
| B: strict today-required | `0 days` | Today is required, so the Thu–Sat run is not shown as current |
| C: trailing seven-day quota, target 5 | `5 of the last 7 days` (quota met), no day streak | The window meets the frequency target even though Wednesday is missing; there is no current day-run to display |
| D: scheduled Mon/Wed/Fri | `1 scheduled day` (Fri 13), with Wed 11 breaking the prior run; Sat 14 is off-schedule and ignored under the stated policy | Only scheduled days count; a different off-schedule policy would produce a different number, which is why D needs one more decision |

Option C replaces the requested day-streak; Option D needs a schedule and an off-schedule policy. The comparison is enough to reject both for this slice without claiming they are bad products for another need.


## Rendering examples

`list` uses one row per habit. The separate `TODAY` column is deliberate: a nonzero streak never means "done today".

```text
ID    NAME  STREAK  TODAY  LAST DONE
read  Read       2  no     2026-11-14
```

`show` makes the grace window and the break visible in words:

```text
Read (read)
  Created:        2026-11-01
  Current streak: 2 days (through 2026-11-14; today not marked)
  Longest streak: 2 days
  Today:          not done
  Last done:      2026-11-14
  Recent:
    2026-11-09  Mon    -
    2026-11-10  Tue    -
    2026-11-11  Wed    -
    2026-11-12  Thu    -
    2026-11-13  Fri    done
    2026-11-14  Sat    done
    2026-11-15  today  -
```

## Boundaries and edge behavior

- **Backfill may predate creation.** `created_on` records when the habit was added; it does not restrict historical completions. This lets a user start tracking and enter the last few days.
- **Derived, not stored.** The streak is recalculated from the completion set on every read. Undo, backfill or a hand edit cannot leave a stale stored counter.
- **Future dates.** `done` rejects them. Loaded future dates are ignored by current and longest streak; `undo --date` can remove them for recovery.
- **Local dates only.** No time of day or timezone is stored. Travel can repeat or skip a local date; `--today` is the correction mechanism.
- **Midnight.** A process that starts before midnight and writes after midnight uses the date resolved at command start. There is no background job.
- **No partial day.** A habit is done for the day or not; there is no count-per-day or duration.

## Acceptance mapping

The pure cases above are covered by `StreakTests`; the reader-visible strings and CLI behavior are covered by `CliTests`. Test names and observed results are recorded in [the ECR requirements table](../change/ecr.md#3-requirements-and-acceptance) and the [test output](../evidence/test-output.txt).
