# EVAL: building `notes.py` with the sdlc skills

This records how the skill library was used for the request in `TASK.md`, what
it changed, what was produced, what actually ran, and where the guidance was
hard to apply. It is written after the work, from the session and the observed
outputs; nothing here is projected.

## 1. Skills read and what changed the approach

All sixteen requested skills were read in full:

`activity-system`, `artifact-system`, `plan`, `refine`,
`requirements-engineering`, `design`, `system-design`, `implement`, `test`,
`review`, `guide-ecr`, `guide-prd`, `guide-design-proposal`, `guide-issue`,
`guide-pr`, `guide-readme`.

Supporting references read because the skills sent me there: the activity
catalog, project fit, the ECR contract, the design-proposal contract, the
software-types overview and `library-cli` file, the artifact quality bar, and
the design option-set method.

| Skill | Material effect on the work |
| --- | --- |
| `activity-system` + catalog | Routed the request as one `develop` engagement carrying plan → refine → design → implement → test → review, with an explicit stopping point. It is why there is no issue, PRD, PR, ADR or ticket: the catalog's artifact column is conditional and the skill says not to create views to fill fields. |
| `artifact-system` + quality bar | Fixed the artifact set and the evidence rules: seven ECR sections, status per claim, past-tense evidence, one authority per concern, relative links verified on disk. It is why `docs/ecr.md` §6 only summarizes and links `docs/verification.md` instead of copying it. |
| `plan` | Forced an explicit proceed/investigate/defer decision with feasibility and the smallest useful slice before code. Produced the non-goals list that kept edit, tags and sync out of the build. |
| `refine` + `requirements-engineering` | The largest behavioral change. Rather than implementing the happy path, I enumerated denial and failure outcomes first: unknown id, invalid id, empty note text, empty search term, corrupt store, unreadable path, missing parent. That produced the exit-code contract (`0/1/2`), the "refuse a corrupt file instead of rewriting it" rule, and negative test cases. It also forced a readiness verdict (ready for design, then implementation). |
| `design` + `system-design` + option-set | Turned "pick JSON" into three materially different persistence options (single document / append-only journal / file per note) and a recorded decision with a revisit trigger. It also produced the seam decisions (record shape, error mapping, config precedence, id contract) and the explicit "C4/sequence not applicable" disposition instead of fabricated diagrams. |
| `implement` | Least usable as written; see §5. Its useful residue was test-alongside-code and a full suite at the end. The commit step was not possible (no repository, pruning side effects out of scope). |
| `test` | Its evidence-to-claim table changed the test mix. I added 20 subprocess tests against the real entry point because "implemented" and "behavior verified" need different evidence, and an in-process call would not establish stdout, stderr or exit codes. It is also why the verification record states A18 (crash injection) as not exercised rather than implying atomicity was proven. |
| `review` | Supplied the findings format (severity, location, impact, fix), the default of assessment over edits, and the instruction to pin a revision. Two low/medium findings were repaired because implementation authority had been granted by the task; the report distinguishes the repaired ones from accepted scope decisions. |
| `guide-ecr` | Structure and honesty rules: current state first, no "see issue", no future-tense verification, compact but complete. |
| `guide-design-proposal` | The option/tradeoff/seam/decision-block shape, and the anti-pattern check that stopped me from presenting three cosmetic variants. |
| `guide-readme` | The README's reader-first order, quickstart that runs from a fresh copy, exact commands with expected output, explicit limits and a docs map. |
| `guide-prd`, `guide-issue`, `guide-pr` | Read and judged not applicable to this request: no product-priority decision, no tracker, no PR. Their "do not create a second authority" rule is why none was fabricated. |
| `system-design` | Applied only through its small-change path: no invented C4 views, but explicit durable statements about state ownership, failure and recovery. |

Net effect: the skills changed the *shape and evidence* of the work far more
than the code. Without them I would likely have written a single-file script,
tested only the happy path, and produced a README without exit-code or failure
semantics.

## 2. Artifacts produced

All paths are relative to
`/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/new-app`.

