# Review rubric: does the document do its job?

Use this rubric before handoff, after the draft is structurally complete. It reviews writing craft; it does not replace the artifact contract, cross-artifact assurance, code review or factual verification by the owner of the subject.

Read the document once as its intended reader, without editing. Then review against the dimensions below, recording only findings that affect the reader's ability to understand, decide or act. A short document can pass; a long one can fail. Counts of sections, words or links are not evidence of quality.

## Reader questions

| Reader | Questions they need answered | Passing evidence |
| --- | --- | --- |
| Newcomer | What is this, why does it exist, is it for me, where do I start? | The first screen answers without requiring another document |
| Decision-maker | What is proposed or decided, what does it cost, what would change it? | The choice, alternatives and reversal condition are visible |
| Operator | When do I act, what do I need, how do I verify, how do I recover? | Prerequisites, expected result and failure path sit beside the action |
| Maintainer | What is authoritative, what changed, what remains open, who owns it? | Status, evidence, links and next action are explicit |
| Returning reader | What is still true at this revision? | Dates, versions, status and supersession are unambiguous |

If a reader must open another artifact to understand the core claim, the section is an index, not an answer. Keep the summary here and link the detail.

## Structure

- Does the opening state subject, purpose, audience and scope, including what is out of scope?
- Does the document follow the reader's question order rather than the author's discovery order?
- Are concepts introduced before they are relied on?
- Do headings describe their sections in sentence case and form a usable outline?
- Is there one authoritative account of each concern, with views linked rather than duplicated?
- Is the length proportionate to the decision or action, with optional depth disclosed?
- Can a reader resume after an interruption and find the next action?

A missing non-scope is a real gap when readers would reasonably expect coverage that is absent. A scope statement that excludes obviously unrelated topics adds nothing.

## Style

- Is the point at the start of the paragraph, followed by its reasoning?
- Are actors and actions named, with active voice where it clarifies responsibility?
- Is the reader addressed consistently, without shifts between "you", "we" and an unnamed operator?
- Are terms, capitalization and units consistent after definition?
- Is unfamiliar jargon defined, while precise domain terms are retained once explained?
- Are claims free of unsupported adjectives such as "seamless", "robust", "secure" or "production-ready"?
- Are emphasis, bolding, callouts and emoji doing real work rather than decorating?
- Does the tone suit the artifact: concise for a runbook, evidence-based for a decision, patient for a tutorial?

Do not reward brevity that removes necessary context, or formality that hides the actor. Style review is about clarity and trust, not adherence to a house aesthetic the project has not adopted.

## Content

- Does each required section answer its reader question with substance?
- Are prerequisites, permissions, versions and environment stated before they are needed?
- Are failure, denial, empty, partial and recovery paths covered where the reader will meet them?
- Are requirements stated as outcomes and observable acceptance rather than preferred technology?
- Are examples complete enough for their stated purpose, with placeholders and prerequisites marked?
- Are edge cases and known limitations stated rather than implied?
- Does the document distinguish current state, proposal, decision and implemented behavior?
- Is any claim about behavior backed by a command, scenario, revision or link, rather than assertion?

Check the document against its source material, not only against its own outline. Resolve contradictions with the authoritative contract or code within scope, or record the discrepancy as unresolved.

## Evidence

- Does the document state its maturity or status when the artifact requires it?
- Is each phase-specific claim supported at the right level: proposed has rationale, accepted has a decision owner, implemented has a revision, verified has an observed result?
- Are evidence claims in the past tense and tied to a revision, environment or scenario?
- Is it clear what was observed, what was assumed and what remains unknown?
- Are numbers, benchmarks and timelines sourced or labeled as estimates?
- Is a future intention presented as a plan rather than a result?
- Are generated summaries, drafts or simulations distinguished from verified behavior?

A claim that cannot be inspected is a liability. If verification was not performed, say so; do not let confident prose imply it.

## Links

- Do all relative links and anchors resolve at the current revision?
- Do external links point to the canonical owner or primary source?
- Does link text describe the destination when read out of context?
- Is access required for a linked resource stated, especially for private or workspace-only material?
- Are revisions identified by a resolvable link or an explicit local-only label rather than a bare hash?
- Is the document linking for depth rather than using a link in place of its core answer?
- Are images and diagrams present, rendering and accompanied by a text equivalent?

Check links in the publication context. A link that works in the editor but breaks on the rendered site is still broken.

## Accessibility

- Do headings form a real hierarchy rather than visually styled text?
- Do images and diagrams have meaningful alternative text or an adjacent description?
- Are tables used for comparison, with real headers and a readable narrow-width layout?
- Is meaning conveyed by more than colour, position or an icon?
- Is link text understandable without the surrounding sentence?
- Are acronyms expanded and language kept plain where the reader may be new to the domain?
- Do code blocks wrap or scroll without hiding critical content?
- Are audio and video captioned or transcribed when they carry required information?

Accessibility review covers the rendered artifact, including diagrams and screenshots that were pasted in as images.

## Severity and output

Separate findings by consequence:

| Severity | Meaning | Examples |
| --- | --- | --- |
| Blocker | The reader cannot understand, decide or act correctly | Missing prerequisite, contradictory status, unsafe step, unverifiable core claim |
| Should fix | The reader can proceed but is likely to misread or waste time | Undefined term, buried decision, broken link, misleading example |
| Polish | The meaning survives; the reading experience does not | Inconsistent capitalization, awkward heading, uneven spacing |

Report each finding with its location, the reader consequence and the smallest fix. Do not rewrite the document inside the review unless asked. State what was checked and what was not: a craft review does not establish factual correctness, independent user comprehension or production readiness.

## Sources and fit

This rubric is original guidance informed by [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience, scope, summary and document organization; the [Google developer documentation style guide](https://developers.google.com/style/highlights) for sentence case, list choice, descriptive links and accessible images; [Diátaxis](https://diataxis.fr/) for distinguishing instruction, reference, explanation and tutorial; and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) for skimmable, exemplary, consistent and current content.

The severity model and reader table are local to this repository. Where the artifact contract or quality bar defines a hard failure, that definition wins.
