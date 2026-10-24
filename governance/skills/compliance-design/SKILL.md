---
name: compliance-design
description: Translate applicable legal, contractual and assurance requirements into
  system boundaries, controls, ownership and evidence. Use during product/system design
  or a scoped compliance assessment; distinguish engineering work from legal interpretation
  and independent assurance.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Connect obligations to system decisions

Establish the intended service, customers/jurisdictions, data processing, delivery model and requested decision. Identify existing commitments, authoritative interpretations and current evidence. Separate a statutory duty, customer contract, voluntary assurance goal and product preference; they have different applicability and decision owners. A small change needs assessment of affected obligations, not an exhaustive organizational audit.

## Establish applicability and authority

Investigate relevant facts before asking the user to settle a tradeoff.

- Record the source, version/date where useful, affected entity/process and why a requirement appears applicable.
- Consult primary material for substantive interpretation using the [source guide](../../references/sources.md).
- When legal or assurance interpretation remains material, identify the exact unresolved question and qualified decision owner; do not ask the user to guess technical facts or invent an approved interpretation.

Describe the service or processing operation to which the requirement applies. Follow the data and responsibility through people/processes, application and infrastructure, identity, vendors, support, telemetry and recovery. Identify who controls each part and where a supplier or customer must perform an action. A requirement may apply to that whole operation rather than a single code repository.

Use this boundary to decide what the project can demonstrate and what needs evidence from elsewhere. Hosted region, encryption, a provider attestation or a passing scanner can answer a particular question, but each leaves other responsibilities unexamined. Preserve that scope when explaining readiness or gaps.

## Derive proportionate controls

For each material applicable obligation or commitment, preserve this reasoning chain:

```text
applicable obligation or commitment
→ intended outcome
→ control, owner and scope
→ implementation and operation
→ evidence and remaining exposure
```

For a proposed control, explain what outcome it protects, where it operates, who maintains it, and how failure becomes visible. Compare prevention, detection and recovery according to the risk: blocking an invalid operation, identifying a missed activity and restoring affected data address different consequences. Reuse adequate accepted controls and explain any uncovered part before adding policy machinery.

Check that the proposed evidence would establish the control's intended operation. Configuration can show how a control is implemented; evidence from the relevant period and population can show whether it operated. Keep design, implementation, observed operation and independent assessment distinct. Describe remaining exposure and any proposed acceptance honestly.

Carry decision consequences into affected product requirements, architecture, implementation, operating procedures and verification. Seek available security, data, delivery and operations expertise by capability; without it use project evidence and primary sources at the same standard. If obligations change intended usage, data handling, spending, retention or customer commitments, present concrete options and seek the unresolved authorized decision while continuing independent work.

## Make evidence useful and bounded

Evidence should identify the control/property, relevant population/period, actual source and reviewer/owner where needed.

- Preserve exceptions and gaps.
- Protect sensitive records and collect only what the assurance purpose needs.

| Evidence | Supports |
| --- | --- |
| Versioned code or configuration | Implementation |
| Performed review or recovery exercise | Operation |
| Generated policy or planned test alone | No proof that the activity occurred |

Preserve the distinction from independent assessment.

Return the scoped applicability/control decisions, evidence and remaining gaps. Use existing project records; no fixed spreadsheet, tracker or compliance platform is required. A readiness assessment does not certify compliance, submit filings, accept terms or authorize production changes.
