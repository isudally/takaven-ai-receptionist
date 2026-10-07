# Execution plan — Receptionist launch preparation

Status: **prototype-functional; launch preparation in progress; production readiness not established**.

This plan supersedes the old Gate 0A/B/C/D sequencing for the active implementation. The old gate documents remain historical records and are not deleted.

## Current evidence

- Retell Receptionist configured and tested with fictional data.
- Dedicated `capture_appointment_request` reaches n8n, appends to Google Sheets and returns synchronous `RECEIVED`.
- French human voice evidence completed; conversation polish implemented.
- Automated regression scenarios A–H pass.
- Final human acceptance is deferred until the release candidate is ready for the first external demo.

## Launch-preparation work

1. Keep the working Retell → n8n → Sheets path unchanged.
2. Make client configuration reproducible without creating multi-tenancy.
3. Configure and prove native n8n header authentication in an owner-controlled environment.
4. Add a simple callback/handoff action and destination path; never imply live transfer.
5. Document customer-owned Mauritius and UAE telephony routes and limits.
6. Define the minimum operational evidence, onboarding checklist and rollback/support procedure.
7. Freeze a polished fictional demo profile and a concise external-demo acceptance checklist.
8. Run one human release acceptance call only when the launch package is otherwise ready.

## Scope exclusions

No booking authority, live availability, reschedule/cancel, customer lookup, CRM, dashboard, generic platform, custom speech stack, new provider, Sales/Admin runtime or Make revival is authorised by this plan.

## Stop conditions

Stop and return `MODIFY` if native authentication, callback capture, telephony routing or truthful failure handling cannot be made reliable without new infrastructure. Do not solve a launch gap by introducing a second platform or a custom backend.

## Evidence required before first external demo

- clean-checkout validators pass;
- demo configuration and approved facts are frozen;
- Retell and n8n credentials are owner-controlled and secrets are not in Git;
- unauthenticated action request is rejected;
- authenticated appointment and callback paths have visible execution evidence;
- customer-owned telephony route is selected or the demo is explicitly browser/web-call only;
- rollback path is tested;
- one final human French acceptance call is completed;
- owner approves the demo wording and data/privacy handling.

## Evidence required before first paying-customer launch

In addition to the above: customer-approved facts, destination ownership, privacy/recording/retention choices, customer-owned telephony route, support contact, monitored pilot, and written customer acceptance. Production launch is not inferred from repository validation.
