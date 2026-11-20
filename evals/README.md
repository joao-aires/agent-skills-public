# Evaluation suite

[What runs when](#what-runs-when) · [One case](#one-complete-case) · [Deterministic and advisory](#deterministic-and-advisory) · [Provider constraints](#provider-constraints) · [Lifecycle map](#lifecycle-map-10--13--20) · [Records and retention](#records-and-retention) · [Limits](#recorded-evidence-and-limits)

A small, runnable [promptfoo](https://www.promptfoo.dev/) suite for the installed bundles. It replaces
the prose catalogue: one YAML file per case, deterministic assertions carry the verdict, and an
optional judge is advisory. V1 has 18 cases. The cap is about 60; do not add a case per skill or per guide.

The previous 225-case catalogue is preserved by the annotated tag
`evals-baseline-2026-11` (commit `11788bf`). The JSON files are gone from the working tree.

## What runs when

| Command | Cases | Needs a model | Purpose |
| --- | --- | --- | --- |
| `npm --prefix evals run lint` | config only | no | Unique ids, valid gate/stage/kind, fixtures, `pr` count, flows |
| `npx promptfoo validate config -c evals/promptfooconfig.yaml` | config only | no | promptfoo schema and file references |
| `npm --prefix evals run eval:pr` | 10 (`gate: pr`) | yes | Per-change gate; deterministic only |
| `npm --prefix evals run eval:ci` | 10 (`gate: pr`) | yes | CI entry point; same set, writes `.runs/` |
| `npm --prefix evals run eval:nightly` | 8 (`gate: nightly`) | yes | Longer journeys and cross-phase checks |
| `EVAL_FULL=1 npm --prefix evals run eval:full -- --yes` | 18 | yes | Explicit full suite |
| `npm --prefix evals run judge -- .runs/<run>` | recorded run | judge model | Advisory grade; always exits 0 |

CI runs only lint and config validation on pull requests. No model runs on PRs. The nightly workflow is
manual or scheduled, uses the model secret, and uploads `.runs/` for 7 days.

## One complete case

```yaml
# cases/compact-ecr-local-fix.yaml
description: compact-ecr-local-fix
metadata: { gate: pr, stage: implement, kind: artifact }
vars:
  id: compact-ecr-local-fix
  prompt: |
    Fix the pagination defect described in BUG.md. Keep the smallest correct change, run
    the existing tests, and record it in ECR.md with the headings "Change" and
    "Verification". State that release and deployment are not applicable.
  fixture: fixtures/bug-fix
  timeout_sec: 300
  expect:
    exit: 0
    headings: { ECR.md: [Change, Verification] }
    commands:
      - run: python3 -m unittest -q
        exit: 0
    diff: { max_files: 4, allowed: [inventory.py, test_inventory.py, ECR.md] }
  judge:
    rubric: The record is proportionate to a one-component local fix.
assert:
  - type: javascript
    value: file://assertions/contract.mjs
```

The provider copies `fixtures/bug-fix` to a fresh temporary workspace, runs one OpenCode session there,
then snapshots the workspace. `contract.mjs` reads `vars.expect` and checks files, headings, commands,
diff scope, tools and budget. Four expectation groups is the normal maximum.

## Deterministic and advisory

| Lane | Owns | Can fail CI | Input |
| --- | --- | --- | --- |
| Deterministic (`vars.expect`) | Files, exit code, commands, diff scope, headings, links, tools, tokens/time | Yes | The workspace and trace |
| Judge (`vars.judge`, `npm run judge`) | Coherence, proportionality, rationale quality | No; always exits 0 | Output, changed-file list and file excerpts |

The judge never receives a summary as a substitute for files, never changes a verdict, and records
`{"status":"unavailable"}` when the judge model is missing or does not answer. It is not in `eval:pr`.
Do not put correctness, policy or authorization decisions in the judge; assert them on disk.

## Provider constraints

`providers/opencode.mjs` runs:

```sh
$OPENCODE_BIN run --standalone --archived --auto --format json \
  --session ses_eval_<id>_<run> -m $OPENCODE_MODEL -- "<prompt>"
```

- The fixture is copied to a fresh temp workspace. Both `cwd` and `PWD` point there.
- `XDG_CONFIG_HOME` is isolated and contains exactly one file: `opencode/opencode.json`, which lists the
  bundle skill sources and denies webfetch/websearch. The session suffix is unique so a rerun cannot
  resume an old session and remember an old workspace path.
- `XDG_DATA_HOME` is **not** created or copied. Provider credentials live there, and a completely fresh
  data home fails with `provider.no-route: Model unavailable`. Set `OPENCODE_DATA_HOME` to a dedicated,
  seeded data home for CI; locally the signed-in user's data home is inherited.
- A recorded run uses `--no-cache --no-write --no-share`; the record keeps version, model, tools, changed
  files, tokens, duration, cost and exit. Traces and changed-file excerpts go under `.runs/`.
- `EVAL_SKILLS_DIR` points at a built collection; without it the provider uses `plugins/` (source) or
  `evals/.bundle/` if present.
- The provider parses the `text`, `tool_use` and `step_finish` events from `--format json`. A change to
  that stream fails loudly and needs a provider update. It uses `spawnSync`, so cases run sequentially
  even when promptfoo allows more concurrency.

`promptfooconfig.control.yaml` + `control/failing.yaml` is a deliberate failing control. Run it to
confirm the wrapper exits 100; it is not part of the suite.

## Lifecycle map (10 / 13 / 20)

| Level | Count | Meaning |
| --- | --- | --- |
| PR gate | 10 | Every change: discovery, scope, small/large records, release boundary, dependency policy, artifacts |
| Release subset | 13 | The ten PR cases plus `new-application`, `artifact-workspace-cross-phase` and `production-readiness-review-scope`; a release decision should not skip these journeys |
| Review threshold | 20 | Before adding more cases, review coverage and cost. V1 is 18; the hard cap is about 60 |

The eight nightly cases add cross-phase journeys, stack-mismatch, fixture authentication, readiness and
current-versus-proposed architecture. They exist because a PR-sized fixture cannot show those outcomes.

## Records and retention

`.runs/` is git-ignored. Each run writes `record.json`, `summary.md`, `raw.json` and `traces/`. The record
is the comparable unit; raw promptfoo output is kept for debugging. CI retains `.runs/` for 7 days.
Commit a record only when a decision depends on it.

`records/legacy/` keeps three earlier records: `browser-extension/`,
`engineering-artifact-workspace/assessment.md` and `independent-scenarios/assessment.md`. They predate
this harness, used different prompts and inventories, and are **not comparable** to current runs.

## Current status

The suite runs against a working-tree checkout and a local or CI OpenCode install. The discovery case
reads the session's configured skill sources; it does not install a marketplace bundle. No installed-client
discovery run, Docker isolation run or calibrated judge has been recorded. Case prompts and fixtures are
the maintained source; a recorded pass belongs to its recorded revision.

## Recorded evidence and limits

| Limit | Consequence |
| --- | --- |
| No installed-client run | Skill discovery is exercised through configured sources, not a marketplace install |
| Copy, not a sandbox | A shell-capable agent can read or write outside the copied workspace |
| Config isolated, data home shared | Globally installed skills and credentials are visible to the session |
| No Docker isolation | Local tools, network and user config are part of the run |
| Judge uncalibrated | Advisory text is useful for review, not a measurement |
| One model | Results do not transfer to another model or client |
| Fixture-scale work | Cases show routing and record quality, not production behavior |

## Compare and simplify

Compare bundles at the same fixture, model, tools, permissions and run budget. Use small-change controls
to catch unnecessary ceremony. When a rule changes, rerun its case and the nearest journey; a shorter
skill is not evidence of better behavior. Keep a concrete reproduction in a case instead of adding a
prohibition to every skill.
