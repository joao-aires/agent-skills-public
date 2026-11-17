# Idea Validation

## Purpose

Validation exists to decide whether a premise deserves more investment, not to accumulate encouraging conversations. Use it when a concept is early enough that its customer, problem, economics or feasibility could still be wrong.

Validation answers four questions in order:

1. Is the premise coherent enough to test?
2. Which unknowns would change the decision if resolved?
3. What is the cheapest credible evidence for each?
4. What result means continue, change shape or stop?

The output is a decision and an updated assumption ledger, not a validation score.

## Challenge the premise first

Most weak validation effort tests execution of an idea nobody has questioned. Start with the premise:

```text
We believe [customer] in [circumstance] will [change behavior / pay / adopt]
because [mechanism], and we can reach them through [route]
before [constraint] closes the window.
```

Then challenge each clause:

- **Customer** — is this a real group with shared circumstances, budget and reachable distribution, or a demographic label?
- **Circumstance** — what triggers the need now, and how often?
- **Behavior** — what must the customer stop, start or reorganize for this to work?
- **Mechanism** — why would the proposed approach produce the claimed outcome rather than a plausible story?
- **Route** — who can actually reach this buyer at a cost the economics survive?
- **Window** — why now, and what happens if adoption is slower than expected?

A premise that cannot be stated in one paragraph cannot be validated; it can only be discussed.

### Forcing questions

Use a short interrogation pass before designing tests. The style of questions popularized by Y Combinator's application and office-hours practice is a useful method reference: direct, concrete and hostile to abstraction. Ask, and answer in specifics:

1. What are you building, in one sentence a stranger could repeat without asking a follow-up?
2. Who is the first user, by role and circumstance, and what did that user do last week instead?
3. What changed in technology, regulation, cost or behavior that makes this newly possible or newly urgent?
4. Why would that user choose this over the alternative they already tolerate, including doing nothing?
5. What have you seen that suggests they will pay, change a workflow or spend political capital — not merely agree the problem exists?
6. What did you learn from direct contact in the last 30 days that you did not believe before?
7. What would have to be true for this to be obviously right, and by when would you know?
8. What are you deliberately not doing?

These questions are a thinking aid. They do not produce a score, a pass mark or a substitute for evidence.

## Separate facts, assumptions and unknowns

Every material statement in a validation plan belongs to one class:

| Class | Test | Handling |
|---|---|---|
| Fact | Directly observed, documented or contractually confirmed | Cite the source and date |
| Derived calculation | Computed from stated inputs | Show inputs and sensitivity |
| Inference | Reasoned conclusion from facts | State the reasoning and what would overturn it |
| Assumption | Required belief without direct evidence | Put it in the ledger with a test |
| Unknown | Not yet knowable at acceptable cost | Bound it, state how the decision changes if it resolves either way |

Most failed validation plans are assumptions presented as facts. The second most common failure is treating an unknown as if it must be resolved before any decision; many unknowns only need a bound and a fallback.

Distinguish unknowns that are:

- **knowable now** through existing data, public evidence or a few conversations;
- **knowable only by running something** — a pilot, a manual service, a priced offer;
- **bounded but not resolvable** — market timing, competitor response, regulation;
- **judgment calls** that will never be evidenced cheaply and must be owned explicitly.

Use the claim-led research approach in [research protocol](research-protocol.md) for the first group and the test ladder in [experiments and PMF](experiments-and-pmf.md) for the second.

## Assumption ledger

Keep one compact ledger for the engagement. Put it inside `strategy-state.md` when persistent state exists; do not create a second register.

| ID | Assumption | Class | Importance | Confidence | Evidence for / against | Falsifier | Cheapest next test | Review date |
|---|---|---|---|---|---|---|---|---|
| A01 | Mid-market operations teams will pay a per-team fee for cross-system review, not per seat | economics | critical | low | Three teams described the workflow; none has seen a price | Fewer than three of eight qualified teams accept the fee | Offer the fee to the next eight qualified teams | End of quarter |

Rules that make the ledger useful:

- **Only material assumptions** — being wrong must change a choice, a number that drives a choice, or the timing of a commitment.
- **One claim per row.** Combined claims hide which part failed.
- **Importance and confidence are separate.** A low-confidence assumption that cannot change the decision is not a priority.
- **Every critical row has a falsifier.** "We would know if customers did not renew" is not a falsifier unless a threshold and window make it observable.
- **Name the decision each test informs.** A test with no attached decision is research for its own sake.
- **Record contradictions** rather than averaging them into a comfortable middle.

Prioritize with the same logic as the research protocol:

```text
test priority ≈ decision impact × uncertainty × cost of being wrong
```

Then divide by the cost and time of the test. The best next test usually resolves a large uncertainty cheaply, not the most interesting question.

