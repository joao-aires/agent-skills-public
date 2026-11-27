---
name: skill-authoring
description: Create, revise or review a skill in this collection. Use when adding a capability, deciding between a new skill and an expansion, writing or shortening SKILL.md, choosing references/scripts/assets, defining triggers, composing optional plugins, or evaluating whether a skill changes agent behavior. Not for writing a product document or a one-off prompt.
user-invocable: true
metadata:
  kind: method
  domain: documentation
  phase: cross-phase
  scope: generic
  invocation: both
---

# Author a capability, not a documentation page

A skill is a scoped capability contract. It tells an agent what outcome it owns, how to reach it, which judgment and local standards matter, what evidence proves completion, and what to load, execute or look up.

This method is the operational loop for creating or revising one. The repository maintainer guide owns the repository-wide rule; [writing-for-agents](../writing-for-agents/SKILL.md) owns instruction-writing mechanics; [technical-writing](../technical-writing/SKILL.md) owns prose craft. Do not duplicate those methods here.

## Reading path

| Need | Read |
| --- | --- |
| Choose the skill shape, boundary or progressive-disclosure layer | [Skill design](references/skill-design.md) |
| Review behavior, tests, repository integration or maintenance | [Review and integration](references/review-and-integration.md) |
| Write the prose inside a document or explanation | [Technical writing](../technical-writing/SKILL.md) |
| Apply the repository-wide knowledge-ownership rule | The maintainer guide's “Own the capability, disclose the detail, link the authority” section |
| Check the current audit and follow-up list | The repository guidance audit |

## Decide what kind of change this is

| Need | Action |
| --- | --- |
| The same outcome is already owned, but the method, examples or references are thin | Expand the existing skill. |
| A different outcome, stopping point, authority or evidence is needed | Add a skill. |
| The work is a stable lookup rather than a capability | Add or expand a reference; do not create a skill for lookup alone. |
| The work is deterministic, repetitive or error-prone | Add a script, not a longer procedure. |
| The output needs a stable template, fixture or asset | Add an asset, not prose describing the file. |
| A different install boundary is useful and at least three cohesive skills exist | Consider a plugin. |

State the nearest adjacent skill and why this one is different. If you cannot name the boundary, the change is probably an expansion.

## Define the capability contract

Before drafting, establish:

- **Outcome.** What can the agent do afterward that it could not reliably do before?
- **Trigger.** Which requests, contexts and near-misses should reach this skill? Put the trigger in the description, not only in the body.
- **Stopping point.** Where does the skill deliberately stop? What is a different activity?
- **Evidence.** What observable result, artifact or check shows the work is complete?
- **Authority.** What may the agent read, write, publish, execute or deploy?
- **Local standard.** Which convention, invariant or accepted decision is specific to this collection?
- **External authority.** Which facts belong to a framework, provider or specification?
- **Composition.** Which optional capabilities might deepen the work, and what happens when they are absent?

A skill that cannot state its stopping point usually overlaps an activity. A skill that cannot state its evidence usually cannot be reviewed.

## Choose the form

| Form | Use when |
| --- | --- |
| Activity | The user requests an outcome with authority, modes and a stopping point. |
| Method | A reusable discipline supplies judgment, selection criteria or procedure. |
| Workflow | A specific ordered sequence is reused across activities. |
| Reference | Lookup material is stable, conditional and too large for the entry point. |
| Guide | One artifact type needs a writing/production method. |

`kind` describes this conceptual layer; `role` describes task versus support packaging. They are not invocation permissions. Use the repository metadata contract for the fields.

## Write the smallest complete contract

### Description

The description is the primary trigger. State what the skill does and the contexts that should reach it. Distinguish it from the nearest adjacent work. Avoid a description that only names a topic; it will under-trigger or collide with a broader skill.

