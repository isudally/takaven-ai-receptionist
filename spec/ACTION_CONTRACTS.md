# Action contracts v1

These are semantic contracts for supported existing integrations, not deployed endpoints. Provider-specific argument schemas are added only for qualified survivors.

## Trusted envelope

Integration supplies customer binding, verified provider call ID, action invocation/operation ID, config version and request time from trusted metadata. The model supplies only allowlisted action arguments. The server/integration checks identity and consent evidence; a model-generated `confirmed: true` is not sufficient authority.

Mutation operation IDs are durable across redelivery and timeout reconciliation. Store canonical payload digest and original outcome; reject changed payload under the same operation. Preserve history across cancellation. Caller corrections before confirmation replace draft data; a new confirmed intention creates a new operation.

Dates use an explicit timezone-aware ISO instant plus IANA business timezone. Read back a full date, local time and service. Clarify “tomorrow”, ambiguous weekdays and timezone conflicts using the actual call date in the business timezone. Durations come from approved service IDs.

## Common result

Every response includes `action`, `operation_id`, `status`, `authority`, `resource_id` (nullable), `committed_at` (nullable), `result`, `safe_message` and `staff_follow_up`. Customer binding is checked before execution and on returned resources.

Statuses: `read_ok`, `committed`, `pending`, `conflict`, `needs_information`, `unauthorised`, `failed`, `unknown`. Only `committed` with an authoritative receipt permits a completed-action claim. Reads use `read_ok`; pending/unknown/failed are never announced as success. `safe_message` contains no internal error or private record details.

## Actions

The first demo supports appointment-request capture, lead creation and truthful human escalation. The scheduling mutation and customer-lookup contracts remain provider-neutral future contracts and are deferred until a customer-owned booking authority is selected and tested.

| Action | Phase | Minimum arguments and checks | Authoritative result |
|---|---|---|---|
| capture_appointment_request | Demo | Service, preferred date/time window, timezone, confirmed contact, vehicle where relevant, explicit intent | `committed`; staff/queue receipt and captured fields; never a calendar booking claim |
| create_lead | Demo | Agreed necessary contact, intent/service, urgency and lead value separately, contact consent where needed | `committed`; CRM/queue ID and recorded fields; duplicate replay cannot create another lead |
| escalate_to_human | Demo | Explicit reason/urgency, supported transfer destination from config, minimum context | Distinct `connected`, `notification_delivered`, `callback_recorded`, `pending` or `failed` in result; receipt when committed; acknowledge means staff accepted |
| check_availability | Deferred | Approved service ID, date window, business timezone; live authority, hours/closures and horizon | `read_ok`; explicit slots, duration and freshness; no reservation claim |
| book_appointment | Deferred | Service, selected slot, required confirmed contact, explicit intent evidence; validate all policy and capacity at commit | `committed`; booking ID, committed start/end/timezone and receipt; otherwise conflict/pending/unknown |
| reschedule_appointment | Deferred | Existing booking ID, approved identity evidence, replacement slot, intent; version/precondition; atomic supported change | `committed`; same/linked authoritative booking and replacement; failed change leaves original intact |
| cancel_appointment | Deferred | Booking ID, identity and intent; cancellation policy, current resource version | `committed`; cancellation receipt and target; replay returns original cancellation outcome |
| lookup_customer | Deferred | Minimum lookup data and permitted purpose; identity before sensitive disclosure | `read_ok`; only approved fields or opaque match ID; caller ID alone cannot disclose records |

Escalation never requires the caller to provide a phone number before a supported direct transfer. If callback is necessary and caller ID is unavailable, ask for a reachable number; if refused, explain limits truthfully. Do not fabricate a callback or staff acknowledgement.

## Race, retry and failure rules

1. A preflight availability result cannot prevent a race. The booking authority must atomically enforce overlap and capacity for create and reschedule.
2. Timeout after mutation is `unknown`, not failure or success. Reconcile by operation/resource reference before a safe retry.
3. Use finite attempts and a terminal manual-review state excluded from scheduled retry selection.
4. Critical actions require explicit confirmation of current details. Earlier corrections invalidate stale draft confirmations.
5. Notifications are separately deduplicated and delivery tracked. Summary creation does not mean delivery.
6. Unavailable or unsafe integration routes to human completion. Do not silently switch to mock data, local success or an unapproved calendar.

## Post-call record

Config version/hash; trusted call/customer/operation IDs; final caller corrections; language; intent; urgency; lead category; authoritative action receipts; requested versus committed appointment; unresolved/unknown actions; notification delivery; staff acknowledgement; next staff task.

Preserve multiple actions and their sequence (create then cancel, reschedule from an earlier call). The final summary must reflect current authoritative state. Record missing fields as null/unknown, not inferred facts. Keep personal data in approved customer systems, not Git.
