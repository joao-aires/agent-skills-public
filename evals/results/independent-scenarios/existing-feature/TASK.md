# Feature request

Add **tags** to tasks and support filtering the list by tag.

Requirements:

- `add` accepts one or more tags without breaking the existing `add "title"` form.
- `list --tag <tag>` shows pending tasks with that tag.
- `list --all --tag <tag>` shows all tasks with that tag.
- Existing JSON files without tags remain readable.
- Existing `list`, `list --all`, `done` and test behavior must be preserved.
- Add or update tests for tags, filtering and backward compatibility.

Inspect the skill library at `/Users/joao/Projects/products/agent-skills-artifact-quality` and use whatever guidance you find relevant. Do not modify the skill repository. Work only in this directory. Produce the change, tests and a short evidence record in `docs/`.
