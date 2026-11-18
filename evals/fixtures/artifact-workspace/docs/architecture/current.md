# Current architecture

Status: current, verified at revision `4f2a1c`.

- `api` accepts note requests and writes PostgreSQL.
- `worker` polls the same database and produces exports.
- PostgreSQL is the only shared data boundary.
