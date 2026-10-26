# Contributor instruction audit

## Outcome and scope

Updated only `AGENTS.md`, `tests/AGENTS.md` and `CLAUDE.md` in the requested input repository. This report is the sole output artifact. Application source, test source, sample data, session notes and canonical contributor/security documents remain byte-for-byte unchanged. No dependencies were installed, no Git repository/worktree was created, and no personal configuration, network service or remote action was used.

## Applied guidance and actual reads

Used the named development bundle's `skills/project-conventions/SKILL.md`, `skills/project-conventions/references/repository-instructions.md` and `skills/agents-md/SKILL.md`. Also read `skills/agents-md/SPEC.md`, `skills/agents-md/SOURCES.md`, `WORKFLOW.md`, `TASKS.md`, `skills/deliver-reliable-changes/SKILL.md`, `skills/git-contributions/SKILL.md` and `skills/writing-for-agents/SKILL.md` for scoped authoring, evidence and workspace boundaries. These reads were confined to the named development bundle. Git/worktree mechanics were unnecessary for this explicitly bounded documentation edit in an input directory without `.git`; the input directory was edited in place as requested.

Repository inventory was inspected with `ls -la` and `rg --files --hidden -g '!.git/**'`. It contains no manifest, lockfile, Makefile, CI definition, README, formatter, linter or typechecker configuration. No toolchain or attribution policy was invented. Actual repository files read:

- `AGENTS.md`
- `tests/AGENTS.md`
- `CLAUDE.md`
- `session-notes.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `app.py`
- `service.py`
- `store.py`
- `tests/test_service.py`
- `items.json`

## Findings and rationale

| Finding | Evidence | Revision |
| --- | --- | --- |
| `npm test` is stale. | No Node manifest exists; `CONTRIBUTING.md` gives the standard-library unittest command; `tests/test_service.py` contains three unittest cases. | Replace with the documented root test command and CLI help command; retain the requirement to run tests before delivery. Preserve Python 3.11+ and no dependency-install requirement. |
| Root instructions carried transient history. | The printer-label commit note does not change future contributor behavior. | Remove that history rather than promoting it to a convention. |
| Export privacy and owner isolation are durable constraints. | Existing root instructions and `SECURITY.md`; `service.py` filters list and rename operations by owner. | Keep both root constraints and link the canonical security document. |
| Tests repeated global rules. | Runtime/privacy rules already apply at the root; the test-specific synthetic-record rule is supported by `ServiceTests.setUp`. | Retain synthetic records and the prohibition on editing `items.json` for expectations; add a precise, verified file-focused command. |
| `CLAUDE.md` contains unique accepted content. | Existing compatibility file and `session-notes.md` explicitly retain the legacy CSV importer UTC requirement, despite the missing importer implementation. | Preserve a regular compatibility file, link shared guidance, retain UTC wording, and add a conditional root pointer so AGENTS-only readers can find the contract. Do not replace it with a symlink that loses the unique requirement. No unverified client import syntax or discovery behavior is asserted. |
| Session observations differ in durability. | Successful test/help observations match repository commands; DNS/certificate bypass was unrelated and removed; Poetry was merely suggested. | Promote the verified command knowledge. Exclude the DNS workaround, certificate bypass and unaccepted package-manager proposal. Keep session notes unchanged. |
| Ownership and fixture caveats already have a canonical home. | `CONTRIBUTING.md` assigns CLI/service/store responsibilities and explains that owner is a local fixture selector, not production authentication. | Link that document with a useful read trigger instead of copying its procedure or implying production identity guarantees. |

## Actual checks and results

All commands ran locally from the input repository root. `PYTHONDONTWRITEBYTECODE=1` (or `-B` for the version check) prevented cache writes. No command modified application state.

1. `python3 -B -c 'import sys; print(sys.version)'` — exit 0; Python **3.14.7**, satisfying the documented minimum. Python 3.11 itself was not separately exercised.
2. `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` — exit 0; **3 tests passed**: `test_list_scope`, `test_rename_other_denied`, `test_rename_own`. This verifies owner-scoped service behavior on synthetic in-memory records; it does not establish export privacy or importer behavior.
3. `PYTHONDONTWRITEBYTECODE=1 python3 app.py --help` — exit 0; printed `usage: app.py [-h] [--data DATA] --owner OWNER {list,rename} ...` and the `--data`, `--owner`, `list` and `rename` options. Static inspection confirms argparse handles help before `store.load`; no credential setup was required.
4. `PYTHONDONTWRITEBYTECODE=1 python3 app.py --owner alice list` — exit 0; output: `[{"id": 1, "owner": "alice", "label": "Printer"}]`. This exercised CLI → store load → service list on the local sample JSON without saving it.
5. `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_service.py' -v` — exit 0; ran after the instruction edits. Captured output:

