# Logic probe: make a state model observable

A logic probe lets someone drive a rule, state machine or data shape through concrete cases and watch what changes. Use it when the question is about **behavior or structure**, not appearance: the model looks reasonable on paper but feels wrong once it meets real actions.

Read the [prototype method](../SKILL.md) first; the throwaway rules and the boundary with design apply here.

## When this is the right shape

- "Does this state machine handle the case where X happens after Y?"
- "Can this data shape represent a partial success, a retry or a reversal?"
- "What should the operation surface look like before we commit to an API?"
- Any question where the owner wants to press actions and inspect the resulting state.

If the question is "what should this look like," use the [UI probe](ui-probe.md) instead.

## Shape the logic before the page

Put the part that answers the question in one portable, pure module. Pick the smallest shape that matches the question:

| Shape | Use when | Watch for |
| --- | --- | --- |
| Pure reducer, `(state, action) => state` | Actions are discrete events and state is one value | Side effects leaking into the reducer |
| Explicit state machine | Which actions are legal depends on the current state | States or transitions that exist only in the UI |
| Set of pure functions over a plain data type | There is no current state, only transformations | Hidden mutation or shared globals |
| Class or module with a method surface | The logic genuinely owns ongoing internal state | The page reaching into private state |

Keep the module free of the DOM, `document`, framework imports and button handlers. The page calls into it; nothing flows back. That separation is what lets a validated rule or function set lift into the real code after the probe is deleted.

## Build the shell

Default to one self-contained HTML file: plain HTML, CSS and JavaScript, everything inline, no framework, bundler or server. It should open by double-click or one project command and survive being sent to someone else.

Write for the person who owns the question, not for the person who wrote the module. Use domain labels, not reducer internals. Explain the state in plain language. The shell is disposable; the module is the part with a possible future.

A useful layout, top to bottom:

1. **Question and one-line explanation.** What this probe lets the owner explore, and what result would change the design.
2. **Current state.** A labeled panel with the full relevant state, re-rendered after every action. Call out what changed when it helps someone follow.
3. **Free play.** One button per action, always available, so the owner can try any order. Each click dispatches the action and re-renders.
4. **Guided scenarios.** One tab per scenario, each with a short description of the situation and what to watch for, followed by the ordered buttons to press. Each step is a real button. Starting a scenario resets to a known initial state so it runs the same way each time.

Choose scenarios that expose the awkward cases: the happy path, a boundary or partial success, a duplicate or retry, an action that should be illegal, and a recovery or reversal if the model has one. Do not turn the tabs into a test suite; they are a guided way to feel the model.

Keep the presentation restrained: clean type, generous spacing, one accent color, no animation that competes with the state. The owner should be looking at the model, not the demo.

## Run and observe

Run it yourself before handing it over. Confirm one command starts it, every action re-renders the full state, and a scenario resets cleanly.

Give the owner the file, command or URL and the scenarios worth trying. The interesting observations are the surprises: "that shouldn't be possible," "I assumed the second request would be rejected," "the order is still pending after the failure." Record the observation, the action sequence that produced it, and whether it contradicts the model or the code.

If the owner asks for another action or scenario, add it. A probe evolves while the question is live. Stop adding once the question is settled.

## Capture

Lift the validated reducer, machine or function set into the real module when implementation follows. Record the answer, the conditions and the limits in the design record or ECR validation section. The HTML shell is evidence and can ride along to the throwaway branch; it is not part of the implementation.

## Anti-patterns

- **Framework or server for a one-file question.** A React app or dev server makes the probe harder to share and adds machinery that answers nothing.
- **DOM inside the logic.** Once the module reads `document` or calls handlers, it cannot be lifted cleanly and the probe tests the page instead of the model.
- **State hidden behind the UI.** If the owner cannot see the full state after an action, the probe is not observable.
- **A test suite in disguise.** Assertions and test cases belong to `test` after the decision; the probe needs guided observation, not coverage.
- **Production concerns.** Persistence, migrations, auth and error handling beyond runnability obscure the question and make deletion harder.
- **Scenarios that only prove the happy path.** The model is least trustworthy at partial success, retries, denial, concurrency and reversal.
