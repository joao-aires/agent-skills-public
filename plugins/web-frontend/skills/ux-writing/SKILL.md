---
name: ux-writing
description: Review, write or harmonize interface labels, instructions, validation, errors, empty states and confirmations in their task context. Use directly for UI copy or during relevant design and implementation; preserve product behavior, established voice, localization and consequential meaning.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Write interface copy for the actual task

Use the requested scope and mode: review proposes changes without editing; rewrite or implementation applies the authorized copy changes; harmonization aligns recurring terms within the named surfaces. Supporting an existing design/development task does not authorize a broader rebrand. Use [interaction design](../interaction-design/SKILL.md) for the underlying flow and [interface quality](../interface-quality/SKILL.md) for rendered fit.

## Understand the action before the sentence

Read the complete affected flow, adjacent states and existing terminology/voice. Identify who is reading, what they are trying to do, what the system actually permits, the stakes and the next available action. Distinguish user-facing text from sample data, annotations and internal names. Reuse accepted vocabulary; do not invent personas, research, features, prices, policies, guarantees or response times to fill a mockup.

If unclear behavior changes the meaning, investigate code/contracts or ask the unresolved product question. Preserve the consequence of consent, payment, security, sharing and deletion. Do not make a sensitive action sound harmless or imply success before the authoritative system confirms it. A copy task cannot silently redesign permissions or recovery behavior.

Match the recommended default to the authoritative state. Queue acceptance is not evidence that processing started or completed; use queued/pending language until the corresponding transition is confirmed. A precise alternative does not repair a misleading preferred recommendation. Keep any proposed notification or download path separate from behavior established by the contract.

## Make the next step understandable

Use specific action labels, stable object names and descriptive destinations. Consequential confirmations should name the action and affected object rather than rely on Yes/No. Visible field labels carry the identity; placeholders can supply examples. Explain requirements before input when useful.

Review a consequential confirmation as a complete message: title, explanation and actions together must identify the affected object and material consequence, including irreversibility when established. A clearer action verb alone cannot supply a missing consequence. Preserve placeholders and provide complete localized replacements for any proposed explanatory text.

Distinguish validation, connection failure, permission denial and a system error. Explain the affected outcome and a recovery action that really exists; retain the user's input where the product supports retry. Distinguish first use, no matching results, loading, partial data and unavailable content. Keep tone appropriate to the stakes and the accepted brand; clarity does not require every product to have the same voice.

Preserve interpolation placeholders, escaping, numeric meaning, pluralization, locale conventions and accessibility names. Use complete localizable messages rather than concatenated fragments. Do not shorten a phrase until it loses the information needed to act; fix an interaction problem through the agreed design scope rather than camouflage it with polished text.

## Verify meaning, consistency and fit

For review, give the exact location/state, current and proposed complete text, reason and any assumption. Group systemic terminology issues once. For authorized edits, change only the intended strings/bindings, compare the whole affected flow and verify realistic wrapping, truncation and relevant narrow/locale variants. Preserve component structure and tokens unless layout work is also requested.

Where code is available, check that copy matches actual pending/saved/failed states and that visible and accessible labels remain coherent. Preserve dynamic-message contracts and relevant existing checks. Report which static or runtime surfaces were inspected and any unverified localization or user comprehension. A clearer sentence or an agent review is not evidence of a completed usability study.
