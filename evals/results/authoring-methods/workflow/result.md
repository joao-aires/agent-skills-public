# Inventory archive and restore: proposed design and implementation plan

Status: design and plan complete; feature implementation and feature verification have not run. No source, fixture, dependency, infrastructure or live-service changes were made. Only this requested report was written.

Repository: `/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/skills-authoring-validation-ehk8boru/workflow/input`.

## Basis and existing behavior

The requested audience is an inventory owner using the local CLI. Success means the owner can hide an item from the ordinary list, find it in an explicit archived view, and restore it without losing its identity or other stored data. Ownership isolation remains mandatory.

I read the supplied `design` and `plan` entry points, their `TASKS.md` and `WORKFLOW.md` framing, and relevant `project-conventions`, `deliver-reliable-changes`, `system-design` and `system-mapping` guidance. Their application here is a bounded service/state design and dependency-ordered plan, not implementation. The named bundle inventory did not provide a separate service-contract or security/privacy design specialist; the authority, failure and sensitive-data reasoning is retained below. No unrelated discovery or optional installation was needed.

Repository instructions require Python 3.11+ and the standard library, service-owned item operations, owner isolation, and exports without private email addresses (`AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`). `--owner` is explicitly a local fixture selector, not production authentication; this plan preserves it.

Current trace, with repository-relative locations:

- `app.py:7–15` parses the selected JSON path, required owner, and `list` or `rename`. It loads records with `store.load` at line 16.
- Listing calls `service.list_items` and prints JSON (`app.py:17–18`). `service.py:1–2` filters only by owner and returns shallow copies; there is no archive filter.
- Rename selects an item by **both ID and owner** before mutation, raises `LookupError("Item unavailable")` for a missing or foreign item, and returns a copy (`service.py:4–9`). The CLI saves before printing success (`app.py:19–22`).
- `store.py:4–8` loads and rewrites a JSON array directly. It provides no transaction, atomic replacement or concurrent-writer protection.
- `items.json` contains two synthetic legacy records without archive state. `tests/test_service.py:8–17` covers owner-scoped list, own rename and denied foreign rename, but no CLI or persistence journey.

## Proposed design

Retain `app.py → service.py → store.py`. A boolean `archived` field on each record is sufficient; missing means `false`. Archive sets it to `true`, restore sets it to `false`. Preserve ID, owner, label, record order and all unrelated stored fields. No bulk rewrite or separate migration is necessary: old records become active through the read default, and a mutation writes the selected item's explicit state.

A boolean fits two states and needs no clock or timestamp migration. Moving records to a separate archive file would require coordinating two writes and complicate ownership and recovery. A timestamp or database is unnecessary for this request.

Proposed CLI contract:

| Command | Observable result |
| --- | --- |
| `python3 app.py --owner alice list` | JSON array of Alice's active items only. |
| `python3 app.py --owner alice list --archived` | JSON array of Alice's archived items only; this is not an include-everything flag. |
| `python3 app.py --owner alice archive 1` | Persist item 1 as archived and print its public JSON representation. |
| `python3 app.py --owner alice restore 1` | Persist item 1 as active and print its public JSON representation. |

Use the existing global `--data` selection for every command. Empty views return `[]`. Add integer ID arguments for archive and restore, and an optional archived selector on the list subparser. Existing rename syntax and owner permissions remain valid. Rename remains allowed for an owner's archived item: archiving controls list visibility, and introducing a rename prohibition would change existing rules.

Proposed service additions are `archive_item(records, owner, item_id)` and `restore_item(records, owner, item_id)`; extend `list_items` with a keyword archive-view option defaulting to active. These names and signatures are proposals, not existing functions. Keep selection, authorization, state decisions and mutations in `service.py`. Both new operations must locate the record by ID **and owner**, using the existing unavailable error before changing anything. Restoring must search archived records too; the default-list filter must not become a mutation lookup restriction.

Repeated archive of an archived owned item and restore of an active owned item succeed with the requested state. This idempotent behavior is a proposed reversible contract: it supports safe same-operation retry without duplicate records. Missing and foreign IDs produce the same unavailable error and leave every record unchanged. CLI failures must exit nonzero, emit no success JSON, and skip saving after service rejection; follow the existing failure convention rather than redesigning all CLI diagnostics.

After a successful service mutation, the CLI calls the existing save operation and prints success only after save returns. A load/save error remains a failed command. On a lost success response, the caller may reload the file or repeat the same desired-state command. Opposite commands intentionally request different final states.

### Authority, data and operating boundaries

`--archived` changes visibility, never authority: both list modes must filter by owner, and archive/restore enforce the same owner-and-ID rule as rename. No authentication rewrite is proposed.

The current service returns every stored key through `dict(item)`. The fixture contains no email fields, so it does not demonstrate a current private-email leak; however, blindly serializing richer records would violate the repository's export rule. Use a small explicit public-output projection at the CLI's JSON boundary for list and mutation responses, including existing rename, with the public fields `id`, `owner`, `label` and normalized boolean `archived`. Never serialize arbitrary private-email fields. Preserve any such fields internally and on disk; output sanitization must not delete stored data. This directly carries the existing security rule into the changed output paths, without adding an export feature.

The local JSON store remains a single-writer fixture mechanism. Its direct rewrite can fail partway, and simultaneous processes can overwrite each other's changes. This plan neither claims transactional durability nor adds locking or a new persistence platform. If concurrent writers or crash-safe durability become requirements, revisit that boundary before relying on it. A save failure can leave an uncertain file, so inspect/recover the selected file before further mutation; a nonzero exit alone does not prove that no bytes changed.

