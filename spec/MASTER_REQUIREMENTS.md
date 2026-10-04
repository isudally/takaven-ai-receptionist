# Provider-neutral master receptionist requirements

**Requirements only.** No live agent or executable configuration exists. The later master configuration must express these once, then map them minimally to the selected provider.

## Identity and conversation

Use client-approved identity, greeting, AI disclosure, voice and languages. Short natural sentences, one question at a time, varied acknowledgements, appropriate pauses, interruption recovery and retention of earlier facts. Do not claim to be human. Handle unknown facts with clarification or human follow-up.

Required markets: Mauritius EN/FR; UAE EN/AR. Language switching follows caller need. No Kreol. Localisation covers names, places, currencies, telephone formats and common pronunciations.

## Knowledge and business rules

Client-approved services, indicative/fixed prices, currency/tax wording, hours, address, holidays, policies and restricted topics. Specify business timezone, date interpretation, appointment duration, booking horizon, availability authority, cancellation rules and confirmation requirements. Availability must come from the designated system, not the prompt.

The fictional automotive fixture will define fixed facts, explicit ISO dates/timezones, available slots and customer/booking IDs. Do not mix Mauritian and UAE currencies or calendars in one ambiguous fixture. Pricing represents demo facts, not market advice. Generate the fixture only in the authorised testing phase.

## Action contracts

| Action | Required behaviour |
|---|---|
| check_availability | Read available slots for explicit service/date/timezone |
| book_appointment | Validate required details; confirm intent; create once; return booking ID and committed slot |
| reschedule_appointment | Verify permitted identity and booking; confirm replacement; return committed outcome |
| cancel_appointment | Verify permitted identity and booking; confirm intent; return cancellation result |
| lookup_customer | Minimum necessary lookup; no sensitive disclosure from caller ID alone |
| create_lead | Capture agreed details and priority; avoid duplicate creation |
| escalate_to_human | Record reason/urgency; transfer or notify; truthful fallback if unavailable |

Benchmark actions later use deterministic mocks. Production actions use supported customer-owned calendar/CRM/integration services.

## Qualification and routing

Capture intent, service, timeframe, urgency and necessary business qualification. Fleet enquiries trigger high-value routing in the demo. Complaint, unknown answer, explicit human request and urgent cases follow client-approved escalation rules. Do not invent a value, promise a callback deadline without authority, or diagnose mechanical safety issues.

## Summary contract

Caller name; validated contact details; language; intent; service; urgency; requested/committed appointment; booking/action IDs; outcome; follow-up required; human action; unresolved detail; lead category. Mark unknown fields explicitly rather than guessing.

Historical lead labels: HOT, WARM, SERVICE, LOW PRIORITY, URGENT. Because urgency and lead value are different, record urgency separately and define precedence if one summary label is required. Returning customers can still represent hot opportunities. Client rules must determine classification consistently.

## Deployment modes

Primary, overflow and after-hours use supported routing. Each client receives approved opening/holiday schedules, escalation contacts, failure fallback, human takeover and rollback instructions. No promise that every mode is available on every customer carrier until verified.
