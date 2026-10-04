# Customer deployment playbook — future template

Target: complete client configuration within approximately one business day after complete information and access are received, excluding carrier provisioning and external approvals. This is an ambition to validate, not a delivery guarantee.

## Intake

Collect business identity, authorised approver, selected market/languages, reception mode, hours/timezone/holidays, services/prices/policies, approved FAQs, restrictions, qualification/VIP rules, escalation contacts and callback expectations. Record spelling/pronunciation preferences.

Confirm that every authoritative system is customer-owned or explicitly customer-authorized: provider/voice account, carrier, Make/webhook, Sheet or CRM, mailbox/notification destination and retained data. Confirm supported routing, delegated access and approved data/disclosure/recording practices. The proposed first-demo route is Retell action → Make webhook → Google Sheet row plus staff email → receipt ID. Gate B must prove authenticity, replay, serialization and notification behaviour before this becomes an authoritative receipt. A calendar/CRM and booking authority are optional later integrations; they are not required for the first demo. Keep secrets and caller data outside this repository.

## First-demo data-flow map — Gate B design, not deployment proof

The following is the minimum data-flow inventory for fictional-data mapping. Retention, processing region, deletion and contractual suitability remain `UNKNOWN — client/legal review required` until the customer-owned accounts and plans are selected.

| System | Data categories and purpose | Owner/access | Storage/retention/deletion | Controls and status |
|---|---|---|---|---|
| Caller / Retell | Caller-confirmed name/contact; language; intent; service/vehicle; timeframe; urgency; classification; call ID; agent/workspace metadata; tool arguments; transcript/recording where provider settings enable them | Customer-owned provider account; approved TAKAVEN/customer admins | Provider storage, processing region, metadata/transcript/recording retention and deletion: `UNKNOWN — client/legal review required` | Fictional data only; recording is disabled in draft config but provider transcript/metadata retention is not assumed absent; disclosure/consent remains client review |
| Make webhook | Signed request headers and original representation required for verification; allowlisted action fields; payload digest; execution/receipt state | Customer-owned Make account; named operators only | Webhook queue, execution logs, incomplete executions, headers/body retention and deletion: `UNKNOWN — client/legal review required` | Gate B must prove raw-body/signature handling, timestamp/replay controls, serialization, fail-closed behaviour and no unnecessary transcript forwarding |
| Google Sheet | Allowlisted handoff/lead/request fields; receipt token; payload digest; delivery/conflict status | Customer-owned Sheet/account; staff ACLs | Sheet row/revision history, retention and deletion owner: `UNKNOWN — client/legal review required` | Protected/append-only semantics and exact replay behaviour are Gate B requirements; do not use a row number alone as an immutable receipt |
| Staff email | Minimal structured handoff and outcome; receipt reference; no full transcript unless separately approved | Customer-owned mailbox/group; named staff recipients | Mailbox retention, forwarding and deletion: `UNKNOWN — client/legal review required` | Notification delivery is separate from staff acknowledgement; duplicate-email prevention is a Gate B/D proof requirement |

No raw transcript or full provider call object should be forwarded to Make, Sheet or email unless an approved mapping requires it. Real customer data remains prohibited until account ownership, disclosure, retention, access and deletion responsibilities are approved.

## Configure

Start from the market-specific draft [client pack](../config/README.md). Replace fictional facts and resolve every prerequisite. Run offline lint and record the configuration hash. Select the qualified vendor's native configuration/tooling and minimally map the action/conversation contracts.

Bind the customer from verified account/agent/destination metadata. Use supported authentication, scoped secret storage, identity checks and consent. For the first demo, require an authoritative staff/queue receipt for appointment-request capture and do not claim a booked slot. If a later customer calendar/CRM authority is added, require authoritative availability, committed receipts, durable operation replay and safe atomic reschedule; if unavailable, route that action to human completion.

Before changing remote settings: snapshot the prior version; name exact customer/account/agent/branch; list owned fields, changes and explicit removals; review rollback and human fallback. Plan and apply are separate operations. After applying, pull/read back and compare owned values, arrays and cleared fields—not only key presence. Track vendor tool/version, config hash, remote IDs and approver.

## Validate

Client approves factual content and business rules. For Gate D, run the client-specific acceptance set as Retell web calls against fictional data; verify action results, Make receipt IDs, staff notifications, deduplication, after-hours behaviour and callback fallback. Test an actual phone route and warm transfer only in Gate E after separate carrier and destination approval. All launch blockers must be resolved.

## Handover and launch

Provide account/access ownership, config hash and remote version, limitations, operating costs, knowledge-update method, staff training, troubleshooting, tested fallback/rollback and support boundary. Explain pending/unknown actions and where staff see new, modified or cancelled requests; delivery is not staff acknowledgement. Agree monitored pilot dates and first-week review. Obtain client approval for factual rules and routing before enabling service.

## One-off scope control

List included languages, workflows, integrations, revisions and handover support in the implementation agreement. Separate vendor recurring charges and optional care from the one-off fee. New integrations, outbound campaigns and ongoing optimisation require separately agreed scope.
