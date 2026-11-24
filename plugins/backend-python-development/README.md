# Backend Python development plugin: FastAPI, persistence and Python automation

The `backend-python-development` plugin carries implementation guidance for Python services and operational tooling: FastAPI and SQLAlchemy structure, Alembic migrations, modern project tooling and automation design. It is stack-specific and applies to an accepted backend design.

## Purpose

Use this package when the decision depends on Python mechanics: how to shape a FastAPI service and its persistence layer, how to evolve a schema safely, how to configure a modern Python project, or how to build a maintainable operational automation with a real CLI.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [backend-conventions](skills/backend-conventions/SKILL.md) | method | FastAPI/SQLAlchemy structure, API contracts, auth, sessions, jobs and Alembic migrations |
| [modern-python](skills/modern-python/SKILL.md) | method (acquired) | Project tooling with uv, ruff and ty; new projects, scripts and migrations |
| [python-automation-engineering](skills/python-automation-engineering/SKILL.md) | method | Operational automation and reporting tools with ergonomic CLIs, typing and tests |

## Boundaries

- Service behavior, authority, transactions and failure contracts belong to backend design; this package implements them.
- Infrastructure, pipelines and release authorization belong to delivery and platform packages.
- Generic language selection and framework comparison remain with the design activity.

### Acquired sources

| Skill | Source | Pin |
| --- | --- | --- |
| modern-python | trailofbits-skills | `82fe822` |

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](../../docs/maintainers/upstreams.md) and never edit the upstream body.
