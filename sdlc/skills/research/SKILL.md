---
name: research
description: Investigate a question against primary sources and return traceable findings.
  Use when facts or behavior must be verified before a planning, refinement or design
  decision, or when reading work is delegated to a background agent.
user-invocable: true
metadata:
  kind: method
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
---

# Research: turn a question into traceable findings

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Existing user evidence that drives a product decision belongs to [run-product-feedback-analysis](../run-product-feedback-analysis/SKILL.md) and its analysis artifact; use a research report for any other bounded inquiry and link the analysis rather than restating it.

Research reduces the uncertainty that blocks a decision. The result is a defensible answer: what the evidence establishes, what it does not, and what the decision owner should do next. The [research report contract](../artifact-system/references/contracts/research-report.md) owns the record when one is warranted; [guide-research-report](../guide-research-report/SKILL.md) owns its craft. Use [artifact system](../artifact-system/SKILL.md) to choose the record and [artifact homes](../artifact-system/references/homes.md) to place it.

## Reading path

| Need | Read |
| --- | --- |
| What must the report contain? | [Research report contract](../artifact-system/references/contracts/research-report.md) |
| How should it be written and reviewed? | [guide-research-report](../guide-research-report/SKILL.md) |
| Source hierarchy, claim table and stopping test | [Investigation notes](references/investigation.md) |
| Where does the record live? | [Artifact homes](../artifact-system/references/homes.md) |
| What happens to the findings? | [plan](../plan/SKILL.md), [refine](../refine/SKILL.md), [design](../design/SKILL.md) |

## Frame the decision-changing question

Name the decision, the uncertain claim that blocks it and the observation that would change the answer. Agree on the boundary: which system, version, environment, population or period the answer must cover.

Start from what is already known in the request, code, decisions and prior reports. Do not re-investigate settled facts, and do not widen the question to make the research look thorough. When no plausible finding would change a decision, give a short answer and stop; a report would be ceremony.

A useful question has an owner and a consequence. "Which is true?" is not enough if either answer leaves the decision unchanged. "Can this integration retry without duplicating the charge, and what would make us choose a different retry design?" is research.

## Work from authority

Follow each claim to the source that owns it: the specification, source code at a revision, first-party documentation, the actual endpoint, the measured run or the accepted decision. A secondary write-up, generated summary or forum answer is a route to authority, not authority itself.

Separate three kinds of statement:

- **documented** — the source says the capability exists;
- **observed** — a probe or reading at a named revision produced the result;
- **inferred** — the conclusion you draw from either.

Do not let documented capability stand in for observed behavior when the decision depends on behavior. Read [investigation notes](references/investigation.md) when sources conflict, when the claim is consequential, or when you need the source hierarchy and claim table.

## Trace claims and keep disagreement visible

For every material claim, retain the authority, the exact revision, version or date, what it directly establishes, and its limit. When behavior matters, run the smallest probe that could distinguish the options, and record the environment, command and result.

Keep competing evidence in view. If a first-party document, the code and an observed run disagree, report the disagreement and investigate why; do not average it into false confidence. An unreachable authority is an explicit limit, not permission to cite a plausible substitute.

Prefer a revision or retrieval date over "current" or "latest." A claim that cannot be checked is recorded as unverified, with the evidence that would settle it, rather than dropped or made to sound certain.

## Decide whether the findings need durability

Answer in the conversation when the result is a bounded lookup and no one needs to revisit it. Choose a research report only when the findings must outlive the conversation, be reviewed by a decision owner, or be cited by later work. Do not create an artifact type or a second narrative: if the research supports an existing change, record the conclusion in that change's ECR and link the evidence.

Resolve the home before writing. The default is the engineering workspace; an application repository is acceptable only when the report is durable project knowledge and that home is authorized. Read the project instructions and artifact home map first. If the home is ambiguous, say so and ask rather than choosing an arbitrary path. Verify access and report the actual path or URL and revision.

Proportionality matters. A short inline answer is the normal result for a bounded factual question. A report earns its cost when the decision is consequential, the evidence is contested, or another owner must review the conclusion without replaying the investigation.

## Delegate or investigate inline

When a background agent is available, give it the decision, the boundary, the known evidence, the source rules above and the required output: recommendation, evidence, alternatives, limits and open decision. Keep working while it reads. Treat its summary as a pointer: check the cited source before accepting a decision-changing claim.

When no background agent exists, do the same work inline in the same order — frame, gather authority, probe, compare, record limits. State that the investigation is inline, proceed, and return the findings. Do not wait for a delegate that cannot exist, and do not lower the evidence standard because the work is local.

## Stop at findings

Return:

- the recommendation and its confidence;
- the condition that would reverse it;
- the strongest evidence, with revisions and limits;
- the credible alternatives and why they lost;
- the unresolved question, its owner and the next evidence that would settle it.

Do not record an accepted design, implementation plan or verification claim. Hand the findings to [plan](../plan/SKILL.md), [refine](../refine/SKILL.md) or [design](../design/SKILL.md) and let that activity own its decision. Stop when further work would improve phrasing or confidence without changing the decision. If the evidence is insufficient, say so and name what would settle it; do not fill the gap with a recommendation the evidence cannot carry.
