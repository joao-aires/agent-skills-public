---
name: project-bootstrap
description: "Bootstrap or adopt the standard applications/ and documentation/ layout, scoped AGENTS.md instructions, project profile, documentation templates, and structural checks for new application projects."
---

# Project bootstrap

1. Read the root and scoped AGENTS.md files, existing code, package manifests, and documentation. Preserve established project choices unless the user asks for migration.
2. For a new project, use the bundled scaffold, rather than recreating conventions from memory:
   `python3 scripts/scaffold.py /absolute/project/path --ai none`
   Choose `--ai adk` or `--ai langchain` only when needed; add `--mcp` only for an actual MCP use case. Paths in this instruction are relative to this skill directory. The default scaffold writes conventions/documentation. Add `--starter` for the locked Project Notes reference application, then follow its runbook and execute its checks; copying a starter is not verification. Optional AI frameworks require their selected plugin/dependencies when a product needs them.
3. Read `references/project-contract.md`. Fill `project-profile.json` with actual package versions, verification commands, deployment choices, and selected upstream skill sources. Use `unresolved` rather than inventing decisions.
4. Install the workflow, backend, and frontend plugins as the full-stack profile; add ai-development when needed. Profiles are this repository's distribution convention, not portable plugin dependencies. Consult https://github.com/joao-aires/agent-skills-public/blob/main/documentation/upstream-sources.md and the stack plugins' bundled references to acquire relevant official skills; installation is a separate client operation.
5. Read and fill the PRD and initial architecture before implementing the smallest end-to-end slice. Record provisional choices as provisional; do not invent requirements.
6. Copy this skill's `scripts/check_project.py` to `applications/tooling/check_project.py` in a new project (the scaffold does this). Run it after creating or adopting the project.
7. Configure CI using real verification commands once runnable code exists. Root `.github/workflows/` contains GitHub workflow entrypoints; keep implementation scripts with each application.
8. Use `scripts/inventory_skills.py --root /actual/client/skills` to inspect existing design guidance without copying private content. New projects receive the helper under applications/tooling; keep local inventory reports ignored.
9. Report the chosen profile, scaffolded conventions, installed versus merely referenced skills, unresolved decisions, and checks actually run. Never claim an empty scaffold is an application.