Compatibility is additive for stored records and the existing service call shape, except for the intentional default-list filtering and the proposed public JSON `archived` field. Older application code may preserve unknown JSON keys but ignores archive visibility, so old and new versions must not be used interchangeably on an archived inventory. Prefer rolling forward. Before using the implemented candidate with meaningful data, retain a known-good copy; restoring it discards later changes and must be an intentional recovery choice. No archive-state cleanup is needed.

## Dependency-ordered implementation plan

All steps below are future work, ready to begin under this proposed contract. They add no dependencies, infrastructure or live services.

1. **Deliver archive through the real CLI and active-list result.** In `service.py`, add backward-compatible active filtering and the owner-checked idempotent archive operation. In `app.py`, replace the rename-only catch-all dispatch with explicit handling, add `archive ID`, and save before success output. Add the public-output projection to the shared JSON boundary. Extend existing service tests and add a proposed CLI test module using standard-library subprocesses and disposable JSON files. Evidence before moving on: an owned legacy item can be archived, the raw file retains that item with `archived: true`, and a fresh default-list process omits it. Foreign and nonexistent archive attempts fail with unchanged fixture bytes; private-email fixture fields stay stored but never appear in output.
2. **Make archived items discoverable and reversible.** Add `list --archived` and the owner-checked restore operation, wiring both through the same service/save/output boundaries. Evidence: a fresh archived-list process contains only the owner's archived item; restore persists `false`, removes it from the archived view and returns it to the active view. A second archive or restore leaves the requested state intact. Foreign/missing restore attempts cannot change data. Check no-match views, mixed owners, active/archived/legacy records, and rename of an owned archived record.
3. **Close compatibility, failure and documentation coverage.** Keep all original rename/list ownership regression tests. Verify copied service results do not allow a caller to mutate stored records accidentally. Exercise the selected `--data` file, parser integer errors, required owner, command help, load failures and a controlled save failure without claiming atomicity. Compare persisted records after successful subprocesses, and fixture bytes after denials. Document commands, active-default/missing-field semantics, idempotent behavior and single-writer limits in the existing `CONTRIBUTING.md`. Run the documented full unit suite plus top-level and affected subcommand help. Perform the complete archive → archived view → restore → active view journey in an isolated temporary file, with another owner's item and a synthetic private-email field. Completion requires the independent disk/output assertions above, not just success text or a passing parser check.

No feature acceptance check is currently claimed to pass: the implementation does not exist. There is no unresolved requirement that blocks returning this proposal. The CLI spelling, same-state success behavior, normalized public output and archived-item rename behavior are explicit proposed choices that can be revised without an architecture ceremony.

## Separate help-description correction

A separately requested correction to `app.py:7`'s current text, `Manage inventory items`, is a bounded copy edit once the intended replacement is known. It changes help wording, not parsing, service behavior, archive state, ownership or persistence. Edit that string and inspect `python3 app.py --help` for the requested wording and intact usage; no data migration, service redesign, new test framework or mandatory design/plan approval gate is warranted. The replacement wording was not supplied here, so this report does not invent or apply it. Updating command help to document archive/restore belongs to the feature plan above and is distinct from that separate correction.

## Actual read and check evidence

All reads were restricted to the repository and named development bundle. Commands below ran from the repository root, used Python's `-B` option to avoid writing bytecode, and had exit code 0. No mutation command was run against `items.json`.

| Actual check | Observed result and limit |
| --- | --- |
| `python3 -B --version` | `Python 3.14.7`; meets the documented 3.11+ minimum. |
| `python3 -B -m unittest discover -s tests -v` | 3 tests passed: `test_list_scope`, `test_rename_other_denied`, `test_rename_own`. This verifies existing service behavior only. |
| `python3 -B app.py --help` | Description `Manage inventory items`; usage advertises `{list,rename}`, `--data`, required `--owner`. No archive/restore command or archived view exists. |
| `python3 -B app.py --owner alice list` | `[{"id": 1, "owner": "alice", "label": "Printer"}]`. Read-only fixture list. |
| In-memory probe of current `service.py` | With Alice IDs 1 archived and 2 legacy, and Bob ID 3 archived, current list returns Alice IDs `[1, 2]`. Foreign ID 3 and missing ID 999 rename both raise `Item unavailable` and leave records unchanged. `hasattr(service, "archive_item")` and `hasattr(service, "restore_item")` are both false. No disk writes. |

Reads: enumerated repository and bundle files with `rg --files`; read repository instructions, all three source files, the test module and fixture with line numbers; read the skill/guidance files named above using `cat`/`sed`. One batched output truncated the end of `project-conventions`; its remaining section was then read separately before applying it. `system-mapping`'s optional deeper mapping guide was unnecessary for this three-module trace. Discovery stopped at the available scope; no external specialist, website, account or live system was inspected.

Content fingerprints captured after the read-only checks (SHA-256):

```text
bfb0f20a49a636a43026edbb4396e06fc12e4143acddcf7e77a60d9ffb2cada2 AGENTS.md
bda0f653d8f6b25a5e7c702946c07bc5f992580fdf706642ffe9dea0798eb2b7 CONTRIBUTING.md
48565afc28488982480df613418bf92967b90de97181a83d157cc6ca27326d60 SECURITY.md
e1b727b72baa09c2c690b62adefdcbc457563adea7e46121c78007f242d71487 app.py
b32be120d6c9ec132e5061bb419bfa2aa87a5875c38d2edb93391e8bd165c128 service.py
640697d9be0ed21e42fe6c991e770270550cff4df4734612370467be568da4d0 store.py
35e04db82f9d3f4d920a4dc41e2524832ec6dca8b8ab0984329826faa147821d tests/test_service.py
d1b714eb9c33ba615529b8a2037bb91e44b16d3a0d9c14ebff03712ebd3f4f20 items.json
```

These fingerprints identify the inspected contents; they are not a before/after comparison or proof of implemented archive behavior.
