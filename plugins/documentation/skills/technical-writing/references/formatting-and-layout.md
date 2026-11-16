# Formatting and layout: choose the form from the reader's job

Presentation is part of the argument. A table invites comparison; a numbered list asserts sequence; prose carries causality; a diagram shows relationships that sentences must otherwise trace twice. Formatting failures are often reasoning failures in disguise: a list that hides a dependency, a table whose rows are not comparable, or a diagram that decorates rather than explains.

## Choose the form

| Form | Use when | Avoid when | Check |
| --- | --- | --- | --- |
| Prose | Context, causality, tradeoffs, a recommendation that needs its reasoning | The reader needs to compare or execute | One point per paragraph; the first sentence carries it |
| Bullets | Parallel facts, criteria or options with conditions attached | Order matters, or the items form a causal chain | Items are peers and share a grammatical shape |
| Numbered steps | Actions with real dependencies, or a ranked order | The order is arbitrary or unknown | Each step has an observable result; verification follows a group |
| Table | Comparison on consistent dimensions, defaults, status matrices | Cells need long prose, nested lists or different dimensions | Headers name the dimension; rows are genuinely comparable |
| Diagram | Relationships, sequence, state or boundaries that prose obscures | The information is a list, a table or decoration | Text explains what to see; a text equivalent exists |
| Callout | A consequence, prerequisite or exception that is easy to miss | Every paragraph is emphasized | The label states the meaning, not the decoration |
| Code block | Exact commands, configuration, payloads or output | The point is conceptual rather than literal | Language tag, runnable from the stated starting point, secrets removed |

A document may need several forms. Do not force one form across a whole artifact because it is easier to generate.

### Prose versus bullets

Convert prose to bullets when the content is genuinely parallel: three prerequisites, four supported platforms, five failure modes under one rule. Keep prose when the reader needs to follow why one fact implies the next. A bulleted causal chain hides the connection the reader came for.

Attach conditions and exceptions to the item they qualify. A note after the list that changes two of five items is easy to miss. If most items carry a different condition, use a table or split the list.

### Bullets versus numbered steps

Numbering is a claim about order. Use it when the reader must do A before B, or when priority matters. Do not number a list of concerns to make it look procedural. Conversely, do not bullet a sequence whose steps depend on the previous result.

For long procedures, group steps under descriptive headings and put verification after each group. A single list of forty steps is difficult to resume after an interruption.

### Tables versus prose

Use a table when the reader will compare cells across a shared dimension. Put the dimension in the header, not in every cell. Keep shared prerequisites outside the table so they visibly apply to every row.

Do not use a table for unrelated facts, for cells containing paragraphs, or for accessibility-sensitive layouts that break on a narrow viewport. If a table needs a legend for each column, prose may be clearer. Long identifiers and commands can force horizontal scrolling; consider a definition list or one short block per item.

### Diagrams versus text

A diagram earns its space when relationships are the hard part: sequence, ownership, state transitions, trust boundaries, data flow. Label the parts with the same names used in the text. State the question the diagram answers and the main thing to notice.

Provide a text equivalent for essential information. A screenshot of a terminal is not a substitute for the command and its output; an architecture image needs a short textual description of the elements and flow. Do not use colour alone to distinguish a boundary or status.

## Headings and order

- Use sentence case for titles and section headings unless the project's style guide says otherwise.
- Make headings descriptive and independently meaningful. "Retry behavior" is easier to find than "More details".
- Keep a logical hierarchy; do not skip levels for visual size.
- Build concepts before relying on them. A reader who lands mid-document should still find the local prerequisite.
- Use a contents list for a long reference or a document with several independent entry points.
- Avoid a heading per sentence, fixed section counts and headings that merely restate the title.
- Keep anchors stable when links point to them; rename the label and the anchor target together.

## Callouts and emphasis

Use a callout for a consequence the reader could reasonably miss: data loss, a required permission, a version limit, a safety stop. Label it by meaning, such as **Before you start**, **Warning** or **Note**, rather than by colour or icon alone.

Do not put the only copy of an essential instruction in a callout that a reader may skip while scanning. Callouts supplement the flow; they do not replace the step. Avoid stacking several callouts, and do not use them for ordinary emphasis.

Bold sparingly: UI labels, a key term at first definition, or the decisive word in a comparison. Italics suit gentle emphasis or a title, not structure. Code font is for identifiers, commands, paths and literal values. Avoid all caps, decorative emoji as status and emphasis that substitutes for a reason.

## Code and commands

- Tag fenced blocks with the language or shell.
- Show the command the reader will actually type, including the working directory when it matters.
- Put expected output in a separate block and say whether it was observed or is illustrative.
- Mark placeholders clearly, for example `<project-id>`, and say how to obtain them.
- Keep secrets, tokens and personal data out of examples.
- Pin versions where behavior differs, or state the supported range.
- Do not present an unexecuted command as verified. "Expected output" is a claim the author must qualify.

## Links

Use descriptive link text that makes sense out of context. Link to the authority for detail instead of copying it, and link once at the point where the reader needs it. In a repository, prefer verified relative paths; for external material, use the canonical URL and say when access is required.

Check that links resolve in the publication context, including anchors. Do not rely on colour to signal a link. Avoid "click here", "this page" and bare URLs used as sentences. When a whole sentence is the link, the reader cannot tell where it goes without reading the surrounding text.

## Accessibility and rendering

- Give images and diagrams meaningful alternative text; describe the purpose, not the file.
- Use real heading levels, list structures and table headers rather than visual formatting that imitates them.
- Keep link text understandable when read alone.
- Do not encode meaning in colour, position or an icon without a textual equivalent.
- Provide captions or transcripts for audio and video, and text for information shown only in an image.
- Use plain language and expand acronyms at first use, especially in safety or decision content.
- Check the rendered view at a narrow width and in the target theme. Tables, long code lines and wide diagrams are common breakages.
- Verify copyable commands, relative paths and images at the current revision.

## Progressive disclosure

Lead with the answer, then disclose depth. A summary, a decision and the next action belong on the first screen; detailed evidence, edge cases and historical alternatives can follow or sit behind a link.

Use a linked reference when the detail is substantial and conditional. Keep the trigger visible: "Read the migration guide if you already run version 2" tells the reader whether to follow the link. A bare "see docs" does not.

Do not hide prerequisites, safety stops or breaking changes behind a collapsed section or a second document. Disclosure is for optional depth, not for the conditions that make the main path safe.

## Review

Read the rendered document, not only the source:

- Does each form match the reader's job, or is it decoration?
- Can a reader scan the headings and predict what each section answers?
- Do tables fit, and do lists preserve dependencies?
- Are code blocks copyable, complete and free of secrets?
- Do links resolve, and does their text explain the destination?
- Is any meaning available only through colour, layout or an image?
- Does the first screen answer the reader's first question?

Fix a structural mismatch before polishing spacing or wording.

## Sources and fit

This reference is original guidance informed by the [Google developer documentation style guide highlights](https://developers.google.com/style/highlights) for sentence case, list types, descriptive links and accessible images; [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience-driven organization; [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/#skimmable) for skimmable structure and examples; and [Diátaxis](https://diataxis.fr/) for keeping instruction, reference and explanation in their appropriate forms.

The decision rules and review checks are local synthesis. Project style guides and the artifact contract take precedence where they specify a format.
