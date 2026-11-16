# CCPA/CPRA applicability and system decisions

Use when California consumers, employees, applicants or business contacts are in scope, or
when a customer asks about California privacy. The California Consumer Privacy Act, as
amended by the California Privacy Rights Act, is a distinct regime from the GDPR. Do not
reuse a GDPR assessment as a CCPA assessment without checking definitions, roles, rights and
notice mechanics.

Confirm the current statute and regulations with the responsible privacy/legal owner. The
CPPA's regulations change; this guide supplies engineering questions, not a legal
conclusion, certification or filing.

## Establish applicability

The CCPA generally applies to a for-profit business that does business in California and
meets at least one current threshold, such as gross revenue, volume of consumers/households
whose personal information is bought, sold or shared, or a revenue share from selling or
sharing personal information. The thresholds are adjusted over time.

Establish:

- whether the entity does business in California and meets a current threshold;
- which people are consumers under the Act, including employees, applicants and B2B
  contacts where applicable;
- which processing is in scope, including analytics, advertising, support and provider use;
- whether the organization acts as a business, service provider, contractor or third party
  for each operation;
- whether any exemption applies, and who owns that interpretation.

Do not infer that a California user, a California hosting region or a `.com` domain alone
creates applicability or excludes it. Record the facts and the unresolved legal question.

## Distinguish the roles

| Role | Meaning for the design |
| --- | --- |
| Business | Determines the purposes and means of processing and owes consumer rights and notice obligations. |
| Service provider | Processes on the business's behalf under a written contract with the required restrictions. |
| Contractor | A service provider with a distinct contractual relationship under the Act. |
| Third party | Receives personal information outside the business/service-provider relationship. |

A vendor is not a service provider merely because the contract says so. The actual data
use, purpose limitation, sale/share restrictions and subcontractor terms must match. A
provider that uses the data for its own purposes or cross-context advertising may be a
third party, which changes notice, opt-out and contract consequences.

## Translate consumer rights into system behavior

| Right or obligation | System question |
| --- | --- |
| Know/access | Can the service locate the categories and specific pieces of personal information for the verified consumer across primary, derived, provider and backup stores? |
| Delete | Can it delete the consumer's data and direct service providers to delete, while handling retention exceptions and backups? |
| Correct | Can it correct inaccurate personal information and propagate the correction to derived stores and providers? |
| Opt out of sale/share | Can it stop the relevant disclosure, including cross-context behavioral advertising, and propagate the choice to tags, pixels and providers? |
| Limit sensitive personal information | Can it restrict use and disclosure to the permitted purposes, and distinguish sensitive from other data? |
| Non-discrimination | Does the product avoid denying service or charging differently because a consumer exercised a right, except where permitted? |
| Notice at collection | Does the collection point state the categories, purposes and retention period before or at collection? |
| Privacy policy | Does it describe categories, sources, purposes, recipients, retention and rights, consistent with actual practice? |

Verification is part of the right, not an obstacle to it. Establish the required degree of
certainty for the request and data type, how authorized agents are handled, and how the
service avoids disclosing another person's data. Record statutory timelines in the operating
procedure and verify them against the current regulations rather than relying on memory.

## Sale, sharing and opt-out signals

"Sell" and "share" have specific meanings. Sharing includes disclosing personal information
for cross-context behavioral advertising, even without money changing hands. Common product
features that can trigger the obligation include advertising pixels, audience matching,
third-party analytics configured for advertising and data enrichment.

- Inventory tags, SDKs and provider purposes; do not assume that a vendor labelled
  "analytics" is outside sale/share.
- Provide the required "Do Not Sell or Share My Personal Information" link and, where applicable, the "Limit the Use of My Sensitive Personal Information" link; honor the choice across the actual disclosure paths.
- Treat a recognized opt-out preference signal, such as Global Privacy Control where the regulations recognize it, as a request where required; verify the current signal and scope.
- Record the consumer's choice, the date and the systems that received it.
- Do not require a new account or unnecessary verification to honor an opt-out.

A consent banner alone does not establish that opt-out propagates to every provider. Test
the downstream path, including cached tags and server-side events.

## Service-provider and contractor terms

For each provider that processes personal information, establish:

- the written contract and its purpose limitation;
- prohibition on selling or sharing outside the permitted purpose;
- restrictions on retaining, using or disclosing the information;
- subcontractor notice and flow-down terms;
- the business's audit or assessment rights;
- deletion or return at termination;
- how the provider handles consumer requests and assists the business.

Keep the executed contract and the actual data flow aligned. A contract clause does not
prevent a misconfigured pixel or an unapproved provider use.

## Retention and minimization

CPRA added purpose limitation, data minimization and retention expectations. For each
category, establish why it is collected, how long it is retained and what triggers deletion.
Disclose the retention period or the criteria in the notice.

Retention must be enforceable in the system, not only stated in a policy. Include logs,
analytics, backups, support transcripts and provider-side copies in the retention map.

## Relationship to the GDPR

| Concern | CCPA/CPRA | GDPR |
| --- | --- | --- |
| Legal basis | Does not use the GDPR's lawful-basis model; obligations center on notice, purpose limitation and opt-out rights. | Requires a lawful basis for processing. |
| Sale/sharing | Specific opt-out rights for sale and cross-context behavioral advertising. | Broader consent/legitimate-interest analysis; ePrivacy rules may also apply. |
| Sensitive data | Sensitive personal information with a right to limit certain uses. | Special categories with a prohibition unless a condition applies. |
| Consumer scope | Includes employees, applicants and B2B contacts in many cases. | Applies to data subjects broadly, with different employment context rules. |
| Enforcement | CPPA and Attorney General; limited private right of action. | Supervisory authorities and private remedies under member-state law. |

A joint assessment can reuse the data map and provider inventory. It cannot reuse the legal
analysis without checking each regime's definitions and the actual jurisdiction.

## Evidence

| Evidence | Supports | Limit |
| --- | --- | --- |
| Current applicability memo with facts and owner | Scope decision | Not a legal opinion unless the qualified owner adopts it. |
| Data map and category inventory | Rights, notice and retention | Does not prove request handling. |
| Tag/pixel/provider inventory with purposes | Sale/share assessment and opt-out scope | Configuration may drift; re-inspect. |
| Verified request log | Rights operation | Sampling and completeness need review. |
| Opt-out propagation test | Choice reaches downstream systems | One provider or path is not the whole population. |
| Executed service-provider contract | Contractual role | Does not establish actual practice. |
| Retention job evidence | Deletion/retention operation | Backups and derived stores may remain. |

A privacy policy, a banner or a vendor's certification does not establish compliance. Report
the assessed scope, evidence, exceptions and unresolved legal questions; do not certify the
service or submit anything to a regulator without separate authorization.
