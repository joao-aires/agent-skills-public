---
name: explain
description: >-
  Expertise and methods for concept explanation. Explain a concept to a specific reader so they can
  predict, apply or decide, using intuition, bounded analogy, mechanism, a worked example,
  boundary cases and a comprehension check. Use for quick intuition, deep mechanism, decision
  or code explanation, and correcting a misconception. A conversational craft method, not an
  artifact contract. It informs the activity that composes it; that activity owns the decision
  and stopping point.
user-invocable: true
metadata:
  kind: method
  domain: documentation
  phase: cross-phase
  scope: generic
  invocation: both
---

# Explain an idea so it can be used

An explanation succeeds when the reader can do something with the idea afterward: restate it in their own words, predict a case they have not seen, choose between options, or notice when the idea stops applying. It is not a shorter document or a friendlier summary. A summary preserves the facts; an explanation builds a working model.

This skill covers the act of explaining. It works from established material. It does not establish what is true, decide what documentation must exist, or produce a governed artifact.

## Boundaries

| Request | Use | Why |
| --- | --- | --- |
| Find out whether something is true, what the sources say, or what remains unknown | Research | Research owns inquiry, source quality and uncertainty. Explanation can expose a factual gap; it must not fill the gap with a plausible mechanism. |
| Document the current architecture, its coverage, views and evidence | System documentation | Mapping owns system discovery and current-state claims. Explanation can make a mapped flow understandable; it does not replace tracing it. |
| Write or revise a README, PRD, ADR, runbook, guide or other document | Technical writing, plus the artifact contract | Document craft owns reader fit, structure, precision and presentation across a complete artifact. Explanation may supply a section or the conversation that informs it. |
| Decide what an artifact must contain, what status it has or where it lives | Artifact system and the domain method | These are artifact requirements, not explanation choices. |

Explanation and document work meet at a clear seam. Explain first when the reader is blocked on understanding. Write the document when the reader needs a durable, reviewable artifact. Do not let a conversational explanation silently become a contract, a decision record or evidence of implementation.

## Start from the reader's model

Establish four things, usually with one or two questions rather than an interview:

- the question behind the question, and the decision or action that prompts it;
- what the reader already knows, including the words they use for it;
- what they will do with the answer;
- how deep they need to go before they can act.

Begin with the smallest true statement that changes their model, not with a definition, unless the term itself is the obstacle. State the scope and non-scope in one line so that a remaining "I still don't understand X" has somewhere to go.

Explanation is anchored by a real question. Diátaxis calls this a *why* question; engineering questions are often "why does it behave this way?", "what happens when...?" or "why is this better than...?" If no question exists, agree on one. "Tell me about X" has no stopping point.

## The explanation ladder

The ladder is a default order, not a ritual. Each rung earns its place by removing a specific confusion.

| Rung | What it does | Done when |
| --- | --- | --- |
| 1. One-sentence intuition | States the load-bearing idea without jargon | The reader can repeat the claim accurately |
| 2. Analogy with limits | Maps the idea onto something the reader already knows and states where the mapping breaks | The reader can say which part is like the familiar thing and which is not |
| 3. Mechanism | Names actors, inputs, state changes, order and feedback | The reader can trace cause to effect without the analogy |
| 4. Worked example | Runs one concrete case, including a decision or failure point | The reader can predict the result of a nearby case |
| 5. Boundaries and edge cases | Says when the idea is false, expensive, unsafe or inapplicable, and compares the alternative | The reader can recognize a case where it should not be used |
| 6. Check understanding | Asks for a prediction, contrast or transfer | The answer reveals which rung is still missing |

A quick explanation can stop after rungs 1, 2 and 6. A deep explanation uses all six. Most failed explanations either stop at rung 2, leaving a confident but wrong model at the edges, or start at rung 3, leaving an accurate account the reader cannot use.

For example, a read-through cache can be explained as "a fast copy of data whose source is slower to reach." The pantry-beside-the-shop analogy carries lookup and refill, but it breaks on expiry and disagreement: a pantry does not serve stale food while the shop has changed. The mechanism adds lookup, hit or miss, fill, eviction and invalidation. A two-request example shows a miss then a hit, and a write that invalidates the copy. The boundary is data that must be strongly consistent or is read once. The check asks what the next reader sees when the source changes and the cache is not invalidated.

Keep the rungs honest:

- Never let an analogy carry a safety, security or correctness claim.
- Re-state the intuition after the mechanism. If it now needs changing, the first sentence was wrong, not merely simplified.
- A worked example must not introduce a new rule. If it does, the rule belongs in the mechanism.
- State what the model omits. A model is a useful projection, not the system.

## Modes

