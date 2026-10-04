# Source-level GitHub review and adoption decisions

Reviewed 2026-10-04. This replaces the earlier README-only assessment. We inspected 42 selected source/configuration/licence files across six repositories, including the critical booking, authentication, retry and deployment paths. [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json) records each exact blob SHA, commit and source URL. No external code or tests were executed. Findings below are static observations and reasoned risks, not demonstrated production exploits or measured quality.

## Decision

Build TAKAVEN's own small configuration and integration pack. Use a selected vendor's existing voice runtime and supported tooling. Adopt useful requirements from all six references; do not stitch together six runtimes, copy restricted implementation, or fork a complete platform before provider qualification. No repository proves Mauritius/UAE telephone availability or EN/FR/AR quality.

| Reference | Keep | Skip or strengthen | Reuse decision |
|---|---|---|---|
| dma-deploy-kit | Strict client configuration; deterministic prompts; plan/apply separation; config fingerprints; raw-body signature/replay checks; explicit messaging consent | US-only phone rules; file-based send deduplication; booking-link-only scope; partial drift detection; unpinned application dependencies | MIT licence inspected. Useful optional Retell tooling later; original TAKAVEN configuration now |
| resto-voice-demo | Booking-store boundary; database overlap/cap enforcement; tenant-scoped calls; distinct modified/cancelled staff follow-up; offline testing seams | Create-only capacity guard; optional HMAC/URL token; caller-ID identity assumptions; default tenant and caller-number routing fallbacks; per-instance rate limiting | README grants no reuse rights. Architecture lessons only; no code, prompts or migrations imported |
| kaa911-syp/ai-voice-receptionist | Service catalogue; required-field checks; canonical retry keys; database constraints; correlated error records; durable alert claims | Stub availability/confirmation; escalation without verified delivery; incomplete retry stop condition; simulator auth on production path; future reschedule/cancel | No licence grant found in root tree or inspected README. No code reuse |
| elevenlabs/cli | Native agent/tool/test files and ID registries; version/branch handling; pull and dry-run workflows | Force-override push; presence-only read-back verification; commands that create remote resources | MIT inspected. Prefer official CLI if ElevenLabs qualifies; do not build another CLI |
| elevenlabs/examples | Server-held provider key; server-issued conversation token; native interruption/guardrail events | Unauthenticated creation/token handlers; caller-supplied agent ID; banking end-call guardrail policy; browser demo as telephone evidence | MIT inspected. Learn supported SDK shapes; avoid shipping public demo endpoints |
| Twilio/OpenAI sample | PCMU audio pass-through; per-call stream state; playback marks; clear/truncate on interruption | Missing visible inbound/stream authentication; raw event logging; no business actions; limited disconnect recovery; conversational joke prompt | MIT inspected. Telephone bridge reference only if a supported bridge qualifies |

## 1. dma-deploy-kit

**Sources:** `config/client.example.yaml`, `config/models.py`, `agent/deploy.py`, `postcall/signature.py`, `postcall/sms.py`, `evals/latency_checks.py`, `evals/transcript_checks.py`, `evals/runlog.py`, `pyproject.toml` (full paths in inventory).

Configuration rejects unknown keys and validates timezone identifiers. Business facts, languages, post-call extraction and voice settings are separated. Deployment distinguishes read-only planning from mutation, records remote IDs and restricts differences to fields it manages. Evaluation records identify prompt/config versions; missing latency data becomes a finding instead of a fabricated pass. These are strong deployment and evidence practices.

The SMS sender normalises US numbers only. Its send-once flow checks a JSONL file, calls Twilio, then records the result; two workers or a crash after send can therefore produce duplicates. The passed idempotency key is not transmitted to Twilio in the inspected send method. This is local best effort, not a transactionally safe distributed guarantee. Missing messaging credentials select a debug sink; production must fail closed instead. Configuration supports sending a booking URL, not proof of direct appointment creation.

The deploy differ explicitly cannot clear fields it omits, such as an unset webhook URL. A safe TAKAVEN release needs field ownership, explicit clearing and comparison of read-back values. Dependencies are broadly specified; if reused later, pin the reviewed release and lock dependencies. Latency budgets belong to that project and are not our SLA.

