# Design: streak rules, storage and command surface

**Status:** Accepted design (2026-11-15). Implemented and locally verified; see [the ECR](ecr.md) and [verification](verification.md). This record owns the decisions, not the build status.

## Question and constraints

Three choices materially shape the product and are expensive to change after data exists:

1. **What does "current streak" mean, and what happens when a day is missed?** The source request leaves this open.
2. **How is the data shaped in the JSON file?** The file is the user's durable record.
3. **How does the user name a habit on the command line?** The surface determines daily ergonomics and compatibility.

Constraints from the product brief: one local CLI, Python standard library only, one JSON file, a few personal habits, no accounts or network, local calendar dates. Baseline: **greenfield; the workspace contained only `IDEA.md` when this change started.** There is no existing API, schema or consumer to preserve.

## Affected software types

| Component | Type | Status | Reason |
| --- | --- | --- | --- |
| `habits.py` | library-cli | designed | The change *is* a command-line surface, its file format and its errors. |
| Frontend | — | not affected | No graphical interface. |
| Backend | — | not affected | No service, database or network boundary. |
| AI | — | not affected | No model or inference. |

Because there is one local component, there is no cross-type seam. C4, sequence and state-machine diagrams are not needed to judge this change; the command surface, schema and state table below carry the evidence a CLI reviewer needs. A state table is included because the missed-day rule is the core behavior.

## Decision 1: streak and missed-day behavior

### Options

| Option | Lens | Behavior | Optimizes | Sacrifices |
| --- | --- | --- | --- | --- |
| **A. Day-grace calendar streak** | User motivation | The streak counts consecutive completed days ending **today** if today is done, otherwise ending **yesterday**. A day that has fully elapsed without a completion resets it. | An honest "current" number all day; no punishment before the day is over. | The number can be non-zero while today's action is still undone; needs a clear "at risk" signal. |
| **B. Strict today** | Simple accounting | The streak is non-zero only if today is already done; otherwise it is 0 until `done` runs. | One rule, no grace to explain; maximum daily pressure. | At 08:00 a perfect 30-day run displays 0, which is misleading and discouraging. |
| **C. Skip-token / weekly quota** | Resilience | Missed days consume a finite allowance (for example one skip per week), or adherence is measured over a rolling window. | Forgives occasional misses; supports imperfect routines. | Adds earning, expiry and skip state; "current streak" becomes policy-dependent and hides real gaps. More rules than a small personal tool needs. |

### Worked comparison

Assume the habit was completed Monday, Tuesday and Wednesday. It is now Thursday at 09:00 and today is not marked.

| Option | Displayed streak | What the user learns |
| --- | --- | --- |
| A | **3**, `not done`, at risk | Three days are banked; today is still open. |
| B | **0** | The run appears lost even though the day has barely started. |
| C | 3 while a skip/quota remains | The run survives a miss, but the number no longer means consecutive days. |

After Thursday passes unmarked, A and B both show 0 on Friday. C depends on whether Thursday consumed an allowance.

### Tradeoffs and failure behavior

- **A** can overstate progress early in the day. That is mitigated in the product, not hidden: `list` shows `TODAY = not done` and prints `At risk (not done today): <habits>` for every non-zero streak that is still open. At local midnight, an unmarked day becomes a full miss and the streak becomes 0 on the next read.
- **B** has no misleading grace, but its number is wrong for most of the day from the user's point of view, and it turns `list` into a list of zeros until every habit is done.
- **C** fails ambiguously: two users can disagree about what the streak means, and a corrupted or hand-edited skip count changes history. It is the right option only if the product goal becomes "flexible adherence" rather than "consecutive days".
- All options need a defined boundary: **local calendar date**, not a 24-hour interval. The tool uses `date.today()`; changing timezone mid-day can change which date a new completion receives.

### Decision

**A. Day-grace calendar streak.** The product promise is a *current* streak, and a day is not missed until it has ended. The grace rule matches how people describe a run ("I'm on day 3, I haven't done today's yet"), while still making a missed day a real reset. Option C is deferred because it changes the meaning of the number and adds state the request does not need.

## Decision 2: data shape

### Options