| Artifact | Path | Type / role |
| --- | --- | --- |
| CLI entry point | `notes.py` | work product; argument parsing, normalisation, output, exit codes |
| Storage module | `notes_store.py` | work product; JSON format, validation, atomic writes, path resolution |
| Search module | `notes_search.py` | work product; folding and substring matching |
| Store tests | `tests/test_store.py` | verification; 25 tests |
| Search tests | `tests/test_search.py` | verification; 11 tests |
| CLI tests | `tests/test_cli.py` | verification; 20 end-to-end subprocess tests |
| Test package marker | `tests/__init__.py` | enables `python3 -m unittest` discovery |
| README | `README.md` | entry-point artifact (repository README contract/guide) |
| ECR | `docs/ecr.md` | change record: seven contracted sections, requirements, acceptance, decisions |
| Design proposal | `docs/design.md` | design record: question, types, three options, tradeoffs, seam, decision block |
| Verification record | `docs/verification.md` | evidence: environment, hashes, commands, results, review findings, gaps |
| Evaluation | `EVAL.md` | this report |

No ECR workspace, issue, PR, PRD, ADR or roadmap exists, and none was invented:
the request names the docs it wants and the skills make those views conditional.

## 3. Commands run and actual results

All commands were run in the working directory above.

| Command | Actual result |
| --- | --- |
| `python3 -m unittest -v` | `Ran 56 tests in 2.044s` — `OK`, exit 0 (five runs ranged 1.978–2.044 s, same 56/OK) |
| `python3 -m unittest tests.test_store` | `Ran 25 tests in 0.013s` — OK |
| `python3 -m unittest tests.test_search` | `Ran 11 tests in 0.000s` — OK |
| `python3 -m unittest tests.test_cli` | `Ran 20 tests in 2.177s` — OK |
| `python3 -m py_compile notes.py notes_store.py notes_search.py tests/test_store.py tests/test_search.py tests/test_cli.py` | exit 0, no output |
| `grep -nE '^(import\|from) ' notes.py notes_store.py notes_search.py` | only `argparse`, `sys`, `json`, `os`, `tempfile`, `datetime`, `pathlib` and the local modules — no third-party import |
| `grep -n 'import notes' notes.py notes_store.py notes_search.py` | only `notes.py` imports the other two; the store and search modules do not import each other or the CLI |
| `python3 notes.py add/list/search/delete …` (14-command session) | outputs and exit codes matched every case the session exercised; full transcript in `docs/verification.md` |
| README quickstart verbatim (2 adds, list, search, delete 1, list) | `1`, `2`, the two-line list, `1\tbuy milk`, `deleted 1`, `2\tcall Ana about the roof` |
| `env -u NOTES_DATA HOME=<scratch>/home python3 notes.py add "default-location"` | `1`, exit 0; `$HOME/.notes.json` created with mode `0600` |
| `cd <scratch>/work && NOTES_DATA=relative/notes.json python3 <tree>/notes.py add "relative-path"` | `1`, exit 0; `relative/notes.json` created with its parent directory |
| `NOTES_DATA=<scratch>/broken.json python3 notes.py list` on `{"notes": [` | exit 1, `notes.py: error: … invalid JSON: Expecting value: line 1 column 12 (char 11)`, no traceback, file unchanged |
| `shasum -a 256 notes.py notes_store.py notes_search.py tests/test_*.py` | six hashes recorded in `docs/verification.md` |
| `uname -sm` | `Darwin arm64` |
| `python3 --version` | `Python 3.14.7` |
| `command -v python` | not found (hence `python3` throughout) |

After the final suite run, generated `__pycache__/` directories were removed and
the scratch data files were deleted. No command was run against the skill
repository; it was only read.

## 4. Key decisions and assumptions

1. **Persistence: one JSON document with read-modify-write and atomic replace.**
   Chosen over an append-only JSON Lines journal and over one file per note.
   Journal and per-note layouts add a second consistency point (replay order, id
   allocator) for capabilities the request does not ask for. The decision and
   its revisit trigger are in `docs/design.md`.
2. **Ids are monotonic integers and are never reused.** `delete <id>` needs a
   short handle; reuse would make a stale id delete a different note. `next_id`
   is persisted and repaired upward if a hand-edited file has a stale value.
3. **Exit codes are part of the contract:** `0` success (including empty
   results), `1` runtime/data error, `2` usage error. Usage errors are resolved
   before opening the store, so a broken file cannot mask a syntax mistake.
4. **A corrupt store is refused, never repaired or overwritten.** Data loss is
   the expensive failure; a diagnostic plus an untouched file is safer than
   best-effort recovery in a tool with no undo.
5. **`created_at` and `version` are stored but not displayed.** Both preserve
   information that cannot be reconstructed later; neither changes the output
   contract.
6. **Notes are single-line.** Input whitespace collapses to single spaces. This
   keeps `<id>\t<text>` unambiguous and search simple. Recorded as assumption A1
   because it does alter input text.