For an expertise skill, open with the area and the word expertise: "Expertise and methods for `<area>` (`aliases`): `<coverage>`." Then state the trigger and the boundary. Use "Informs `<adjacent>`; `<owner>` owns the decision" for adjacent work the method can help with. Reserve "Not for" for genuine exclusions such as another artifact type or authority the skill does not hold.

### Body

Keep the entry point focused on what every invocation needs:

1. the job and boundary;
2. the reading path for conditional detail;
3. the method, decisions or steps;
4. local standards, invariants and failure modes;
5. completion evidence and limits;
6. optional composition.

Explain why a rule matters when the reason changes how the agent applies it. Prefer a causal explanation to an unexplained `MUST`. A rigid sequence is appropriate only when ordering is a real dependency or safety invariant.

Each step should end on a completion criterion the agent can recognize. For a flat reference skill, state the exhaustiveness or review demand instead.

### Progressive disclosure

| Material | Home |
| --- | --- |
| Outcome, triggers, authority, decisions, every-path guidance | `SKILL.md` |
| Stable checklists, decision tables, examples, source notes | `references/` |
| Deterministic transformation or validation | `scripts/` |
| Templates, fixtures, icons, output assets | `assets/` |

Inline what every branch needs. Disclose what only some branches need. A reference needs a clear trigger and a reason to read it. A large reference should have a table of contents. Keep `SKILL.md` legible; line count alone is not the test, but a body approaching 500 lines usually has branch detail to disclose.

### Knowledge ownership

Own the judgment and procedure. Disclose the branch detail. Execute the deterministic part. Link or verify the external authority.

Keep API signatures, flags, config keys, exact syntax, version matrices, pricing and full tutorials out of durable skill text unless the detail is a local safety invariant, a non-obvious trap or an offline fallback. When the external authority changes, the skill should need a link or version note, not a rewrite.

## Compose without assuming installation

Name optional capabilities by capability or skill name, say when they help, and state the fallback. Do not make the core outcome depend on another plugin. Do not link across package boundaries; a standalone build will not contain the target. Use links only within the same package.

If a capability is absent, retain the essential reasoning and evidence standard using project evidence and primary sources. Missing optional guidance is not permission to lower the standard.

## Test the skill

A passing validator proves packaging, not behavior.

1. **Define realistic test prompts.** Include the intended request, a near-miss that should use another skill, and a case with missing optional capabilities.
2. **Run with and without the skill** where the harness allows it. For an improvement, compare against the previous version.
3. **Check the output and the transcript.** Did the agent choose the skill, follow the method, stop at the right point and produce the evidence?
4. **Write negative controls.** A clear failure signal is more useful than another positive example.
5. **Revise the method, not the examples.** Do not overfit the skill to the test prompts.
6. **Record what was executed.** A definition check, a local fixture and a live provider run establish different evidence.

Use the repository's the repository evaluation guide for scenario definitions and evidence limits.

## Integrate and maintain

- Add the skill under `plugins/<bundle>/skills/<name>/` with matching folder and frontmatter name.
- Declare the required metadata and native invocation controls.
- Update the owning plugin version when packaged content changes.
- Update the source catalogue, counts, generated skills map and migration notes when the inventory changes.
- Add or update evaluation cases.
- Run the validation, link, registry, build and test commands in the the repository maintainer guide.
- For an upstream acquisition, follow the the repository upstream-maintenance policy; never edit acquired bytes.

Keep each meaning in one authoritative place. When a fact already lives in the environment, a generated inventory or another skill, link or read it instead of caching a copy.

## Review pass

Before finishing, run the [prose review](../technical-writing/references/prose-review.md) on the skill body. One check is specific to skills: the first sentence states the job and where the skill stops, and declarations stay in `## Composition`.

## Stop and review

Stop when the skill has a clear outcome, a working trigger, a method the agent can apply, evidence a reviewer can inspect and a maintenance path. More prose is not more capability.

If the skill is only a plan, a link list or a restatement of external docs, return to the capability contract. If the behavior is unmeasured, say so; packaging and a successful build do not establish that the skill changes what the agent does.