**TAKAVEN changes:** strict offline configuration lint; market-specific phone/timezone/currency; approved facts; config hashes; separate local validation, vendor plan and apply; durable action replay requirement; no debug-success fallback.

## 2. resto-voice-demo

**Sources:** `lib/bookings.ts`, `lib/voice-handlers.ts`, `lib/http-guard.ts`, `lib/restaurant-routing.ts`, `lib/rate-limit.ts`, `lib/reconciliation.ts`, `lib/agent-functions.ts`, overlap/cap migrations and README.

Booking correctness is enforced beyond the prompt. The service rechecks on database conflicts; a range exclusion constraint blocks overlapping table bookings. A transaction-scoped lock and recount guard allocation caps during creation. Handlers replace model-supplied call IDs with provider call metadata and keep post-call outcomes connected to the acting call. Staff reconciliation distinguishes new, changed and cancelled bookings after earlier handover. This avoids a misleading single “booked” outcome.

There are important limits. The modification path explicitly lacks the same capacity guard as create, so concurrent modifications can exceed a cap. Cancellation clears the original create key; delayed old requests need a durable operation history to avoid recreating a cancelled intention. HMAC is optional in the handler and a secret query parameter can be the active authentication. Our deployment will require the provider's supported verified authentication and keep credentials out of URLs. Caller ID must not substitute for an approved identity check.

The routing helper can use the caller's number or return a default restaurant when forwarding metadata does not match. For our customer pack, use a verified destination/agent/account binding and fail closed on ambiguity. The rate limiter documents per-instance memory limits; do not describe it as distributed protection.

**TAKAVEN changes:** require atomic capacity protection on both create and reschedule in the existing booking authority; retain replay records after cancellation; bind customer from trusted metadata; distinguish changed/cancelled/unknown outcomes; preserve staff acknowledgement status. We will not implement this repository's custom restaurant database or dashboard.

## 3. kaa911-syp/ai-voice-receptionist

**Sources:** router and retry-worker JSON, service/idempotency migrations, tool definitions, limitations and workflow docs.

The router makes service IDs/durations authoritative, normalises envelopes and computes deterministic retry keys. Database overlap and unique-key constraints are useful complements to preflight checks. Error records carry call/action context. These are sensible integration patterns to require from existing automation.

However, availability generates slots from opening hours and labels the calendar as a stub; it does not intersect live calendar occupancy. Create inserts a `pending_confirmation` row yet returns `confirmed`, with no external calendar event ID. When persistence is disabled it can still return confirmed with a null appointment ID. A database row is also not necessarily the customer calendar's commitment. We reject all three confirmation shortcuts.

Escalation returns `escalated` even though the branch only attempts an error-row write for high urgency; no verified transfer or delivery appears in that branch. Retry processing mostly reconciles or defers, rather than replaying failed actions. At its limit it sets the next retry time to null but leaves the event open and retriable; the selection includes null times, so the record can be selected again. The comment saying it stops is not sufficient.

The signature node falls back to JSON reserialization if raw body is unavailable, which can fail genuine signatures. The internal simulator signature has no timestamp replay window and is accepted on the same path. These concerns require provider-specific raw-body verification and isolated test credentials, not blindly reused authentication.

**TAKAVEN changes:** explicit committed/pending/conflict/unknown outcomes; authoritative booking ID; no simulated facts in production; bounded attempts and terminal/manual-review status; verify transfer/delivery; data retention and customer isolation before launch. Reschedule/cancel are roadmap items here, not implemented capability evidence.

## 4. ElevenLabs native CLI

**Sources:** hand-written workflow modules `agents.rs`, `tools.rs`, `tests.rs`, `project.rs`, `verify.rs`; generated API code was not exhaustively audited.

Agent/tool/test registries and raw vendor configuration files keep remote IDs and versions visible. Native pull, push, branch and dry-run support reduces the need for a TAKAVEN orchestration platform. Test definitions are useful after a provider survives qualification.

Push identifies itself as a force override and can include registered branch configurations when a single target is not specified. Read-back verification recursively checks key presence; arrays and scalar values are leaves, so a present but wrong value can pass that check. Verification issues warn rather than fail the push. TAKAVEN must scope the target, snapshot before changes and compare managed values explicitly, including cleared settings and tool destinations. Test-add creates remote resources; a command's name does not make it offline.

