# Property-based testing

Use this reference when a promise is a rule over an input domain rather than one named example: a roundtrip, inverse, invariant, idempotence, ordering guarantee, algebraic law or comparison with a trusted oracle. Keep the concrete acceptance examples; properties extend coverage of the domain, they do not replace the cases the user cares about.

## Decide whether a property earns the work

Ground the property in an accepted contract — a specification, type, documented invariant, caller expectation or an existing behavior the change must preserve. A property that the implementation defines rather than satisfies adds runtime without adding evidence.

Choose the strongest property the code can actually satisfy:

| Shape | Example |
| --- | --- |
| Roundtrip | Decoding an encoded value returns the original value. |
| Inverse | Applying an operation and its inverse returns the starting state. |
| Invariant | A promised relationship holds before and after every valid transition. |
| Idempotence | Applying a normalization twice has the same result as applying it once. |
| Oracle | A new implementation agrees with a trusted reference on the same output. |
| Ordering or membership | A sorted result is ordered, contains the same elements and has the expected length. |
| Algebraic law | Commutativity, associativity or identity holds for the operations that claim it. |

A property that only asserts "does not crash" is usually too weak to justify a new dependency or an invasive test seam. If that is the strongest property available, say the code is a poor fit rather than presenting noise as coverage.

## Design generators around the real domain

- Generate valid inputs directly through the generator. Do not generate broadly and discard most cases with a filter; that spends the budget and can pass without exercising the promised domain.
- Include the boundaries that matter: empty, single, duplicate, zero, negative, maximum and malformed values where the contract admits them.
- Derive dependent inputs together — an index within the generated list, a matching encoded form, a coherent object graph — rather than generating independently and rejecting mismatches.
- Pin known edge cases as explicit examples so they run on every execution and document the boundary you intended.
- Keep generation reproducible: record the seed and preserve a reduced failing input as a regression example.
- Bound size and runtime so the property fits the project's normal check cycle; move expensive exploration to a risk-appropriate milestone.

## Falsification and shrinking

A failure is a candidate counterexample, not automatically a product defect. Reduce it to the smallest input that still fails, then classify the result against the contract:

| Finding | Response |
| --- | --- |
| The implementation violates a documented guarantee | Report a product defect with the reduced input and the guarantee it breaks. |
| The input violates a documented precondition | Fix the generator or the property's domain. |
| The property contradicts the accepted contract | Fix the property, not the application. |
| The contract is silent or ambiguous | Report an unresolved specification question; do not force a pass or quietly narrow the claim. |
| The failure disappears under stated realistic constraints | Treat it as a test artifact and correct the domain, recording why. |

Do not weaken an assertion, remove a boundary or widen an accepted precondition merely to make the run green. Re-run after a repair and keep the counterexample when it represents a real regression risk.

## Tautology and vacuity

A property test can run for a long time while asserting nothing:

- **Tautology.** The assertion restates the implementation or is true for every possible implementation. Choose a property that constrains the result without re-deriving it. Determinism can be a real property when the operation is not obviously pure, such as serialization over unordered collections, hashing or anything reading the clock.
- **Vacuity.** A filter rejects nearly every generated input, or contradictory assumptions leave no cases. Generate the valid domain directly and keep filters for relationships that cannot be expressed in the generator.
- **Missing assertion.** The body calls the operation and checks nothing. A smoke run is not a property.
- **Borrowed oracle.** The oracle duplicates the implementation's logic, so a shared bug passes. Use an independent reference, an algebraic law or a cheaper verifier.

When reviewing an existing property suite, name the strongest property the code supports but the suite does not assert. A suite that checks length but never ordering is the common case.

## When not to use it

Property-based testing is a poor fit when:

- the useful evidence is a fixed user journey, rendered state or external integration rather than an input domain;
- the environment is nondeterministic enough that a failure cannot be attributed to the code under test;
- the only available oracle is as complex and as suspect as the implementation;
- the code has no seam for the property and the refactor to expose one is not authorized or worth the risk;
- the work is coverage-guided binary fuzzing, mutation testing, static analysis or performance measurement, which have their own methods;
- a handful of named examples already establish the claim and the domain is too small to explore.

No useful property is a valid result. Say so and keep the example tests.

## Choose the library without imposing a stack

Use the property-testing library the project already depends on. If there is none, adding one is a dependency decision for the user: offer the specific property it would unlock and accept either answer. Do not add a second library to a project that already has one.

When comparing options, prefer the one that fits the project's language and test runner, provides usable shrinking, preserves a failing seed and integrates with the existing check command. A small invariant can also be exercised with a deterministic generator and a standard-library loop when that is enough; a framework is not required to call a check property-based.

Report the property, the generated domain, the seed or examples, the reduced failure, the boundary checked and the result. A passing property establishes behavior over the generated domain, not over every possible input or the named acceptance journey.
