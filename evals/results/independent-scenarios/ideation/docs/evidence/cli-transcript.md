# CLI evidence transcript

Observed on macOS 27.0.1 with Python 3.14.7, using a temporary data directory.
The date was fixed with `--today 2026-11-15` so the streak result is reproducible.
`$DEMO` stands for that temporary directory; the absolute path is elided.

```text
$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 list
No habits yet. Add one with: python3 habits.py add "Read"
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 add 'Read 30 minutes'
Added "Read 30 minutes" with id read-30-minutes.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 add Walk
Added "Walk" with id walk.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done read-30-minutes
Marked "Read 30 minutes" done on 2026-11-15. Current streak: 1 day.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done read-30-minutes
Already marked "Read 30 minutes" done on 2026-11-15. Current streak: 1 day.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done read-30-minutes --date 2026-11-14
Marked "Read 30 minutes" done on 2026-11-14. Current streak: 2 days.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 list
ID               NAME             STREAK  TODAY  LAST DONE
read-30-minutes  Read 30 minutes       2  yes    2026-11-15
walk             Walk                  0  no     -
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 show read-30-minutes
Read 30 minutes (read-30-minutes)
  Created:        2026-11-15
  Current streak: 2 days (through 2026-11-15)
  Longest streak: 2 days
  Today:          done
  Last done:      2026-11-15
  Recent:
    2026-11-09  Mon    -
    2026-11-10  Tue    -
    2026-11-11  Wed    -
    2026-11-12  Thu    -
    2026-11-13  Fri    -
    2026-11-14  Sat    done
    2026-11-15  today  done
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done walk --date 2026-11-12
Marked "Walk" done on 2026-11-12. Current streak: 0 days.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done walk --date 2026-11-13
Marked "Walk" done on 2026-11-13. Current streak: 0 days.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 list
ID               NAME             STREAK  TODAY  LAST DONE
read-30-minutes  Read 30 minutes       2  yes    2026-11-15
walk             Walk                  0  no     2026-11-13
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done walk
Marked "Walk" done on 2026-11-15. Current streak: 1 day.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 undo walk
Removed "Walk" from 2026-11-15. Current streak: 0 days.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 remove read-30-minutes
habits: refusing to remove "Read 30 minutes" without --yes (this deletes its history)
[exit 1]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 remove read-30-minutes --yes
Removed habit "Read 30 minutes" (read-30-minutes) with 2 completions.
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 list
ID    NAME  STREAK  TODAY  LAST DONE
walk  Walk       0  no     2026-11-13
[exit 0]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done nope
habits: no habit matches 'nope'; run 'list' to see ids
[exit 1]

$ python3 habits.py --file "$DEMO/habits.json" --today 2026-11-15 done walk --date 2026-11-16
habits: cannot mark a future date (2026-11-16) as done; today is 2026-11-15
[exit 1]
```
