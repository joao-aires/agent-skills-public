# Terminology notes: sharpen, test, record

Read this when a term is contested, when the design keeps sliding between meanings, or when you need to decide whether a glossary entry or a decision record is warranted. The [domain modeling method](../SKILL.md) owns the sequence; the artifact system owns the glossary artifact and the decision record contract.

## Term-sharpening prompts

Ask these about the specific word in the sentence that was just used, not about the domain in general.

- **Actor and action.** Who uses the term, and what do they do with it? A term used by an operator, a customer and an API client may name three different things.
- **Kind.** Is it an entity, role, event, state, policy, measurement or container? Mixing kinds is a common source of drift.
- **Boundary.** What is included, what is excluded and what is the nearest neighboring term? "Suspended" is only useful if it differs from "inactive" and "blocked".
- **Evidence.** Which code identifier, schema field, UI label, API name or accepted decision claims the same idea? Read it before proposing a definition.
- **Consequence.** Which requirement, state transition, permission or test changes if the term is read differently? If none, the term may not be load-bearing.
- **Definition.** Can you state it in one sentence a new contributor can apply, plus one example and one non-example?
- **Stability.** Is this a project term, a platform term or a regulated term? Do not redefine a term the platform or regulation already owns.

Put the proposed definition back into the user's sentence. If the sentence becomes clearer and the edge case becomes answerable, the term is probably right.

## Edge-scenario prompts

Definitions fail at boundaries. Pick the scenarios that the affected behavior can actually reach.

- **Partial success.** The first step committed; the second failed. Is the thing still "created", "pending" or "failed"?
- **Duplicate and retry.** The same request arrives twice. Does the second one create a new entity, return the first result or get rejected?
- **Concurrency.** Two actors change the same state at once. Which term describes the losing result?
- **Authority change.** The owner loses permission while work is pending. Does the entity become inaccessible, transferred or frozen?
- **Deletion and retention.** Is removal immediate, scheduled, reversible or only hidden from one view? What happens to exports, backups and legal holds?
- **Legacy and migration.** A record created under the old rule is read under the new one. Which term applies, and what does the actor see?
- **Time.** Does the term depend on a time zone, billing period, deadline or grace window?
- **Empty and absent.** Is "no record" different from "record with no value", "never activated" or "not applicable"?
- **Quantity and money.** Does rounding, currency, unit or proration change the meaning?
- **Cancellation.** Is it a request, a completed reversal, a partial stop or a future prevention?

For each scenario, ask: which term applies, what does the actor observe, and which obligation follows? If two people answer differently, the model is not settled.

## Glossary and decision triggers

Record the smallest artifact that carries the resolution.

| Situation | Record |
| --- | --- |
| A term with one agreed meaning is reused across requirements, design, code or support | One glossary entry in the project's existing glossary home, with the boundary and an example |
| A rule, transition, permission or quality obligation follows from the term | The ECR, design record or requirements; link the term rather than turning the glossary into a specification |
| An accepted choice is hard to reverse, surprising without context and the result of a real trade-off | An ADR or PDR using the local [decision record contract](../../artifact-system/references/contracts/adr.md) and [ADR guide](../../guide-adr/SKILL.md) |
| The choice is reversible, obvious or had no credible alternative | The design record, ECR or code comment; no separate decision record |
| Code, documentation and the stated model disagree | Investigate and correct the authority that is wrong; do not record the contradiction as a new term |
| No glossary home exists and creating one is not authorized | Report the proposed entry and suggested home; do not invent a file layout |

The glossary owns terminology, not rationale. The decision record owns the accepted choice and its consequences. Do not copy one into the other.

A decision record is not a naming log. "We chose `workspace` over `team`" is a glossary decision unless the choice carries a hard-to-reverse boundary, migration or permissions consequence.

## Anti-patterns

- **Glossary as specification** — burying state transitions, permissions or acceptance rules in a definition.
- **Definition without a user** — inventing terms no requirement, interface or support conversation will use.
- **Rename without migration** — changing the language while code, data, APIs and tests keep the old name and no mapping exists.
- **Silent correction** — rewriting the user's term without saying which meaning you chose.
- **Taxonomy for a small project** — introducing bounded contexts, maps and a glossary tree when one context and one page suffice.
- **Decision inflation** — writing an ADR for every naming choice, making the durable record noisy and untrustworthy.
- **Format imposition** — requiring a root `GLOSSARY.md`, `docs/adr/` or a fixed one-paragraph record regardless of the project.
- **Authority by convenience** — treating the newest document as correct when the code or an accepted decision is the actual authority.
- **Synonym chase** — polishing words that cannot change behavior while the load-bearing boundary remains unresolved.

## Worked example: delete, archive and purge

The team says "delete the workspace". The code marks it inactive, keeps the data for 30 days and allows restore; the interface says "permanently deleted"; an operator expects immediate removal.

**Sharpen.** "Delete" is doing three jobs: the actor's request to remove the workspace from active use, the scheduled irreversible removal, and the read-only retention option. The boundary question is what the actor can still do after each step.

**Test.** After a delete request, can the owner restore it? Can an admin still export it? What happens to a pending invitation or an active integration? Does a legal hold stop the purge? The answers distinguish three states and expose a permission the interface never named.

**Resolve.** Record three glossary terms in the existing home: **archive** (actor-chosen read-only retention), **delete request** (removal from active use, restorable during the retention window) and **purge** (irreversible removal after the window or an authorized exception). Keep the retention rule and the permission behavior in the design or requirements.

**Decide.** The retention period and the purge guarantee are hard to reverse, surprising to a future maintainer and traded off against recovery and legal obligations. They warrant a decision record through the local contract. The button label change alone does not.
