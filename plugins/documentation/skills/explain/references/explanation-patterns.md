# Explanation patterns

Use this reference when the default ladder needs a specific shape. The pattern is chosen by the concept and by the reader's question, not by the subject area.

## Choose a pattern by concept type

| Concept type | Opening move | Load-bearing middle | Useful check | Common failure |
| --- | --- | --- | --- | --- |
| Mechanism or process | Follow one item from trigger to result | Ordered state changes, queues, retries and handoffs | Predict the next state | A box diagram with no transitions |
| Abstraction or interface | State the contract before the implementation | Inputs, guarantees, errors and ownership | What may a caller assume? | Examples before the contract |
| Data or state | Show the state that exists and who may change it | Invariants, transitions and concurrent writers | Two writers race | Nouns without a lifecycle |
| Algorithm or protocol | Name the invariant and the termination condition | Steps, message order, failure and retry | Trace a small input | Code or message narration |
| System or architecture | Start at a real entry point | Responsibilities, data flow, trust and deployment boundaries | Which component sees the failure? | A layer inventory |
| Tradeoff or decision | Name the constraint, not the winner | Real alternatives, consequences and reversal condition | What would change the choice? | One-sided advocacy |
| Policy or configuration | Show the default and its observed effect | Precedence, scope and exceptions | Which rule wins here? | A list of keys |
| Failure or incident | Start from observed impact | Causal chain, contributing conditions, detection and recovery | What was the earliest detectable signal? | A single root cause |
| Quantitative or mathematical | State the quantity and its units | Assumptions, derivation and sensitivity | Change one input | A formula without meaning |
| Code or API | Start from the caller's goal | Data and control path, invariant and error | What does an edit change? | Line-by-line paraphrase |

## Patterns worth naming

### Follow one item end to end

Use when handoffs or relationships are the confusion. Choose a request, order, job or message, label it, and trace it through each owner. At every stop, say what the item becomes, who may change it and what can reject it. Generalize only after the path reaches an outcome.

One happy path hides concurrency, rejection and partial failure. Add a second pass through one failure branch rather than describing every branch at once.

### Contract, then implementation

Use for an abstraction: a function, service boundary, interface or protocol. State the promise first: inputs, outputs, guarantees, errors and who may call it. Give one example that satisfies the contract and one that violates it. Then show an implementation and name any constraint that leaks through.

A contract is not behavior. If callers depend on an implementation detail, say that the contract is incomplete rather than presenting the detail as a guarantee.

### Invariant and violation

Use when the point of a mechanism is safety or correctness. State what must always remain true, show the step that preserves it, then show a plausible change that breaks it. This pattern explains locks, ownership rules, validation, transactions and idempotency better than a component tour.

State the scope of the invariant. "The balance never goes negative within one account" says something different from "no transfer can overdraw the system."

### Two-column tradeoff

Use for a decision with real alternatives. For each option, give what it makes easier, what it makes harder, when it wins and the signal that would reverse the choice. Keep shared constraints outside the rows so they clearly apply to every option.

A comparison table implies that the options are comparable. Say when they compose, when one is a subset of another, or when the decision is actually about sequencing rather than selection.

### Minimal counterexample

Use to repair a misconception. Take the reader's rule, construct the smallest case where it predicts the wrong result, show the actual result, name the missing distinction and restate the rule. The counterexample should be small enough to hold in working memory.

One counterexample refutes a universal claim, not a statistical or probabilistic one. Say which kind of claim is under discussion.

### Zoom levels

Use when a system spans scales. Give three levels, such as one request, one service and one deployment, and say what changes at each level. Connect the levels explicitly: which part of the request view appears in the service view, and which service view becomes a box in the deployment view.

Do not imply that the levels are separate systems. They are views of one system, and a failure can cross all three.

## Analogy limits

An analogy is a loan against the reader's existing model; the limits are the interest. Map relations, not just nouns, and state where the mapping stops.

| Analogy | Carries | Breaks when | Repair |
| --- | --- | --- | --- |
| Pipe or plumbing | Flow, pressure, bottlenecks | Fluids are conserved; data can be copied, dropped or replayed | Say "copies, not a fixed amount" |
| Warehouse | Storage, retrieval, capacity | Goods do not expire or conflict; access control and consistency differ | Add expiry and concurrent writers |
| Recipe | Ordered steps and prerequisites | Cooking tolerates variation and has no rollback; code can fail partially | Add a failure branch |
| Contract | Obligations, expectations and breach | A human contract is interpreted; a software contract is enforced by code and tests | Say who enforces it |
| Ledger | Append-only history and audit | A ledger is authoritative; a log may be compacted, replicated or eventually consistent | Name the guarantee |
| Mailbox or queue | Buffering, ordering, delivery | Mail is addressed and durable; queues may drop, redeliver or reorder | State the delivery semantics |
| Thermostat or control loop | Feedback, setpoint and oscillation | A thermostat has one loop and a physical plant; distributed control has delay and competing actors | Add delay and competing controllers |
| Budget or currency | Consumption, limits and cost | Money is conserved and fungible; quotas may expire, reset or be refunded | State the accounting rule |
| Traffic | Congestion, throughput and priority | Traffic has self-interested actors; schedulers enforce policy | Do not imply fairness |
| Filing cabinet or index | Lookup, keys and duplicates | Real indexes have stale entries, write costs and consistency rules | Name them |

