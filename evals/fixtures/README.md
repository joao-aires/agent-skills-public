# Behavioral evaluation fixtures

Initial states for the scenarios in `evals/behavioral-scenarios.json`. Copy a fixture to a fresh temporary directory before each run; never run the actor in the fixture itself.

| Fixture | Initial state | Check |
| --- | --- | --- |
| `new-app` | `TASK.md` only | No code or tests exist |
| `existing-feature` | Working task CLI, 3 passing tests | `python3 -m unittest -v` → OK |
| `bug-fix` | Pagination library with a deliberate off-by-one | `python3 -m unittest -v` → 3 failures |
| `ideation` | `IDEA.md` only | No code, tests or docs exist |

## Run

```bash
tmp=$(mktemp -d)
cp -R evals/fixtures/existing-feature/. "$tmp/"
cd "$tmp"
python3 -m unittest -v
```

Give the actor the copied directory and the task file. Do not give it the expected criteria or prior evaluation records. Run the reviewer in a separate context against the actor's output.

Fixtures are intentionally small and use only the Python standard library. They are not production applications.
