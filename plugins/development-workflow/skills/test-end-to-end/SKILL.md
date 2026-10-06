---
name: test-end-to-end
description: Plan, write or debug end-to-end tests for important application journeys, including real integration, persistence and authorization behavior.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Test what users depend on

- Use Playwright for important browser journeys. Start with the main useful flow, then add failure cases that matter to the product.
- For full-stack claims, exercise the actual frontend, API and migrated PostgreSQL database. Check persisted state after reload or a new session, and verify that one user cannot access another user's resources.
- Keep test data isolated and repeatable. Use the application's real authentication path where authentication is part of the journey.
- Use unit and integration tests for focused logic and edge cases. Mock external providers when useful, but state the boundary: a mocked test does not prove the live provider or full application works.
- Keep CI reliable and proportional. Capture traces/screenshots for failures, investigate the cause, and avoid masking failures with arbitrary delays, endless retries or weakened assertions.
- Inspect affected UI on representative mobile and desktop sizes. Include keyboard access, focus, labels and meaningful loading/error/empty states when relevant.
- Use available Playwright expertise for exploration and debugging; retain committed tests for repeatable verification. Report the journeys actually exercised and any important gaps.