| Option | Shape | Optimizes | Sacrifices |
| --- | --- | --- | --- |
| **A. Habit records with date arrays** | `habits: [{name, created, completions: ["YYYY-MM-DD", ...]}]` | Per-habit streaks, add/remove, readable diffs, easy hand edits. | Whole-document rewrite on every change; a date-oriented query scans habits. |
| **B. Date-indexed map** | `{"2026-11-15": ["Read", "Walk"]}` | Natural "what did I do that day" view; no repeated habit metadata. | Habit rename/remove needs every key touched; per-habit history and creation metadata are awkward; streak reads many keys. |
| **C. Append-only event log** | One record per event: `{event: "done", habit, date}` | Audit trail, append-only writes, easy recovery of history. | Needs replay and compaction; duplicate events; hand-editing is harder; overkill for a few habits. |

### Decision

**A. One versioned document with a sorted, unique date array per habit.** It keeps the file understandable without tooling, makes the streak a direct per-habit read, and lets `remove` delete one record. The whole-file rewrite is acceptable at personal scale. Version 1 is stated in the file so a future reader can refuse or migrate rather than guess.

Consequences:

- Completions are stored as `YYYY-MM-DD`, sorted and deduplicated on load and save.
- A completion is unique per habit per date; repeating `done` never appends a second entry.
- Extra keys are ignored when reading but not preserved when saving; a schema change that needs them must bump `version`.
- There is no locking. A second concurrent writer can overwrite the first; the design assumes one user and one command at a time.
- Writes use a temporary file in the same directory, `fsync`, then `os.replace`, so an interrupted write does not leave a half-written JSON document. The guarantee is reasoned and exercised on the success path; it was not fault-injected.

## Decision 3: command surface and habit identity

### Options

| Option | Surface | Optimizes | Sacrifices |
| --- | --- | --- | --- |
| **A. Name-addressed subcommands** | `add NAME`, `done NAME`, `remove NAME`, `list` | Readable daily use; no lookup step; easy to script. | Names must be unique; renaming is not supported; a long name must be quoted. |
| **B. ID-addressed commands** | `add` prints an ID; `done 3`; `remove 3` | Stable identity under rename; short arguments. | Requires a lookup before every action; IDs are not memorable; needs allocation and display. |
| **C. Interactive menu** | Run with no command; choose from a numbered list | Discoverable; no argument syntax. | Not scriptable; more code and terminal handling; slower for the one daily action. |

### Decision

**A. Name-addressed subcommands.** With a handful of habits, the name is the memorable identity. Matching is forgiving: whitespace is collapsed and comparison is case-insensitive, while the first-added display name is preserved. A duplicate add is rejected rather than silently merging. Rename is out of scope; `remove` plus `add` is the escape hatch.

The global option `--file PATH` is accepted **before** the command. Precedence is `--file` > `HABITS_FILE` > `~/.habits.json`.

## Linked design artifacts

### Command surface

```text
habits.py [--file PATH] add NAME
habits.py [--file PATH] done NAME
habits.py [--file PATH] remove NAME
habits.py [--file PATH] list
habits.py --help
```

| Command | Success output | Side effect |
| --- | --- | --- |
| `add NAME` | `Added "<name>".` | Appends a habit with an empty history. |
| `done NAME` | `Marked "<name>" done for <date>. Current streak: N.` | Adds today once; second run prints `Already marked` and writes nothing. |
| `remove NAME` | `Removed "<name>" and N completion(s).` | Deletes the habit and its history immediately. |
| `list` | Aligned table plus an optional at-risk line. | None; a missing file is not created. |

### Data schema (version 1)

```json
{
  "version": 1,
  "habits": [
    {
      "name": "Read 10 pages",
      "created": "2026-11-15",
      "completions": [
        "2026-11-15"
      ]
    }
  ]
}
```

Invariants: top-level object; `version == 1`; `habits` is a list; each name is a non-empty string unique under case-insensitive whitespace normalization; `created` is a valid `YYYY-MM-DD`; `completions` is a list of valid `YYYY-MM-DD` values, sorted and unique after load.

### Streak state table

| Stored state for one habit | Streak | `TODAY` | At-risk hint |
| --- | --- | --- | --- |
| Today and the preceding N−1 days completed | N | `done` | No |
| Today not completed; yesterday and the preceding N−1 days completed | N | `not done` | Yes |
| Today not completed; yesterday not completed | 0 | `not done` | No |
| No completions, or only dates in the future | 0 | `not done` | No |

