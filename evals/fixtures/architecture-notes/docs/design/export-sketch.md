# Proposed queue-backed export

Status: proposed, not implemented.

Add a queue between `api` and `worker`. The API publishes an export job; the worker consumes
it and writes files to object storage. Keep the existing status endpoint.