## Validation plan

Order work from cheapest to most costly, and let each step gate the next. Each step states what it can and cannot establish.

| Step | Typical form | Can establish | Cannot establish |
|---|---|---|---|
| Existing evidence | Public data, support logs, analytics, prior attempts | Whether the problem appears in real behavior at some scale | Whether this customer will change for this offer |
| Problem interviews | Behavioral conversations with people in the target circumstance | Current workaround, cost of the status quo, language, trigger | Demand or willingness to pay |
| Artifact reaction | Prototype, mockup, sample output, landing page | Whether the framing is understood and attractive | Whether anyone will pay or switch |
| Manual delivery | Concierge or service delivered by hand | Whether the outcome is valuable and what the workflow requires | Whether it can be delivered at margin or scale |
| Priced commitment | Paid pilot, deposit, signed letter of intent with terms, prepayment | Willingness to exchange money or risk for the outcome | Repeatability, retention, expansion |
| Repeatable motion | Multiple similar customers through the same path | Whether demand and delivery repeat | Long-run durability or competitive response |

Rules:

- **Match the method to the claim.** A landing-page click does not validate a B2B purchase decision; a friendly pilot does not validate a self-serve funnel.
- **Prefer behavior over sentiment.** What someone did with money, time, data access or internal approval is stronger than what they said.
- **Do not pitch during problem discovery.** Pitching contaminates the evidence; see [customer discovery](customer-discovery.md).
- **Test the riskiest premise, not the most convenient one.** A plan that validates only the easy parts is a schedule, not validation.
- **Set the decision rule before the test.** Otherwise the result will be interpreted to fit the preferred outcome.
- **Stop when a test cannot change the decision.** More evidence has a cost even when it feels free.

## Continue, pivot or kill

Define the response before running each test. Use evidence thresholds tied to the decision, not effort or elapsed time.

### Continue

Continue when the tested assumption held at the stated bar, the next assumption is the binding one, and the remaining plan is proportionate to the new confidence.

Continuing does not mean the thesis is proven. It means the next uncertainty is worth buying.

### Change shape

Distinguish three changes, because they have different costs:

- **Tactic change** — same customer, problem and model; a different channel, message or workflow. Cheap, and usually not a strategy event.
- **Thesis change** — a different customer, wedge, value proposition, business model or route to market. Reopen the affected strategy question and compare against the option set in [strategy option set](strategy-option-set.md).
- **Premise change** — the underlying opportunity is smaller, later, more contested or less valuable than believed. This is a kill or park decision, not a pivot.

Record which one occurred. Teams routinely call a premise failure a tactic problem and keep spending.

### Park or kill

Use explicit criteria:

- **Demand kill** — the target customer does not have the problem at the assumed frequency, urgency or budget, and no adjacent segment shows a materially stronger signal.
- **Economics kill** — the cost to serve, acquire or deliver cannot produce acceptable contribution at a plausible price, and no plausible model change fixes it.
- **Distribution kill** — there is no affordable, repeatable route to the buyer within the window the strategy needs.
- **Capability kill** — the required capability is unavailable, unaffordable or slower to build than the opportunity allows.
- **Timing kill** — the window has closed or moved beyond the reachable horizon.

Park rather than kill when the premise may become true later and the cost of keeping the option alive is low. State the signal that would reopen it, and stop investing until that signal appears.

Sunk cost is not evidence. Prior spend changes the accounting, not the expected value of the next dollar.

## Failure modes

- **Validation theater** — interviews, surveys and prototypes designed to produce encouragement.
- **False precision** — sample sizes, confidence language or market numbers that overstate what was observed.
- **Proxy substitution** — measuring clicks, waitlists or compliments when the decision needs payment, retention or approval.
- **Premise drift** — the team quietly changes the customer or problem between tests and compares the results as if they were the same hypothesis.
- **Single-test closure** — one positive result treated as proof; one negative result treated as disproof without checking method.
- **Endless discovery** — more research instead of the cheapest test that would actually produce behavior.
- **Goalpost movement** — thresholds revised after seeing results without recording the revision and its reason.
- **Founder-only evidence** — the founder's network, enthusiasm and personal selling ability are mistaken for a repeatable market.

## Completion evidence

A validation pass is complete enough to decide when:

- the premise is stated in one paragraph and its weakest clause is identified;
- material assumptions are in the ledger with confidence and falsifiers;
- each critical assumption has a test, a decision rule and an owner, or is explicitly accepted as judgment;
- results are classified as fact, observation, inference or opinion;
- the recommendation states continue, change shape, park or kill, with the evidence and the next review trigger;
- rejected alternatives and their opportunity cost remain visible.

Starting structure: [`assets/validation-plan.md`](../assets/validation-plan.md). Adapt or omit sections; do not fill it with invented evidence.