Rules for analogies:

- Announce the mapping: "X is like Y in that..., but not in..."
- Use one analogy per idea. Retire it explicitly when the mechanism lands.
- Never let an analogy establish safety, security, correctness or a numeric limit.
- Avoid analogies that import blame or agency: "the database decides" hides the code that decides.
- Prefer the reader's domain. For a cook, a kitchen analogy beats a factory; for a network engineer, a postal analogy may be worse than a routing one.

## Worked examples

A worked example earns its place when it makes a rule checkable. Keep one path, a small cast, concrete values and visible state before and after. Include one decision or failure point. Use synthetic data and label it.

Three useful shapes:

1. **Trace.** Follow one request through authentication, cache lookup, storage and response. Show the state at each step.
2. **Contrast pair.** Send the same input through two configurations and show different results. This teaches which variable matters.
3. **Counterexample.** Show the prediction from the old model beside the observed result. This teaches the missing distinction.

A retry example can carry idempotency without a long definition:

| Attempt | State before | Request | Result | Stored effect |
| --- | --- | --- | --- | --- |
| 1 | No order | Create order `A` | Timeout after the write | Order `A` exists |
| 2, no key | Order `A` exists | Create order `A` | Success, new record | Two orders |
| 2, key `A` | Order `A` exists | Create order `A` with key `A` | Original result returned | One order |

The example shows why a retry key changes the outcome. It does not establish the key retention window, concurrent requests with the same key, or side effects that are not idempotent. Those are boundary cases, not footnotes to omit when they affect the reader's design.

## Check-understanding questions

Ask one question at a time and wait. The question should distinguish the intended model from the likely wrong one; recall of terminology is rarely discriminating.

| Target | Question shape | A good answer shows | A weak answer points to |
| --- | --- | --- | --- |
| Restate | "In one sentence, what is X?" | Own words, no analogy | A vague rung 1 |
| Predict | "What does the next request see if...?" | A traced mechanism | Missing rungs 3–4 |
| Transfer | "How would this change for a batch job?" | The model applied to a new case | An overfitted analogy |
| Contrast | "Why not just do Y?" | The constraint or tradeoff | Missing rung 5 |
| Boundary | "When would this be the wrong choice?" | Cost, limit or failure mode | Overgeneralization |
| Diagnose | "This is slow; where would you look first?" | A causal chain | An inventory without causality |
| Teach-back | "Explain it to a new teammate in two minutes." | Selection of the load-bearing idea | Detail without priority |

Question etiquette:

- Do not lead with the answer inside the question.
- Do not use terminology the explanation has not defined.
- Follow the error to the rung it reveals instead of repeating the whole explanation louder.
- Keep the check proportionate. A quick intuition needs one question, not an exam.

## Anti-patterns

- **Analogy as proof.** The analogy illustrates; the mechanism and evidence establish.
- **Definition chain.** A sequence of definitions with no model or example leaves the reader unable to predict anything.
- **Curriculum dump.** Everything known about the topic, in the order the explainer learned it.
- **Line-by-line narration.** Restating syntax or message fields instead of explaining the invariant and the path.
- **"Simply" and "under the hood".** Both claim ease while withholding the mechanism.
- **Premature formalism.** Notation before the reader knows what the notation describes.
- **Confirming example only.** An example that works under the stated rule but never probes its edge.
- **Hiding the hard part.** Moving the difficult step into "and then it works" or "the system handles it".
- **Contradiction without replacement.** Correcting a wrong model but leaving nothing in its place.
- **Invented numbers or rationale.** A clean benchmark or historical reason that was never observed.
- **One perspective as fact.** Presenting a design choice as the only reasonable option, without its alternatives or costs.
- **Explaining with the thing itself.** Using the unexplained term, diagram or code as the definition.
- **Quiz as gotcha.** A check designed to catch the reader rather than locate the missing rung.
- **Repetition as emphasis.** Saying the same thing in stronger words instead of adding the missing distinction.

## Sources and fit

The pattern catalog is a local synthesis for this repository. It is informed by [Diátaxis: Explanation](https://diataxis.fr/explanation/) for bounded, perspective-aware understanding; [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience, scope and compare-and-contrast openings; and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) for skimmable structure, examples and currency.

The analogies and worked examples are original and synthetic. They illustrate explanation mechanics; they are not evidence about any particular product or standard.
