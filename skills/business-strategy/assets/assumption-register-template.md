# Assumption Register

Track beliefs that must be true for the strategy to work.

| ID | Assumption | Type | Importance | Confidence | Supporting evidence | Contradicting evidence | Falsifier / tripwire | Next test | Review trigger | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 |  | demand / behavior / competition / technology / GTM / economics / regulation / future-market | critical / high / medium / low | high / medium / low |  |  |  |  |  | open |

## Assumption Classes for Future Markets

Optionally classify long-horizon assumptions as:

- **Invariant** — likely valuable across futures
- **Structural** — durable for several years
- **Transitional** — useful during the current market phase
- **Fragile** — dependent on today's architecture or behavior

## Rules

1. Critical assumptions must have a falsifier.
2. Confidence is evidence-based, not optimism-based.
3. A failed critical assumption should trigger explicit strategy mutation or a decision to stop.
4. Do not silently delete disproven assumptions; mark their status and reference the decision log.
5. Prioritize tests by decision impact × uncertainty × cost of being wrong.