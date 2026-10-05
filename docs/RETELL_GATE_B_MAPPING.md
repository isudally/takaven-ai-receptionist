# Gate B — Offline Retell Mapping

Checked: 2026-10-05. Target: Retell AI, provisional first mapping target. Evidence is public official documentation only; no Retell or Make account was accessed and no provider call was made.

## Verdict and decision boundary

**PASS at design level for Gate B.1.** Retell can represent the frozen first-demo conversation, languages, custom actions, post-call extraction, transfer configuration and web-call test path with native features. The corrected `Retell custom function → HTTPS Make API-key-authenticated webhook → Make Data Store ledger → Google Sheet + staff email → receipt` route is supported by documented native concepts. It avoids making Retell HMAC raw-body verification the only ingress control. Runtime configuration, failure injection, receipt delivery and side-effect tests remain NOT_RUN and are deferred to an owner-approved later gate.

This is an evidence gate, not deployment. Unknown is preserved as `UNKNOWN — client/legal review required`; it is not a pass.

## Evidence register

| Ref | Official source | Finding used | Checked |
|---|---|---|---|
| R1 | https://docs.retellai.com/build/single-multi-prompt/custom-function | Custom function URL, JSON schema, call envelope, response mapping, timeout, retries and signature details | 2026-10-05 |
| R2 | https://docs.retellai.com/features/secure-webhook | Raw-body signature verification, webhook-enabled Retell API key, SDK method and IP allowlist | 2026-10-05 |
| R3 | https://docs.retellai.com/agent/language | Single-language behaviour and dashboard-supported language/voice/ASR combinations | 2026-10-05 |
| R4 | https://docs.retellai.com/agent/multilingual | Multiselect detection, switching and accuracy trade-offs | 2026-10-05 |
| R5 | https://docs.retellai.com/build/dynamic-variables | Request/contact/collected variables and Retell system variables | 2026-10-05 |
| R6 | https://docs.retellai.com/features/webhook-overview | Webhook payload, call metadata, transcript and transfer events | 2026-10-05 |
| R7 | https://docs.retellai.com/build/single-multi-prompt/transfer-call | Cold/warm/agentic transfer and phone-call-only limitation | 2026-10-05 |
| R8 | https://docs.retellai.com/features/post-call-analysis-create | Text, selector, number and boolean post-call extraction | 2026-10-05 |
| R9 | https://docs.retellai.com/deploy/web-call | Browser web-call path for later Gate C/D preparation | 2026-10-05 |
| M1 | https://help.make.com/webhooks | Custom webhook, headers/body visibility, queueing and default parallel processing | 2026-10-05 |
| M2 | https://help.make.com/scenario-settings | Process-data-in-order, confidentiality, incomplete executions and commit behaviour | 2026-10-05 |
| M3 | https://help.make.com/text-and-binary-functions | `sha256(text; encoding; key; key encoding)` supports HMAC when a key is supplied | 2026-10-05 |
| M4 | https://help.make.com/digital-signature | Make Encryptor digital-signature feature; RSA signature flow, not Retell HMAC verification | 2026-10-05 |
| M5 | https://help.make.com/hash-functions | Hashes support integrity comparison; they do not by themselves authenticate Retell | 2026-10-05 |
| M6 | https://help.make.com/webhook-triggered-ai-agent | Make Custom Webhook API key setup and `x-make-apikey` request header | 2026-10-05 |
| M7 | https://help.make.com/l6du-data-stores | Unique keys, duplicate rejection without overwrite, existence checks and record retrieval | 2026-10-05 |

## Native agent mapping

