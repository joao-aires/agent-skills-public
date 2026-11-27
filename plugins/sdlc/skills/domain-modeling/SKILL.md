---
name: domain-modeling
description: >-
  Expertise and methods for domain modeling. Sharpen a project's domain language while
  designing. Use when terms are overloaded or inconsistent, boundaries are unclear, or a
  resolved term or consequential choice needs a glossary entry or decision record. It informs
  the activity that composes it; that activity owns the decision and stopping point.
user-invocable: true
metadata:
  kind: method
  domain: design
  phase: design
  scope: generic
  invocation: both
---

# Domain modeling: make the language carry the design

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Domain modeling is the active discipline of deciding what the project's words mean while the design is still forming. Reading a glossary for vocabulary is not this method. This method changes terms, tests their boundaries against concrete behavior, and records the resolution where the project already keeps shared language and decisions. Use [artifact system](../artifact-system/SKILL.md) to choose the artifact and [artifact homes](../artifact-system/references/homes.md) to place it.

## Reading path

| Need | Read |
| --- | --- |
| Where glossary entries and decisions live | [Artifact system](../artifact-system/SKILL.md), [artifact homes](../artifact-system/references/homes.md) |
| What a decision record must contain | [Decision record contract](../artifact-system/references/contracts/adr.md), [guide-adr](../guide-adr/SKILL.md) |
| Sharper prompts, edge cases and recording triggers | [Terminology notes](references/terminology.md) |
| Where the method is used | [refine](../refine/SKILL.md), [design](../design/SKILL.md) |

## Find the terms that carry weight

A term is load-bearing when a different reading changes behavior, a boundary, ownership, state, an obligation or a test. Look for:

- one word used for two concepts, such as "account" meaning both the customer and the login;
- two words used for one concept, such as "cancel", "void" and "revoke";
- a vague word hiding a decision, such as "sync", "active", "deleted" or "admin";
- a term the code, documentation and accepted decisions define differently.

Challenge the ambiguity directly: state the readings you heard, the consequence of each and the canonical term you propose. Do not silently rename the user's language or the code; ask which meaning is intended. Preserve a term that a platform, regulator or upstream contract already owns rather than redefining it locally.

## Test the model with edge scenarios

Definitions are cheap until a boundary case arrives. Invent concrete scenarios that force the distinction:

- partial success, duplicate requests, retries and replays;
- two actors changing the same thing at once;
- a permission or ownership change while work is pending;
- deletion, retention, export and legacy records;
- migration, backfill or data created under an older rule;
- empty, new, suspended or never-activated cases;
- time, quantity, currency, rounding or proration where meaning depends on them.

For each scenario, ask which term applies, what the actor observes and which state or obligation follows. A definition that cannot answer the scenario is still open.

## Cross-check code and accepted decisions

When the stated model and the code, schema, tests or accepted decision disagree, surface the contradiction with the evidence: "The code cancels the whole order, but the model says partial cancellation exists. Which is authoritative?" Resolve the conflict before the new term spreads into requirements, design or tests. Do not update the code or the decision to match a definition that has not been agreed.

Read the identifiers, fields, labels and API names that already claim the idea. A term that exists only in conversation is a proposal; a term the code and users already rely on has a migration cost. Name that cost before changing it.

## Record the resolved language

Write a resolved term to the project's existing glossary or knowledge home, using the home map rather than a habitual path. The default is `docs/glossary.md`, but preserve an established glossary or docs site. Do not impose a root `GLOSSARY.md`, a glossary map file or a new documentation tree.

Keep the glossary terminology only: one term, one meaning, the boundary that matters and any accepted decision it depends on. Implementation rules, state machines and behavioral requirements belong in the ECR, design record or requirements, not in the glossary. If no glossary home exists and creating one is not authorized, report the suggested entry and its home instead of writing it.

Capture the resolution when the term is settled enough to reuse. Do not batch terminology changes until the end of the work; by then the old word has already spread into requirements and tests.

## Record a decision only when it earns one

Use the existing [decision record contract](../artifact-system/references/contracts/adr.md) and [ADR guide](../guide-adr/SKILL.md) when a resolved choice must outlive the work. Offer an ADR or PDR only when all three are true:

1. the choice is hard to reverse;
2. a future reader would be surprised without the context;
3. the result came from a real trade-off between credible alternatives.

If any condition is missing, keep the rationale in the design record, ECR or code. A reversible naming choice, an obvious rule or a decision with no alternative does not need a record. Follow the local contract fields and supersession rules; do not impose `docs/adr/` or a fixed one-paragraph record format.

The glossary owns terminology, not rationale. The decision record owns the accepted choice and its consequences. Do not copy one into the other, and do not use a decision record to settle a definition that the glossary should carry.

## Use it inside the work

Apply this method during [refine](../refine/SKILL.md) when acceptance depends on a term, during [design](../design/SKILL.md) when options change the model, and during a grilling interview when the user's answers expose a boundary. The sharpened language should appear in requirement names, acceptance criteria, interface contracts and tests.

Stop when the terms that could change behavior or a decision are defined, checked against evidence and recorded in their existing home. Do not chase every synonym or produce a taxonomy the project will not use. Read [terminology notes](references/terminology.md) for sharper prompts, recording triggers and examples.
