# Current architecture

Status: current at revision `9c31ab`.

- `api` accepts export requests and writes PostgreSQL.
- `worker` polls PostgreSQL and writes files to object storage.
- `web` reads export status from `api`.
