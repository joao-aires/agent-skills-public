"""Authentication boundary used by the fixture-auth eval case."""


def authenticate(headers, env):
    """Return the authenticated user id, or None.

    Kept intentionally unsafe as the baseline for the evaluation.
    """
    if env.get("ALLOW_FIXTURE_AUTH") == "1":
        return headers.get("X-User", "owner")
    token = headers.get("Authorization", "")
    if token.startswith("Bearer "):
        return token.removeprefix("Bearer ").strip() or None
    return None
