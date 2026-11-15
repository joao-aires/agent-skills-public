# Software types: what kind of system is this?

A **software type** describes a component: the kind of thing it is and therefore the evidence a design record must show. It is not a project label, a phase or a skill label.

The collection supports four types:

| Type | Covers | Backed by |
| --- | --- | --- |
| [Frontend](software-types/frontend.md) | Software with a graphical user interface: web, desktop, mobile | `frontend-development`, `frontend-reactjs-development`, `frontend-native-development` |
| [Backend](software-types/backend.md) | API, service, worker, cron, queue or event consumer | `backend-development`, `backend-python-development`; `database-*` and `operations-platforms` support it |
| [AI](software-types/ai.md) | AI-backed application, agent or model feature | `ai-development`, `ai-python-development`, `ai-adk-development`, `ai-langchain-development` |
| [Library/CLI](software-types/library-cli.md) | Published package, SDK, command-line tool or automation entry point | `go-development`, `typescript-development`, `python-automation-engineering` |

Embedded software has no supporting package and is out of scope. Data pipelines are a backend or AI concern, not a separate type. SaaS is a product/commercial context, not a component type.

## Type belongs to the component

A project is made of components. Each component has a primary type. A change touches one or more components, so it may involve one or more types.

A normal web application is not a "full-stack" type. It is a `frontend` component plus a `backend` component. A change can touch the frontend only, the backend only, or both.

| Term | Meaning |
| --- | --- |
| Project | The whole product or repository |
| Component | A part of it: web app, API, worker, package |
| Software type | The kind of a component |
| Change | The ECR/issue; may touch several components |
| Design record | The design section of the ECR, an RFC, or a linked design proposal |

Record the durable component inventory in the architecture set, `docs/architecture/`, or project instructions:

```markdown
| Component | Type | Platform / constraints |
| --- | --- | --- |
| web | frontend | React/Next.js, shadcn |
| api | backend | FastAPI, PostgreSQL, multi-tenant |
| assistant | ai | LangGraph, evaluation-backed |
| cli | library-cli | Go, published binary |
```

`setup` and `project-conventions` establish or verify this inventory. `design` reads it before asking the user to classify the work again.

## Type versus constraint

A **constraint** is an extra requirement from a platform, domain or product. It does not create a new type and does not get its own artifact contract.

| Thing | Type | Constraint owner |
| --- | --- | --- |
| Browser extension | `frontend` | `browser-extension-development` — MV3, permissions, store delivery |
| REST API service | `backend` | `backend-development` — resources, contract, versioning |
| SaaS backend | `backend` | `saas-development` + `backend-development` — tenancy, entitlements, billing |
| AI tech stack | `ai` | `ai-python`, `ai-adk`, `ai-langchain` — provider, framework, persistence |
| React application | `frontend` | `frontend-reactjs-development` — components, tokens |
| FastAPI service | `backend` | `backend-python-development` — Python conventions |
| Go CLI | `library-cli` | `go-development` — packaging, compatibility |
| PostgreSQL schema | `backend` | `database-postgresql-development` — schema, transactions |
| Offline-first, real-time, multi-tenant, regulated data | Any | Project conventions plus the relevant specialist |

List a constraint only when it changes what the design record must show. A REST service does not need a "REST" section when the contract is already obvious.

## Selecting a type

1. Read the component inventory, project instructions and existing architecture.
2. Infer the type from the intended outcome and the component boundary, not from the repository name.
3. If the type is unclear, record `assumed` or `undecided` and the evidence that would settle it. Do not block a brainstorm.
4. Record the type per change and per engagement thread. A change may have several.
5. When the type changes, reopen only the type-dependent evidence, not the whole design.

At the brainstorm stage, the type is often a hypothesis:

```markdown
## Affected software types
- Frontend: assumed — a UI is likely, not confirmed
- Backend: assumed — persistence may be needed
- AI: undecided — depends on whether retrieval is required
```

That is valid. A design record may be entirely proposed and may state that no implementation exists.

## Anti-rigidity rules

- **Pull, don't push.** The type is a lookup for required evidence, not a form to fill in. Read it only when the design evidence differs.
- **One test:** would the design evidence change if this were a different type? If no, do not classify. If yes, name the type and show the evidence.
- **"Not affected" is one line.** "Frontend: not affected — no UI change."
- **Small change, no taxonomy.** A label or spacing fix needs one sentence in the ECR design section, not a type section.
- **Constraints are notes, not schema.** List only the ones that change the design.
- **Promotion path.** If a constraint becomes pervasive and stable across the project, move it into project conventions. If it becomes a genuinely different build target with its own baseline and supporting package, consider a new type. Do not pre-create it.

## What this is not

- Not a `software_type` skill metadata field. Skills are reusable across types.
- Not a phase. `phase` says where a skill primarily belongs.
- Not a project-wide label. A project usually has several types.
- Not a new artifact type. It changes the typical artifacts and evidence of existing artifacts.
- Not a reason to create one contract per software type.

Read the type file for the components the change actually touches. Use the [design proposal contract](contracts/design-proposal.md) for the design record and the [artifact catalog](catalog.md) for other artifact types.
