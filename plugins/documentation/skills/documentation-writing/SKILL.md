---
name: documentation-writing
description: Write and review clear, accurate, useful product and engineering
  documentation, including PRDs, requirements, architecture, decisions, feature
  specifications and operational guides. Use for new documents and substantive
  documentation revisions, adapting explanations, examples and presentation to readers.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

Read [composition guidance](../../COMPOSITION.md) for scope and invocation boundaries.

# Write useful project documentation

Help the intended reader understand, decide or act correctly. Readability and navigation support that outcome; brevity or scanability alone does not establish quality. Preserve the project's vocabulary, language, document responsibilities and accepted decisions. A writing request does not authorize changing the product, restructuring folders or implementing a proposal.

## Establish purpose and sufficient context

Identify the reader, what they already know and what they need from this document. Use existing context instead of repeating settled interviews. Ask only about gaps that affect meaning or correctness; do not require an outline approval for routine authorized revisions.

Choose the dominant purpose using Diátaxis where it helps:

| Purpose | Reader needs | Writing emphasis |
| --- | --- | --- |
| Tutorial | Learn through a bounded exercise | Prerequisites, guided progress and a visible result |
| How-to / runbook | Complete a specific task | Ordered actions, verification, failure handling and recovery |
| Reference | Look up precise facts | Consistent terminology, contracts, units, defaults and exceptions |
| Explanation | Understand how and why | Mental model, relationships, rationale, consequences and examples |

PRDs, design proposals and decision records also need their own product/decision conventions. Do not force them into a four-folder taxonomy. An architecture overview usually explains the system and links detailed reference and operational instructions.

Open with the subject, useful scope and relevant status. Supply the background a new reader needs without reproducing another document. Define unfamiliar acronyms and domain distinctions before relying on them. Keep editorial dates separate from implementation reviews.

## Explain the subject, not just its inventory

Build from the reader's question to the answer. For systems, connect responsibilities, data flow, ownership and failure boundaries. Explain why a distinction matters and what follows from it; a component list alone rarely teaches the design.

For consequential choices, state the reason, relevant alternative and tradeoff supported by evidence. If rationale is unknown, mark the gap or link the decision record; do not invent historical intent. Requirements describe the needed outcome and observable acceptance, not merely preferred technology.

Include a small concrete example when an abstract rule is easy to misread. State the starting condition, action and resulting state. Examples illustrate rules; they do not establish new requirements or imply unavailable capabilities. Use synthetic data. Keep runnable examples complete enough for their stated purpose, identify placeholders and prerequisites, and report whether execution was actually verified.

## Make the text coherent and easy to navigate

Use descriptive sentence-case headings for independently useful topics, with a short contents list when it helps a long reference. Group related detail and build concepts in a logical order. Avoid a heading per sentence, fixed section counts or lists that break causal reasoning.

Lead a paragraph with its point, then develop the explanation. Split when the subject changes; do not remove necessary context to meet a word limit. Name the actor and action, use familiar language, and retain precise domain terms. Avoid unexplained shorthand, vague pronouns, decorative emphasis and unsupported adjectives such as “secure” or “seamless”.

Use bullets for parallel facts, numbers for dependent steps and compact tables for comparisons with consistent columns. Keep conditions and exceptions attached to their rule. Diagrams should show relationships or sequences that prose alone obscures; explain their meaning and provide a text equivalent where needed. Link with descriptive labels. Never rely solely on colour or visual layout to convey a boundary.

## Preserve precision and trust

Keep identifiers, units, quantities, conditions, negative cases and source links exact. Distinguish facts, interpretation, assumptions, proposals, approvals and verified results. Configuration is not deployment evidence, a draft is not a committed write, and reformatting is not a new implementation audit.

For existing docs, compare against source material before and after rewriting. Resolve contradictions against the authoritative contract/code within scope, or identify an unresolved discrepancy; do not smooth it over. Leave generated blocks intact unless updating their generator is authorized. Avoid duplicating a canonical schema or requirements baseline.

For operational instructions, preserve safety prerequisites, expected results and recovery limits beside the affected action. Keep secrets and sensitive payloads out of examples. Do not invent targets, owners or supplier/legal assurances to make a document appear complete.

## Review usefulness, not just formatting

Check a few realistic reader questions against the finished document: can a new contributor explain the main flow and authority boundary, can a decision-maker understand the choice and open conditions, or can an operator perform and verify the task? Review for missing prerequisites, undefined terms, ambiguous references, contradictions and misleading examples. Fix substantive gaps before polishing headings.

A manual reader-question review is sufficient for ordinary edits. A fresh reader or authorized independent agent can help for consequential documents; do not claim independent testing when only the author reviewed it. Use proportionate link, example, schema and command checks. Packaging and Markdown checks do not establish comprehension or factual correctness.

Apply `humanizer` for natural wording when available, preserving necessary explanation and useful structure. Report which documents changed and any unresolved evidence gaps; do not manufacture a complete rewrite of unrelated or historical material.

## Sources and fit

This is original project-writing guidance informed by [Diátaxis](https://diataxis.fr/), [Google's audience guidance](https://developers.google.com/tech-writing/one/audience) and [document guidance](https://developers.google.com/tech-writing/one/documents). Reviewed skills: [Anthropic doc-coauthoring](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/doc-coauthoring/SKILL.md) for context and reader review, and [GitHub documentation-writer](https://github.com/github/awesome-copilot/blob/8bc0f5715b2ddc7901a62fddf144ded30d56de8b/skills/documentation-writer/SKILL.md) for purpose, accuracy and consistency. Their mandatory collaboration/approval workflows are not imported. Source evaluation is in the repository's maintainer reference.
