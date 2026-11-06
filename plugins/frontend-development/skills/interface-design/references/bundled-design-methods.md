# Select bundled design methods

Read when choosing supporting design guidance. The same-package paths below are required resources included in the built frontend bundle. Do not ask users to install them separately. The agent loads their entrypoints/relevant references through its supported file or skill tools; a Markdown link does not execute another skill.

| Need | Method and bounded input | Completion evidence |
| --- | --- | --- |
| Open visual identity or palette/type exploration | [UI/UX Pro Max](../../ui-ux-pro-max/SKILL.md): product, task, constraints and actual stack | Inspect candidate fit and translate useful choices into the existing brief/tokens. |
| Scoped UX concern with no broad redesign | One targeted Pro Max domain search if useful; existing project evidence first | Result addresses the actual question; unrelated style suggestions discarded. |
| Rendered critique or refinement | [Impeccable](../../impeccable/SKILL.md): target, accepted brief, requested command and edit boundary | Findings identify screen/state and observed impact; authorized repairs are re-rendered. |
| Expressive motion/editor | Creative implementation reference plus compatible bundled animation guidance | Purposeful mechanism, usable static/reduced-motion fallback, measured runtime evidence. |
| Routine UI bug with accepted design | Existing implementation and relevant local reference | Focused repair and regression evidence; no new direction questionnaire. |

Use both only for distinct needs, such as candidate exploration followed by critique of the implemented slice. Direct user invocation of either upstream method remains useful and retains its native controls. In an orchestrated task, interface-design owns feedback and one brief; upstream methods own their specialist judgment. Preserve the requested stopping point even if a method's prose suggests further changes. Do not claim a method ran merely because it is installed.

## Resolve actual package paths

UI/UX Pro Max's upstream entrypoint includes client-specific `.claude/skills` examples. In this distribution its complete resources live beside its entrypoint, under `skills/ui-ux-pro-max/`. Resolve the installed entrypoint's directory through the client; run the included Python search there by absolute path, with the user's project as working directory. For example, replace `/installed/frontend-development` with the actual built package location:

```sh
python3 -B /installed/frontend-development/skills/ui-ux-pro-max/scripts/search.py "creative portfolio gallery" --design-system
python3 -B /installed/frontend-development/skills/ui-ux-pro-max/scripts/search.py "keyboard focus visible" --domain ux
```

No network service is needed for its local search. Avoid writing Python caches into managed snapshots; use `-B` or `PYTHONDONTWRITEBYTECODE=1`. Do not use `--persist` for unreviewed candidates or overwrite the project's accepted design record. Its search ranking is advice, not user research or a compliance verdict.

Impeccable resolves commands against its skill directory (`CLAUDE_SKILL_DIR` in its packaged examples). Other clients must substitute the actual installed skill directory. The snapshot includes its launcher, version/checksum manifest, references, agent prompt resources, Apache license and third-party notice. Its optional engine binary is **not** part of this repository; the launcher can fetch a versioned platform binary on first execution and may use an operator override. Snapshot pinning therefore establishes the shipped text/scripts, not all runtime execution. Review the launcher and checksum policy before enabling it in a constrained environment. Do not substitute an unpinned `npx ...@latest` installation to claim offline completeness.

The upstream launcher-unavailable path uses existing project context and the relevant playbooks. Follow that documented fallback and disclose omitted detector/engine evidence. This package does not install Impeccable hooks, register named agents, open its live server, or configure third-party image services. Its preserved agent prompts can be supplied as task context where supported; file presence does not register a client agent. Respect host delegation rules and upstream degraded-run labeling; do not claim a dual-agent critique or detector run that did not occur. A direct advanced command may need additional setup described upstream.

Accepted product decisions, accessibility/platform requirements and measured evidence resolve conflicting advice. Keep original upstream copies immutable; maintenance, licenses and exact pins belong to [the source catalogue](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/maintainers/sources.md), not a copied heuristic list here.
