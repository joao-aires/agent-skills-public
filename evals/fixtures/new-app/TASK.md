# New application request

Build a small local **notes** command-line application from scratch.

Requirements:

- `python3 notes.py add "text"` stores a note and prints its id.
- `python3 notes.py list` lists notes.
- `python3 notes.py search "term"` finds notes containing the term.
- `python3 notes.py delete <id>` deletes a note.
- Notes persist in a local JSON file; `NOTES_DATA` overrides the path.
- No third-party dependencies.
- Include tests using the standard library and a README with exact commands.
- Preserve a clear separation between the CLI, storage and search behavior.
