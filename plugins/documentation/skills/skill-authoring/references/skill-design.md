# Skill design decisions

Use this reference when the capability is understood but its shape is still open.

## New skill, expansion or something else

| Signal | Decision |
| --- | --- |
| Same outcome, stopping point and evidence; only examples or detail are thin | Expand the existing skill or its references. |
| Different outcome, authority, evidence or stopping point | New skill. |
| Stable lookup material used only in some branches | Reference; no new skill. |
| Deterministic transformation, validation or generation | Script. |
| Stable output template, fixture or binary asset | Asset. |
| Different install boundary with several cohesive skills | Plugin. |
| No behavior change after the draft | Do not ship it. |

Name the nearest adjacent skill and the boundary. If a reader would not know which one to choose, the design is not finished.

## Capability contract

Write these before prose:

- outcome and intended user;
- trigger contexts and near-misses;
- stopping point and authority;
- required artifacts or observable result;
- evidence and limits;
- local standards and invariants;
- external authorities to verify;
- optional composition and fallback.

A skill that cannot state its stopping point is probably an activity. A skill that cannot state its evidence is probably a topic.

## Kind and role

`kind` is conceptual: `system`, `activity`, `method`, `workflow`, `guide` or `reference`.
`role` is packaging: `task` or `support`.

They are independent. A method can be a task entry point; an activity can be support in a larger composition. Native invocation controls are separate again. Use [metadata](https://github.com/joao-aires/agent-skills-public/blob/main/docs/metadata.md) for the current fields and meanings.

## Description and trigger

The description is the primary trigger. It should state:

- what the skill enables;
- the contexts that should reach it;
- what distinguishes it from the nearest adjacent skill.

Specific branches are better than a list of synonyms. Do not put all “when to use” detail only in the body; the body is not read until the description wins.

Test the description against realistic prompts, including near-misses. A skill that never triggers is not available; a skill that triggers adjacent work is a collision.

## Information hierarchy

| Tier | Content | Loaded |
| --- | --- | --- |
| Metadata | Name, description | Always |
| Body | Outcome, method, decisions, local standards, completion criteria, pointers | On selection |
| Reference | Conditional checklists, examples, source notes, compatibility detail | On demand |
| Script | Deterministic operation | On execution |
| Asset | Output template, fixture, icon, font | On use |

Put every-path guidance in the body. Disclose branch detail. Inline a definition beside its rules rather than scattering it.

A reference needs a trigger and a reason to read it. A large reference needs a table of contents. A script needs a clear interface and failure behavior. An asset needs an owner and a stable format.

## Steps, reference or both

A procedure needs ordered steps when order is a real dependency or safety invariant. A method with judgment needs decisions, criteria and failure modes rather than a false sequence. A review skill can be mostly flat reference with an exhaustiveness demand.

Do not turn a judgment call into a rigid recipe. Do not leave a real dependency implicit. Each step needs a recognizable completion criterion; a flat reference needs a clear review demand.

## Knowledge ownership

| Knowledge | Home |
| --- | --- |
| Outcome, stopping point, authority, local convention | Skill body |
| Stable checklist, decision table, example, source interpretation | Reference |
| Deterministic operation | Script |
| API signature, flag, config key, syntax, version matrix | External authority |
| Pricing, quota, plan limit, vendor claim | External authority or dated vendor note |
| Environment fact, generated inventory | Environment or generated check |

The rule: own the judgment and procedure, disclose branch detail, execute the deterministic part, link or verify the authority.

Keep external detail only when it is a safety/authority invariant, a local convention, a non-obvious trap, an unreliable or inaccessible source, a minimal orientation name or an offline fallback.

## Composition

Name optional capabilities. State when they help and what the fallback is. Do not require another plugin for the core outcome. Do not link across package boundaries; use a capability name instead.

Examples:

- a release activity composes with a pipeline method and a provider implementation, but still performs its own boundary and verification checks;
- a backend design method composes with architecture, API, event and distributed-system methods, but retains its own service contract;
- an evaluation method composes with a selected runner, but does not require it.

## Examples from this collection

| Skill | Shape | Why it works |
| --- | --- | --- |
| `design` | Activity | Owns the decision, authority, option set and stopping point; delegates domain methods. |
| `release` | Activity | Owns target, authorization, verification and recovery; pipeline design is separate. |
| `architecture-patterns` | Method | Owns forces, pattern candidates and costs; the architecture decision stays with `design-system`. |
| `ai-evaluation` | Activity | Owns the evaluation program; method, runner and delivery remain separate. |
| `guide-ecr` | Guide | Owns the artifact shape; the contract owns required content. |
| `cli-development` | Method | Owns the command surface; shell implementation and packaging mechanics are separate. |

Use these as shape examples, not templates to copy.
