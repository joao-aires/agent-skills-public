# Skill routing

Read project-profile.json, scoped AGENTS.md and the local contract for the current task before upstream guidance. User instructions and application decisions remain authoritative. A skill is expertise, not permission to broaden scope or enable tools.

| Task | Local contract | Acquired specialist skills |
| --- | --- | --- |
| Scope/bootstrap | project-bootstrap | business-strategy when selected |
| Python/API/data | build-python-backend | modern-python |
| UI implementation | build-consistent-frontend | shadcn, vercel-composition-patterns, vercel-react-best-practices |
| Browser journey | test-end-to-end | playwright-cli |
| Failure diagnosis | deliver-reliable-changes | systematic-debugging |
| Completion | verify-delivery | verification-before-completion |
| CI/CD | deliver-reliable-changes | github-actions-hardening |
| Documents | maintain-documentation | architecture-diagraming when selected |
| AI | build-evaluated-ai | Selected ADK or LangChain skills, never both by default |
| MCP authoring | build-python-backend | mcp-builder when selected |
| Risk review | deliver-reliable-changes | Optional code-review, differential-review, property-based-testing |

Only claim a specialist is available after reading its installed metadata. Use task-relevant references; do not load the whole catalogue. Version-match application libraries. Upstream provider examples, design preferences, interview steps or approval rituals do not change accepted local choices. Preserve tests and assertions during debugging.

## Existing design guidance

Inventory the current client's installed skills and record selected names/paths in a local ignored file, not in this public template. Preserve compatible user-installed design skills. Apply them within documentation/ux/design-system.md and existing shadcn components. Do not introduce a second visual system or copy private skills into distributable plugins.

## Installation evidence

Record client/version, installed paths, discovered names, a task that invoked the local contract plus a relevant specialist, and resulting test evidence. A directory copied to disk is structural installation evidence; it is not proof that a client discovers or invokes it. No MCP capability exists until configured and tested separately.
