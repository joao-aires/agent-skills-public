---
name: write-spec
description: >-
  Turn an existing conversation, decision or brief into specification content using
  the ECR problem, requirements and acceptance structure. Use inside refine to
  synthesize what is already decided, ask only behavior-changing gaps and leave
  readiness and publication with the owning activity.
metadata:
  kind: workflow
  origin: local
  pack: sdlc
  domain: development
  phase: requirements
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# Write a spec from what already exists

Read [refine](../refine/SKILL.md) for the activity, [guide-ecr](../guide-ecr/SKILL.md) and the [ECR contract](../artifact-system/references/contracts/ecr.md) for the artifact shape. Apply [requirements-engineering](../requirements-engineering/SKILL.md) when behavior, quality constraints or acceptance need analysis rather than restatement.

This is a support workflow inside `refine`. It turns a conversation, a decision or an existing brief into spec content. It is not a second requirements activity: `refine` still owns scope, readiness and the handoff, and this workflow does not authorize publication.

## Start from the existing material

- Read the conversation, accepted decisions, current behavior and the repository contracts the change touches. Read any existing ECR before writing a competing version.
- Extract the decision that is already made. Do not re-interview. Ask only about a gap that changes promised behavior, a boundary, acceptance or risk.
- Separate what was decided from what was suggested, assumed or deliberately left open. Record an open decision with its owner; do not settle it by writing a plausible requirement.
- Use the project's existing vocabulary. Do not add a story catalogue, persona inventory or tracker hierarchy to make the spec look complete.

## Choose the output

Write only the shape the existing material supports:

1. **Problem and scope.** The observed problem, affected actor, intended outcome, inclusions, exclusions, relevant existing behavior and assumptions.
2. **Requirements and acceptance.** Affected areas, functional and quality requirements with stable IDs, denial/partial/failure behavior, and named acceptance cases mapped to the requirements they check. Add design requirements only when a user-facing or contract surface must show, say or accept something.
3. **A spec section.** A focused addition to an existing ECR, PRD or design record, with enough of its own context that a reader who was not in the conversation can use it.

Do not force all three when the request needs one. A tracker item is optional, a story catalogue is not the spec, and content production does not publish anything.

## Use stable IDs and observable acceptance

- Use the ECR prefixes `FR-<area>-###`, `NFR-<dimension>-###`, `DR-<surface>-###`, `AC-###` and `DEC-###`/`ASM-###`. Use short `R<n>` labels only for a local change that nothing outside the record will cite.
- Write each requirement as actor, trigger or precondition, observable result and durable effect. Include denial, partial completion, timeout or retry where that changes the promise.
- Map each acceptance case to the requirement IDs it checks, with environment, revision, result and evidence. A requirement with no acceptance case is a gap, not an accepted commitment.
- Keep IDs stable. Add a new ID for a changed commitment and mark the old one superseded; do not renumber to match implementation order.

## Agree the test seam when implementation follows

When the conversation already implies implementation, agree the seam before the spec closes. Prefer an existing seam. Choose the highest seam that can observe the promised behavior, and use the fewest seams; the ideal is one. Record the seam as a testing decision in the spec rather than a new artifact. Name the behavior observed there and any prior art. Use [test](../test/SKILL.md) for verification strategy and [tdd](../tdd/SKILL.md) for seam selection and the red-green loop. If the seam is still contested, return it as an open decision instead of shaping tests around an unconfirmed boundary.

## Return to refine

Report the spec content, the requirements and acceptance that are ready, the open decisions with owners, and what remains unverified. Do not declare the work ready; `refine` owns the readiness disposition. If publication is requested and authorized, use the established artifact home and the owning activity's publishing rules.

Consult [references/synthesis.md](references/synthesis.md) for the conversation-to-spec checklist, what to omit, acceptance mapping and anti-patterns.
