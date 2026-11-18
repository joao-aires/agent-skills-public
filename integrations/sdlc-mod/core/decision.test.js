import assert from "node:assert/strict";
import test from "node:test";
import { emptyState } from "./state.js";
import {
  buildDecisionInput,
  buildDecisionQuestions,
  decisionHints,
  gateCommands,
  interpretDecisions,
  shouldExtract,
} from "./decision.js";

test("asks for change, intent, activity and focus", () => {
  const state = emptyState();
  state.threads.push(
    { id: "T1", name: "API contract", activity: "design", softwareType: "frontend" },
    { id: "T2", name: "pagination works", activity: "implementation", softwareType: null },
  );

  const questions = buildDecisionQuestions(state);
  assert.deepEqual(
    questions.map((question) => question.name),
    ["changed", "intent", "activity", "focus"],
  );
  assert.equal(questions[0].type, "predicate");
  assert.deepEqual(
    questions[3].choices.map((choice) => choice.value),
    ["none", "new", "T1", "T2"],
  );
  const t1 = questions[3].choices.find((choice) => choice.value === "T1");
  assert.match(t1.label, /T1 API contract/);
});

test("builds input from state and recent messages", () => {
  const state = emptyState();
  const input = buildDecisionInput({
    state,
    messages: [{ role: "user", text: "move to implementation" }],
  });
  assert.match(input, /Current state:/);
  assert.match(input, /USER: move to implementation/);
});

test("interprets predicate and choice answers", () => {
  const decision = interpretDecisions({
    answers: [
      { type: "predicate", name: "changed", probability: 0.66 },
      { type: "choice", name: "intent", choice: "phase", confidence: 0.9 },
      { type: "choice", name: "activity", choice: "implementation", confidence: 1 },
      { type: "choice", name: "focus", choice: "T1", confidence: 0.8 },
    ],
  });
  assert.equal(decision.probability, 0.66);
  assert.equal(decision.intent, "phase");
  assert.equal(decision.activity, "implementation");
  assert.equal(decision.focus, "T1");
});

test("handles an error answer without losing the rest", () => {
  const decision = interpretDecisions({
    answers: [
      { type: "predicate", name: "changed", probability: 0.2 },
      { type: "choice", name: "intent", choice: "none", confidence: 0.95 },
      { type: "error", name: "activity", message: "unavailable" },
    ],
  });
  assert.equal(decision.activity, null);
  assert.equal(decision.intent, "none");
});

test("gates extraction on probability and intent confidence", () => {
  assert.equal(shouldExtract(null), true, "a failed gate must fall back to extraction");
  assert.equal(shouldExtract({ probability: 0.66, intent: "phase", intentConfidence: 0.9 }), true);
  assert.equal(shouldExtract({ probability: 0.2, intent: "none", intentConfidence: 0.95 }), false);
  assert.equal(shouldExtract({ probability: 0.2, intent: "decision", intentConfidence: 0.4 }), false);
  assert.equal(shouldExtract({ probability: 0.2, intent: "decision", intentConfidence: 0.8 }), true);
  assert.equal(shouldExtract({ probability: 0.2, intent: "none", intentConfidence: 0.95 }, { probabilityThreshold: 0.1 }), true);
  assert.equal(
    shouldExtract(
      { probability: 0.35, intent: "none", intentConfidence: 0.66, activity: "testing", activityConfidence: 1 },
      { currentActivity: "implementation" },
    ),
    true,
    "an activity change must survive a weak predicate",
  );
  assert.equal(
    shouldExtract(
      { probability: 0.2, intent: "none", intentConfidence: 0.95, activity: "implementation", activityConfidence: 1 },
      { currentActivity: "implementation" },
    ),
    false,
    "the same activity with no intent stays gated",
  );
  assert.equal(
    shouldExtract(
      { probability: 0.25, intent: "none", intentConfidence: 0.9, activity: "implementation", activityConfidence: 1, focus: "T2", focusConfidence: 0.9 },
      { currentActivity: "implementation", currentFocus: "T1" },
    ),
    true,
    "a focus change must survive a weak predicate",
  );
});

test("applies confident phase and focus changes structurally", () => {
  const state = emptyState();
  state.threads.push(
    { id: "T1", name: "pagination works", activity: "implementation", status: "waiting", artifacts: [] },
    { id: "T2", name: "API contract", activity: "design", status: "waiting", artifacts: [] },
  );
  state.focusThreadId = "T1";

  assert.deepEqual(
    gateCommands(
      { intent: "phase", activity: "testing", activityConfidence: 1, focus: "T1", focusConfidence: 1 },
      state,
    ),
    [{ type: "thread.phase", id: "T1", activity: "testing" }],
  );

  assert.deepEqual(
    gateCommands(
      { intent: "phase", activity: "design", activityConfidence: 1, focus: "T2", focusConfidence: 0.9 },
      state,
    ),
    [{ type: "thread.focus", id: "T2" }],
  );

  assert.deepEqual(
    gateCommands(
      { intent: "phase", activity: "testing", activityConfidence: 0.4, focus: "new", focusConfidence: 1 },
      state,
    ),
    [],
  );
  assert.deepEqual(gateCommands({ intent: "decision", activity: "testing", activityConfidence: 1 }, state), []);
});

test("turns a decision into compact hints", () => {
  assert.equal(decisionHints(null), null);
  assert.equal(
    decisionHints({ activity: "implementation", intent: "phase", focus: "T1" }),
    "activity=implementation, intent=phase, focus=T1",
  );
  assert.equal(decisionHints({ activity: "none", intent: "none", focus: "none" }), null);
});

test("uses the named thread instead of a low-confidence focus choice", () => {
  const state = emptyState();
  state.threads.push(
    {
      id: "T1",
      name: "pagination works",
      activity: "implementation",
      status: "waiting",
      completedPhases: [],
      artifacts: [],
    },
    {
      id: "T2",
      name: "API contract",
      activity: "design",
      status: "waiting",
      completedPhases: [],
      artifacts: [],
    },
  );
  state.focusThreadId = "T1";

  assert.deepEqual(
    gateCommands(
      { intent: "phase", activity: "testing", activityConfidence: 1, focus: "T1", focusConfidence: 0.2 },
      state,
      { latestText: "move API contract to testing" },
    ),
    [
      { type: "thread.focus", id: "T2" },
      { type: "thread.phase", id: "T2", activity: "testing" },
    ],
  );
});
