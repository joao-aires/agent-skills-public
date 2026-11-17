# Architecture scan

Use this reference when an improvement request concerns architecture: understanding, boundaries, dependency direction, change cost or testability. Read [codebase-design](../../codebase-design/SKILL.md) for the shared vocabulary and its principles; this reference covers where to look, how to judge a candidate and how to present it. The scan is an assessment. Stop at findings unless implementation is requested separately.

## Scope before scanning

Weight the scan toward where change already happens. Deepening a module pays off by making future changes to it easier, so a rarely touched area needs stronger evidence before it earns work.

- If the user named a module, subsystem, direction or pain point, scan there and skip the inference below.
- Otherwise read recent history — `git log`, recent changes and their linked records — for files and areas that keep appearing, and start from those paths. If changes are scattered with no clear hotspot, widen the net rather than inventing one.
- Read the project's domain glossary and accepted ADRs in the affected area before judging a boundary. They name useful seams and record decisions the scan should not re-litigate.
- Treat reported pain points — repeated fixes, slow checks, failed changes, onboarding confusion — as evidence about friction, not only commit frequency.

## Judge candidates

Look for architecture friction that a bounded change could remove:

- **Shallow modules.** The interface is nearly as complex as the implementation, or the module mostly forwards calls without adding behavior.
- **Leaked seams.** Tightly coupled modules reach across an interface or share internal state, so a change in one forces edits in the other.
- **Untestable interfaces.** The promised behavior can only be observed through internals, or functions were extracted for testability while the real failures happen at their call sites.

Apply the **deletion test** to anything that looks shallow: if deleting the module makes complexity vanish, it was a pass-through; if complexity reappears across its callers, it was earning its keep. "No worthwhile candidate in this area" is a valid result.

Keep the candidate set small and evidence-backed. Name the paths, commits, failed changes or tests that cannot be written, and distinguish observed friction from a disliked coding style. Do not propose an interface yet.

## Label recommendation strength

| Strength | Meaning |
| --- | --- |
| Strong | Named files, observed friction, and a bounded change with protected behavior and a credible test improvement. |
| Worth exploring | Real friction, but the shape or payoff still needs a decision or a small experiment. |
| Speculative | A hypothesis from structure alone; state the evidence that would confirm or drop it. |

## Call out ADR conflicts

If a candidate contradicts an accepted ADR, surface it only when the friction is strong enough to warrant revisiting that decision. Name the ADR and the reason in the finding. Do not list every theoretical refactor an ADR forbids. Revising an ADR, the glossary or an architecture record is a separate authorized decision, not part of the scan.

## Optional visual report

When a before/after comparison communicates faster than prose, use available visualization or interface-design expertise to build one for each candidate: involved files, the problem, the bounded change, the expected locality and leverage, how tests would improve, a side-by-side before/after view of the structure, and the strength label. End with the candidate to tackle first and why.

Keep the report outside the repository — a temporary directory is usually enough — unless the user asks for a durable artifact; if they do, resolve its home through [artifact homes](../../artifact-system/references/homes.md). The report presents the findings; it is not a new artifact type and does not authorize implementation.

## Return findings

For each candidate, report the affected area and files, the observed friction and its evidence, the bounded change, the behavior that must be protected, the recommendation strength and the verification that would show improvement. Order by strength and cost.

Stop at findings. Implementation, tickets, ADR changes and publication each need their own request.