**TAKAVEN changes:** select and pin native tooling only after qualification; record target account/agent/branch/version; release plan, previous version, owned fields and read-back evidence; do not treat CLI warnings or presence checks as acceptance.

## 5. ElevenLabs examples

**Sources:** Next.js quickstart agent/token handlers and guardrails agent handler.

Provider credentials stay server-side and conversation tokens are obtained through the vendor SDK. Native interruption and guardrail event hooks are useful for later observation. No need to build speech components.

The inspected agent POST handler provisions an agent on request and has no application authentication check. The token GET handler accepts the caller's agent ID and contains no caller entitlement/rate check. Those routes are demonstrations; an exposed deployment would need authenticated access, authorised agent allowlisting and abuse controls. Provider API errors also reach responses.

The guardrail example is for banking and ends the call for an investment violation. That policy does not fit an automotive receptionist: our unknown/safety/complaint routes should usually reach an approved human fallback. Browser WebRTC does not establish PSTN route or language performance.

**TAKAVEN changes:** server-side credentials, scoped supported integrations and an automotive conversation policy; no public provisioning/token demo or browser dashboard.

## 6. Official Twilio/OpenAI Realtime sample

**Sources:** `index.js`, `package.json`, licence.

The sample streams PCMU without a custom speech pipeline. Playback marks, media timestamps and clear/truncate handling show why interruption must synchronise heard audio and model context. Keep this as an acceptance requirement for the selected managed telephone route.

The inspected HTTP and WebSocket handlers show no Twilio signature/stream-origin validation. The incoming stream URL derives from the request host; a deployed service should use a validated configured origin. Error/event logging can include full message bodies, so caller data needs minimisation. OpenAI closing only logs an event; the inspected path does not move the caller to a verified human fallback. No booking, identity, transfer or tenant controls are provided. A zero media timestamp is also tested by truthiness in response-start tracking; precise interruption timing needs regression coverage.

**TAKAVEN changes:** require authenticated carrier entry, safe disconnect/transfer behavior, redacted logs and meaningful telephone interruption tests. Do not run this sample as our receptionist or assume its model/settings are the qualified shortlist.

## Licence and provenance

The four inspected MIT licences permit reuse subject to their notices and other applicable obligations; we imported none of their code. The restaurant source is published without a reuse grant; KAA's inspected root/README provides none. No restricted code, prompts, migrations or workflow files are included in TAKAVEN. Our configuration, contracts, lint and QA cases were independently authored from our requirements. If a dependency or source fragment is adopted later, record exact version, licence and attribution first.

Static source review does not establish security, uptime, commercial suitability, vendor terms or language quality. Existing test files and assertion counts are authors' evidence, not tests we reran. The next product decision still requires official provider qualification and later authorised telephone testing.

## Reuse Scout checkpoint — 2026-10-04

The dedicated read-only scout made two focused queries and opened three strong matches. These are new discovery leads, separate from the completed 42-file source audit. No code was downloaded, executed or adopted. Licence grants remain UNKNOWN where a full licence was not retrieved.

| Asset | Useful overlap | Action and limits |
|---|---|---|
| [elevenlabs/plugin](https://github.com/elevenlabs/plugin), [agent guide](https://github.com/elevenlabs/plugin/blob/main/skills/general/agents/SKILL.md) | Native scheduling/CRM and human-transfer configuration guidance | Resolve exact supported booking lifecycle and failure handling during ElevenAgents qualification; guide metadata is not a verified licence grant |
| [twilio/twilio-agent-connect-python](https://github.com/twilio/twilio-agent-connect-python) | Existing GPT-Live telephone/channel integration SDK | Verify supported package/model pairing and licence before proposing custom bridge work; not a complete receptionist |
| [RetellAI/retell-typescript-sdk](https://github.com/RetellAI/retell-typescript-sdk) | Existing typed vendor API client and provisioning operations | Prefer supported SDK if selected; verify version/licence first; no new client needed now |

Scout disposition: FLAG useful qualification/reuse leads; CLEAR for desk work. Native tools do not prove atomic booking, replay protection, local routing or bilingual quality. Keep all complete provider stacks UNRESOLVED. Future checks are triggered by a concrete custom-code proposal, not repeated broad discovery.