7. **Default path is `~/.notes.json`, with `NOTES_DATA` taking precedence.**
   Keeps notes out of the project tree; a relative override stays relative to
   the working directory and missing parents are created on first write.
8. **Three modules, no framework.** The store knows nothing about argv; search
   knows nothing about files; the CLI owns streams, formatting and statuses.
9. **No lock, no commit, no packaging.** Concurrency, VCS history and
   distribution were outside the requested stopping point. Each is recorded as
   a limitation rather than half-implemented.
10. **Revision evidence is SHA-256, not a commit.** The directory is not a Git
    repository, so the quality bar's link form cannot be satisfied; file hashes
    are the strongest available identifier.

Assumptions that could have gone the other way and are stated in the ECR:
single-line notes, no locking, and `~/.notes.json` as the default. If any is
wrong, the affected behavior is isolated to normalisation, the write path, or
path resolution respectively.

## 5. Gaps, contradictions and friction in the skills and guides

Ordered by how much they affected the work.

1. **`implement` is not usable as an activity in this environment.**
   `plugins/sdlc/skills/implement/SKILL.md` is 15 lines: "Use /tdd",
   "Run typechecking regularly", "use /code-review", "Commit your work", and it
   sets `disable-model-invocation: true`. The activity catalog nonetheless lists
   `implement` as a core activity with artifacts and evidence. In an unattended
   run with no slash commands, no type checker and no Git repository, almost
   none of it applies. I followed the catalog's outcome and the `test` skill's
   evidence rules instead. A reader who takes the skill literally would try to
   commit in a non-repository.
2. **"Commit your work" vs. a non-Git workspace.** `project-fit` says explicit
   implementation includes commits; the quality bar requires linked revisions.
   Neither says what to do when the directory is not versioned and creating a
   repository would be an unrequested side effect. I used SHA-256 hashes and
   labelled the tree "not published"; that convention is not sanctioned
   anywhere.
3. **Invocation metadata conflicts with the requested engagement.** `implement`,
   `test` and `review` are marked `disable-model-invocation: true` (and `test`
   and `review` are user-invocable only), yet the task instructs an agent to run
   test and review as part of the process. The skills are readable and
   applicable, but the frontmatter says an agent should not have selected them.
4. **Artifact home resolution has no precedence rule for an explicit TASK path.**
   `plan` and `refine` say to resolve the home and, if the repository map is
   missing, say so rather than choosing an arbitrary path. Here there is no map,
   no `setup` activity, and the task explicitly dictates `docs/ecr.md` etc. I
   followed the explicit request and recorded it, but the skills do not state
   that an explicit user path outranks a missing map.
5. **The three-option requirement catches small greenfield CLI work.** The
   design-proposal contract triggers an option set for "a greenfield component"
   and "a change that touches more than one software type", while the
   proportionality text says a small local change needs only a rationale. A
   CLI of a few hundred lines is both. I produced three real options (it
   improved the record), but a "small greenfield" threshold or example is
   missing.
6. **Linked artifacts for rejected options are required but disproportionate.**
   The contract asks for one or more linked artifacts per option at comparable
   fidelity. For a CLI, a full command surface and usage examples for each of
   three storage layouts would be padding. I produced the chosen option's
   surface and stated why the rejected options' artifacts were not produced;
   that is a deliberate partial nonconformance, not an oversight.
7. **`refine` points at the wrong guides for its actual output.** It says to read
   `guide-prd` and `guide-issue` for the artifact it produces, but its own text
   says the output is the ECR requirements section. The craft guidance for that
   section lives in the ECR contract, not in either guide. I used the contract
   and the requirements-engineering skill.
8. **The ECR's seven sections overlap for a small change.** "Overview and
   lifecycle" repeats status that also appears in §3 and §6, and the
   phase-completion table adds a third status view. Kept compact, it still reads
   as ceremony for a one-command change. The compact bug example in the ECR
   contract helps, but there is no equally compact design-proposal example.
9. **Guide duplication.** `guide-ecr`, `guide-design-proposal` and the quality
   bar each carry a review checklist with overlapping items. Reconciling three
   checklists for a small project cost more than the checks themselves.
10. **Software-type naming inconsistency.** `software-types.md` lists
    `python-automation-engineering` as the backing package for library/CLI,
    while `software-types/library-cli.md` names `backend-python-development` for
    "Python automation or CLI". Neither package is installed here, so no
    stack-specific Python guidance was available; the skill's fallback ("retain
    the standard using project evidence") was the only workable path.
