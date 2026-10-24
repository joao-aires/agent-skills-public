# Structure instructions around their meaning

Use this reference when writing or restructuring skills, repository instructions or other agent-facing guidance. Choose presentation for the decision or action the reader needs to find. Preserve the instruction's meaning and authority while making its organization visible.

## Teach the method before compressing it

Write for a capable practitioner who understands the field but has not reconstructed this particular method. A skill should explain how to approach its task: where to begin, what to inspect, how to interpret the result, and why a consequential choice follows. A list of concerns is useful as a reminder after that reasoning is clear; on its own it leaves the reader to supply the method.

When an instruction uses an abstraction such as a contract, invariant, boundary or verification, name the thing involved and what the practitioner does with it. Define domain terms when understanding them changes the work. Connect the action to its consequence so the reader can recognize when another approach would be appropriate. Retain the explanation at the point of use instead of scattering it across several small fragments.

Depth should resolve uncertainty about the task. Useful detail includes a distinction that changes a decision, a mechanism that makes the decision work, an assumption that limits it, or a way to recognize success and failure. Generic encouragement, repeated safeguards and longer restatements of a concern add reading without adding guidance. There is no target word count: a narrow skill can be short, while a substantial discipline needs room for its reasoning.

Examples earn their place when they clarify something the explanation cannot make sufficiently tangible. Keep useful existing examples and executable resources. Do not add a sample scenario or code block simply to make every skill look substantial; improve the explanation first. Detailed conditional procedures belong in linked references, with enough of the method in the entry point that readers know when they need them.

## Choose the structure locally

A skill can mix workflow and reference. Put shared purpose and essential constraints in the entry point; disclose substantial conditional detail through a link that says when to read it. A short skill may remain self-contained.

| Content | Useful treatment | Check |
| --- | --- | --- |
| Context, rationale or a causal explanation | Short connected paragraphs | Does the explanation make the decision understandable? |
| Parallel criteria, responsibilities or invariants | Bullets grouped under their shared subject | Are the items peers, with conditions and exceptions attached? |
| Actions with dependent prerequisites | Numbered sequence | Is this order necessary, or would numbering invent a requirement? |
| Alternatives assessed on common dimensions | Compact decision table | Can the reader compare applicability and consequences? |
| A branch used only in some tasks | A descriptive “When…” heading or conditional reference | Can the reader tell whether it applies? |
| An abstract rule that is easy to misapply | A small example with starting condition, action and result | Does it clarify the rule without adding a new default? |
| Completion evidence | A short list of observable outcomes | Does it distinguish performed work from a plan or claim? |

A comparison table does not imply that its rows are mutually exclusive. State when mechanisms compose, and keep a shared prerequisite outside the rows so it clearly applies to every option. Separate operating modes from authorization constraints that apply in every mode.

Use only the structures the content needs. Avoid replacing every sentence with a bullet, inserting a table for unrelated facts, or giving every skill the same sections. Labels help when readers need to locate a specific concern; bolding every item adds little hierarchy. Keep code, commands and contracts in their appropriate literal form.

## Keep the rule and its conditions together

Consider this instruction:

> When a deployment overlaps application versions, assess reader and writer compatibility, use bounded resumable backfills where needed, and verify the new representation before removing the old one.

A useful restructuring retains the applicability condition:

**When application versions overlap during deployment:**

- Assess reader and writer compatibility.
- Use bounded resumable backfills where needed.
- Verify the new representation before removing the old one.

The last item contains a real dependency. The list does not require every migration to use a backfill, prescribe a migration framework, or imply authority to change a live database. Retain such distinctions when reorganizing existing guidance.

For an approach comparison, use columns such as “Approach”, “Useful when” and “Tradeoff to resolve”. Fill them from supported guidance or evidence; a missing cell is a reason to investigate or choose another structure, not to invent a capability.

## Review the reader's path

For the skill's actual modes, ask:

- Can a reader determine when it applies and what scope it permits?
- Can they explain how to perform the work, including what they inspect and how a finding changes the next action?
- Can they locate a decision and understand its rationale without decoding shorthand or piecing together scattered fragments?
- Are alternatives, dependencies, optional techniques and required safeguards distinguishable?
- Can they find the relevant reference at the point it becomes useful?
- Can they identify completion evidence and remaining uncertainty?

Compare a revision against its source. Preserve invocation controls, accepted choices, fallback behavior, prerequisites, exceptions, authority boundaries and evidence limits. Check that moving a sentence has not changed its apparent applicability. Upstream-owned content keeps its provenance and adaptation policy.

A reader-question review can establish that the author checked those paths; it is not independent user validation. Link, metadata and package checks establish structural properties. Use behavioral trials when a consequential interpretation changes, and report their actual scope. Counts of headings, lists or tables do not establish comprehensibility.
