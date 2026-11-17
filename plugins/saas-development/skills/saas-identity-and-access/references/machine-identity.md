# Machine identity and service credentials

Use when a non-human client calls the product or when the product calls another service on
a tenant's behalf. Machine credentials need an owner, a purpose, a scope and a removal path;
without them they accumulate as permanent access.

## Choose the credential shape

| Shape | Suitable when | Main risk |
| --- | --- | --- |
| API key | A server or integration needs a simple long-lived secret scoped to a tenant. | Broad scope, difficult rotation, leakage in logs or repositories. |
| OAuth client credentials | A service needs scoped, revocable tokens and standard token handling. | Client-secret storage, token lifetime and scope design. |
| Service account | An automation or integration needs its own identity, ownership and audit trail. | Orphaned accounts and inherited privileges. |
| Short-lived workload identity | The platform can issue identity to a workload without a static secret. | Misconfiguration and trust-policy scope. |
| Delegated user token | An integration acts for a specific user with their consent. | Over-broad scopes, stale consent and revocation gaps. |

Prefer the narrowest shape that supports the integration. Do not give an automation a
human owner's full session token, and do not let a shared key stand in for several tenants.

## Scope and ownership

Record for every credential:

- the tenant or organization it acts for;
- the environment (test, staging, production);
- the actions and resources it may reach;
- the human or team owner and the integration purpose;
- creation time, expiry or rotation interval and last use;
- the revocation procedure and who may invoke it.

Scope to a tenant and a purpose. An account-wide key that happens to be filtered by code is
one bug away from cross-tenant access. If the provider supports per-tenant credentials,
use them; if not, keep a local mapping and test that an unmapped or cross-tenant request is
rejected.

## Issue, display and store

- Generate secrets with sufficient entropy and a recognizable prefix for scanning.
- Show the secret once at creation; store a hash or a provider reference, not the plaintext.
- Separate credentials by environment and never reuse a test key in production.
- Keep secrets out of source, build logs, error reports, analytics and client bundles.
- Support multiple active credentials during rotation and record the overlap window.

A credential shown in a dashboard, screenshot or support transcript should be treated as
compromised and rotated.

## Rotation and revocation

Define a rotation interval from the credential's exposure and the provider's capability, not
from a universal policy. Support:

- creating a replacement before revoking the old credential;
- observing last use to avoid breaking an active integration;
- immediate revocation on suspected compromise, owner departure or integration retirement;
- a bounded propagation window through caches, gateways and token introspection;
- customer-visible revocation for credentials the customer owns.

A revoked key must fail on the next request within the promised window. If the product uses
cached authorization, test the cache path rather than only the database row.

## Audit and anomaly detection

Log credential use with the credential identity (not the secret), tenant, action, source
and outcome. Alert on:

- use from an unexpected location, network or user agent where the risk warrants it;
- a spike in failed authentication or authorization;
- a credential used outside its tenant or scope;
- a long-unused credential suddenly active;
- creation of highly privileged credentials.

Audit records should let an owner answer "what did this credential do" without exposing the
secret or unrelated customer data.

## Agents and delegated automation

An AI agent or automation acting for a user is a delegated principal. Keep its credential
narrower than the user's full authority, scope it to the task's tenant and resources, and
require the same server-side authorization as a human request. Do not place a broad token
in a prompt or tool configuration and rely on the model to behave.

## Evidence

| Behavior | Evidence |
| --- | --- |
| Scoped access | Credential can reach its tenant's resources and is denied another tenant's. |
| Rotation | Old and new credentials overlap without downtime; old one fails after revocation. |
| Immediate revocation | Revoked credential fails within the accepted window, including cached paths. |
| Owner departure | Credential is found and revoked or reassigned. |
| Audit | Use is attributable to a credential, tenant and action without logging the secret. |
| Compromise response | Revocation, investigation and replacement are exercised or documented. |

A key list in an admin screen is not evidence that keys are scoped, rotated or revoked.
Exercise the denial and revocation paths.
