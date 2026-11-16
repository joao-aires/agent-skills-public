# New application request

Build a small local **notes** command-line application from scratch.

Requirements:

- `python notes.py add "text"` stores a note and prints its id.
- `python notes.py list` lists notes.
- `python notes.py search "term"` finds notes containing the term.
- `python notes.py delete <id>` deletes a note.
- Notes persist in a local JSON file; `NOTES_DATA` overrides the path.
- No third-party dependencies.
- Include tests using the standard library and a README with exact commands.
- Preserve a clear separation between the CLI, storage and search behavior.

Use the installed `sdlc` skills. Start from planning and requirements, then design, implementation, tests and review. Produce `docs/ecr.md`, `docs/design.md`, `docs/verification.md` and `EVAL.md` in this directory. Do not edit the skill repository.
