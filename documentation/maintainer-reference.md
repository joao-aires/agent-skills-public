# Maintainer guide

Use this page when changing the collection. For installation and everyday use, start with [Installation](installation.md) and [Usage](usage.md).

<a id="upstream-catalogue"></a>
<a id="source-selection"></a>
<a id="matt-pocock-selection"></a>
<a id="generation-trials"></a>
<a id="recorded-evidence-and-limits"></a>

| Need | Reference |
| --- | --- |
| Understand composition, discovery and fallback | [Plugin and skill architecture](architecture.md) |
| Inspect plugin boundaries and every skill owner | [Plugin ownership map](maintainers/sources.md#plugin-ownership) |
| Add a framework, language or platform | [Adding stack support](maintainers/adding-stack-support.md) |
| Acquire, verify or update committed snapshots | [Upstream maintenance](maintainers/upstreams.md) |
| Check origins, licenses, adaptations or selection decisions | [Sources and compatibility](maintainers/sources.md) |
| Run behavior trials or inspect evidence and open limits | [Evaluating the collection](maintainers/evaluations.md) |
| Find skills by development phase | [SDLC map](sdlc.md) |
| Rename or replace an installed skill | [Migration](migration.md) |

## Maintaining the collection

1. Edit the owning skill under `plugins/<bundle>/skills/<name>/`, keeping its resources intact. Put specialist methods/diagrams beside that skill and user-facing usage in the reader guides.
2. For upstream changes, follow [maintaining upstream snapshots](maintainers/upstreams.md). Agent Depot owns acquisition and snapshot integrity; consumer metadata owns adaptations and attribution. Preserve dependency groups, native controls and licenses. Never acquire private installed content or execute upstream setup during packaging.
3. Update affected links, catalogue entries and migration notes. Bump the plugin version when packaged content changes. Add focused regression coverage for packaging behavior changes.
4. Run the checks below. Build into a fresh destination; replace client installations with complete bundles rather than overwriting local edits.

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
python scripts/validate_evaluations.py
python -m unittest discover -s tests -v
```

CI builds all pinned bundles and each independently, checks inventories/notices/local-resource parity and duplicate names, and runs explorer smoke checks. Build the complete collection with `python scripts/build_plugins.py --all --destination <new-destination>`, then run `python scripts/check_collection.py --built <destination>`. For a selected build, repeat the checker's `--plugin` arguments to identify its expected packages. The checker rejects missing/extra packages, escaping/transitively missing owned resources and missing acquisition-framing context. The link checker covers maintained Markdown guides and entry points; it does not fetch external URLs or parse every preserved resource example. Render changed diagrams separately. Evaluation-definition checks validate structure and flow references; behavioral trials remain explicit, separately recorded runs. Packaging checks do not establish application behavior.

The [marketplace publisher](../.github/workflows/publish-claude-marketplace.yml) calls this same validation workflow at its own revision before publishing from `main`. It builds complete packages and uses `scripts/build_plugin_marketplaces.py` to add Claude Code and Codex catalogs. Only the publication job has repository write permission; failed validation prevents it from running, including a manual dispatch.

The generated `claude-marketplace` branch is distribution output; never edit it by hand. Each publication retains its parent commit, removes stale build files and pushes without forcing history. Unchanged output creates no commit, and a conflicting remote update fails rather than overwriting it. Branch protection must allow the workflow's ordinary publication push if it covers this branch. Enable Actions in a fork to publish under that fork's owner. Native client installation and update verification remain separate from catalog generation; use [installation](installation.md) for client routes.

## Naming and invocation

Use lowercase kebab-case: short activities for tasks (`develop`, `test`, `review`) and recognizable disciplines for support (`interface-design`, `performance-testing`). Preserve upstream names and established operations terminology. Rename folders, frontmatter and maintained references together; record old names in [migration](migration.md#local-skill-naming), without duplicate aliases.

| Metadata | Meaning |
| --- | --- |
| `scope` | `generic` or `stack-specific` applicability |
| `stack` | Technologies matched by stack-specific guidance |
| `role` | `task` entry point or `support` guidance |
| `invocation` | Preferred `user`, `agent` or `both` usage |

Labels do not enforce permissions. Task entries use native explicit-only controls; most local support is model-available with `user-invocable: false`. Product-management, interface-design, backend-design, UX writing and usability research are also directly selectable with `user-invocable: true`, using the same body for people and agents. Preserve upstream controls and record client limitations. [TASKS.md](../plugins/development/TASKS.md) owns execution scope; [WORKFLOW.md](../plugins/development/WORKFLOW.md) owns upstream project fit and consequential-finding decisions across phases.

## Capability architecture

| Responsibility | Owner |
| --- | --- |
| Engagement, stopping point and requested execution | Activity entry point and TASKS.md |
| Product priorities, useful scope and success signal | product-management; business-strategy owns business direction |
| Architecture / service behavior | system-design / backend-design |
| Visual direction / interaction behavior / critique | interface-design |
| AI application/capability/protocol design | ai-development |
| AI testing/evaluation strategy | ai-testing |
| AI operating decisions and quality monitoring | ai-operations |
| Selected Python AI implementation | ai-conventions, ai-deepeval-testing and python-ai-observability |
| Framework APIs, configuration and platform mechanics | Matching technical conventions and upstream specialists |
| Scope, consequential decisions and completion evidence | Shared workflow and the existing verification owner |

UI design composition follows the [capability architecture](architecture.md#compose-domain-interface-and-technical-guidance): the requested activity coordinates application/archetype context, general interface methods, and compatible platform implementation. Future blueprint specialists advertise applicability through descriptions and conditional references; there is no global registry, fixed dependency chain or requirement to update the generic interface skill for each archetype.

Role (task/support), applicability (generic/stack-specific) and invocation are independent dimensions. Plugins package useful capabilities and may contain multiple dimensions. Methods and adapters can use conditional references; a separate skill is justified by a coherent independently useful decision, not by a requirement to split every paragraph. Navigation describes needed capabilities and matches observed specialist descriptions, rather than hardcoding optional skill names or using a global router/metadata engine.

Select only relevant expertise, reuse accepted decisions and preserve existing stack choices. Each capability retains its essential reasoning without assuming optional plugins exist. Missing guidance falls back to project evidence, general expertise and appropriate primary sources; missing execution tools have a separate evidence boundary. See [composition](architecture.md#compose-without-optional-dependencies). See [architecture decisions and product-source review](maintainers/sources.md#product-and-capability-architecture) for the rationale and boundaries.

## Keep guidance focused

| Rule | Owner |
| --- | --- |
| Request and automation scope | TASKS.md |
| Upstream project fit and consequential user decisions | WORKFLOW.md |
| Repository foundations | project-conventions |
| Worktrees, commits and PRs | git-contributions |
| Verification and completion evidence | deliver-reliable-changes |
| Domain methods and exceptions | Relevant specialist skill |

Link the owner instead of copying its rules. Optional guidance is selected from actual inventory and relevance; it does not require a dependency engine. Consolidate further only after [behavior trials](maintainers/evaluations.md#compare-and-simplify) show what agents actually read or miss.

When revising a skill, start from the decision it helps make and the evidence that marks completion. Keep the principle, its applicability and the required outcome together. State the desired behavior directly; reserve strict sequences for dependencies and operational invariants that require them. Use Matt's pinned `writing-for-agents` for instruction hierarchy and pruning.

Use [structured instructions](../plugins/documentation/skills/documentation-writing/references/structured-instructions.md) to choose the form of guidance and its explanatory depth. A workflow needs useful transitions; craft guidance needs judgment and critique; technical reference needs precise mechanisms; maintenance needs criteria for retaining, changing and removing information. These are authoring choices, not new metadata or required sections. Explain consequential decisions without expanding a narrow, already usable skill into a playbook.

Assess each authored skill against its actual job:

| Question | Review for |
| --- | --- |
| Can someone select it for the right work? | A recognizable job, applicability and useful scope. |
| Can they perform that work? | A method or decision principles with enough concrete explanation. |
| Can they make a different choice when appropriate? | Constraints distinguished from defaults, heuristics and examples. |
| Can they find the needed detail? | Meaningful structure, conditional references and clear ownership. |
| Can they judge the result? | Observable outcomes or relevant quality criteria and honest evidence limits. |

Choose paragraphs, lists, sequences, comparisons and examples according to meaning, with no common template, formatting quota or target length. A result can be a decision, an interaction or a verified change; it need not be another document. Retain guidance that already does its job. Review applicability, conditions and completion evidence after rewriting.

Give each rule one owning location within a bundle. Keep material needed on every relevant path in the entry point; link conditional technical detail with a clear trigger. Independently installable bundles may need small overlapping defaults to remain useful on their own. Preserve resources and invocation controls when adapting upstream guidance.

An observed failure should improve a general decision rule, a navigation pointer, a deterministic tool or an evaluation. Keep its concrete reproduction in the evaluation rather than adding another prohibition to every skill. Check that the revision preserves the intended outcome, safeguards, explicit user preferences and completion evidence. Compare both old regressions and unfamiliar scenarios; shorter text alone is not evidence of better behavior.
