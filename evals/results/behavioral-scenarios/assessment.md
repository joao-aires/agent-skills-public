# Behavioral scenario results

Four end-to-end application scenarios were run against the `sdlc` skills on 2026-11-15. Each scenario used a separate disposable fixture and an independent agent.

- Skills revision: `0d75e0b`
- Scenario specification: `458e0e7` (`evals/behavioral-scenarios.json`)
- Prompting: each agent was given the task and a list of relevant skills to read. This measures **application and usability**, not discovery or routing.
- Grading: the author inspected the artifacts, reran the tests and compared the result with the scenario expectations. The agents' `EVAL.md` reports are retained verbatim.

## Scenario results

| Scenario | Delivered result | Tests | Artifacts | Outcome |
| --- | --- | ---: | --- | --- |
| [New application](new-app/EVAL.md) | Modular notes CLI with add/list/search/delete, JSON persistence, validation and exit codes | 56/56 pass | README, ECR, design, verification, 3 modules, 3 test files | Complete |
| [Existing feature](existing-feature/EVAL.md) | Tags and `list --tag` filtering added to the task CLI; legacy JSON and existing behavior preserved | 22/22 pass | README, ECR, design, verification, updated tests | Complete |
| [Bug fix](bug-fix/EVAL.md) | Pagination off-by-one fixed with a one-expression change; regression coverage strengthened | 9/9 pass | ECR, verification, updated tests | Complete |
| [Idea to implementation](ideation/EVAL.md) | Habit tracker CLI with explicit grace-streak semantics, storage, validation and tests | 33/33 pass | Product, ECR, design, verification, README, tests | Complete |

All tests were rerun by the evaluator. No agent modified the skill repository.

## Expectation match

| Scenario | Expectations met | Partial | Failed |
| --- | ---: | ---: | ---: |
| New application | 5/5 | 0 | 0 |
| Existing feature | 5/5 | 0 | 0 |
| Bug fix | 5/5 | 0 | 0 |
| Idea to implementation | 5/5 | 0 | 0 |

“Met” means the delivered behavior, artifacts and evidence satisfied the scenario expectation. It does not mean the application is production-ready, cross-platform or independently reviewed.

### New application

- Working CLI and persistence: met.
- Standard-library tests: met, including 20 subprocess tests.
- ECR with requirements, design, implementation and verification: met.
- README with exact commands and limits: met.
- No invented implementation or deployment evidence: met; the report explicitly marks crash injection, cross-platform and concurrency as untested.

### Existing feature

- Tags and filtering for pending/all tasks: met.
- Existing behavior and legacy JSON preserved: met.
- New and preserved tests: met; the original three tests remained unchanged.
- ECR and design describe the actual change: met.
- No unrelated refactor: met; the change stayed within the task CLI.

### Bug fix

- Reproduction before repair: met; baseline 3 failures, strengthened suite 5 failures before green.
- Minimal fix and preserved contract: met; one expression, signatures and validation untouched.
- Regression coverage: met; tests cover first/middle/last page, size one, beyond-last and full reconstruction.
- ECR separates reproduction, cause, repair and verification: met.
- No unrelated refactor or release claim: met.

### Idea to implementation

- Bounded product outcome and acceptance: met; non-goals and deferred ideas are explicit.
- Streak and missed-day behavior: met; grace-before-midnight, at-risk and reset rules are explicit in help, README, design and tests.
- Useful slice, not a platform: met with a caveat; `remove`, file overrides, validation and atomic writes enlarged the slice but stayed within a personal CLI.
- Product, ECR, design and verification agree: met.
- Open ideas deferred: met; sync, reminders, packaging and UI are explicitly out.

## Skill usage observations

### What materially changed the work

| Skill or guide | Observed effect |
| --- | --- |
| `requirements-engineering` | Produced denial/failure cases, exit-code contracts and acceptance before code in three scenarios. |
| `design` + `guide-design-proposal` | Forced real persistence/streak options, tradeoffs and seam decisions instead of a single implementation choice. |
| `test` | Changed the evidence mix: subprocess CLI tests, red/green reproduction, explicit untested boundaries. |
| `review` | Produced scoped findings and self-review limits rather than an approval claim. |
| `guide-ecr` | Kept the ECR current-state-first, claim-specific and evidence-based. |
| `guide-readme` | Produced reader-first quickstarts with exact commands and limits. |
| `artifact-system` | Resolved local `docs/` homes, enforced one authority and prevented invented issues/PRs. |
| `fix` + `diagnosing-bugs` | Kept the bug fix at the smallest correct seam and required reproduction. |
| `guide-design-spec` | Correctly judged not applicable to a CLI, while its state-completeness discipline informed the streak states. |

### What was read but not applied

`guide-issue` and `guide-pr` were read in three scenarios but no issue or PR was created: the fixtures had no tracker, VCS remote or publication authority. The agents explicitly recorded this rather than fabricating views.

`guide-prd` was used in the ideation scenario; in the new-application scenario it was read and judged not applicable because the task already supplied the product outcome.

## Cross-cutting friction

