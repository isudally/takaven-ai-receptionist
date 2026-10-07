# Acceptance design and evidence

> **Current evidence note (2026-10-06):** The staged catalogue below is retained as the broader acceptance design. Current Receptionist evidence is recorded separately: automated regression scenarios A–H **PASS**, fictional French human voice evidence **COMPLETED**, conversation polish **IMPLEMENTED**, and final human release acceptance **DEFERRED until first external-demo readiness**. Do not read the legacy `NOT_RUN` values in the example catalogue as a claim that current A–H regression evidence is absent.

[acceptance-cases.csv](acceptance-cases.csv) is a staged catalogue, not executed results. The initial screen is seven logical smoke scenarios in [execution plan](../docs/EXECUTION_PLAN.md); language variants and actual calls are separate sessions. Select/translate cases into supported native tests only for qualified survivors; use targeted repeats for critical receipt/action cases. Human telephone cases remain distinct from offline checks. Booking-lifecycle cases are explicitly `DEFERRED` until a customer-owned booking authority is selected.

[run-record.example.json](run-record.example.json) shows a NOT_RUN evidence record. Record config hash, scenario version, provider/model/voice/region, telephone path, session references, action receipts, spoken result and reviewer. Missing evidence stays null and cannot pass. Do not commit real transcripts, recordings or personal information; keep access-controlled evidence references.

Status vocabulary: PASS / FAIL / BLOCKED / NOT_RUN. Every blocker must pass before pilot launch. Local config-lint PASS proves only lint conformance, never receptionist readiness. Native vendor tests do not establish telephone quality or cross-system commitment.

For action cases, compare the authorised intent, exact tool arguments, authoritative stored result and spoken claim. The active v0.1 path is Retell → authenticated n8n → Google Sheets → synchronous `RECEIVED`; it does not promise exactly-once semantics. Callback delivery and staff acknowledgement remain separate statuses. Natural-conversation review covers interruption, hesitation/silence, difficult names/numbers, accents/background noise, changing intent and upset callers without claiming achieved performance. Booking-specific races remain deferred with the booking lifecycle. Do not average a critical failure into a subjective quality score.

Test execution still requires qualified survivors, approved session/spend limits and reviewer/telephone access. No external tests or calls were run during this source review.
