# Diagnose and refine a rendered interface

Use for UI critiques, scoped visual improvements and cross-page consistency assessments. Ground findings in the exact screen/state and accepted design. An aesthetic preference is not a verified usability defect.

## Inspect, correct and recheck

1. Identify the user's goal, actual state, viewport, appearance mode and supplied/rendered evidence.
2. Locate concrete weaknesses and plausible causes; distinguish observation, hypothesis, measured defect and subjective preference.
3. Compare a limited set of corrections consistent with accepted components/tokens and the task; prioritize smallest effective repair.
4. If authorized, change shared owners, re-render the target and recheck affected route/state variants. A read-only review never changes code or design files.
5. Report actual checks and uncovered states without implying participant validation from an agent's critique.

| Symptom | Likely causes to inspect | Candidate correction and proof |
| --- | --- | --- |
| No obvious focus | Equal emphasis across actions, cards and headings | Rank information/actions; compare first-glance scanning order |
| Screen feels cluttered | Excess nested borders, repeated chips and labels | Replace some boxes with proximity, surface contrast or space; keep meaningful boundaries |
| Sections appear unrelated or merged | Ambiguous gaps, inconsistent internal/external padding | Restore grouping through reusable spacing roles; test long/narrow variants |
| Generic SaaS aesthetic | Decoration independent of product/workflow | Derive an appropriate composition and focal point from the real task |
| Hard-to-scan text | Weak type roles, long measures, tight lines | Correct hierarchy and readable measures; inspect actual wrapping and zoom |
| Noisy or low-contrast color | Too many accents, unstructured semantic roles | Consolidate roles; measure actual applicable contrast and include non-color cues |
| Arbitrary shadows or borders | Unclear elevation or selection model | Use depth only to explain layers; inspect overlays and focus |
| Dashboard wastes screen space | Uniform KPI cards, oversized padding, hidden context | Make data/action hierarchy suit the work; preserve useful information density |
| Poor photo or upload rendering | Uncontrolled crop and text overlay | Set aspect/focal behavior, responsive sources and fallback/scrim; test unusual input |
| Empty/error state has no direction | Decorative filler or ambiguous outcomes | Explain state and a real recovery action; check the action's implementation |
| Related views feel inconsistent | Divergent shells, tokens, action placement | Compare routes side by side and repair shared primitives; retain justified variants |
| Happy screenshot hides broken flow | Missing denied, draft, keyboard or failed-save state | Exercise critical journeys and recovery with runtime evidence |

Prioritize blocked/inaccessible actions and misleading consequences above comprehension and polish. Use [component and token audits](component-and-token-audits.md) for drift and [measurement and applicability](measurement-and-applicability.md) for quantified accessibility claims. Do not report that a proposed replacement satisfies a numerical threshold without measuring it.

Return the location/state, observation, impact, proportionate recommendation, evidence and remaining uncertainty. A passing build, component story or attractive screenshot alone does not prove experience quality.
