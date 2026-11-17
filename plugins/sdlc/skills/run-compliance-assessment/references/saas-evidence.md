# SaaS assurance evidence

Use when a hosted product must show customers, procurement or an assessor how it handles
their data and service commitments. The purpose is to connect each claim to a scoped control,
owner and evidence source, not to assemble a trust page.

## Start with the claim

Write down what is being asserted before collecting evidence. A customer may ask "where is
our data", "can you delete it", "who can access it", "are you SOC 2 certified" or "do you
support GDPR". These are different claims with different scopes and evidence.

For each claim, record:

- the service, environment and customer cohort it covers;
- the obligation or commitment behind it;
- the control that is intended to satisfy it;
- the owner and operating frequency;
- the population and period the evidence covers;
- what the evidence does not establish.

Reuse existing records. Do not create a second compliance universe because a customer asks
for a security questionnaire.

## Subprocessors

A subprocessor list should identify the entity, the service it provides, the data categories
and locations involved, and the mechanism by which customers are notified of changes.

Check:

- the list matches the actual production data flows, including analytics, support, email,
  hosting, error monitoring and AI providers;
- test and development environments do not quietly use additional providers with customer
  data;
- the notice mechanism and objection process match the contract;
- the list is current and has an owner and review cadence;
- a provider's own subprocessors are considered where the contract requires flow-down.

A list is a disclosure, not evidence that each provider is securely configured or that the
customer's data is limited to the stated purpose.

## Data processing agreements and contract flow-down

For each provider that processes customer personal data, establish:

- an executed DPA or equivalent terms, not only a link to a template;
- the roles (controller/processor or business/service provider) and the processing purpose;
- confidentiality and personnel obligations;
- security measures and breach notification;
- subprocessor terms and notice;
- assistance with data-subject/consumer requests;
- audit or assessment rights;
- deletion or return on termination;
- international transfer mechanisms where applicable.

Keep the contract version and the provider/service mapping. A DPA that covers one service
does not automatically cover a new product, region or data category.

## Residency and location

Residency evidence must cover the whole processing path, not only the primary database:

- application and data stores, including read replicas;
- backups and disaster-recovery copies;
- logs, analytics, error monitoring, search and queues;
- support access and remote administration;
- provider subprocessors and support organizations;
- metadata and control-plane data that may leave the region.

Record the actual configuration and the date inspected. A region selector, a provider's
data-centre list or an architectural diagram is a design claim; it does not prove that every
store and access path stays in the region.

## Export and deletion

Export evidence should show:

- what data is included, in what format and at what granularity;
- whether the export is complete for the tenant, including files, derived records and
  integration data;
- how access to the export is authorized and how long the export artifact is retained;
- whether a representative export was produced and inspected.

Deletion evidence should show:

- the request authority and scope;
- primary, derived, cached, search, analytics and provider-side copies;
- retention exceptions and their justification;
- backup handling and the risk of deleted data returning after restore;
- confirmation of deletion or a documented residual limitation;
- a representative exercise, including a restored environment where feasible.

A deletion button and a policy statement are not evidence that deletion reached every store.
Test the path and preserve the exceptions honestly.

## Audit logs

Audit logs support attribution and investigation. Establish:

- which events are recorded: authentication, authorization changes, administrative actions,
  support access, data export/deletion, configuration and billing changes;
- the actor, tenant, resource, action, time and outcome;
- integrity and access controls; an actor should not be able to edit their own trail;
- retention and export;
- time synchronization and clock assumptions;
- what is excluded for privacy or volume reasons.

Configuration of audit logging is not evidence that the relevant events were captured.
Inspect representative records and a gap or failure path.

## SOC 2 Type II evidence

A SOC 2 report is an independent examination of scoped controls over a period. It is not a
certification, a guarantee for every service, or a substitute for the application's own
controls.

When a customer asks for SOC 2 Type II evidence, establish:

- the report period and whether it covers the customer's service and environment;
- the Trust Services criteria and the system description scope;
- the controls tested and any exceptions or qualified opinions;
- subservice organizations and complementary controls;
- the bridge letter for the gap between the report period and the current date;
- whether the customer's contractual use permits sharing the report;
- which customer responsibilities remain.

A Type I report covers design at a point in time; a Type II report covers operating
effectiveness over a period. Neither establishes that a new feature, a new region or a
provider outside the scope is covered.

Do not describe the service as "SOC 2 certified". Report what the examined scope and period
support, and keep the auditor's report and any confidential material within the authorized
recipients.

## Evidence register

| Field | Content |
| --- | --- |
| Claim | The customer- or assessor-facing statement being supported. |
| Obligation or commitment | Law, contract, policy or assurance criterion behind it. |
| Control | What is done, by whom, where and how often. |
| Population and period | The events, tenants, environments and dates covered. |
| Source | The actual record, system, report or exercise. |
| Inspected date and owner | When and by whom the evidence was checked. |
| Limitation | What the evidence does not establish, or the known gap. |

Keep sensitive customer, personnel and vulnerability data protected. Share only what the
recipient is authorized to receive.

## Reporting

Distinguish design, implementation, observed operation and independent examination. A
policy, a screenshot and a green dashboard establish different things. Report gaps and
exceptions with an owner and a remediation path; do not convert an absent check into a pass
or a provider report into a service certification.
