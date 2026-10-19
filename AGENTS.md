# Repository instructions

## Source and ownership

- Edit owning sources under `plugins/<bundle>/`: `plugin.json`, `skills/<name>/SKILL.md`, neighboring resources and package-root framing. Build output is generated.
- Use the [ownership map](documentation/maintainers/sources.md#target-plugin-ownership) to locate a capability. `upstream.lock.json` owns reviewed acquisitions; the builder adds them to complete bundles.
- Keep packages self-contained. Preserve original strategy/visual resources, complete upstream groups, native invocation controls and licenses. Acquire public sources at reviewed commit/tree pins and record adaptations in notices; never redistribute private installed skills.

## Architecture and authoring

- Preserve independently useful generic activities, application disciplines, technical expertise and supporting capabilities. Development is the default build; technical packages are explicit additions and do not select an application stack.
- Select optional expertise by capability and actual available descriptions, without hardcoded cross-package names or a dependency resolver. Required same-package resources may use precise relative links. Without a specialist, retain acceptance standards using project evidence, general expertise and primary sources; distinguish missing guidance from missing tools or decisions.
- Write decision principles with applicability and completion evidence. Keep ordinary implementation choices with the project and agent; reserve strict sequences for real dependencies. Link conditional detail with a reading trigger, and keep each rule with its owner.
- Generalize findings into decision guidance; put concrete reproductions in `evals/` or justified deterministic tests. Avoid incident-specific prohibition lists, generated applications, scaffolds and mandatory process machinery.
- Preserve explicit-only activity controls and the requested action scope. Descriptive metadata does not enforce permissions. Add MCP connections or client hooks only for a concrete need with documented setup.
- Use lowercase kebab-case: short activities for tasks and recognizable disciplines for support. Preserve upstream names and established operations terminology. Rename folders, frontmatter and maintained references together; record old names in migration notes without duplicate aliases.

## Documentation and contributions

- Update affected documentation alongside source changes and accepted decisions. Keep manifests, README, ownership/source catalogue and pins aligned; bump the owning version for packaged changes.
- Keep user guides organized by reader need and the maintainer entry short. Put source/evaluation detail in the existing maintainer references rather than a report per change. Add focused how-tos for recurring tasks.
- Use Humanizer when available for prose edits, preserving technical meaning, caveats, commands and links. Verify client-specific examples against primary documentation and distinguish documented setup from exercised behavior.
- Follow [Git contributions](plugins/development/skills/git-contributions/SKILL.md) for objective worktrees, Conventional Commits and structured PRs. Commit/push authority is separate from merge or deployment authority.

## Verification

Use the virtual environment and dependencies in [installation](documentation/installation.md#build-the-bundles).

| Check | Command |
| --- | --- |
| Manifests, metadata, pins and containment | `python scripts/validate_plugins.py` |
| Maintained links and names | `python scripts/check_collection.py` |
| Scenario definitions | `python scripts/validate_evaluations.py` |
| Packaging and validation regressions | `python -m unittest discover -s tests -v` |

- Run relevant checks above; for packaging/resource changes also build into a new destination and check complete output. CI checks the default, full collection and each package independently. Add focused tests for changed packaging behavior; render/inspect changed diagrams and run affected resource checks.
- Package and definition checks establish structure, not agent adherence, application behavior or deployment. Run client installation, account setup and behavioral trials only within the request; record the actual revision, actions, results and limits.

## Detailed references

| Need | Source |
| --- | --- |
| Composition, discovery and fallback | [Architecture](documentation/architecture.md) |
| Contribution procedure, naming and build/check commands | [Maintainer guide](documentation/maintainer-reference.md) |
| Sources, licenses, adaptations and ownership | [Source catalogue](documentation/maintainers/sources.md) |
| Behavioral scenarios and recorded limits | [Evaluation guide](documentation/maintainers/evaluations.md) |
| New framework, language or platform | [Adding stack support](documentation/maintainers/adding-stack-support.md) |
| Replacing old packages or names | [Migration](documentation/migration.md) |
