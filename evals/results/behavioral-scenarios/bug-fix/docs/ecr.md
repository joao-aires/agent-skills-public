# ECR: inventory pagination off-by-one

**Change ID:** `bug-fix/inventory-pagination`
**Date:** 2026-11-15
**Home:** local fixture only — `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/bug-fix` (not published; no URL, no git repository).

## 1. Overview and lifecycle

`inventory.paginate(items, page, size)` returned the wrong slice for every page because it treated the public 1-based page number as a 0-based offset. The repair is one expression in `inventory.py`: `start = page * size` became `start = (page - 1) * size`. Public signatures and invalid-input behavior are unchanged.

| Claim | Status | Evidence |
| --- | --- | --- |
| Proposed | Done | This record |
| Accepted | Done — task scope is the reported defect | [BUG.md](../BUG.md) |
| Implemented | Done — one line changed | `inventory.py` at sha256 `55382498...` (§6) |
| Verified | Done locally — 9/9 tests passed after repair | §6, [verification.md](verification.md) |
| Released | Not applicable — local evaluation fixture, no deployment target | — |
| Superseded | No | — |

**Next action:** review the diff and the evidence in [verification.md](verification.md). Owner: evaluation reviewer.

## 2. Problem and scope

At baseline, `paginate` computed `start = page * size`. With the fixture list `["a","b","c","d","e"]`, size 2:

- page 1 returned `["c","d"]` instead of `["a","b"]`;
- page 2 returned `["e"]` instead of `["c","d"]`;
- page 3 returned `[]` instead of `["e"]`.

The first page was always skipped, every later page shifted forward, and the final page was truncated to empty. `page_count` was already correct, so the API advertised pages that `paginate` could not return. Callers observing the result (a UI page, a CLI listing) see missing and misordered records.

**In scope:** the slice offset in `paginate`, plus regression coverage that locks first/last/complete-sequence behavior and the existing denial path.
**Out of scope:** `page_count` arithmetic, input validation wording, public signatures, return type, ordering, item types, and any file outside this fixture directory. No unrelated refactor was performed.

**Baseline identity:** `inventory.py` before the change, sha256 `d7d14db2aa69328956c5964b50476b6591b8b0f81082ab7c081afdaecb3cee18` (local-only, not published).

## 3. Requirements and acceptance

| ID | Observable acceptance | Status |
| --- | --- | --- |
| R1 | `paginate(items, 1, size)` returns the first `size` items in order | Accepted, verified |
| R2 | `paginate(items, 2, size)` returns the next `size` items | Accepted, verified |
| R3 | The last page returns the remaining items | Accepted, verified |
| R4 | `paginate(items, page_count + 1, size)` returns `[]` | Accepted, verified |
| R5 | Concatenating pages 1..`page_count` reconstructs the input exactly once, in order | Accepted, verified |
| R6 | `page < 1` or `size < 1` still raises `ValueError` | Accepted, verified (both branches) |
| R7 | `paginate` and `page_count` signatures and return shapes are unchanged | Accepted, verified by inspection and tests |
| R8 | `page_count` still returns `ceil(len(items) / size)` | Accepted, verified |

No open requirement decisions. The denial path is part of the promise because the bug report explicitly requires invalid-input behavior to be preserved.

## 4. Solution design

**Baseline at sha256 `d7d14db2...`:**

```python
def paginate(items, page, size):
    if page < 1 or size < 1:
        raise ValueError("page and size must be positive")
    start = page * size
    return items[start:start + size]
```

**Proposed (implemented):**

```python
start = (page - 1) * size
```

Why this is the smallest correct change: the public contract is 1-based (`page < 1` is rejected, and `page_count` produces 1..n). The only mismatch was the conversion from 1-based page to 0-based list offset. The slice length, boundary behavior, and validation guard were already correct.

**Affected software type:** library/CLI (generic Python module). No frontend, service, persistence, network, auth, or migration seam is involved. The interface seam is in-process list slicing; error/denial mapping is the unchanged `ValueError`.

**Alternatives considered:**

1. Keep `page * size` and change the public API to 0-based pages — rejected: breaks the documented contract and `page_count`; larger blast radius.
2. Clamp `page` into range and infer intent — rejected: changes invalid-input behavior and hides caller errors.
3. Patch `page_count` to match the broken slicing — rejected: the report states page count is already correct; this would preserve the defect.
4. Rewrite pagination as a generator or utility — rejected: unnecessary refactor, changes return type.

**Failure behavior:** a page beyond the last returns `[]` (verified); non-positive inputs raise `ValueError` before slicing (verified). No new failure mode is introduced.

## 5. Implementation strategy

1. Confirm the red loop: run the existing suite, observe the page failures (§6, before).
2. Strengthen the regression test at the same public seam — add size-1 first page, beyond-last page, full-sequence coverage, and the `size < 1` denial path.
3. Re-run to confirm the strengthened suite is red for the reported symptom.
4. Apply the single-expression repair.
5. Re-run the suite and a broader ad-hoc property check over sizes 1..11.
6. Record verification and reconcile docs.

No dependency-ordered increments, compatibility shims, migrations, rollout, or rollback steps apply. The module is self-contained and the change is reversible by restoring one expression.

## 6. Verification and release

**Environment:** macOS (Darwin arm64), Python 3.14.7, local fixture, no VCS, no network. Full record: [verification.md](verification.md).

- **Before (original suite):** `python3 -m unittest -v` → `Ran 5 tests`, `FAILED (failures=3)` — `test_first_page`, `test_second_page`, `test_last_page`.
- **Before (strengthened suite, still buggy):** `python3 -m unittest -v` → `Ran 9 tests`, `FAILED (failures=5)` — the five page-content tests, including `test_first_page_of_size_one` and `test_pages_cover_every_item_once`.
- **After:** `python3 -m unittest -v` → `Ran 9 tests in 0.000s`, `OK`.
- **Broader check:** an ad-hoc property script over sizes 1..11 on 11 items confirmed each page is at most `size`, pages reconstruct all items in order, and the page after the last is empty.
- **Signatures/validation:** unchanged by diff inspection; `test_invalid_input` and `test_invalid_size` passed.

**Revision verified:** fixed `inventory.py` sha256 `55382498ca12e36c42407ce548b4aa515c64d1e546e2a7ecc04261497c3e2b85`; tests sha256 `e8368cf850d930304c923126ff44f2b13fb047bcb10571ecc26e80e8506247a5` (local-only, not published).

**Not exercised:** no external callers exist in this fixture; no downstream application, CLI wiring, network, or persistence path was available to test. No release was performed and none is claimed.

## 7. Decision history and references

| Date | Decision | Owner | Rationale |
| --- | --- | --- | --- |
| 2026-11-15 | Repair the 1-based-to-0-based offset rather than change the public API | evaluation agent (task-scoped) | Smallest change that restores documented behavior and preserves signatures/validation |
| 2026-11-15 | Add four regression cases instead of replacing existing tests | evaluation agent | Existing tests already encoded the contract; additions close the size-1, beyond-last and no-gap/no-duplicate gaps |
| 2026-11-15 | Do not touch `page_count` | evaluation agent | It was already correct; the bug report says so and tests confirm it |

**References:** [BUG.md](../BUG.md), [README.md](../README.md), [inventory.py](../inventory.py), [test_inventory.py](../test_inventory.py), [verification.md](verification.md). All local-only; no repository or publication URL exists.

**Open items:** none for this change. Independent review by a second actor was not available in this evaluation.
