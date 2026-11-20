# Proposed export architecture

Status: proposed, not implemented.

Introduce a queue between `api` and `worker` so large exports do not poll the database.
