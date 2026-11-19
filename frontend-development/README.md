# Frontend development plugin: interface decisions, precedent, language and journey evidence

The `frontend-development` plugin carries the generic methods for deciding what a user interface should be and for checking that the built journey works: interface design, precedent research, interface copy, usability study design and journey verification.

It does not own product direction, framework implementation, backend authority or design-tool installation. Two acquired design-method bundles are included as optional expertise; they are inputs to the local decision, not replacements for it.

## Purpose

Use this package when the question is what users see, read or do, or whether they can complete a journey. It composes with the product and design activities that accept scope, the selected React or native package that implements the surface, and the verification and release activities that decide what happens next.

## Conceptual model

Five local methods separate the decision from its inputs and its evidence. Two acquired systems supply candidate material and an alternative critique workflow.

| Layer | Question | Owner |
| --- | --- | --- |
| Design decision | What should this interface be, how should it behave, and what is the handoff? | [interface-design](skills/interface-design/SKILL.md) |
| Precedent | What have comparable shipped products already established? | [design-research](skills/design-research/SKILL.md) |
| Language | What do the labels, instructions and errors actually promise? | [ux-writing](skills/ux-writing/SKILL.md) |
| Participant evidence | Can intended users complete the task, and what did observation show? | [usability-research](skills/usability-research/SKILL.md) |
| Journey evidence | Does the built journey work across real surfaces, states and platforms? | [testing-journey](skills/testing-journey/SKILL.md) |
| Candidate material | Which styles, palettes, type pairings and UX rules are worth considering? | `ui-ux-pro-max` (acquired) |
| Alternative craft workflow | What does a rendered critique, refinement or rebuild conclude? | `impeccable` (acquired) |

Research informs the decision, copy expresses it, usability evidence judges it with participants, and journey testing verifies the implementation. None of these layers silently becomes the design decision.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [interface-design](skills/interface-design/SKILL.md) | method | Navigation, hierarchy, interaction contracts, shared composition, accessibility behavior, design review and handoff | An accepted or delegated direction plus rendered checks | Product scope, framework mechanics or participant evidence |
| [design-research](skills/design-research/SKILL.md) | method | Research question, comparable set, observation versus inference, rights and access limits | Evidence and a comparable option set | Choosing the direction or copying a shipped design |
| [ux-writing](skills/ux-writing/SKILL.md) | method | Labels, instructions, validation, errors, empty states and confirmations in task context | Copy that fits the actual behavior and voice | Changing behavior, permissions or product commitments |
| [usability-research](skills/usability-research/SKILL.md) | method | Study questions, tasks, neutral guides, observation notes and synthesis of supplied sessions | A defensible finding or an explicitly proposed study | Inventing participants, quoting unobserved behavior or generalizing beyond the sample |
| [testing-journey](skills/testing-journey/SKILL.md) | method | Journey claims, platform and evidence choice, automation, exploration and failure diagnosis | A verified journey, a reported gap or a failing check | Unit coverage, load testing or release approval |
| [impeccable](skills/impeccable/SKILL.md) | method (upstream) | Its own design, redesign, critique, polish and animation workflow across web, native and design-system targets | Output of the selected mode | Becoming the project's design authority or a mandatory baseline |
| [ui-ux-pro-max](skills/ui-ux-pro-max/SKILL.md) | method (upstream) | Searchable style, palette, typography, icon, motion, chart and UX-rule candidates | Candidate material to evaluate | Research evidence, accessibility proof or a fixed aesthetic |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Design brief, discovery, direction and handoff | [design discovery](skills/interface-design/references/design-discovery.md), [visual direction](skills/interface-design/references/visual-direction.md) |
| Choosing among bundled design systems | [bundled design methods](skills/interface-design/references/bundled-design-methods.md) |
| Rendered inspection and visual review | [rendered QA](skills/interface-design/references/rendered-qa.md), [visual review](skills/interface-design/references/visual-review.md) |
| Precedent research method | [research methods](skills/design-research/references/research-methods.md) |
| Acquired systems and licences | `skills/impeccable/UPSTREAM-NOTICE.md`, `skills/ui-ux-pro-max/UPSTREAM-LICENSE.txt` |
| Optional reference libraries | [mcp.json](mcp.json) |

## Reading paths

1. **New product surface** → [interface-design](skills/interface-design/SKILL.md) for scope and depth → [design-research](skills/design-research/SKILL.md) for precedent → three materially different directions → handoff → [testing-journey](skills/testing-journey/SKILL.md) on the built slice.
2. **Visual or interaction refinement** → [interface-design](skills/interface-design/SKILL.md) → render and inspect the actual surface → [ux-writing](skills/ux-writing/SKILL.md) when wording is part of the defect.
3. **Copy repair** → [ux-writing](skills/ux-writing/SKILL.md) → [interface-design](skills/interface-design/SKILL.md) only if the fix changes hierarchy or behavior.
4. **Usability question** → [usability-research](skills/usability-research/SKILL.md) to design the study → [interface-design](skills/interface-design/SKILL.md) to act on the finding.
5. **Journey failing in a real environment** → [testing-journey](skills/testing-journey/SKILL.md) → [interface-design](skills/interface-design/SKILL.md) for the repair → [ux-writing](skills/ux-writing/SKILL.md) when the message caused the failure.

## Boundaries

- **Product direction.** Which problem, segment and outcome to pursue belongs to the product and design activities; a design request does not reopen accepted branding or scope.
- **Implementation.** Framework, component-library, styling and native-platform mechanics belong to the selected frontend package. This package stops at a handoff and rendered acceptance evidence.
- **Backend and tenancy.** Authority, permissions, tenant isolation and persistence belong to backend, SaaS and security capabilities. Interface states must express their outcomes, not reimplement them.
- **Design tooling.** A design-tool request does not install Figma, Mobbin or Refero, and a declared MCP endpoint does not establish authenticated access.
- **Evidence.** A screenshot does not prove keyboard behavior, persistence or participant success. A heuristic review is not a usability study.
- **Acquired systems.** `impeccable` and `ui-ux-pro-max` retain their upstream controls and bodies. When their advice conflicts, the local decision reconciles against accepted product direction, the design system, accessibility requirements and observed evidence.

## Authority and optional tools

[mcp.json](mcp.json) declares optional endpoints for Figma, Mobbin and Refero. Declaration is not connection; MCP access for Mobbin and Refero requires a paid plan, and the package's methods work without them. Publishing a design, capturing a participant, contacting a customer or changing a production surface requires scope from the request and the relevant account.

## Acquired sources

| Skill | Source | Pin | Licence |
| --- | --- | --- | --- |
| `impeccable` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | `c3bb418` | Apache-2.0 |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `b7d5353` | MIT |

## Maintenance

Owning sources are the local `SKILL.md` files and their references, plus the acquired folders recorded in the maintainer source catalogue. Update this README when the local method split, an acquisition or the implementation boundary changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests, and recheck acquisition pins through upstream maintenance.
