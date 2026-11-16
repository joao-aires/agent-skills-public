# Verification: task tags and tag filtering

## Claim under test

`taskcli.py` stores optional tags, `add` accepts tags without breaking `add "title"`, `list --tag <tag>` filters pending tasks, `list --all --tag <tag>` filters all tasks, old JSON remains readable, and the existing `list`, `list --all`, `done` and test behavior is preserved.

**Status: verified locally.** No deployment, package installation or CI result is claimed.

## Revision and environment

- Fixture directory: `/private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/existing-feature`
- The directory is not a Git repository. The checked state is local-only, not published, with no commit or URL. Local pin: `taskcli.py` SHA-256 `32f2faecb02ce76a0995a0cb00f700ca84e5735b11cfeaee7ef2841710560506`; `test_taskcli.py` SHA-256 `0cd042660352dee2aa1b1d904aee3ba55022edf285da9a74a78b340fc411c0f5`.
- Platform: macOS 27.0.1 (Darwin 27.0.0), arm64.
- Runtime: Python 3.14.7 (`macOS-27.0.1-arm64-arm-64bit-Mach-O`), standard library only.
- Date: 2026-11-15. No network access and no third-party dependencies were used.

## Automated checks

Command:

```bash
cd /private/var/folders/73/9y4j_bps23d_7w1_bkznpzsh0000gn/T/opencode/agent-skills-evals/existing-feature
python3 -m unittest -v
```

Observed result (full run): `Ran 22 tests in 0.011s` followed by `OK`. 0 failures, 0 errors, 0 skips. All 22 test methods reported `ok`, including the three original methods:

- `test_add_and_list_pending`
- `test_done_hides_from_pending_and_persists`
- `test_unknown_index_raises`

The added methods cover: empty tag list on plain `add`; tag persistence; normalization/dedupe; string tags; pending filter; include-done filter; case-insensitive filter; unknown tag; legacy JSON read; legacy shape after `done`; exact new JSON record; CLI add/filter; tag before title; `--tag=` plus comma list; `list --all --tag`; unchanged untagged list format; multiple `list --tag` rejection; missing title; empty tag rejection.

## CLI scenario

A temporary `TASKCLI_DATA` file was used. Commands and observed output, in order:

```text
$ python3 taskcli.py add "write report" --tag Work --tag urgent
added 0
$ python3 taskcli.py add "buy milk" --tag home
added 1
$ python3 taskcli.py add "review report" --tag=work,urgent
added 2
$ python3 taskcli.py add "legacy style"
added 3
$ python3 taskcli.py list
0	 	write report
1	 	buy milk
2	 	review report
3	 	legacy style
$ python3 taskcli.py list --tag work
0	 	write report
2	 	review report
$ python3 taskcli.py list --tag URGENT
0	 	write report
2	 	review report
$ python3 taskcli.py done 0
done write report
$ python3 taskcli.py list --tag work
2	 	review report
$ python3 taskcli.py list --all --tag work
0	x	write report
2	 	review report
```

The resulting JSON file was:

```json
[
  {"title": "write report", "done": true, "tags": ["work", "urgent"]},
  {"title": "buy milk", "done": false, "tags": ["home"]},
  {"title": "review report", "done": false, "tags": ["work", "urgent"]},
  {"title": "legacy style", "done": false, "tags": []}
]
```

(The saved file is pretty-printed with two-space indent; the content above is the same data, condensed for this record.)

This establishes: title-only `add` still works; tags are canonicalized from `Work` to `work`; comma and repeated forms both work; pending filtering excludes the completed task; `--all` includes it with mark `x`; list columns are unchanged; `done` still persists.

## Legacy JSON scenario

Input file, written directly:

```json
[{"title": "old pending", "done": false}, {"title": "old done", "done": true}]
```

Observed:

```text
$ python3 taskcli.py list
0	 	old pending
$ python3 taskcli.py list --all
0	 	old pending
1	x	old done
$ python3 taskcli.py list --tag work
$ python3 taskcli.py done 0
done old pending
$ python3 taskcli.py list --all
0	x	old pending
1	x	old done
```

After `done 0`, the file was:

```json
[
  {"title": "old pending", "done": true},
  {"title": "old done", "done": true}
]
```

This establishes backward compatibility: records without `tags` load, list and complete normally; filtering treats them as untagged; `done` does not invent a `tags` key. No migration was run.

## Failure and denial paths

```text
$ python3 taskcli.py add "write report" --tag "  "
invalid tag: tag cannot be empty
exit=1
$ python3 taskcli.py add "write report" --tag
option --tag requires a value
exit=1
$ python3 taskcli.py list --tag work --tag home
list accepts a single --tag
exit=1
$ test -f "$TASKCLI_DATA" && echo yes || echo no
no
```

Each rejected command returned 1 and wrote no file, confirming validation happens before `save`.

## Not exercised / limits

- No concurrent-writer, file-lock, partial-write, disk-full or non-POSIX test.
- No test of a consumer outside this fixture; compatibility is established for the documented JSON shape and this code only.
- No JSON-schema validator; the exact record shape was asserted in a test and observed in the scenario above.
- No package installation, VCS diff, CI run, pull request or release. None exists in the fixture.
- Timing (0.011s) is informational, not a performance claim.

## Conclusion

All eight requirements in the [ECR](ecr.md#3-requirements-and-acceptance) have local, observed evidence. The original behavior remains covered by the original tests and by the unchanged list format in the CLI scenario. Remaining gaps are the pre-existing concurrency/atomicity limits and the deliberately deferred tag display/editing features, not unmet acceptance criteria.