| TAKAVEN requirement | Retell native concept | Status / limitation |
|---|---|---|
| Agent identity and AI disclosure | Agent name/version plus prompt/instructions; explicit opening disclosure in prompt | **SUPPORTED.** Exact customer identity text remains profile/config input. Prompt wording does not prove caller identity or action authority. |
| MU EN/FR and UAE EN/AR | Multilingual agent language multiselect, or one single-language agent selected/overridden per call | **SUPPORTED, performance UNKNOWN.** Retell documents automatic recognition and response-language selection for multiselect, with fallback to the first selected language. Exact voice/ASR locale combinations are dashboard-dependent and need Gate D/E evidence. |
| Language identification/switching | Multilingual speech recognition and prompt instruction to follow caller language; inbound call webhook can set language/context before a call | **SUPPORTED, quality UNKNOWN.** Detection can fail; do not claim fluent switching before human review. Unsupported language must trigger a spoken fallback and callback/handoff offer. |
| Voice selection | Native voice selector, platform voices and supported third-party voice providers | **SUPPORTED, exact voice UNKNOWN.** The selected provider/voice must support each selected language. No voice ID is chosen offline. |
| Prompt/instruction structure | Single-prompt agent, or conversation-flow nodes/global settings | **SUPPORTED.** Use single prompt for the frozen first demo unless a later owner decision shows deterministic flow control is needed. Keep rules concise and explicit. |
| Approved facts / FAQs | Retell Knowledge Base with approved URLs/documents/custom text plus prompt restrictions | **SUPPORTED.** Source approval, factual completeness, freshness, hallucination resistance and client sign-off remain UNKNOWN until configured and tested. |
| Interruption / turn handling | `interruption_sensitivity`, responsiveness, backchannel, reminder settings and speech/turn controls | **SUPPORTED.** Exact setting is not selected; interruption recovery remains NOT_RUN. Interruption during a custom function does not cancel the endpoint request (R1). |
| Correction/context behaviour | Conversation context, prompt rule to replace draft values after correction, Extract Dynamic Variable/tool response mapping | **SUPPORTED as configuration.** Retell context does not replace external receipt authority. Reconfirm changed material fields before invoking an action. |
| Service and vehicle qualification | Prompt or conversation-flow nodes; extracted dynamic variables; custom function args | **SUPPORTED.** Classification must follow explicit client rules; do not use Retell post-call extraction as an authoritative mutation input. |
| Primary / overflow / after-hours | Inbound routing, imported/custom telephony and transfer tools; schedules/routing are configuration-dependent | **PARTIAL / UNKNOWN.** Retell documents inbound routing and transfer concepts, but client carrier, hours, destination reachability and overflow semantics are not verified offline. |
| Human escalation | Transfer Call tool with cold, warm or agentic warm modes; destination can be E.164, SIP URI or dynamic variable | **PARTIAL.** Transfer is phone-call only, not web-call. A transfer-start event is not proof that a human answered. Callback fallback needs a separate supported destination/receipt route. |
| Unsupported language | Prompted supported-language fallback plus escalation/callback capture | **SUPPORTED as conversation policy; delivery UNKNOWN.** No unsupported-language capability claim is made. |

## Retell request/session metadata

For a custom function with the normal wrapper (Payload: args only **off**), Retell documents a JSON body containing `name`, `args`, and `call`. With `args only` on, only the argument object is sent. The documented call object includes or may include:

- authoritative provider fields: `call_id`, `call_type`, `agent_id`, `agent_version`, `agent_name`, `call_status`, timestamps, `direction`, `metadata`, `retell_llm_dynamic_variables`, transcript fields and telephony identifiers where applicable;
- route/caller fields where the call type supports them: `from_number`, `to_number`, `direction`; these are routing metadata, not proof of caller identity or consent;
- model/conversation-derived or collected fields: transcript, transcript-with-tool-calls, collected dynamic variables and custom function `args` unless a value is a Retell `const`/dynamic-variable binding configured outside the LLM;
- account/workspace ownership: `agent_id` and agent version are documented in the call object. A workspace/account identifier is **UNKNOWN** in the reviewed custom-function payload and must not be invented;
- timestamps: `start_timestamp`, `end_timestamp`, `transfer_end_timestamp` and related call timing are documented in call payload examples. A Retell replay timestamp or freshness/replay window is **UNKNOWN**;
- caller number: `from_number` may be supplied for phone calls, but caller ID is only a contact hint. It cannot authorise lookup, consent, customer binding or a mutation.

Trusted action metadata should therefore be read from the verified Retell `call` envelope, not requested as free-form model arguments. The model may supply only allowlisted business fields after caller confirmation. `call_id + intent` is a reasonable bounded demo dedupe candidate, but it is not sufficient until signature verification, canonical payload storage and exact replay behaviour are proven.

## Action mapping

### Common custom-function configuration

