# Design review: is the proposal ready to hand off?

Use this review on a design proposal, an ECR solution-design section or a design change. It checks whether the decision is understandable, the options are real and the evidence is sufficient for implementation to depend on them.

It complements [artifact assurance](../../artifact-system/references/assurance.md) and the `change-review` activity. `change-review` remains the activity; this reference supplies the design-specific questions.

## Review the proposal

### Decision and scope

- Is the decision stated, with the accepted outcome and constraints?
- Is the current state or "greenfield" explicit?
- Is the scope bounded, and are non-goals clear?
- Is the authority source or decision owner named?

### Software types

- Are the affected types and components stated?
- Are unaffected types stated with a reason?
- Is each type's evidence appropriate, or is a frontend proposal carrying backend ceremony (or vice versa)?
- Is the seam decided once when more than one type is involved?

### Options

- Are there at least three materially different options for a consequential choice?
- Do the options differ on a consequential dimension, not cosmetics?
- Does each name its lens and say what it optimizes and sacrifices?
- Is the recommended option explicit, with the rejected alternatives explained?
- Is the decision reversible or expensive to reverse, and is that stated?

### Linked artifacts

- Does each option have a linked artifact a reviewer can judge?
- Is the fidelity comparable across options?
- Does the linked artifact show the states that matter: empty, loading, error, denied, stale, conflict?
- For a C4, sequence or data view, is current versus proposed explicit?
- For an AI option, is the evaluation plan or behavior shown?
- For a library/CLI, is the public surface and compatibility shown?

### Behavior and failure

- Are error, denial, concurrency, retry, migration and recovery consequences stated?
- Is the seam behavior consistent across the type sections?
- Are authority and accessibility preserved where relevant?
- Are performance, cost or operational consequences stated when they affect the choice?

### Reuse and handoff

- Does the proposal reuse the existing system, components and conventions?
- Are changed responsibilities and integration points named?
- Is the first implementation slice representative?
- Are open questions, owners and evidence gaps explicit?
- Does the handoff state what implementation may start and what is blocked?

## Findings

Report each finding with:

- severity and location;
- the reader or implementer impact;
- the evidence that supports it;
- an actionable correction.

Separate a missing section from a wrong decision. A clean structure with cosmetic options is not ready. A short proposal with a real decision and adequate evidence can pass.

## Reopen when the design changes

If review or new evidence invalidates the chosen option, reopen the design decision, update the design proposal or ECR, and recheck dependent artifacts. Do not keep implementing on a contradicted design.

## Anti-patterns

- reviewing style preference instead of the accepted outcome;
- accepting three cosmetic variants as an option set;
- accepting a proposal with no linked artifact for the question;
- ignoring the seam because each type section looks complete alone;
- requiring a design document for a trivial change;
- approving a design because it is long or polished.
