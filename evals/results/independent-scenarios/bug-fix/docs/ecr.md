# Fix pagination skipping the first page

## Overview

`inventory.paginate(items, page, size)` returned the wrong slice for every page. Page 1 returned
the items that belong on page 2, and the final page fell past the end of the list. The bug is
fixed and verified locally by the test suite. No release or commit was made.

Local revision: this workspace is not a Git repository; no commit or URL exists. Source identity
is the content hashes below, recorded 2026-11-15.

| File | SHA-256 |
| --- | --- |
| `inventory.py` | `55382498ca12e36c42407ce548b4aa515c64d1e546e2a7ecc04261497c3e2b85` |
| `test_inventory.py` | `52bca3153c1bbf4b9469052911922c4e231e7d96f2315dcf31364d9967b4219e` |

Not published; content hashes, not a commit.

## Change and acceptance

- Observed before the repair: `paginate(["a","b","c","d","e"], 1, 2)` returned `["c","d"]`
  instead of `["a","b"]`; page 2 returned `["e"]`; page 3 returned `[]`.
- Cause: the start index was `page * size`. With one-based pages it must be
  `(page - 1) * size`. The first page therefore began one page too far into the list, and the
  last page started beyond the final item. `page_count` was already correct and was not changed.
- Repair: one expression changed in `paginate`; `page_count` is untouched.
- Preserved: both public function signatures, the existing `ValueError` checks for `page < 1`
  or `size < 1`, and the existing empty-list result for a page beyond the last page.
- Acceptance cases, all verified:
  - page 1 returns the first `size` items;
  - each full page returns exactly `size` items;
  - the last page returns the remaining items;
  - all pages in order, concatenated, reproduce the original list with no gaps or duplicates;
  - an exact multiple of `size` has no extra page;
  - a page after the last page returns `[]`;
  - `page` or `size` below one still raises `ValueError`.

The regression test strengthens the original three page assertions with an exhaustive
page-partition invariant for every `size` from 1 through `len(items) + 1`, plus exact-multiple,
past-the-end and invalid-size cases. It uses only the public functions.

## Verification

Environment: macOS `Darwin 27.0.0 arm64`, `Python 3.14.7`, standard library `unittest`.

| When | Command | Observed result |
| --- | --- | --- |
| Before fix, original tests | `python3 -m unittest -v` | 5 run, 3 failed (`test_first_page`, `test_second_page`, `test_last_page`) |
| Before fix, strengthened tests | `python3 -m unittest -v` | 8 run, 5 failed (also `test_pages_cover_all_items_in_order`, `test_exact_multiple_has_one_page`) |
| After fix | `python3 -m unittest -v` | 8 run, 0 failed, `OK` |
| After fix, direct behavior probe | `python3 -c '...'` | `[['a', 'b'], ['c', 'd'], ['e']]`; page count `3` |

The failing output before the fix showed `['c','d'] != ['a','b']` for page 1 and `[] != ['e']`
for the last page, matching the reported symptom. Not exercised: other Python versions, other
input types, packaging or CI.

## Decisions and open items

- Kept one-based page numbering because the report and the existing tests define it that way.
- Left the out-of-range page contract as an empty list rather than adding an error; this
  preserves the previous slicing behavior and avoids a new boundary decision.
- Used a deterministic exhaustive loop instead of a property-testing dependency; the task
  permits no third-party dependencies and the input space is small.
- Open: nothing required by BUG.md. A commit, PR or release was not requested and no repository
  exists here.