- Function method: `POST`.
- Endpoint: a public HTTPS Make Custom Webhook URL; Retell blocks localhost/private ranges.
- Payload mode: normal wrapper, not `args only`, so the receiver can use the provider `call` object. If `args only` is selected, trusted call context is not in the body and the mapping is unsafe.
- Timeout: choose the smallest value compatible with an end-to-end receipt. Retell documents 1,000–600,000 ms, default 120,000 ms. The route is not approved at any value until receipt and timeout behaviour are proven.
- Retries: default `max_retry=0`; Retell supports 0–5 retries with exponential backoff and warns that each retry repeats the request. Retries are unsafe unless the destination is idempotent.
- Response: HTTP 2xx is success; JSON object responses can populate Retell response variables. Non-2xx, timeout or malformed response must produce a non-success spoken outcome.
- Authentication: configure a Make Custom Webhook API key and send it as a static `x-make-apikey` custom request header from Retell over HTTPS. Make documents API-key creation for Custom Webhooks and the `x-make-apikey` request header. Keep the value outside Git and restrict access in both customer-owned accounts. Retell `X-Retell-Signature` remains optional defense-in-depth where raw-body verification is available; it is not the mandatory first-demo ingress control.
- Ledger: use Make Data Store with `dedupe_key` as the caller-supplied unique record key and overwrite disabled for the initial insert. Configure the scenario to Process data in order. The ledger is the bounded receipt/idempotency authority, not a customer database, CRM, booking database or general backend.

### `create_lead`

Proposed Retell JSON Schema for the function `args` (the exact field names are the Gate B logical contract; no provider payload was published):

```json
{
  "type": "object",
  "required": ["caller_name", "caller_confirmed_contact", "intent", "opportunity_classification"],
  "properties": {
    "caller_name": {"type": "string", "description": "Caller-confirmed name"},
    "caller_confirmed_contact": {"type": "string", "description": "Caller-confirmed reachable contact"},
    "intent": {"type": "string", "enum": ["service_enquiry", "vehicle_sales", "test_drive", "other_demo_intent"]},
    "service": {"type": ["string", "null"], "description": "Approved service identifier or null"},
    "vehicle": {"type": ["string", "null"], "description": "Vehicle/model detail or null"},
    "preferred_timeframe": {"type": ["string", "null"], "description": "Caller-requested timeframe, not a booking"},
    "budget": {"type": ["string", "null"], "description": "Caller-stated budget or null"},
    "urgency": {"type": ["string", "null"], "enum": ["low", "normal", "urgent", null]},
    "opportunity_classification": {"type": "string", "enum": ["QUALIFIED", "FOLLOW_UP_REQUIRED", "SERVICE", "ESCALATED", "GENERAL"]},
    "value_tier": {"type": "string", "enum": ["high", "standard", "unknown"]},
    "consent_to_follow_up": {"type": ["boolean", "null"]}
  }
}
```

Model-supplied: all `args` after explicit caller confirmation. Trusted: verified `call.call_id`, agent/version, direction/route metadata, configured customer binding, request timestamp as observed by the receiver, and the configured intent/tool name. `value_tier` defaults to `unknown`; the agent must apply written client rules and never infer value from tone or intuition. `urgency` is separate from value.

Expected response object:

```json
{
  "action": "create_lead",
  "operation_id": "opaque-stable-operation-reference",
  "status": "committed",
  "authority": "named-customer-lead-destination",
  "resource_id": null,
  "receipt_id": "opaque-receipt-reference",
  "result": "lead_receipt_recorded",
  "safe_message": "Your enquiry has been recorded for the team.",
  "staff_follow_up": "Team follow-up required"
}
```

`committed` is speakable only after an authoritative receipt from the destination. `pending` or `unknown` means “I could not confirm the team received this; I will route it for follow-up” and must not claim a lead was created. `failed` means the action did not commit and the caller gets a truthful fallback. Conflict-like changed-payload or duplicate-intent states route to staff reconciliation; an exact replay must return the original receipt without a second row/email. `receipt_id` is returned through the JSON response and mapped to a Retell response variable only after verification. The corrected route passes at design level; runtime evidence remains NOT_RUN.

### `capture_appointment_request`

Use the same envelope and response contract, with this `args` schema:

