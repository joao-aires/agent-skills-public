# Concept explanation in a document

Some documents report facts; others must leave the reader with a model they can use. A PRD explains why an outcome matters, an architecture overview explains how responsibilities connect, an ADR explains why a decision followed from its constraints, and a how-to may need one paragraph of mechanism before a step that would otherwise look arbitrary.

This reference is about embedding explanation in a document. For the live act of explaining a concept to a reader, including quick intuition and misconception repair, use the [explain](../../explain/SKILL.md) skill. For document-wide structure, precision and presentation, stay with [technical writing](../SKILL.md).

## Find the load-bearing idea

Before drafting, name the one distinction that changes how the reader predicts or decides. Common forms:

- a boundary: what this component owns and what it does not;
- an invariant: what stays true across every operation;
- a causal link: why this step must precede that one;
- a tradeoff: what the chosen option makes easier and what it makes harder;
- a lifecycle: which states exist and which transitions are legal.

If you cannot state the load-bearing idea in one sentence, the document does not yet have an explanation. It may have a topic, a history or an inventory. Write the sentence first and organize the section around it.

Test the sentence against a reader question. "Why does the queue exist?" should produce something more specific than "to handle messages." A useful version names the problem: "The queue absorbs bursts so the worker can retry without blocking the request path." Now the reader has a model that predicts where latency and duplication can appear.

## Define terms where they become necessary

Define a term at its first useful occurrence, not in a glossary at the end unless the document is a reference. A definition that arrives before the reader has a use for it is easy to skip; one that arrives after the reader is already confused is too late.

A working definition has four parts when the term is consequential:

1. the name, spelled and capitalized consistently afterward;
2. what it is, in the reader's vocabulary;
3. what it is not, or which nearby term it is often confused with;
4. one example or a pointer to one.

Expand acronyms at first use. Keep the expanded form and the acronym together once, then use the shorter form. Do not rename an established domain term to make the prose sound simpler; explain the term instead.

A definition by role is usually more useful than a definition by mechanism: "the scheduler decides which job runs next" tells the reader what to expect from the component before the algorithm arrives.

## Build a mental model

A mental model names the entities, their relationships, the state that changes and the forces that change it. Start from a model the reader already has, then add only the distinctions the document needs.

For a system, prefer one real path over a layer inventory:

- an entry point the reader recognizes;
- the first owner that accepts or rejects the work;
- the state that is created or changed;
- the boundary where failure becomes visible;
- the result the caller or user observes.

For a decision, prefer the constraint over the org chart: what made the previous approach insufficient, which option relieves that constraint, and what new cost it introduces.

For a data model, prefer the lifecycle over the schema dump: which states exist, who may move an item between them, and what happens to concurrent readers or writers.

State what the model omits. A model that silently ignores replication, permissions or retries will produce confident wrong predictions at exactly the boundary the document was meant to clarify.

## Use analogies with limits

An analogy borrows structure from something the reader already understands. It works when it maps relationships, not just names, and when the document says where the mapping stops.

A useful analogy sentence has three parts:

> A cache is like a pantry beside the shop: it shortens the trip for common items, but unlike a pantry it can serve a stale copy after the shop changes.

The first clause maps the benefit, the second maps the mechanism, and the third states the limit that matters for the reader's decision. Without the limit, the analogy teaches a model that fails on consistency.

Keep one analogy per idea. If a second analogy is needed to repair the first, replace the first. Retire the analogy explicitly when the mechanism takes over: "From here, the pantry picture is no longer useful; the cache has an eviction policy and a source of truth."

Never let an analogy carry a safety, security, legal or numeric claim. "Like a locked door" does not establish an access-control guarantee, and "like a highway" does not establish a latency bound.

## Show a worked example

An example makes an abstract rule checkable. It should be small enough to hold in working memory and concrete enough that the reader can predict a nearby case.

Include:

