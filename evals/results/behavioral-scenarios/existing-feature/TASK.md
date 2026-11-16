# Feature request

Add **tags** to tasks and support filtering the list by tag.

Requirements:

- `add` accepts one or more tags without breaking the existing `add "title"` form.
- `list --tag <tag>` shows pending tasks with that tag.
- `list --all --tag <tag>` shows all tasks with that tag.
- Existing JSON files without tags remain readable.
- Existing `list`, `list --all`, `done` and test behavior must be preserved.
- Add or update tests for tags, filtering and backward compatibility.

Use the installed `sdlc` skills. Produce `docs/ecr.md`, `docs/design.md`, `docs/verification.md` and `EVAL.md` in this directory. Do not edit the skill repository.
