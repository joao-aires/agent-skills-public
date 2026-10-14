# Maintainer guide

Use this page when changing the collection. For installation and everyday use, start with the [README](../README.md#quick-start) and [Usage](usage.md).

<a id="upstream-catalogue"></a>
<a id="source-selection"></a>
<a id="matt-pocock-selection"></a>
<a id="generation-trials"></a>
<a id="recorded-evidence-and-limits"></a>

| Need | Reference |
| --- | --- |
| Check origins, licenses, adaptations or selection decisions | [Sources and compatibility](maintainers/sources.md) |
| Run behavior trials or inspect evidence and open limits | [Evaluating the collection](maintainers/evaluations.md) |
| Find skills by development phase | [SDLC map](sdlc.md) |
| Rename or replace an installed skill | [Migration](migration.md) |

## Maintaining the collection

1. Edit the owning skill under `plugins/<bundle>/skills/<name>/`, keeping its resources intact. Put specialist methods/diagrams beside that skill and user-facing usage in the reader guides.
2. For upstream changes, review source/license changes and update full commit/tree pins in [upstream.lock.json](../upstream.lock.json). Preserve dependency groups, native controls and licenses; record adaptations in notices. Never acquire private installed content or execute upstream setup during packaging.
3. Update affected links, catalogue entries and migration notes. Bump the plugin version when packaged content changes. Add focused regression coverage for packaging behavior changes.
4. Run the checks below. Build into a fresh destination; replace client installations with complete bundles rather than overwriting local edits.

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
python -m unittest discover -s tests -v
```

CI also builds all seven pinned bundles, checks inventories/notices/local-resource parity and duplicate names, and runs explorer smoke checks. To check a fresh all-plugin build locally, run `python scripts/check_collection.py --built <destination>`. The link checker covers maintained Markdown guides and entry points; it does not fetch external URLs or parse every preserved resource example. Render changed diagrams separately. Packaging checks do not establish application behavior.

## Naming and invocation

Use lowercase kebab-case: short activities for tasks (`develop`, `test`, `review`) and recognizable disciplines for support (`interaction-design`, `performance-testing`). Preserve upstream names and established operations terminology. Rename folders, frontmatter and maintained references together; record old names in [migration](migration.md#local-skill-naming), without duplicate aliases.

| Metadata | Meaning |
| --- | --- |
| `scope` | `generic` or `stack-specific` applicability |
| `stack` | Technologies matched by stack-specific guidance |
| `role` | `task` entry point or `support` guidance |
| `invocation` | Preferred `user`, `agent` or `both` usage |

Labels do not enforce permissions. Task entries use native explicit-only controls; most local support is model-available with `user-invocable: false`. Preserve upstream controls and record client limitations. [TASKS.md](../plugins/development-workflow/TASKS.md) owns execution scope; [WORKFLOW.md](../plugins/development-workflow/WORKFLOW.md) owns upstream project fit.

## Keep guidance focused

| Rule | Owner |
| --- | --- |
| Request and automation scope | TASKS.md |
| Upstream project fit | WORKFLOW.md |
| Repository foundations | project-conventions |
| Worktrees, commits and PRs | git-contributions |
| Verification and completion evidence | deliver-reliable-changes |
| Domain methods and exceptions | Relevant specialist skill |

Link the owner instead of copying its rules. Optional guidance is selected from actual inventory and relevance; it does not require a dependency engine. Consolidate further only after [behavior trials](maintainers/evaluations.md#compare-and-simplify) show what agents actually read or miss.
