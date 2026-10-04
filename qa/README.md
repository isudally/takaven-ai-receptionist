# Acceptance design and evidence

[acceptance-cases.csv](acceptance-cases.csv) is a staged 20-case catalogue, not executed results. The initial ~5-case screen in [execution plan](../docs/EXECUTION_PLAN.md) remains lean. Select/translate cases into supported native tests only for qualified survivors; use targeted repeats for critical races/actions. Human telephone cases remain distinct from offline checks. Booking-lifecycle cases are explicitly DEFERRED until a customer-owned booking authority is selected.

[run-record.example.json](run-record.example.json) shows a NOT_RUN evidence record. Record config hash, scenario version, provider/model/voice/region, telephone path, session references, action receipts, spoken result and reviewer. Missing evidence stays null and cannot pass. Do not commit real transcripts, recordings or personal information; keep access-controlled evidence references.

Status vocabulary: PASS / FAIL / BLOCKED / NOT_RUN. Every blocker must pass before pilot launch. Local config-lint PASS proves only lint conformance, never receptionist readiness. Native vendor tests do not establish telephone quality or cross-system commitment.

For action cases, compare the authorised intent, exact tool arguments, authoritative stored result and spoken claim. For summary/delivery cases, verify both delivery and staff acknowledgement separately. Races and replay cases must cover create AND reschedule, delayed duplicate after cancellation and outcome-unknown reconciliation. Do not average a critical failure into a subjective quality score.

Test execution still requires qualified survivors, approved session/spend limits and reviewer/telephone access. No external tests or calls were run during this source review.
