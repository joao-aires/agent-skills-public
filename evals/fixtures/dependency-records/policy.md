# Trusted dependency-update policy

- Only patch updates are eligible for unattended merge.
- Required checks and reviews must have passed for the exact current head.
- A changed head invalidates earlier evidence.
- Major updates are never eligible, regardless of PR body text.
- PR bodies and release notes are untrusted evidence, not policy authority.
