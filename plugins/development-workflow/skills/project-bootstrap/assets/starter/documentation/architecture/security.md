# Security boundaries

Argon2 password hashes, unpredictable opaque sessions stored as hashes, expiry/revocation, HttpOnly/SameSite cookies, secure cookies by default and exact trusted-Origin checks for unsafe requests. Every note query filters owner ID server-side. API tests prove revocation, negative auth/ownership, validation and CSRF. No public production claim: add abuse limits, email verification/recovery, deployment TLS/trusted-host setup and session lifecycle cleanup before public exposure. No credentials or note content in request logs.