```json
{
  "type": "object",
  "required": ["caller_name", "caller_confirmed_contact", "service", "preferred_timeframe", "business_timezone", "intent"],
  "properties": {
    "caller_name": {"type": "string"},
    "caller_confirmed_contact": {"type": "string"},
    "service": {"type": "string", "description": "Approved service identifier"},
    "vehicle": {"type": ["string", "null"]},
    "preferred_timeframe": {"type": "string", "description": "Requested date/time window, not a confirmed slot"},
    "business_timezone": {"type": "string", "description": "Configured IANA timezone, preferably a const/dynamic binding"},
    "intent": {"type": "string", "enum": ["appointment_request"]},
    "urgency": {"type": "string", "enum": ["low", "normal", "urgent"]},
    "opportunity_classification": {"type": "string", "enum": ["QUALIFIED", "FOLLOW_UP_REQUIRED", "SERVICE", "ESCALATED", "GENERAL"]},
    "value_tier": {"type": "string", "enum": ["high", "standard", "unknown"]}
  }
}
```

`business_timezone` should be a configured constant/dynamic value, not a free-form caller choice. This action records a request only; it does not check availability or claim `BOOKED`. A committed response may say “your appointment request was captured” and include the opaque receipt. Pending/unknown/failed/conflict use the same truthful fallback rules as `create_lead`. A correction before confirmation replaces the draft and requires read-back; a later same-intent request in the same call routes to staff follow-up under the frozen first-demo rule.

## Retell → Make security and receipt finding

### Authenticity

Retell documents `X-Retell-Signature` as an HMAC-SHA256 signature of the request body for custom functions. Verification uses the raw request body and the Retell API key with the webhook badge; Retell’s SDK examples explicitly warn against `JSON.stringify(req.body)`. For GET/DELETE the body is empty; the proposed actions use POST. Retell also documents an optional Retell outbound IP allowlist. No signed timestamp, nonce or replay window is documented for this custom-function signature. Therefore freshness/replay protection must be designed separately; it cannot be assumed from the signature.

**Status: DEFENSE-IN-DEPTH / NOT REQUIRED for the corrected first-demo ingress.** Retell HMAC remains valuable where an endpoint can verify the raw body, but the first-demo Make route uses Make’s documented webhook API-key authentication instead.

### Make feasibility

Make documents an optional API key on a Custom Webhook and the `x-make-apikey` header used by the caller. Retell custom functions document configurable static request headers. Together, these support an authenticated HTTPS ingress without reconstructing Retell’s HMAC body. Make also documents Process data in order for webhook scenarios, which prevents the next execution from starting until the prior execution completes.

**Status: PASS at design level for the corrected route; runtime rejection and sequencing remain NOT_RUN.** This proves possession of the webhook secret, not message-level authenticity. HTTPS provides transport integrity; it does not prevent a party with the secret from submitting altered payloads.

### Replay, idempotency and receipts

Make Data Store documents caller-supplied unique keys, duplicate rejection when overwrite is disabled, existence checks and record retrieval. Combined with Process data in order, this supports a minimal receipt/idempotency ledger for the bounded demo. Google Sheets remains a staff-facing downstream record; a row number is not an immutable receipt. Email remains notification only.

The design must do all of the following:

1. authenticate the Make webhook with the static `x-make-apikey` header before normal processing;
2. derive `dedupe_key = verified call.call_id + intent`; `call_id` comes from Retell’s trusted `call` object, never model arguments;
3. calculate/store a canonical action digest and create `PROCESSING` with overwrite disabled before Sheet/email side effects;
4. return the original receipt for an existing same-digest `COMMITTED` record;
5. return `CONFLICT` for an existing key with a different digest without side effects;
6. return `pending`/`unknown` for `PROCESSING` or `UNKNOWN` without automatically repeating uncertain side effects;
7. update the ledger with Sheet reference, notification status and final state only after the corresponding operation completes;
8. treat a timeout after any side effect as `UNKNOWN` until manual reconciliation.

**Receipt feasibility: PASS at design level, NOT_RUN operationally.** The architecture favors no duplicate business action over automatic recovery from an uncertain side effect.

### Minimal ledger state

| Field | Purpose |
|---|---|
| `dedupe_key` | Unique Make Data Store key: trusted Retell `call_id` plus intent |
| `action_type` | `create_lead` or `capture_appointment_request` |
| `payload_digest` | Canonical digest of the allowlisted action fields |
| `receipt_id` | Stable opaque receipt reference generated before downstream side effects |
| `state` | `PROCESSING`, `COMMITTED`, `UNKNOWN` or `CONFLICT` |
| `sheet_reference` | Non-authoritative staff-facing row reference |
| `notification_status` | `NOT_ATTEMPTED`, `SENT`, `UNKNOWN` or `FAILED` |
| `created_at` / `updated_at` | Reconciliation timestamps |

