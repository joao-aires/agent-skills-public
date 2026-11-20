# Plugin README template

A package README is framing for two readers: someone deciding whether to install the package, and a maintainer deciding where a rule belongs. It is not a second skill catalog. Keep per-skill detail in `SKILL.md` and link the catalog or registry that already owns the list.

Use the template proportionately. A small package needs Purpose, Responsibilities, Boundaries and Maintenance; it can fold the rest into a sentence or two. A package with a real model — `sdlc` is the current example — keeps the model in the README and may link a `MODEL.md` appendix when the detail would crowd the default reading path. Aim for roughly 50–100 lines. A package that carries an artifact model and many skills will run longer; `sdlc` is the deliberate exception, not the target. Depth is justified by a model the reader must hold, not by completeness.

Compare the [sdlc README](../../plugins/sdlc/README.md) for a model-heavy package and the [documentation README](../../plugins/documentation/README.md) for a compact one.

## Template

```markdown
# <Package> plugin: <one-line job>

<One paragraph: what the package is for, and what it deliberately does not own.>

## Purpose

<The reader's job, the outcome the package enables, and the nearest package or model it composes with.>

## Conceptual model

<The few concepts a reader must hold to use the package. A short table or one diagram. Omit when the package has no model beyond its skill list.>

| Concept | Question it answers |
| --- | --- |
| <Concept> | <Question> |

If the model needs more than a screen, put the detail in `MODEL.md` and link it here with a reading trigger.

## Responsibilities

<Who owns what. One row per skill or coherent group; link the skill instead of restating its method.>

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [<Skill>](skills/<skill>/SKILL.md) | activity, method, guide, workflow, system or reference | <Responsibility> | <Boundary> | <Nearest adjacent owner> |

## How it materialized

<Map model elements to files, so a maintainer can change the right one.>

| Model element | Implementation |
| --- | --- |
| <Concept, contract or catalog> | <Skill, reference, script or generated file> |

## Artifacts

<Only when the package produces artifacts. Omit this section when it does not.>

| Artifact | Contract/template | Guide | Home |
| --- | --- | --- | --- |
| <Artifact> | <Contract or template> | <Guide or domain method> | <Where the authoritative copy lives> |

## Reading paths

<Three to five short sequences for real requests. Link the owner at each step.>

1. <Request> → <skill> → <artifact or decision>

## Boundaries

<What the package does not do, what its checks do not prove, and which adjacent package owns the missing work.>

## Authority and optional tools

<Action scope, approvals, external systems, MCP connections and optional dependencies. Say what is declared versus connected or exercised.>

## Maintenance

<Owning sources, generated files, validators, versioning and the trigger for updating this README.>
```

## Section notes

| Section | Keep it useful by | Leave it out when |
| --- | --- | --- |
| Purpose | Naming the outcome and the non-goal in the same paragraph | Never — a package needs a reason to exist |
| Conceptual model | Showing only concepts the reader must hold to use the skills | The package is a flat set of independent skills |
| Responsibilities | Making ownership and stopping points concrete | The package has one skill; fold ownership into Purpose |
| How it materialized | Connecting each model element to one place a maintainer can edit | The package has no model beyond its skill list |
| Artifacts | Pairing each artifact with its contract and guide | The package produces no durable artifacts |
| Reading paths | Starting from requests, not from the file tree | A single obvious path already appears in Responsibilities |
| Boundaries | Naming the adjacent owner of excluded work | Never — silence invites scope creep |
| Authority and optional tools | Distinguishing declared, connected and exercised | The package has no external systems or optional dependencies |
| Maintenance | Naming the owning sources and checks | Never — every README needs an update trigger |

## Keep the default readable

- Do not turn the README into a catalog of every skill, artifact or reference. Link the activity catalog, guide registry or contract index that owns it.
- Add a `MODEL.md` appendix when the conceptual model has more detail than a default reader needs. Link it from the model section with a clear trigger, and keep the README's summary sufficient on its own.
- Preserve the package's voice. A template is a checklist of concerns, not required prose or a fixed heading order.
- Update the README when ownership, boundaries, package composition or the model changes. Regenerating a generated inventory is not the same as revising the framing.
