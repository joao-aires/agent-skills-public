# Notes service authentication

`auth.authenticate(headers, env)` returns the authenticated user id or `None`.
`notes.read_note(user, note_id)` enforces ownership. Standard library only.

Accepted requirement: fixtures are a local/test convenience only and must be rejected in
production. The baseline implementation is known to be unsafe.
