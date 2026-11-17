# Organization and membership model

Use when defining the organization, workspace, role or invitation contract. Keep the model
small enough to enforce consistently and explicit enough to explain a denial.

## Entities and relationships

| Entity | Owns | Notes |
| --- | --- | --- |
| User | A person's authentication identity and personal profile | May belong to several organizations; the user is not the tenant. |
| Organization | The primary customer/tenant boundary, billing relationship and ownership | Can contain workspaces and resources. |
| Workspace | A grouping of resources within an organization | Decide whether it is a permission boundary, a billing unit or a view. |
| Membership | The link between a user and an organization with a role | Per-organization; removal affects sessions and jobs. |
| Role | A named set of permitted actions | Built-in or custom; must be enforceable server-side. |
| Invitation | A pending grant of membership to a recipient | Bound to organization, role, expiry and intended recipient. |
| Service account | A non-human principal owned by an organization | Has its own credentials and owner. See [machine identity](machine-identity.md). |
| Ownership | The authority to administer and eventually close the organization | At least one owner must remain. |

Decide whether a deployment, an environment or a database is a tenant. A logical tenant
can share infrastructure, but every resource still needs one owning organization. Do not
let a workspace silently become the billing customer unless that is the accepted product
model.

## Membership rules

- Joining requires an invitation, an accepted domain/SSO rule or an authorized
  administrative action. Self-service creation of a new organization is a separate path.
- A membership carries one role, or a small set of grants that the product can explain.
- Role changes take effect at the next trusted check; existing sessions need a bounded
  revalidation window.
- Removing a member removes their organization access, active invitations and service
  credentials they personally own; decide what happens to resources they created.
- A user may leave voluntarily; the last-owner invariant still applies.
- Guest or external membership is a scoped membership with explicit expiry and resource
  access, not an unauthenticated share link.

Record the effective role and the source of the grant (invitation, SCIM group, manual
administration, ownership transfer). A role that cannot be traced to a source is difficult
to review and revoke.

## Roles and permissions

Separate these questions:

| Question | Owner |
| --- | --- |
| Who is this user? | Authentication. |
| Is this user a member of this organization? | Membership. |
| May this member perform this action on this resource? | Resource permission. |
| Has this organization paid for this capability? | Entitlement, owned by `saas-billing`. |

Define the smallest roles that support real work: owner, administrator, member, billing
contact, read-only or guest. Add custom roles only when customers need them and the product
can test their boundaries. A role name is not a policy; enumerate the actions and resources
it permits, including bulk, export and administrative operations.

Privileged actions such as ownership transfer, organization deletion, SSO configuration and
support access need additional confirmation and audit. Do not let a general administrator
role imply every privileged operation by default.

## Invitations

An invitation is a grant waiting to happen. Establish:

- who may invite and which roles they may grant;
- how the recipient is identified and how the invitation is delivered;
- the expiry and whether it can be resent or revoked;
- whether the same email can hold invitations to several organizations;
- what happens if the recipient already has an account or is already a member;
- how a domain restriction or SSO requirement affects acceptance;
- whether accepting twice creates duplicate membership.

Possession of a forwarded link is not proof that the recipient is the intended person.
Verify the signed-in identity against the invitation's recipient or use a single-use token
bound to that identity. Do not let an invitation silently upgrade an existing member's role.

## Ownership transfer and last owner

The last-owner invariant prevents an organization from becoming unadministrable. Define:

- whether an owner can leave while remaining the only owner;
- how a new owner is nominated and how acceptance is proven;
- whether transfer requires two-person approval or a cooling-off period;
- what happens to the previous owner's role and active sessions;
- how a stranded organization is recovered through support without bypassing audit.

Transfer is a domain operation with a recorded initiator, recipient, acceptance time and
resulting membership. A database update alone does not establish that the recipient
accepted or that the previous owner's access was reduced.

## Removal, closure and data

When a member is removed, decide what happens to:

- their sessions, personal API keys and delegated tokens;
- resources they created or exclusively own;
- scheduled jobs, integrations and webhooks authorized by them;
- audit records and support notes that reference them.

When an organization is closed, follow `saas-design` for export, deletion, retention and
backup handling. Organization deletion is not a cascade that can leave provider data,
search indices or analytics untouched.

## Evidence

| Behavior | Evidence |
| --- | --- |
| Cross-organization access denied | Request by a member of another organization returns no resource data. |
| Invitation replay or wrong recipient | Second acceptance fails; mismatched identity is rejected. |
| Role escalation prevented | Inviter cannot grant above their permitted role. |
| Last owner protected | Removal/leave is refused or requires a completed transfer. |
| Removal propagates | Existing session/job loses access within the accepted window. |
| Duplicate membership avoided | Concurrent acceptance produces one membership. |
| Ownership transfer | Initiator, recipient, acceptance and resulting roles are recorded. |

A role matrix in documentation is not evidence that enforcement matches it. Exercise the
actual server-side path, including bulk and export operations.
