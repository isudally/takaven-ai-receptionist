# Receptionist release-candidate evidence

Updated 2026-10-07. Fictional demo data only. Secrets, private endpoint values and credential IDs are intentionally omitted.

## Current result

- Technical baseline: **FUNCTIONAL**.
- Production readiness: **NOT ESTABLISHED**.
- Human release acceptance: **NOT YET REQUESTED**.
- First external-demo mode: **BROWSER / WEB CALL**; no paid number or carrier route is implied.

## Non-human evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Authenticated appointment request | PASS | Retell custom-function test reached the published n8n workflow, appended a fictional appointment row, and returned `RECEIVED`. |
| Appointment request without header | PASS | A fictional request was rejected with HTTP 403; no matching Sheet record was created. |
| Authenticated callback request | PASS | Retell custom-function test reached the callback workflow, appended a fictional `Handoffs` row, and returned `CALLBACK_RECEIVED`. |
| Callback request without header | PASS | A fictional request was rejected with HTTP 403. |
| Safe semantics | PASS | Responses mean sent for team confirmation/follow-up. Neither claims booking, availability, live transfer or staff acknowledgement. |
| Operational trace | PASS with limitation | n8n execution, action name, destination row and safe response are visible. Native function tests use a test reference when no real call envelope is supplied; real Retell call-ID capture remains part of final human release acceptance. |
| Rollback | PASS for documented demo procedure | Retell version controls and n8n workflow controls are available; no destructive disable was performed. The documented fallback is to disable the agent/remove its route and use existing business handling. |

## Privacy and retention

The fictional MU and UAE demo profiles use recording **off**, zero-day retention, and deletion owner **TAKAVEN demo owner**. Customer deployments must replace these with customer-approved values before launch.

## Remaining gates

1. Freeze the external-demo configuration and approve demo facts, wording, handoff destination and privacy values.
2. Perform one human release-acceptance call at that milestone only.
3. Before a paying customer: customer-owned telephony route, customer-approved privacy/retention, support ownership and monitored pilot.