11. **Documentation of a "no license" state is missing.** `guide-readme` asks
    for a license link unless it does not apply, but does not model the common
    local-only case. I wrote an explicit "no license declared" line rather than
    inventing one.
12. **`docs/verification.md` is not a catalog type.** The `test` skill says to
    record verification in the change record or return a structured unpersisted
    record. The task requires a separate file. I kept it as the evidence
    authority and made ECR §6 a summary plus link, which satisfies the
    single-authority rule but is a mapping the skills do not describe.
13. **Environment/task mismatch.** `TASK.md` writes `python notes.py`; this
    machine has no `python` on `PATH`. No skill covers command-line portability
    or interpreter naming. The README documents `python3` explicitly.
14. **Assurance is self-review.** The review skill warns that missing evidence
    and defects differ, but there is no independence mechanism; the same agent
    wrote and reviewed the code. I stated this limit in `docs/verification.md`
    rather than presenting the review as independent.

## 6. Self-assessment against TASK.md

| Requirement | Status | Evidence / gap |
| --- | --- | --- |
| `python notes.py add "text"` stores a note and prints its id | Done | Works as `python3 notes.py add "text"` → id on stdout, exit 0. `python` is not on `PATH` on this machine; README documents the substitution. |
| `list` lists notes | Done | `<id>\t<text>`, ascending id; 2 CLI tests plus transcript |
| `search "term"` finds notes containing the term | Done | Case/whitespace-insensitive substring; 4 CLI tests, 11 unit tests |
| `delete <id>` deletes a note | Done | `deleted <id>`; unknown id exit 1 without file change; invalid id exit 2 |
| Notes persist in a local JSON file | Done | One JSON document, atomic replacement, validated on read |
| `NOTES_DATA` overrides the path | Done | 5 path tests plus default-path and relative-path CLI checks |
| No third-party dependencies | Done | Import inspection; stdlib only |
| Tests with the standard library | Done | 56 `unittest` tests, `python3 -m unittest -v` → OK |
| README with exact commands | Done | `README.md`, quickstart run verbatim and matched |
| Separation of CLI, storage and search | Done | Three modules; only the CLI imports the other two; tests target each boundary |
| `docs/ecr.md` | Done | Seven contracted sections with requirements, acceptance and decisions |
| `docs/design.md` | Done | Three options, tradeoffs, seam, decision block, revisit trigger |
| `docs/verification.md` | Done | Environment, hashes, commands, observed results, review findings, gaps |
| `EVAL.md` | Done | This file |
| Start from planning and requirements | Done, with a caveat | The plan decision, scope, non-goals, requirement and acceptance reasoning came before the code; the written documents were authored after the code worked (see the ordering note below). |
| Make consequential design choices | Done | Persistence, identity, error/exit contract, text and path rules recorded in `docs/design.md` |
| Implement, test, review | Done, with limits | Implemented and tested; review was a self-review and two findings were fixed. No independent reviewer. |
| Do not modify the skill repository | Done | Read-only access; no writes or commands against it |
| Commit the work | **Not done** | The directory is not a Git repository; initializing one and committing would be an unrequested side effect. Revision is identified by SHA-256 instead. |
| Crash-safety fully proven | **Not done** | Atomic replace is implemented and failure paths are tested, but no process kill between `fsync` and `replace` was injected (acceptance A18 marked not exercised). |
| Cross-platform support claim | **Not done** | Only macOS/CPython 3.14.7 was exercised; README states Linux/Windows are unverified. |
| Concurrency safety | **Not done, by design** | Documented limitation; last writer wins. |
| Independent verification / CI | **Not done** | No CI, linter or second reviewer available; `py_compile` and the suite are the whole automated gate. |

Overall: the functional request is complete and locally verified, and the
required documents exist and agree with each other on commands, format, exit
codes and limits. The honest shortfalls are the missing commit (no repository),
the unexercised crash-injection case, and the fact that verification and review
were performed by the same agent that wrote the code.

**Ordering caveat.** The design choices, requirement branches and test cases were
settled in reasoning before the code was written, but `docs/ecr.md`,
`docs/design.md`, `docs/verification.md` and `README.md` were authored after the
application worked, from the session and the observed output. They record
decisions that preceded implementation; they were not a pre-implementation gate.
The ECR §7 history therefore lists one date for all decisions, which reflects
when they were recorded, not six separate moments.
