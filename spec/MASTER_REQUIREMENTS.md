# Provider-neutral master receptionist requirements

**Provider-neutral requirements.** Draft client configuration and offline lint now exist in [config](../config/README.md). No live agent or provider payload exists. The selected provider will express these requirements through a minimal supported mapping.

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
| create_lead | Capture agreed details and priority; avoid duplicate creation |
| escalate_to_human | Record reason/urgency; transfer or notify; truthful fallback if unavailable |

The following contracts are deferred until a customer-owned booking authority is selected and tested: `check_availability`, `book_appointment`, `reschedule_appointment`, `cancel_appointment` and `lookup_customer`.

See [Action contracts v1](ACTION_CONTRACTS.md) for trusted customer binding, operation/payload deduplication, identity, atomic changes, committed receipts and unknown-outcome reconciliation. Benchmark actions later use explicitly isolated mocks. Production uses supported customer-owned calendar/CRM/integration services; simulated success must never enter a production result.

## Qualification and routing

Capture intent, service, timeframe, urgency and necessary business qualification. Fleet and vehicle-sales enquiries trigger high-value routing in the demo. Complaint, unknown answer, explicit human request and urgent cases follow client-approved escalation rules. Do not invent a value, promise a callback deadline without authority, or diagnose mechanical safety issues.

## Summary contract

Caller name; validated contact details; language; intent; service; urgency; requested/committed appointment; booking/action IDs; outcome; follow-up required; human action; unresolved detail; lead category. Mark unknown fields explicitly rather than guessing.

Historical lead labels: HOT, WARM, SERVICE, LOW PRIORITY, URGENT. Because urgency and lead value are different, record urgency separately and define precedence if one summary label is required. Returning customers can still represent hot opportunities. Client rules must determine classification consistently.

## Deployment modes

Primary, overflow and after-hours use supported routing. Each client receives approved opening/holiday schedules, escalation contacts, failure fallback, human takeover and rollback instructions. No promise that every mode is available on every customer carrier until verified.
