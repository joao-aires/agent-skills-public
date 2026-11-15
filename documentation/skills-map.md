# Skills map

Generated from `SKILL.md` metadata and `agent-depot.json` labels. Open [skills-map.html](skills-map.html) for the filterable explorer.

## The simple model

```mermaid
flowchart LR
  P[Packs / install boundaries] --> S[Skills]
  S --> W[Activities]
  S --> G[Methods and guides]
  S --> C[Contracts]
  W --> A[Artifacts]
  G --> A
  C --> A
  A --> V[View artifacts]
  D[Dimensions: phase, role, software type, home, evidence] -.-> S
  D -.-> A
```

Two core models, one method layer, three cross-cutting dimensions:

- **Activity** — what work is requested and where it stops.
- **Artifact** — what durable output exists, with authority, home, maturity, relations and evidence.
- **Method** — how to deepen or produce the work; `guide-*` methods own artifact craft.
- **Dimensions** — phase, role, software type, home and evidence filter the two core models.

## Counts

119 skills · 21 plugins · 4 packs · 19 domains

| Pack | Skills |
| --- | ---: |
| `sdlc` | 58 |
| `technical` | 50 |
| `craft` | 7 |
| `product` | 4 |

| Kind | Skills |
| --- | ---: |
| `method` | 78 |
| `activity` | 30 |
| `workflow` | 9 |
| `system` | 2 |

## Artifact guides

| Guide | Domain | Use for |
| --- | --- | --- |
| [guide-compatibility-matrix](../plugins/sdlc/skills/guide-compatibility-matrix/SKILL.md) | development | Guide to producing and reviewing a compatibility matrix. Use for public surfaces, versions, platforms, runtimes, deprecation, migration and consumer evidence across libraries, CLIs and APIs. |
| [guide-state-machine](../plugins/sdlc/skills/guide-state-machine/SKILL.md) | development | Guide to producing and reviewing state machines. Use for states, triggers, guards, terminal states, denied transitions, invariants and concurrent or retried behavior. |
| [guide-design-spec](../plugins/sdlc/skills/guide-design-spec/SKILL.md) | frontend | Guide to producing a design specification that implementation can build and verify from. Covers flows, wireframes, mockups, prototypes, states, content, components, responsiveness, accessibility, motion, assets, handoff and design QA. |
| [guide-c4-view](../plugins/sdlc/skills/guide-c4-view/SKILL.md) | visualization | Guide to producing and reviewing C4 context, container and component views. Use for system boundaries, actors, responsibilities, directed dependencies, current versus proposed state and text equivalents. |
| [guide-sequence-view](../plugins/sdlc/skills/guide-sequence-view/SKILL.md) | visualization | Guide to producing and reviewing sequence views. Use for participant responsibilities, request ordering, synchronous versus asynchronous work, branches, failure, retry and recovery. |

## Full inventory

Run `python scripts/skill_map.py` to regenerate this page and the HTML explorer. The generated HTML is the filterable view; this page is the stable summary.
