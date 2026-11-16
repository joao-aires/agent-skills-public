# Start here

Choose the path that matches the work. Each path is a composition, not a compulsory pipeline. Stop at the requested outcome.

## New application

`setup` → `plan` → `refine` → `design` → `implement` → `test` → review → `release` when authorized.

- Artifacts: ECR (compact or full), design proposal when a consequential choice is open, README, code and tests.
- Guides: [guide-readme](../plugins/sdlc/skills/guide-readme/SKILL.md), [guide-ecr](../plugins/sdlc/skills/guide-ecr/SKILL.md), and [guide-design-proposal](../plugins/sdlc/skills/guide-design-proposal/SKILL.md) when a design record is needed.
- Software type: read [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md) and the matching type file.
- Review: `code-review` for the diff, `test` for evidence, [artifact assurance](../plugins/sdlc/skills/artifact-system/references/assurance.md) for convergence.

## Existing feature

Inspect the current system → `refine` → `design` if the choice is consequential → `implement` → `test` → review.

- Artifacts: compact ECR when the change is local and reversible; full ECR when it changes a boundary, migration, compatibility or coordination.
- Guides: [guide-ecr](../plugins/sdlc/skills/guide-ecr/SKILL.md), [guide-design-proposal](../plugins/sdlc/skills/guide-design-proposal/SKILL.md), [guide-pr](../plugins/sdlc/skills/guide-pr/SKILL.md) when a PR exists.
- Preserve existing behavior, tests, JSON/contract shapes and project tooling.

## Bug fix

Reproduce → [fix](../plugins/sdlc/skills/fix/SKILL.md) → [test](../plugins/sdlc/skills/test/SKILL.md) → review.

- Artifacts: compact ECR or a commit/PR note; a regression test is the evidence.
- Use [diagnosing-bugs](../plugins/sdlc/skills/diagnosing-bugs/SKILL.md) when the cause is not evident.
- Stop at the repaired behavior and observed verification. Do not refactor unrelated code.

## Idea to implementation

`plan` → `refine` → `design` → `implement` → `test` → review.

- Artifacts: product brief/PRD, design proposal, compact or full ECR, README and tests.
- Decide the consequential product/design choices explicitly; defer the rest.
- Keep a useful slice, not a platform.

## Compact or full ECR?

Use a **compact** record when the change is local and reversible, one component, one evident approach, and does not change a boundary, migration, security, compatibility or a consequential decision. Otherwise use the **full** record.

Read the [ECR contract](../plugins/sdlc/skills/artifact-system/references/contracts/ecr.md) for both shapes.

## Review is a composition

Review is not a separate skill. Use:

| Concern | Owner |
| --- | --- |
| Code-diff standards and spec | [code-review](../plugins/sdlc/skills/code-review/SKILL.md) |
| Verification evidence | [test](../plugins/sdlc/skills/test/SKILL.md) |
| Cross-artifact convergence | [artifact assurance](../plugins/sdlc/skills/artifact-system/references/assurance.md) |
| Artifact-specific questions | The matching `guide-*` |
| Shared artifact properties | [quality bar](../plugins/sdlc/skills/artifact-system/references/quality-bar.md) |

Stop at findings. Posting comments, editing source, merging and deploying require separate authority.

## Where to look next

- Activity selection: [SDLC coverage](sdlc.md) and [activity catalog](../plugins/sdlc/skills/activity-system/references/catalog.md).
- Artifact types and contracts: [artifact catalog](../plugins/sdlc/skills/artifact-system/references/catalog.md).
- Contract/guide pairing: [guide registry](../plugins/sdlc/skills/artifact-system/references/guide-registry.md).
- Software types: [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md).
- Composition and fallback: [composition](../plugins/sdlc/skills/activity-system/references/composition.md).
