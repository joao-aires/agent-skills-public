# Add support for a tech stack

Use this guide to add language, framework or platform expertise without creating another development process. Start from a real project need and the [existing skill map](../sdlc.md#skills-by-area). A new stack usually needs focused technical conventions; product decisions, system design, implementation and verification keep their existing owners.

The Go examples below illustrate an extension. This collection does not currently package Go-specific guidance, and these examples do not establish Go support.

## 1. Define the useful boundary

Describe the requests the addition should improve and the technologies that make its advice applicable. Check existing local and upstream guidance before adding another owner.

| Need | Change |
| --- | --- |
| A small variation within an existing stack | Add a conditional section or reference beside its owning skill |
| Coherent expertise useful across several activities | Add a supporting skill with a precise description and applicability |
| A separately useful installation choice | Add a plugin bundle containing the relevant skills and resources |
| A new user outcome with a different stopping point | Consider a task entry point; a new framework alone does not need one |

For example, Go service conventions could explain module/dependency management, request cancellation, database transactions, migrations, diagnostics and suitable verification tools. Product-management still selects useful scope; system-design and backend-design still establish boundaries and service contracts. The Go guidance explains how the chosen stack realizes those decisions.

Keep accepted project choices. State defaults for compatible new projects and conditions for alternatives. Select guidance from actual installed capabilities; adding support must not cause unrelated Python applications to migrate or require every bundle to be installed.

## 2. Write the technical guidance

Place a skill at `plugins/<bundle>/skills/<name>/SKILL.md`. Use a clear discipline or technology name and keep the folder and frontmatter name identical. The [naming and invocation reference](../maintainer-reference.md#naming-and-invocation) explains the independent metadata dimensions.

An illustrative Go conventions skill could begin:

```yaml
---
name: go-conventions
description: Build, extend or review Go services; use for Go modules, request
  lifecycles, persistence, diagnostics and stack-specific verification.
metadata:
  scope: stack-specific
  stack: Go
  role: support
  invocation: both
user-invocable: false
---
```

Here, `invocation: both` describes usage, while `user-invocable: false` hides ordinary support from compatible clients' menus. It remains model-available. Use direct selection when the discipline itself has a useful requested outcome. Preserve native invocation controls when acquiring upstream skills; metadata does not implement routing or permissions.

Explain the technical decisions, applicability, failure boundaries and evidence needed to finish. Keep essential guidance in the skill and put substantial conditional detail in adjacent references, linked with a trigger. Consult current primary documentation when choosing APIs and defaults; record consequential compatibility or licensing limits. Avoid freezing an entire generated application into instructions.

Reuse generic methods through clear conditional pointers. Keep links within the independently installable bundle; another bundle's source path will not exist in a standalone installation. Name optional capabilities for discovery through the actual inventory and retain the essential behavior when they are absent. For example, a service still needs transaction and recovery reasoning even without backend-design installed.

## 3. Package the capability

For an existing bundle, add the skill/resources and bump its `plugin.json` version. A new independently installable bundle needs `plugins/<bundle>/plugin.json`, using the [Python bundle manifest](../../plugins/python-backend/plugin.json) and [bundled schema](../../schemas/plugin.schema.json) as references. Give it its own name, description, version and applicable license metadata. Keep resources inside the package.

When acquiring upstream material, review its fit and redistribution terms, pin its commit and tree in [upstream.lock.json](../../upstream.lock.json), and preserve licenses, dependency groups and invocation controls. The builder acquires listed resources and writes notices. Use the existing lock entries and [source-selection reference](sources.md) rather than copying an unreviewed installed skill. New adaptation logic requires its own focused packaging tests.

No global router registration is required. Descriptions and conditional references let agents find relevant expertise. If an existing activity needs a new selection pointer, add it at that decision rather than copying its workflow into the new skill.

## 4. Update the reader-facing map

Keep each fact in its authoritative home:

| Changed capability | Update |
| --- | --- |
| New installation choice | README plugin table and installation selection examples where useful |
| New technical expertise | SDLC area catalogue; representative diagram examples only when they improve understanding |
| New source or adaptation | Lockfile and source-selection reference |
| Rename or replacement | Migration guide and every maintained reference |
| New bundle | CI's explicit all-plugin build list in `.github/workflows/validate.yml` |

The builder accepts explicit `--plugin` selections. The default remains the three Python/React application bundles unless deliberately changed; it does not automatically include a new bundle. Inspect callers and documented build examples when changing that policy. Package validation discovers manifests, but CI's build list is explicit.

Describe the supported scope and remaining platform limits. Adding a skill file, loading it successfully and observing correct agent behavior are separate milestones.

## 5. Verify the contribution

From a checkout with the [validation dependencies installed](../installation.md#build-the-bundles), run:

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
python scripts/validate_evaluations.py
python -m unittest discover -s tests -v
```

Build into a fresh destination with explicit selections that include the addition. For a new bundle, add it to the existing all-plugin CI command as well. Run `python scripts/check_collection.py --built <destination>` against a complete all-plugin build; that checker expects every package, so a partial build is insufficient. Check inventories, notices, resource parity and duplicate names before publishing. The [maintainer guide](../maintainer-reference.md#maintaining-the-collection) owns the general contribution checks.

Before claiming behavioral support, run appropriately scoped [evaluations](evaluations.md) and retain the evidence at the tested revision. Useful cases include a matching-stack implementation, an existing application whose different stack must remain intact, and a standalone installation missing optional methods. Verify relevant application behavior with the stack's real tools; package checks alone cannot establish it. Native, live-service and publication boundaries require their own capabilities and authorization.

For the illustrative Go extension, a representative path would be: design the service contract with generic methods, implement it using Go conventions, exercise meaningful service behavior with compatible tools, then verify the applicable build and delivery artifacts. Evaluate whether the agent applies that expertise within the requested activity and stops at the agreed outcome. A small bug fix should still remain a small bug fix.
