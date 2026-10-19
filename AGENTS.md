# Repository instructions

This repository publishes reusable agent guidance as independently selectable plugins. Make changes in the owning source package and keep the collection useful across projects and clients. Start with [architecture and composition](documentation/architecture.md); use the [maintainer guide](documentation/maintainer-reference.md) for contribution details.

## Find the owner

- `plugins/<bundle>/plugin.json` identifies a package; `skills/<name>/SKILL.md` contains each local skill and its neighboring resources. Package-root documents own shared framing.
- [Sources and ownership](documentation/maintainers/sources.md#target-plugin-ownership) maps skills to packages. `upstream.lock.json` records reviewed acquisitions; the builder adds them to complete bundles. Generated build output is not the editing source.
- `scripts/` and `tests/` maintain validation, acquisition and packaging. `evals/` describes behavioral scenarios; [evaluation guidance](documentation/maintainers/evaluations.md) records procedures, findings and limits.

## Preserve the architecture

Keep generic activities, application disciplines, technical expertise and supporting capabilities independently useful. Development is the default build; technical packages are explicit additions. Installing guidance does not select an application stack.

Route optional expertise by needed capabilities and actual available descriptions. Do not hardcode optional cross-package skill/plugin names or introduce a global router or dependency resolver. Required resources inside a package may use precise relative links. When a specialist is absent, use project evidence, general expertise and appropriate primary sources while preserving acceptance and verification standards. Distinguish absent guidance from unavailable tools or unresolved user decisions.

Keep packages self-contained. Preserve the original strategy/visual resources, complete upstream dependency groups, invocation controls and licenses. Acquire public upstream content at reviewed commit/tree pins; record adaptations in source notices. Never redistribute private installed skills. Add MCP connections or client hooks only for a concrete need with documented setup.

## Write decision guidance

Start from the decision a skill helps make, its applicability and the evidence that marks completion. Write concise principles that leave ordinary implementation choices to the project and agent. Use strict sequences for real dependencies or operational invariants. Put conditional detail in linked resources with a clear reading trigger.

Give a rule one owning location within its package and link it where needed. Generalize an observed failure into a decision principle; keep the concrete reproduction in an evaluation or a justified deterministic test. Avoid growing lists of incident-specific prohibitions, generated applications, scaffolds or mandatory process machinery.

Preserve native invocation controls. Descriptive metadata is not permission enforcement. Explicit-only activities require an explicit request; automatically selected supporting guidance stays within the requested scope. Client limitations and missing evidence remain visible.

Use lowercase kebab-case: short recognizable activities for task entry points, clear topics/disciplines for support. Preserve established operations terminology and upstream names. Rename the folder, frontmatter and maintained references together; record old names in migration notes without duplicate aliases.

## Maintain the documentation

Write repository prose in my singular voice (João), using "I" and "my" for my choices. Keep examples in their author's voice. Use Humanizer for prose edits while preserving technical meaning, caveats, commands and link targets.

Organize docs by reader need. README introduces the collection; installation and usage explain how to start; architecture and SDLC explain composition and lifecycle coverage; migration explains updates. Keep the maintainer entry short, with source and evaluation detail under `documentation/maintainers/`. Put current decisions/evidence in their existing homes rather than adding a report per change.

Update affected documentation alongside source changes and accepted decisions. Keep manifests, README, ownership/source catalogue and acquisition pins aligned. Bump the owning package version when packaged content changes. Verify client-specific examples against current primary documentation; keep documented setup distinct from exercised behavior. [Adding stack support](documentation/maintainers/adding-stack-support.md) explains extensions without new workflow dependencies.

## Verify the affected contract

Install dependencies from `requirements-validation.txt` in a virtual environment as described in [installation](documentation/installation.md#build-the-bundles). Run these repository checks after relevant changes:

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
python scripts/validate_evaluations.py
python -m unittest discover -s tests -v
```

For packaging or resource changes, build into a fresh destination and check the complete output. CI also checks the development-only default and every package independently; see [maintainer checks](documentation/maintainer-reference.md#maintaining-the-collection) for commands and coverage. Add focused regression tests for packaging behavior. Render and inspect changed diagrams; run affected resource checks when their behavior changes.

Do not install clients/plugins, connect accounts or run behavioral evaluations merely to complete structural checks. Run those when the request includes them, and record the actual target revision, actions, results and limits. Package, link and evaluation-definition checks establish structure; they do not establish agent adherence, application behavior or successful deployment.
