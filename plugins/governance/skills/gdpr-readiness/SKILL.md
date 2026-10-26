---
name: gdpr-readiness
description: Assess GDPR applicability and engineering readiness for an actual service
  or changed processing operation. Use for personal-data flows, privacy-by-design,
  rights/retention/provider consequences and evidence gaps rather than reproducing
  the regulation.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Assess the actual processing operation

Establish the service, entities, people affected, purposes, categories/sensitivity, locations and provider/data flows. Determine which processing operation is being assessed and whether the organization's role differs across customer data, account administration, analytics or model/provider use. Preserve accepted interpretations and distinguish facts from unresolved legal judgments. Read [applicability and system decisions](references/applicability-and-decisions.md) for conditional concerns and [official sources](../../references/sources.md) when determining substantive requirements.

## Establish applicability from facts

Consider establishment and relevant offering/monitoring activity, not just server location, nationality or the product being commercial.

- Establish controller/processor roles from actual purposes/means and relationships; do not infer that every SaaS vendor is always only a processor.
- Record material uncertainties and seek the appropriate legal/business interpretation when required.
- Assess relevant national/sectoral and ePrivacy requirements separately where the actual feature raises them.

For each processing purpose, establish the accepted basis, necessary data, transparency and retention.

Consent is not a universal fallback and a privacy notice does not establish a lawful basis.

### When processing raises additional concerns

Check special-category/children's data, profiling or other elevated-impact processing when present. Investigate whether a DPIA or other responsibility applies; neither impose one for every feature nor silently omit it.

## Translate requirements into the system lifecycle

Follow each assessed processing purpose through the actual data lifecycle. Identify where data first enters, which people and services can access it, what it is used for, and which copies or derived forms are created. Include logs/analytics, AI/provider requests, exports and recovery paths, since these can continue processing data outside the main application record.

Use the lifecycle map to ask implementation questions against the accepted interpretation:

- Which fields are necessary?
- How is access limited?
- Where is retention enforced?
- How can the system locate relevant data when handling a request?

Keep the legal requirement and the chosen engineering mechanism distinguishable. A change in purpose or provider must be assessable without treating the old design as proof of continued applicability.

- Minimize fields and exposure; use suitable defaults, access controls and purpose/retention boundaries.
- A regional deployment does not settle remote support, subprocessors or international transfers.
- Identify actual provider arrangements and required decisions using current official guidance.

Design applicable rights handling around request authority, search/matching scope, response obligations and justified exceptions.

- Deletion must account for derived stores/providers and restored backups; retained data needs restricted handling and a defensible purpose rather than a silent promise of immediate erasure everywhere.
- Avoid exporting another person's data while satisfying a request.

## Assess readiness and gaps

Inspect representative data flows, configuration and exercised request/retention/recovery behavior. Check operating ownership for access, requests, provider changes, incidents and required records. Distinguish implementation, actual operation and proposed remediation; a checklist or successful test is not a legal conclusion.

Return the processing scope, supported applicability findings, proposed/accepted decisions, evidence and prioritized gaps. Cite the relevant official provision/guidance beside consequential interpretations. Ask only for unresolved legal/product choices that change the outcome, and keep external submissions, new processing and live deletion within separately authorized scope.