```text
test_list_scope (test_service.ServiceTests.test_list_scope) ... ok
test_rename_other_denied (test_service.ServiceTests.test_rename_other_denied) ... ok
test_rename_own (test_service.ServiceTests.test_rename_own) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

Static review of the final instruction files also confirmed:

- `AGENTS.md` → `CONTRIBUTING.md`: exists.
- `AGENTS.md` → `SECURITY.md`: exists.
- `AGENTS.md` → `CLAUDE.md`: exists.
- `AGENTS.md` → `tests/AGENTS.md`: exists.
- `CLAUDE.md` → `AGENTS.md`: exists.
- `CLAUDE.md` → `CONTRIBUTING.md`: exists.
- `AGENTS.md`: 20 lines; under the 60-line editing target.
- `tests/AGENTS.md`: 11 lines; under the 60-line editing target.
- `CLAUDE.md`: 4 lines; under the 60-line editing target.
- Root commands agree with `CONTRIBUTING.md`; the test-specific command selects the existing test file and was executed successfully.
- Nested test guidance adds only subtree-specific data handling and a focused command; global privacy/runtime rules are inherited rather than repeated.
- `CLAUDE.md` remains a regular file, shares root command guidance by reference and retains its accepted importer requirement.
- Repository inventory before and after is identical; only the three allowed instruction files changed.

## Preservation evidence

The following SHA-256 digests were computed before the edits and compared against the final bytes; all matched:

| Unchanged file | SHA-256 before = after |
| --- | --- |
| `CONTRIBUTING.md` | `bda0f653d8f6b25a5e7c702946c07bc5f992580fdf706642ffe9dea0798eb2b7` |
| `SECURITY.md` | `48565afc28488982480df613418bf92967b90de97181a83d157cc6ca27326d60` |
| `app.py` | `e1b727b72baa09c2c690b62adefdcbc457563adea7e46121c78007f242d71487` |
| `items.json` | `d1b714eb9c33ba615529b8a2037bb91e44b16d3a0d9c14ebff03712ebd3f4f20` |
| `service.py` | `b32be120d6c9ec132e5061bb419bfa2aa87a5875c38d2edb93391e8bd165c128` |
| `session-notes.md` | `af8316e88613e6e7c4fa6b7a09c5448f04b18aa12cb69441a469036e0072e7af` |
| `store.py` | `640697d9be0ed21e42fe6c991e770270550cff4df4734612370467be568da4d0` |
| `tests/test_service.py` | `35e04db82f9d3f4d920a4dc41e2524832ec6dca8b8ab0984329826faa147821d` |

## Limits

The fixture has no export or CSV importer implementation, so those accepted requirements are preserved as policy rather than claimed as tested behavior. The three unit tests cover the service's list/rename operations; CLI help and sample listing provide narrower local entrypoint evidence. No production authentication, remote behavior, release readiness or deployment claim is made. No unresolved instruction conflict remains within the inspected scope.

## Unified diff

```diff
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,6 +1,20 @@
 # Inventory project instructions

-Use Python 3.11 or newer. Run `npm test` before delivering a change.
-Exports must never contain private email addresses.
-The last task fixed a printer-label typo in commit deadbee.
-Keep owner isolation in item operations.
+- Use Python 3.11 or newer and its standard library; no dependency installation is needed.
+- Read [CONTRIBUTING.md](CONTRIBUTING.md) for setup, code ownership and the CLI's fixture-owner limitations.
+
+## Commands
+
+Run from the repository root; run tests before delivering a change:
+
+| Task | Command |
+| --- | --- |
+| Tests | `python3 -m unittest discover -s tests -v` |
+| CLI help | `python3 app.py --help` |
+
+## Project constraints
+
+- Preserve owner isolation and exclude private email addresses from exports, as required by [SECURITY.md](SECURITY.md).
+- For legacy CSV importer data changes, follow the retained UTC contract in [CLAUDE.md](CLAUDE.md).
+- For test changes, also read [tests/AGENTS.md](tests/AGENTS.md).
+- Update affected contributor instructions when commands or accepted contracts change.
--- a/tests/AGENTS.md
+++ b/tests/AGENTS.md
@@ -1,5 +1,11 @@
-# Tests
+# Test instructions

-Use Python 3.11 or newer.
-Exports must never contain private email addresses.
-Use synthetic records created by each test; never edit items.json to establish test expectations.
+- Use synthetic records created by each test; never edit `items.json` to establish test expectations.
+
+## Focused check
+
+Run from the repository root; run tests before delivering a change:
+
+| Task | Command |
+| --- | --- |
+| Service tests | `python3 -m unittest discover -s tests -p 'test_service.py' -v` |
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -1,5 +1,4 @@
 # Contributor entrypoint

-Read AGENTS.md and CONTRIBUTING.md for project instructions and commands.
-
-The legacy CSV importer uses UTC dates; preserve that contract when editing importer data. This is a retained project requirement.
+- Read [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for shared project instructions and commands.
+- The legacy CSV importer uses UTC dates; preserve that contract when editing importer data. This is a retained project requirement.
```