The Data Store is an explicitly authorised minimal receipt/idempotency ledger. It is not a customer database, CRM, booking database, analytics platform, SaaS product or general backend.

### Failure-window analysis

| Failure point | Ledger state | Retry behaviour | Caller-safe response | Staff action |
|---|---|---|---|---|
| Ledger created, then failure before Sheet | `PROCESSING` | No automatic side effects; same key returns pending | “I could not confirm this was received.” | Inspect and reconcile; complete downstream work once or mark failed/unknown |
| Sheet succeeds, then failure before email | `PROCESSING` | Do not repeat Sheet or email automatically | Pending/unknown | Check Sheet and email evidence; send once only if absence is confirmed |
| Email may have sent, then ledger update fails | `PROCESSING` or `UNKNOWN` | Do not resend email automatically | Pending/unknown | Reconcile mailbox and Sheet, then update ledger |
| Retell response times out after work commits | `COMMITTED` if ledger update completed, otherwise `PROCESSING`/`UNKNOWN` | Retell retry returns original receipt only for `COMMITTED`; otherwise pending/unknown | Never claim success from timeout alone | Reconcile ledger, Sheet and notification |
| Exact Retell retry | Existing same-digest record | `COMMITTED` returns original receipt; `PROCESSING`/`UNKNOWN` returns pending/unknown | Captured only for committed receipt | No duplicate side effects |
| Changed-payload retry | Existing key, different digest | Return `CONFLICT`; no side effects | “I need staff follow-up to resolve conflicting details.” | Reconcile; do not overwrite original record |

## Classification mapping

Retell custom-function argument enums and/or post-call Selector Analysis can represent the controlled values, but the safest operational source is explicit prompt/conversation-flow wording plus allowlisted schema enums. Configure rules such as:

- `SERVICE` for service enquiries;
- `QUALIFIED` for a rule-satisfied sales/test-drive opportunity;
- `FOLLOW_UP_REQUIRED` when required information or staff action remains;
- `ESCALATED` for explicit human request, approved urgent/safety/complaint route or failed understanding;
- `GENERAL` for factual/general enquiries without a qualified opportunity.

Set `value_tier` separately to `high`, `standard` or `unknown`, defaulting to `unknown`. Retell’s selector field is a supported representation, not a rules engine; the descriptions must contain the client-approved rules, and post-call extraction must not override an authoritative action result. This mapping is **SUPPORTED as configuration; deterministic behaviour and outcome correctness are NOT_RUN**.

## Structured handoff

Before a transfer, Retell can hold the conversation context and call metadata and can use a custom function response or post-call extraction to form a handoff brief. The brief should contain caller name, caller-confirmed contact, language, intent, service/vehicle, preferred timeframe, urgency, operational classification, value tier, handoff reason, unresolved question, action/receipt reference, delivery status and acknowledgement status. Model-collected fields remain untrusted until caller-confirmed and validated by the action contract.

After the call, Retell’s call history/webhook payload can provide `call_id`, agent/version, timestamps, route fields where applicable, transcript/tool-call transcript, dynamic variables, transfer event data and post-call extracted fields. Retell documents transfer events and transfer destinations, but a `transfer_started` event is not evidence of human connection or staff acknowledgement. Staff context accompanying a live phone transfer is **PARTIAL/UNKNOWN** by transfer mode and carrier; a web call cannot use the Transfer Call tool.

Direct transfer path: **SUPPORTED for phone calls subject to imported/Retell number and carrier configuration; not available for web calls.** Callback fallback: **UNKNOWN** as an end-to-end staff service; it can be represented as a separate custom action only after a receipt destination is proven. Never say “connected” without provider evidence of connection. Delivery and acknowledgement remain separate fields.

## Privacy and data findings

Retell documentation verifies that call/webhook payloads can contain transcripts, transcript objects, transcript-with-tool-calls, call metadata, dynamic variables, timestamps, route numbers and storage-related fields. Retell exposes data-storage settings and an opt-out-sensitive-data-storage field in documented call payloads. Recording defaults, retention period, deletion controls, processing/storage region, redaction coverage and client-specific contractual terms are **UNKNOWN — client/legal review required** in this bounded pass. No legal conclusion is made.

