# Design validation: test the direction before building it

Design validation gathers evidence that the chosen direction works before dependent implementation. It reduces uncertainty about comprehension, task success, interaction behavior, feasibility, compatibility or AI quality.

It is not the same as `test`. Validation checks a proposed direction with a prototype, critique, rendered slice, contract sketch, bench observation or evaluation set. `test` verifies implemented behavior at a revision. If validation happens after implementation, it is verification, not design validation.

## When to validate

Validate when the cost of being wrong is material:

- the user must understand or complete a task the design has not exercised;
- interaction, navigation or information hierarchy is uncertain;
- a visual or brand direction must be judged rendered;
- an architecture or contract decision depends on feasibility;
- a migration, compatibility or recovery path is uncertain;
- an AI behavior needs an evaluation set before it is trusted;
- a device, hardware or platform limit is unverified.

Do not turn every design into a study. A reversible local change may proceed on review alone.

## Modes

| Mode | Use for | Evidence |
| --- | --- | --- |
| Expert critique | Early structure, interaction or architecture | Reviewer, criteria and findings |
| Heuristic or accessibility review | UI states, keyboard, focus, contrast, labels | Checklist, screenshots or rendered inspection |
| Rendered slice | Layout, density, typography, responsive behavior | Rendered target, viewport, observed result |
| Interactive prototype | Flow, state model, comprehension | Prototype link, tasks, observations |
| Usability observation | Task success and confusion | Participant or proxy, tasks, observed result |
| Contract/integration probe | API, schema, event or compatibility | Target, command or scenario, observed result |
| Bench or device observation | Embedded or platform limits | Target, conditions, measurement |
| Evaluation set | AI quality, regression, refusal or citation behavior | Cases, baseline, result, limits |
| Consumer test | Library/CLI surface and packaging | Clean environment, install or invocation, result |

## Evidence rules

- Name the target, revision, environment and date.
- Say what was exercised and what was not.
- Separate observed behavior from opinion or expectation.
- Record the conditions that could invalidate the result.
- Keep a local probe distinct from production behavior.
- Do not claim a participant, user or customer result that did not happen.

## Stopping point

Validation ends with one of:

- **validated** — the direction is supported for the intended scope;
- **limited** — it works under stated conditions, with remaining uncertainty;
- **blocked** — the evidence contradicts the direction or the probe could not run.

A validated design is still proposed relative to implementation. It does not authorize building beyond the design request.

## Output

Record the mode, target, evidence, result, limits and the decision it supports in the design proposal or ECR solution-design section. If the result changes the chosen option, reopen the decision and update dependents.

## Anti-patterns

- calling a review a usability study;
- using a prototype as proof of implemented behavior;
- reporting a plan as a result;
- one happy-path observation standing in for failure and denial states;
- validating only the visual layer when the seam or contract is the risk;
- skipping validation because a specialist is absent.
