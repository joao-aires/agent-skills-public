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

Make the action, current state and consequences understandable in the product's voice. Use [interaction design](../interaction-design/SKILL.md) for behavior and [interface quality](../interface-quality/SKILL.md) for rendered fit.

## Ground language in behavior

Read the whole affected flow, adjacent states and established vocabulary. Identify the reader's goal, what the system permits and knows, the stakes and the available next action. Separate UI text from sample data and annotations. Resolve technical facts from contracts/code; ask about unresolved product decisions that change meaning.

Match every recommended message, including the preferred default, to authoritative state and supported behavior.

- Distinguish an acknowledged request, work in progress and confirmed outcome.
- Recovery, notification, timing and download promises require a real contract.
- Preserve material consequences of consent, payment, security, sharing and deletion; a copy change cannot redefine permissions or recovery.

## Make decisions and recovery clear

Name the action by what happens to the user's object, using the same term before and after the action. A label should let the user predict the result without needing to understand the implementation. Keep field labels visible when values have been entered, and make destinations clear enough that navigation does not depend on surrounding decoration.

Review consequential confirmations as a whole. The title, explanation and actions should identify the affected object, what will happen, and any material consequence such as loss of access or irreversibility when established. Remove repetition that competes with that decision, while retaining information the user needs to choose safely. Supply complete localized replacements with their placeholders intact.

Distinguish validation, connectivity, denied authority and system failure. Explain the affected outcome and an available recovery action; preserve input where retry is supported. Give first use, no matches, loading, partial and unavailable data meanings suited to the task. Clarity should preserve the accepted brand voice.

Preserve interpolation, escaping, numeric meaning, pluralization, locale conventions and accessible names. Use complete localizable messages. If clarity requires an interaction change, surface that decision within the agreed design scope.

## Verify the complete recommendation

| Mode | Deliver and verify |
| --- | --- |
| Review | Propose the location/state, current and complete replacement text, reason and assumptions. Group systemic terminology issues once. |
| Authorized rewrite/implementation | Preserve bindings/structure; compare the affected flow, dynamic states, accessible labels and realistic narrow/locale wrapping. |
| Harmonization | Align established terms within the named scope. |

Use code/runtime evidence where available to check semantic accuracy. Report inspected surfaces and unresolved meaning, localization or comprehension gaps. A clearer sentence or agent critique does not establish participant usability findings.
