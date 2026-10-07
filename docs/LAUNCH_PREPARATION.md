# Receptionist launch preparation

This is the minimum launch layer around the functional Receptionist prototype. It is a single-client deployment method, not a multi-tenant platform.

## Current baseline

```text
Retell -> capture_appointment_request -> authenticated n8n webhook
       -> Google Sheets -> synchronous RECEIVED / FAILED response
```

The prototype uses fictional data. `RECEIVED` means the request was sent to the team for confirmation; it never means booked, confirmed, reserved, available or staff-acknowledged.

## Client configuration model

Copy [`config/client-deployment.template.json`](../config/client-deployment.template.json) once per customer. Keep facts and destinations in the client-owned deployment record; do not add a tenant registry or universal runtime.

The client configuration must provide:

- business name, locations, timezone, hours and closures;
- services and approved prices, with human-quote wording where needed;
- approved FAQs and languages;
- receptionist persona and greeting;
- fields required for an appointment request;
- callback/handoff destination and business hours;
- allowed actions and n8n endpoint references;
- customer-owned Retell, n8n, Google and telephony account references;
- privacy, recording and retention choices.

## Production authentication

The sanitized appointment and callback workflows use n8n's native Webhook `headerAuth` credential. Configure the same high-entropy value in the Retell custom function header and the n8n credential store. The value must not appear in Git, screenshots, exports, chat or logs.

Deployment evidence required:

1. authenticated fictional request succeeds;
2. the same request without the header is rejected;
3. the credential is owned by the customer deployment and can be rotated;
4. the old value is removed from Retell and n8n after rotation.

This is a static shared secret for the prototype launch path, not a custom cryptographic protocol. Do not add Data Store/idempotency infrastructure solely for this check.

## Human callback / handoff

Use [`retell/tools/request_human_callback.schema.json`](../retell/tools/request_human_callback.schema.json) and the sanitized [`n8n/request_human_callback.sanitized.workflow.json`](../n8n/request_human_callback.sanitized.workflow.json) for a customer-owned callback destination.

The callback path captures the caller name, contact and reason where available, appends a callback record, and returns a truthful result. The spoken result is that the team will follow up. It must not claim that a person is already connected or that a response time is guaranteed.

## Telephony deployment

See [TELEPHONY_DEPLOYMENT.md](TELEPHONY_DEPLOYMENT.md). The demo may remain a Retell browser/web call until a customer-owned route is selected and accepted. Do not purchase numbers or carrier services as part of prototype validation.

## Operational evidence

See [OPERATIONS.md](OPERATIONS.md). The minimum evidence is a provider call reference, action name, n8n execution result, request/callback reference, destination receipt and a safe failure outcome. Use existing Retell and n8n logs; do not build a dashboard.

## Client delivery

- [CLIENT_ONBOARDING.md](CLIENT_ONBOARDING.md) defines the short customer checklist.
- [ROLLBACK_SUPPORT.md](ROLLBACK_SUPPORT.md) defines disable/reroute and support handling.

## Release acceptance

Human voice acceptance is completed as evidence but final release acceptance remains deferred until the first external-demo candidate is frozen. It is one milestone call, not a recurring test loop.

Before that call, the owner must approve the demo facts, wording, handoff destination, telephony mode and privacy/recording choices. Production readiness is not established by this document alone.