| Mode | Begin with | Effective depth | Stop when | Characteristic failure |
| --- | --- | --- | --- | --- |
| Quick intuition | The decision the reader is about to make | Rungs 1–2, one check | They can restate it and ask a sharper question | A clever analogy that hides the cost |
| Deep mechanism | One real path through the system | All rungs | They can trace an unseen case and name a failure | A component inventory with no causal chain |
| Decision explanation | The constraint and the real alternatives | Rungs 1, 3, 5 | They can say what would reverse the recommendation | Advocacy that omits the losing option's advantage |
| Code explanation | The entry point and the data | Mechanism at the level of the proposed change | They can predict the effect of an edit | Line-by-line paraphrase of syntax |
| Correcting a misconception | The reader's current model | Rungs 1–3, 5–6 | Their old model makes a wrong prediction they can see | Contradiction without a replacement model |

### Quick intuition

Lead with the smallest true sentence, one analogy and one limit, then check. Stop before completeness. Do not strip a caveat that changes the decision; say that the full version adds a condition and name when it matters.

### Deep mechanism

Pick one concrete path: a request, an item, a job or a command. Follow it through ownership, state and failure, then widen to variants. Name the invariant that stays true and the transition that preserves it. Use a diagram only when relationships are the hard part, and explain what the reader should see in it.

### Decision explanation

Explain the choice as a consequence of constraints, not as a preference. State the situation, the options that were real, what each made easier or harder, and the condition that would change the choice. Separate the recommendation from the decision authority. If the historical rationale is unknown, say so; do not invent a clean story.

### Code explanation

Start from the caller's goal or a failing behavior, then follow data and control to the relevant code. Name the invariant the code protects and the error path it does not. Show the smallest snippet that carries the idea, with types, units and enough surrounding call to be meaningful. Explain why an edit would be safe or unsafe, not what each line does.

### Correcting a misconception

Ask what the reader expects and why. Acknowledge the part that is right; it is usually a real pattern in a narrower case. Present the discriminating case where their prediction fails, replace the model, then re-ask the original question. Do not open with "actually" and a list of corrections.

## Make it accurate, not merely simple

- Simplify the path, not the truth. If a caveat changes the reader's action, keep it and explain it.
- Prefer causal verbs: reads, writes, retries, rejects, expires. "Handles" and "manages" hide the mechanism.
- Quantify only what you can support. "Faster" needs a baseline; an invented number is worse than a range with a source.
- Borrow structure from the reader's domain, not vocabulary. A good analogy maps relations, not nouns.
- Keep one load-bearing idea per explanation. If two ideas compete, separate them and connect them explicitly.
- Mark uncertainty. "The code does X; why it was chosen is not recorded here" is a complete answer to a different question.
- Avoid "just", "simply", "obviously" and "under the hood" as substitutes for mechanism.
- Use synthetic data in examples, state prerequisites, and never present an unexecuted example as verified.

## Check understanding without quizzing

Ask one question that discriminates between the intended model and the likely wrong one. Prefer prediction, transfer, contrast, boundary or diagnosis over recall. "Does that make sense?" invites a polite yes; "what does the next request see if the write lands first?" produces evidence.

Wait for the answer. Treat a wrong answer as information about the explanation, not about the reader. Locate the missing rung: inability to restate points to rung 1; inability to predict points to rung 3 or 4; success on the normal case but failure at the edge points to rung 5; correct understanding with a poor choice may be a decision-context problem, not an explanation problem.

Do not turn the check into a gotcha or a terminology test. The goal is a better model, not a score.

## Stop and review

Stop when the reader can use the idea for the stated purpose. More detail is a different request: a document, a course or a design review.

- Can the reader state the intuition without repeating your words?
- Can they trace a new case through the mechanism?
- Do they know where the model stops?
- Did you preserve every caveat that changes their action?
- Is the example doing work, or decorating the prose?
- Did you answer the question they asked rather than the one you prepared?

If the explanation will become durable documentation, hand the settled content to technical writing and the artifact's contract. A clear conversation is not evidence that the artifact is complete.

## Sources and fit

This is original explanation guidance informed by [Diátaxis: Explanation](https://diataxis.fr/explanation/) for understanding-oriented, bounded and perspective-aware explanation; [Google Technical Writing One: audience](https://developers.google.com/tech-writing/one/audience) and [documents](https://developers.google.com/tech-writing/one/documents) for reader needs, scope and opening with the key point; and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) for skimmable structure, examples and current content.

The ladder, modes, analogy limits and misconception repair are local method, not claims from those sources. [Explanation patterns](references/explanation-patterns.md) holds reusable shapes, analogy limits, worked-example forms, check questions and anti-patterns. The skill does not import a documentation taxonomy or require a specific artifact.