- the starting state and the relevant inputs;
- the action or event;
- the state change and the observed result;
- one decision or failure point;
- a note on what the example does not cover.

Use synthetic data and label it. Keep placeholders visible. If the example is executable, state the prerequisite and whether it was run; if it is illustrative, say so. Do not let an example introduce a rule that the surrounding text never states.

A contrast pair is often stronger than a single trace: the same input under two configurations, with the different result explained by one variable. A counterexample is stronger still when the document is correcting a plausible misconception.

## Keep a clean reasoning line

For a decision or recommendation, the reader should be able to follow one line without reconstructing the meeting:

1. **Situation.** The constraint, observed problem or changed condition.
2. **Choice.** The selected direction, stated plainly.
3. **Reason.** Why this choice relieves the situation better than the alternatives.
4. **Consequence.** What becomes easier, harder, slower or riskier.
5. **Reversal condition.** What evidence or change would justify revisiting the choice.

Keep facts, interpretations and proposals distinguishable. A measured latency is a fact; "the database is the bottleneck" is an interpretation; "add a read replica" is a proposal. If the historical rationale is unknown, say so and link the decision record rather than inventing a coherent story.

Do not hide the losing option's advantage. A recommendation that admits a real cost is easier to trust and easier to revisit than one that presents the choice as obvious.

## Present tradeoffs without false balance

Compare alternatives on dimensions the reader cares about, using the same dimensions for every option. Useful columns include what the option optimizes, what it sacrifices, its failure behavior and the condition under which it wins.

State shared constraints outside the table. Say when options compose, when one is a subset of another, and when the real decision is about sequencing rather than selection. A table with three rows implies three comparable choices; do not use it to make a predetermined option look empirically selected.

False balance is also a failure. If one option is unsafe or incompatible with an accepted constraint, say that directly rather than giving it a symmetrical row. The goal is a decision the reader can act on, not the appearance of neutrality.

## Repair common misconceptions

A misconception is usually a reasonable model applied outside its range. Name it before correcting it:

- "It is tempting to read the retry as a second request; the server treats it as the same request only when the key matches."
- "The component is often described as stateless; it keeps a per-request cache, which is why two identical calls can differ."

Then show the discriminating case, replace the model and re-ask the original question. Avoid opening with a correction list; the reader needs to see why the old model predicted the wrong result. Do not strawman the misconception into something no competent reader believed.

## Decide where the explanation belongs

Explanation competes with the document's primary job. Place it where it changes the reader's next action:

- **Before a procedure** when the step would otherwise look arbitrary or unsafe.
- **After a summary** when the reader needs orientation before detail.
- **In a linked explanation document** when the depth would overwhelm a reference or runbook.
- **In the decision record** when the reasoning is durable and the proposal is temporary.

Do not interrupt a runbook with history the responder cannot use under pressure; link it. Do not bury a prerequisite in an explanation section the operator may skip. Keep the short version at the point of use and the full version behind a visible trigger.

Explanation should not absorb instruction or reference. If the section starts listing every option or every command, move that material to its proper type and link it.

## Review

- Can the reader state the load-bearing idea after one reading?
- Are terms defined before they are relied on, and used consistently afterward?
- Does the model name entities, state and change rather than only components?
- Does every analogy state where it breaks?
- Does the example test the rule rather than merely illustrate it?
- Can the reader follow the reasoning line from situation to reversal condition?
- Are facts, interpretations, proposals and unknowns distinguishable?
- Does the explanation change the reader's next action, or is it self-indulgent depth?
- Is the depth in the right place, with the short version where the reader needs it?

## Sources and fit

This reference is original guidance informed by [Diátaxis: Explanation](https://diataxis.fr/explanation/) for understanding-oriented, bounded explanation with alternatives and perspective; [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience, scope and compare-and-contrast openings; and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) for examples, consistency and current content.

The four-part definition, reasoning line and misconception repair are local method. The artifact contract and domain guide still decide whether the explanation belongs in the document at all.