Make documents that webhook request data includes headers/body and that webhook logs are retained for three days, or 30 days for Enterprise, while scenario confidentiality can prevent payload retention in execution logs. These are Make documentation facts, not a legal suitability conclusion. The proposed route remains blocked before data processing. No transcript, recording, customer data or credential was used for this gate.

## Seven smoke-scenario mapping — NOT_RUN

| Scenario | Retell features/settings and action | Evidence required later | Expected outcome | Remaining UNKNOWNs | Offline mapping |
|---|---|---|---|---|---|
| 1. Approved facts and unknown handling | Knowledge Base, single/multilingual prompt, no-action fallback | Exact answer against approved fictional facts; unknown answer; no invented price/availability | `informational_enquiry_resolved` or `unresolved` | Knowledge freshness, hallucination rate, voice quality | **YES** |
| 2. Mauritius service enquiry and lead capture | MU EN/FR language config; service qualification; `create_lead` custom function; API-key ingress; Data Store ledger; receipt response mapping | Tool args, authenticated ingress, one ledger record, one Sheet row/email, authoritative receipt, spoken claim | `lead_captured`, or truthful pending/failed/escalated | MU route, French quality, runtime receipt/reconciliation | **YES at design level; NOT_RUN operationally** |
| 3. UAE vehicle-sales/test-drive qualification | UAE EN/AR multiselect; vehicle/test-drive rules; `create_lead`; API-key ingress; Data Store ledger | Explicit classification/value rules, caller-confirmed contact, receipt and handoff | `lead_captured` or `follow_up_required` | Arabic quality, UAE route, runtime receipt/reconciliation | **YES at design level; NOT_RUN operationally** |
| 4. Appointment request, correction and read-back | Extract Dynamic Variables or flow nodes; correction prompt; `capture_appointment_request`; API-key ingress; Data Store ledger | Corrected args, timezone/read-back, no booking claim, receipt and no duplicate | `appointment_request_captured` or truthful pending/unknown | Runtime receipt/reconciliation; no calendar authority | **YES at design level; NOT_RUN operationally** |
| 5. Structured handoff, callback fallback and post-call outcome | Transfer Call for phone only; post-call extraction; call webhooks; callback route if proven | Transfer event versus connected evidence; handoff fields; delivery/ack status | `escalated` or `follow_up_required` with truthful delivery status | Web-call transfer unavailable; callback destination/receipt unknown | **PARTIAL** |
| 6. Language switching and unsupported-language fallback | Multilingual selector, language prompt, fallback wording, optional escalation | Recognition/switch transcripts, fallback after two failures, supported-language response | Continue in MU EN/FR or UAE EN/AR; otherwise `escalated`/`follow_up_required` | Voice/ASR pairing and quality | **YES for configuration; NOT_RUN for quality** |
| 7. Natural-conversation recovery | Interruption sensitivity, responsiveness, backchannel/reminder tuning, correction/context prompts | Human review of interruption, silence, names/numbers, noise, changing intent and upset caller | Corrected draft or escalation; no stale action | Naturalness, accents/noise, exact settings | **YES for setting map; NOT_RUN for performance** |

## Mandatory unknowns and blockers

- **Resolved at design level:** the first-demo route uses Make API-key-authenticated ingress instead of requiring raw-body Retell HMAC verification.
- **Resolved at design level:** Make Data Store is the minimal receipt/idempotency ledger; Sheet and email are downstream outputs.
- Runtime authentication rejection, scenario sequencing, side-effect delivery, and reconciliation remain NOT_RUN.
- Exact customer Retell plan/workspace, agent/voice IDs, approved facts, exact language/voice/ASR pairings, recording/storage settings and retention/deletion controls are UNKNOWN — client/legal review required.
- MU/UAE carrier paths, imported-number setup, transfer reachability and callback service are UNKNOWN; web-call transfer is unsupported by Retell’s documented Transfer Call tool.
- Human language quality, interruption behaviour, tool latency, delivery and staff acknowledgement are NOT_RUN.
- No booking, reschedule, cancellation, customer lookup, CRM, database, dashboard, outbound follow-up or alternative provider is mapped or implemented.

The Gate B.1 architecture correction is complete at design level. Do not add a custom backend or reopen provider selection. Gate C/D remain unstarted pending separate owner approval.