A future-dated entry is ignored by the streak calculation. The CLI cannot create one; it can appear only through hand-editing, and it is retained in the file.

### Compatibility matrix

| Dimension | Claim | Evidence |
| --- | --- | --- |
| Python syntax | 3.9+ | Test suite ran on 3.14.7 and 3.9.6. |
| Platform | macOS | Exercised on macOS (Darwin). Linux and Windows are unverified. |
| Dependencies | None beyond the standard library | Imports: `argparse`, `json`, `os`, `sys`, `tempfile`, `datetime`, `pathlib`, `typing`. |
| Install | None; run the file from its directory | `python3 habits.py ...` is the supported entry point. |
| File schema | Version 1, exact-match gate | A different `version` exits 2 with a diagnostic; no migration exists. |
| Backward compatibility | No prior released surface | Greenfield personal tool; no versioning promise yet. |
| Concurrency | Single writer assumed | No locking; last successful replace wins. |
| Locale | English messages; dates ISO-8601 | No localization. |

### Usage: main path and one failure path

```text
$ python3 habits.py --file ./demo.json add "Read 10 pages"
Added "Read 10 pages".
$ python3 habits.py --file ./demo.json done "read 10 pages"
Marked "Read 10 pages" done for 2026-11-15. Current streak: 1.
$ python3 habits.py --file ./demo.json list
NAME           STREAK  TODAY
Read 10 pages       1  done

$ python3 habits.py --file ./demo.json done "Meditate"
habits: error: no habit named "Meditate"; run "habits.py list" to see habits
$ echo $?
1
```

## Error and exit-code contract

| Condition | Diagnostic | Exit |
| --- | --- | --- |
| Successful command | Normal output | 0 |
| Duplicate habit, unknown habit, whitespace-only name | `habits: error: ...` on stderr | 1 |
| Missing file on `list` | Empty-state guidance, no file created | 0 |
| Missing file on `add` | Created with parent directories | 0 |
| Malformed JSON, wrong schema version, invalid date, duplicate names in file | `habits: error: ...` on stderr, no write | 2 |
| Unreadable or unwritable path | `habits: error: cannot read/write ...` | 2 |
| Invalid command-line usage (argparse) | Usage plus argparse diagnostic | 2 |

Expected errors never print a traceback. Unexpected programming errors are allowed to surface as tracebacks so they are not mistaken for user error.

## Seam decisions

Not applicable. The change has one local component and no service, UI, provider or multi-type boundary. The file is the only interface, and its schema and atomic-write behavior are decided above once.

## Recommendation and decision

```text
Decision: day-grace calendar streak; per-habit sorted date arrays in a
  versioned JSON document; name-addressed add/done/remove/list commands.
Options considered: strict-today streak; skip-token/weekly adherence;
  date-indexed map; append-only event log; ID-addressed commands;
  interactive menu.
Chosen because: it matches the user's language for a current streak,
  keeps a human-readable file, and makes the daily action one short command.
Rejected because: strict-today misreports a run for most of the day;
  skip tokens change the meaning of the number and add state;
  a date map makes per-habit history awkward; an event log needs replay and
  compaction; IDs add a lookup; a menu is not scriptable.
Accepted/delegated by: author, who is the sole user.
Status: accepted.
Revisit if: backfilling, timezone travel, multiple writers, or a desire for
  best-streak/history makes this schema or rule insufficient.
```

## Evidence and open questions

At decision time the implementation did not exist, so the evidence was the source request, the constraints above and the compared behavior. After implementation, the rules in the state table were exercised through 33 standard-library tests on Python 3.14.7 and 3.9.6, and the CLI was run on a demo file; see [verification](verification.md). The tests establish the implemented behavior, not long-term user satisfaction.

Open, non-blocking:

- Whether missed days should ever be repairable. Current answer: no; `done` records today only.
- Whether a best-streak or history view should read the existing completions. Current answer: deferred; the data supports it later.
- Whether Windows and Linux behave identically. Not exercised.
- Whether display alignment holds for double-width scripts. Not tested.