| Finding | Severity | Evidence | Recommendation |
| --- | --- | --- | --- |
| `implement` is not usable as written in an unattended, non-git, no-slash-command environment | High | Three reports call it the least usable skill; it assumes `/tdd`, typechecking, `/code-review` and a commit. | Add a local implementation guidance reference or a `develop` fallback that preserves its intent without assuming a client command surface. Do not rewrite the upstream bytes. |
| VCS-less fixtures lack a sanctioned revision/evidence form | Medium | Agents used SHA-256 and “local-only”; the quality bar only describes commit links or local-only paths. | Document a local-only revision form for non-versioned fixtures: content hash, tree path, environment and “not published”. |
| `test` and `review` are `disable-model-invocation: true` | Medium | Agents could read them only because the task explicitly instructed it; a real autonomous run could not select them. | Decide whether the local policy should allow model invocation for these activities, or state the explicit-invocation requirement in the scenario prompt. |
| ECR and design ceremony are heavy for small greenfield work | Medium | New-app and ideation reports call the seven-section ECR and three-option design more ceremony than the risk. | Add a “small greenfield” threshold and a compact design-proposal example, or allow a short decision with one linked artifact for low-risk CLI work. |
| `refine` points at the wrong guides | Medium | It links `guide-prd`/`guide-issue`, but its output is the ECR requirements section. | Point `refine` at the ECR contract and `requirements-engineering`; use `guide-issue` only when an issue is actually produced. |
| Guide review checklists overlap | Low | `guide-ecr`, `guide-design-proposal` and the quality bar each carry overlapping review items. | Keep one review checklist per artifact and link the quality bar for shared properties. |
| Software-type backing-package names disagree | Low | `software-types.md` names `python-automation-engineering` for library/CLI; `library-cli.md` names `backend-python-development`. | Make the type files the source of truth and correct the summary. |
| A separate `docs/verification.md` is not a catalog type | Low | The new-app task required it; the skills describe verification inside the ECR. | Either add a verification-record artifact type or state that a separate evidence file is an optional home for ECR §6. |
| README license guidance assumes a license exists | Low | `guide-readme` does not model the local-only “no license declared” case. | Add a short no-license example. |
| `python` vs `python3` portability | Low | One fixture required `python3`; no skill covers interpreter naming. | Keep exact commands in the README; this is a project convention, not a skill defect. |
| No independent review or CI | Known limit | All runs were self-review; no CI or second actor. | Retain the limitation in every result; do not present self-review as independent assurance. |

## Positive findings

- Agents did not fabricate issues, PRs, ADRs, C4 views or deployment evidence when the fixture lacked the home or authority.
- The artifact/guide pairing was discoverable: agents found the ECR, design and README guides and applied their structure.
- The ECR and quality bar prevented “tests pass” from becoming a release or production claim.
- The design guidance changed real decisions: storage layout, identity, exit codes, streak semantics and failure behavior.
- The test guidance produced stronger evidence than a happy-path unit suite: subprocess CLI tests, red/green reproduction, denial paths and explicit untested boundaries.

## Limitations

- One model, one run per scenario. This is not a statistical or independent-actor study.
- The prompts named the relevant skills. The results show application and usability, not discovery, routing or whether an agent would find the right guide unaided.
- The fixtures are local, non-git, single-machine and Python-standard-library only.
- No provider, browser, native, deployment or production capability was exercised.
- The evaluator reran the tests and inspected the artifacts, but did not perform a blind second review.
- The reports are retained in the scenario directories; their code and docs are the evidence, not the prose alone.

## Recommended sequence

1. Fix `refine`'s guide links and the software-type backing-package summary.
2. Add a local-only revision convention to the quality bar.
3. Decide the model-invocation policy for `test` and `review`.
4. Add a small-greenfield proportionality threshold and a compact design-proposal example.
5. Add a local implementation fallback that does not depend on slash commands or a git repository.
6. Re-run this battery after those changes with the same fixtures and a second model or independent reviewer.

## Follow-up fixes after this record

Applied after the evaluation, without changing the recorded results:

- Corrected `refine` to point at the ECR contract and `requirements-engineering`, with `guide-issue` only when an issue is actually produced.
- Corrected the library/CLI backing-package summary to `backend-python-development` for Python automation.
- Added a non-versioned local revision form to the quality bar.
- Added a small-greenfield proportionality rule and a compact design-proposal example.
- Removed the separate verification-record requirement; ECR §6 or existing test/CI evidence is the authority. The fixture prompts that required `docs/verification.md` were evaluation artifacts, not skill requirements.
- Added an explicit no-license state to the README guide.
- Added a local implementation flow for environments without slash commands, a typechecker or a Git commit.
- Replaced the upstream `implement` entry point with a local SDLC activity; the upstream body and license remain a reference.
- Renamed `review` to `change-review` (later retired into the review composition); `test` is model-invocable.
- Added compact ECR mode and quick-fix/self-fix rules.
- Added review ownership to the quality bar and assurance.

Open: the model-invocation policy for `test` and `review` remains an explicit decision. The evaluation used them because the task explicitly named them; a real autonomous run may not be able to select them.
