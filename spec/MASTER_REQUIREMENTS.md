# Provider-neutral master receptionist requirements

**Provider-neutral requirements.** TAKAVEN Receptionist Standard is the vendor-neutral implementation package: conversation behaviour, approved knowledge, qualification rules, action contracts, handoff logic, outcome classification, QA methodology and deployment/handover method. Retell is the provisional engine, not the product. Customer-owned provider accounts, telephone routes, calendar/CRM systems and data are preferred where supported and practical; no zero-lock-in or effortless portability claim is made. Draft client configuration and offline lint exist in [config](../config/README.md). No live agent or provider payload exists.

## Identity and conversation

Use client-approved identity, greeting, AI disclosure, voice and languages. Short natural sentences, one question at a time, varied acknowledgements, appropriate pauses, interruption recovery and retention of earlier facts. Do not claim to be human. Handle unknown facts with clarification or human follow-up.

Required markets: Mauritius EN/FR; UAE EN/AR. Language switching follows caller need. No Kreol. Localisation covers names, places, currencies, telephone formats and common pronunciations.

## Knowledge and business rules

Client-approved services, indicative/fixed prices, currency/tax wording, hours, address, holidays, approved FAQs, policies and restricted topics. Specify business timezone, date interpretation, appointment-request fields and confirmation requirements. A requested date/time window is captured and read back; availability and committed booking are deferred until a designated customer system exists.

The rebuilt pack has separate fictional automotive draft facts for Mauritius and UAE. Prices/hours are illustrative and unapproved. Deterministic action fixtures with explicit ISO dates, slots and customer/booking IDs remain for the later authorised testing phase. Do not mix markets, calendars or currencies. Demo pricing is not market advice.

## Action contracts

| Action | Required behaviour |
|---|---|
| capture_appointment_request | Capture service, preferred date/time window, caller details and vehicle; read back and return a staff receipt; do not claim a booking |
| create_lead | Capture caller-confirmed contact, intent, service/vehicle details and budget where relevant, urgency and client-approved opportunity classification; use the proposed shared receipt route only after a named customer-owned lead authority is proven; otherwise fail closed to staff follow-up and avoid any CRM/lead claim or duplicate creation |
| escalate_to_human | Record reason/urgency and the structured handoff brief; transfer or notify; truthful fallback if unavailable |

The following contracts are deferred until a customer-owned booking authority is selected and tested: `check_availability`, `book_appointment`, `reschedule_appointment`, `cancel_appointment` and `lookup_customer`.

See [Action contracts v1](ACTION_CONTRACTS.md) for trusted customer binding, operation/payload deduplication, identity, atomic changes, committed receipts and unknown-outcome reconciliation. Benchmark actions later use explicitly isolated mocks. Production uses supported customer-owned calendar/CRM/integration services; simulated success must never enter a production result.

## Qualification and routing

Capture intent, service, timeframe, urgency and necessary business qualification. Use the client-approved operational classification values `QUALIFIED`, `FOLLOW_UP_REQUIRED`, `SERVICE`, `ESCALATED` or `GENERAL`; keep urgency separate from optional commercial value (`high`, `standard`, `unknown`). Never infer commercial value from model intuition. Complaint, unknown answer, explicit human request and urgent cases follow client-approved escalation rules. Do not invent a value, promise a callback deadline without authority, or diagnose mechanical safety issues.

## Summary contract

Caller name; caller-confirmed contact details; language; intent; service/vehicle; preferred timeframe; urgency; opportunity type; value tier; requested/committed appointment; booking/action IDs; call outcome; follow-up required; human action; unresolved detail; receipt reference; delivery status; staff acknowledgement status. Mark unknown fields explicitly rather than guessing. First-demo outcome labels are appointment request captured, lead captured, follow-up required, escalated, informational enquiry resolved or unresolved; never `BOOKED`.

Legacy labels such as HOT, WARM, LOW PRIORITY and URGENT are deprecated for the first-demo schema because they mix urgency, intent, disposition and commercial value. Client-approved rules determine classification; returning callers do not receive a value label by model intuition.

## Deployment modes

Primary, overflow and after-hours use supported routing. Each client receives approved opening/holiday schedules, escalation contacts, failure fallback, human takeover and rollback instructions. No promise that every mode is available on every customer carrier until verified.
