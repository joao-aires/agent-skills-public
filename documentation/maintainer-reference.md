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
| Write or revise a package README | [Plugin README template](maintainers/plugin-readme-template.md) |
| Inspect plugin boundaries and every skill owner | [Plugin ownership map](maintainers/sources.md#plugin-ownership) |
| Add a framework, language or platform | [Adding stack support](maintainers/adding-stack-support.md) |
| Acquire, verify or update committed snapshots | [Upstream maintenance](maintainers/upstreams.md) |
| Check origins, licenses, adaptations or selection decisions | [Sources and compatibility](maintainers/sources.md) |
| Run evals or inspect evidence and open limits | [Evaluation suite](../evals/README.md) |
| Classify a skill, pack or domain | [Metadata contract](metadata.md) |
| Find skills by development phase | [SDLC coverage](sdlc.md) and [skill reference](sdlc-reference.md) |
| Rename or replace an installed skill | [Migration](migration.md) |

## Maintaining the collection

1. Edit the owning skill under `plugins/<bundle>/skills/<name>/`, keeping its resources intact. Put specialist methods and diagrams beside that skill and user-facing guidance in the reader pages. Frame package responsibilities with the [plugin README template](maintainers/plugin-readme-template.md); keep a complex model in a linked `MODEL.md` appendix rather than expanding the default README.
2. For upstream changes, follow [maintaining upstream snapshots](maintainers/upstreams.md). Agent Depot owns acquisition and snapshot integrity; consumer metadata owns adaptations and attribution. Preserve dependency groups, native controls and licenses. Never acquire private installed content or execute upstream setup during packaging.
3. Update affected links, catalogue entries and migration notes. Bump the plugin version when packaged content changes. Add focused regression coverage for packaging behavior changes.
4. Run the checks below. Build into a fresh destination; replace client installations with complete bundles rather than overwriting local edits.

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
npm --prefix evals run lint
python scripts/artifact_registry.py --check
python scripts/skill_map.py --inventory
# Regenerate a Mermaid diagram (requires Node/npx and a local Chrome):
# PUPPETEER_EXECUTABLE_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
#   npx -y @mermaid-js/mermaid-cli -i documentation/diagrams/<name>.mmd \
#   -o documentation/images/<name>.svg -b white --size 1400
python -m unittest discover -s tests -v
```

CI builds all pinned bundles and each independently, checks inventories, notices, local-resource parity and duplicate names, and runs explorer smoke checks. Build the complete collection with `python scripts/build_plugins.py --all --destination <new-destination>`, then run `python scripts/check_collection.py --built <destination>`. For a selected build, repeat the checker's `--plugin` arguments to identify its expected packages. The checker rejects missing or extra packages, escaping or transitively missing owned resources, and missing acquisition-framing context. The link checker covers maintained Markdown guides and entry points; it does not fetch external URLs or parse every preserved resource example. Render changed diagrams separately. Evaluation-definition checks validate structure and flow references; behavioral trials remain explicit, separately recorded runs. Packaging checks do not establish application behavior.

The [marketplace publisher](../.github/workflows/publish-claude-marketplace.yml) calls this validation workflow at its own revision before publishing from `main`. It builds complete packages and uses `scripts/build_plugin_marketplaces.py` to add Claude Code and Codex catalogs. Only the publication job has repository write permission; failed validation prevents it from running, including a manual dispatch.

The generated `claude-marketplace` branch is distribution output; never edit it by hand. Each publication retains its parent commit, removes stale build files and pushes without forcing history. Unchanged output creates no commit, and a conflicting remote update fails rather than overwriting it. Branch protection must allow the workflow's ordinary publication push if it covers this branch. Enable Actions in a fork to publish under that fork's owner. Native client installation and update verification remain separate from catalog generation; use [installation](installation.md) for client routes.

## Naming and invocation

Use lowercase kebab-case: short activities for tasks (`develop`, `test`, `code-review`) and recognizable disciplines for support (`interface-design`, `performance-testing`). Preserve upstream names and established operations terminology. Rename folders, frontmatter and maintained references together; record old names in [migration](migration.md), without duplicate aliases.

| Metadata | Meaning |
| --- | --- |
| `scope` | `generic` or `stack-specific` applicability |
| `stack` | Technologies matched by stack-specific guidance |
| `role` | `task` entry point or `support` guidance |
| `invocation` | Preferred `user`, `agent` or `both` usage |

Labels do not enforce permissions. `user-invocable` controls the direct user command surface; it does not hide a skill from the agent. `disable-model-invocation` is the actual agent auto-invocation gate. Most local support is agent-usable with `user-invocable: false`. product-direction, interface-design, backend-design, UX writing and usability research are also directly selectable with `user-invocable: true`, using the same body for people and agents. Preserve upstream controls and record client limitations. [activity-system](../plugins/sdlc/skills/activity-system/SKILL.md) owns activity selection, execution scope, project fit and consequential decisions. The engineering artifact and workspace skills own their respective contracts.

## Capability architecture

| Responsibility | Owner |
| --- | --- |
| Engagement, stopping point and requested execution | Activity entry point and activity-system |
| Product priorities, useful scope and success signal | product-direction; business-strategy owns business direction |
| Architecture and service behavior | design-system, backend-design, architecture-patterns |
| Visual direction, interaction behavior and critique | interface-design |
| AI application, capability and protocol design | ai-development |
| AI testing strategy and evaluation program | ai-testing, ai-evaluation |
| AI operating decisions and quality monitoring | ai-operations |
| Selected Python AI implementation | ai-conventions, ai-deepeval-testing, python-ai-observability |
| Pipeline design and release flow | ci-cd-pipelines |
| Framework APIs, configuration and platform mechanics | Matching technical conventions and upstream specialists |
| Scope, consequential decisions and completion evidence | Shared workflow and the existing verification owner |

UI design composition follows the [capability architecture](architecture.md#compose-domain-interface-and-technical-guidance): the requested activity coordinates application context, general interface methods and compatible platform implementation. Future blueprint specialists advertise applicability through descriptions and conditional references; there is no global registry or fixed dependency chain.

Role (task/support), applicability (generic/stack-specific) and invocation are independent dimensions. Plugins package useful capabilities and may contain multiple dimensions. Methods and adapters can use conditional references; a separate skill is justified by a coherent independently useful decision, not by the need to split every paragraph. Navigation describes needed capabilities and matches observed specialist descriptions rather than hardcoding optional skill names or using a global router.

Select only relevant expertise, reuse accepted decisions and preserve existing stack choices. Each capability retains its essential reasoning without assuming optional plugins exist. Missing guidance falls back to project evidence, general expertise and appropriate primary sources; missing execution tools have a separate evidence boundary. See [composition](architecture.md#work-without-optional-dependencies) and [product and capability architecture](maintainers/sources.md#product-and-capability-architecture) for the rationale and boundaries.

## Keep guidance focused

| Rule | Owner |
| --- | --- |
| Request and automation scope | activity-system |
| Upstream project fit and consequential user decisions | activity-system |
| Repository foundations | project-conventions |
| Worktrees, commits and PRs | git-contributions |
| Verification and completion evidence | test |
| Domain methods and exceptions | Relevant specialist skill |

Link the owner instead of copying its rules. Optional guidance is selected from actual inventory and relevance; it does not require a dependency engine. Consolidate further only after [eval comparisons](../evals/README.md#compare-and-simplify) show what agents actually read or miss.

When revising a skill, start from the decision it helps make and the evidence that marks completion. Keep the principle, its applicability and the required outcome together. State the desired behavior directly; reserve strict sequences for dependencies and operational invariants that require them. Use the pinned `writing-for-agents` guidance for instruction hierarchy and pruning, and [structured instructions](../plugins/documentation/skills/technical-writing/references/structured-instructions.md) to choose the form and explanatory depth. A workflow needs useful transitions; craft needs judgment and critique; technical reference needs precise mechanisms; maintenance needs criteria for retaining, changing and removing information.

Assess each authored skill against its actual job:

| Question | Review for |
| --- | --- |
| Can someone select it for the right work? | A recognizable job, applicability and useful scope |
| Can they perform that work? | A method or decision principles with enough concrete explanation |
| Can they make a different choice when appropriate? | Constraints distinguished from defaults, heuristics and examples |
| Can they find the needed detail? | Meaningful structure, conditional references and clear ownership |
| Can they judge the result? | Observable outcomes or relevant quality criteria and honest evidence limits |

Choose paragraphs, lists, sequences, comparisons and examples according to meaning. There is no required template, formatting quota or target length. A result can be a decision, an interaction or a verified change; it need not be another document. Retain guidance that already does its job.

An observed failure should improve a general decision rule, a navigation pointer, a deterministic tool or an evaluation. Keep its concrete reproduction in the evaluation rather than adding another prohibition to every skill. Check that the revision preserves the intended outcome, safeguards, explicit user preferences and completion evidence. Compare both old regressions and unfamiliar scenarios; shorter text alone is not evidence of better behavior.

### Own the capability, disclose the detail, link the authority

A skill is a scoped capability contract, not a summary of external documentation. It states what outcome it owns, how to reach it, which judgment and local standards matter, what evidence proves completion, and what to load, execute or look up.


| Knowledge | Where it belongs | Why |
| --- | --- | --- |
| Outcome, entry conditions, stopping point, authority | Skill body | The agent must know what work it is doing and where it stops |
| Local standards, conventions and accepted decisions | Skill body or a local reference | They cannot be reconstructed from a public source |
| Judgment, tradeoffs, failure modes and evidence | Skill body | This is the capability the skill exists to provide |
| Stable checklists, decision tables and worked examples | Local reference | Useful, but too long for every invocation |
| Deterministic transformation or check | Script | Executable knowledge beats prose and can be tested |
| Output template, fixture, icon or font | Asset | It is used in the result, not read as guidance |
| API signatures, flags, config keys and syntax | External authority | The framework or provider owns them and changes them |
| Version-specific behavior, quotas and pricing | External authority or a dated vendor note | Commercial and release facts change independently |
| Environment facts and generated inventories | The environment or a generated check | A copy becomes a stale cache |

The rule of thumb: **own the judgment and procedure, disclose branch detail, execute the deterministic part, and link or verify the authority.** A skill that only links has abdicated its method; a skill that mirrors docs has taken on maintenance it cannot win.

Keep the detail when it is a safety, security or authority invariant; a local convention or accepted decision; a non-obvious trap or a criterion for choosing between external options; the external docs are unreliable, inaccessible or version-fragmented; a minimal name or command is needed for orientation; or an offline fallback is required.

## Authoring a skill

Use the repository's [skill-authoring](../plugins/documentation/skills/skill-authoring/SKILL.md) method for the operational loop: define the contract, choose the form, draft the smallest complete capability, test with realistic prompts, and validate packaging. It also covers progressive disclosure, cross-plugin composition and the review questions. [Writing for agents](../plugins/documentation/skills/writing-for-agents/SKILL.md) owns agent-facing instruction craft, and [technical writing](../plugins/documentation/skills/technical-writing/SKILL.md) owns prose craft.

Creating or revising a skill is a loop, not a one-pass draft: define the outcome and nearest adjacent skill; choose a new skill, expansion, reference, script, asset or no change; draft; test with and without the skill; read the outputs and revise; validate; repeat only while evidence shows a real improvement.

## Review before handoff

- Can a reader select the skill for the intended work without choosing a near neighbour?
- Can an agent start, act, verify and stop using the guidance?
- Is every claim about behavior tied to a command, scenario, revision or link?
- Is each meaning in one authoritative place, with a clear owner and validation path?
- Do the links resolve inside an independently built package?
- Does the change preserve native controls, licenses and accepted project decisions?

Validation commands and evidence limits are above. A manual reader review is sufficient for ordinary edits; a fresh reader or authorized independent agent helps for consequential documents. Do not claim independent testing when only the author reviewed it.
