# Bug report

Pagination skips the first page of results.

Reproduction:

```bash
python3 -m unittest -v
```

Expected: page 1 returns the first `size` items, page 2 returns the next `size`, and the last page contains the remainder. The page count is already correct.

Preserve the public function signatures and invalid-input behavior.
