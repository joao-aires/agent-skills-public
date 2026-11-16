# Document types: the shape before the sections

A document type is a promise to a reader about what kind of help they will get. The same facts can be a reference entry, a how-to, an explanation or a decision record; the type determines where the reader starts, how they scan and what counts as complete.

Use this reference to recognize a common shape, choose its first section and avoid category errors. It is not a contract. For governed artifacts, the artifact system and its guide own required content, status, evidence and home; a local project convention may narrow or extend the shape. The table below describes the cross-type minimum that makes the document usable.

## Common types

| Type | First section | Mandatory sections | Format | Common failure |
| --- | --- | --- | --- | --- |
| README | One paragraph: purpose, audience, status and outcome | Quickstart; what it does; documentation map; development; support and contribution; status and limits; license | Short Markdown; copyable commands; links to authorities | Vision without a working start |
| PRD or product brief | The problem and promised outcome, for whom and why now | Users and problem; outcomes and success measures; scope and non-scope; requirements; assumptions and risks; open decisions | Narrative for judgment, tables for comparison, links to evidence | A feature list with no outcome or owner |
| RFC | The proposal in one paragraph, the decision requested and the response date | Context; proposal; alternatives; impact and risks; open questions; decision | Numbered sections, stable anchors, reviewable rationale | A design document with no explicit ask |
| ADR or PDR | The decision, its status and its date | Context; decision; alternatives considered; consequences; supersession link when replaced | One page, durable, immutable after acceptance | Meeting notes or a second design document |
| ECR | The change, its scope, its status and the affected components | Why; requirements; design; plan; verification evidence; history | Evolving record; claims tied to revisions | Duplicating the issue or PR, or claiming evidence it does not have |
| Runbook | When to use it, the impact and any safety stop | Prerequisites and access; symptoms; steps; verification; rollback or recovery; escalation | Numbered, scannable, copyable; expected output beside each check | Commands without a result or a recovery path |
| How-to | The outcome and its prerequisites | Steps; check of the result; common failures; next step | One task path; branches only where they change the action | A tutorial that teaches instead of completing the task |
| Reference | Scope and the lookup model | Complete entries; types, defaults and errors; version or applicability; examples | Consistent entries or tables; stable names and anchors | Partial coverage presented as complete |
| Explanation | The question and a one-sentence intuition | Context; mental model; mechanism; example; boundaries; alternatives | Prose, diagrams and a worked example | Instructions or reference material in disguise |
| Release note | What shipped, who is affected and what action is required | Changes; breaking or migration notes; verification; known issues; rollback | Grouped by audience or impact; versioned and dated | A commit list or a marketing announcement |
| Architecture overview | The system's purpose, boundary and key quality constraints | Context; elements and responsibilities; runtime flows; data; interfaces; deployment; decision links | Views plus explanatory text; detail linked, not duplicated | Boxes without ownership, flow or failure boundaries |
| Contribution guide | Who can contribute and the fastest working path | Setup; workflow; standards; review; commit and PR expectations; reporting route; license or DCO terms | Task steps plus links to policy | A policy wall with no runnable setup |
| Incident record or postmortem | Impact, duration and current status | Timeline; detection; cause and contributing conditions; recovery; what went well or badly; actions and owners | Blameless, timestamped, linked to evidence and logs | Blame, or a timeline with no decisions |

## Choose between near neighbours

Several types share vocabulary but answer different questions.

- **PRD, RFC, design proposal, ADR and ECR.** A PRD owns product intent and outcomes. An RFC asks a named audience for a decision on a consequential proposal. A design proposal compares options and recommends a direction. An ADR records one accepted decision for the future. An ECR coordinates one change through requirements, design, plan and evidence. If a document is doing two of these jobs, split it or link the other authority rather than growing one hybrid.
- **Tutorial, how-to and runbook.** A tutorial teaches through a bounded exercise. A how-to completes a task the reader already intends to do. A runbook is executed under pressure and needs verification, recovery and escalation. A runbook that teaches background delays the responder; a tutorial that assumes production access is unsafe.
- **Reference, explanation and architecture overview.** Reference is for lookup, explanation is for understanding, and an architecture overview explains the implemented system at a level that connects the two. Reference completeness and explanatory depth are different tests; neither substitutes for the other.
- **Incident record and postmortem.** The incident record is the durable account of impact and response while it matters. The postmortem is the later learning document about cause, conditions and prevention. Do not make the live record carry speculative causes, or the postmortem omit the evidence the record preserved.

## First section by reader mode

The first section should match how the reader arrived:

- **Scanning for fit:** state what this is, who it is for, what changed or what it costs. README, PRD, release note.
- **Deciding:** state the question, the recommendation and the condition that would change it. RFC, ADR, design proposal.
- **Executing:** state when to use the procedure, the prerequisite and the safety stop. Runbook, how-to.
- **Looking up:** state the scope and the naming or version rule. Reference.
- **Learning:** state the question and the smallest useful intuition. Explanation, architecture overview.

A document can serve more than one mode, but the first screen cannot. Choose the dominant mode and link the others.

## Format follows the reader's job

| Reader job | Useful form | Poor form |
| --- | --- | --- |
| Understand a causal chain | Connected prose and a diagram with explanation | A bullet list of components |
| Compare options | A table with shared dimensions | Three prose sections with different criteria |
| Execute under pressure | Numbered steps, expected output, recovery | Long background before the first action |
| Look up a fact | Consistent entries and anchors | Narrative that buries the value |
| Decide | Recommendation, alternatives, consequences, reversal signal | A neutral survey with no recommendation |
| Adopt a practice | A worked example plus the rule | A policy statement alone |

## What every type still needs

Regardless of shape, a usable document supplies self-contained context, a clear scope boundary, defined terms, evidence for its claims, resolvable links and an honest status. The artifact quality bar owns those shared properties; this reference does not restate its thresholds.

## Sources and fit

This reference is original guidance informed by [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for scope, audience and opening summary; [Diátaxis](https://diataxis.fr/) for the tutorial, how-to, reference and explanation distinction; [Write the Docs: how to write software documentation](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/) for entry-level coverage; and [GitHub: about READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) for the README's reader questions.

The RFC shape is informed by [RFC 7322](https://www.rfc-editor.org/rfc/rfc7322), the ADR shape by the [ADR community material](https://adr.github.io/), runbook and incident practice by the [Google SRE book](https://sre.google/sre-book/table-of-contents/), and release-note practice by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). These are reference points for reader expectations, not mandatory local templates. The repository's artifact contracts take precedence where they apply.
