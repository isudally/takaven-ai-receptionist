# Acceptance and launch gates

**No gate has been tested.** These are acceptance requirements for later execution, not achieved performance or statistical guarantees.

## Reliability blockers

Any unresolved wrong appointment/date/time, fabricated price/policy, restricted action, disclosure to an unauthorised caller, lost material correction, failed explicit escalation without a truthful fallback, or unreliable telephone path blocks launch. Do not average these away.

| Area | Required evidence before a paid pilot |
|---|---|
| Knowledge | Exact approved facts; unknowns acknowledged and routed without invention |
| Appointment requests | Requested service/date/time window, contact and vehicle read back accurately; staff/queue receipt recorded; no booking claim |
| Changes/cancellation | **Deferred for the first demo.** When booking lifecycle is enabled, appropriate identity check; correct booking targeted; committed result matches spoken response |
| Contact capture | Correct name/phone; confirm ambiguous spelling/numbers; accurate actionable handoff |
| Corrections | Final details replace earlier details in both tool arguments and summary |
| Escalation | Explicit human requests respected; urgent path and transfer-failure/callback fallback verified |
| Language | Fluent-reviewer pass in EN/FR/AR; natural required switching; no Kreol testing |
| Telephone | Actual customer-like phone route tested, including disconnect, noise, interruption and call ending |
| Tool failure | No success claim when action fails; safe retry/fallback; clear staff action |
| Data handling | Client-approved access, disclosure/recording approach, retention and handover controls |
| Operations | Mode/routing/after-hours, rollback and human backup demonstrated |

## Source-review regression requirements

Use the cases in [qa/acceptance-cases.csv](../qa/acceptance-cases.csv) as the staged catalogue. The first demo catalogue covers approved facts and unknown handling; service and vehicle-sales/test-drive qualification; lead capture; corrected appointment-request capture and readback; structured handoff, escalation/callback fallback and outcome summaries; language switching and unsupported-language fallback; and natural-conversation recovery for interruption, hesitation, difficult names/numbers, noise, changing intent and upset callers. Replay and changed-payload receipt checks apply to action paths. Booking availability, confirmed booking, reschedule, cancellation, lookup, duplicate-booking and capacity-race cases are marked `DEFERRED` until a customer-owned booking authority is selected and tested. Later critical checks include timeout reconciliation, terminal retry exclusion, authenticated customer binding, no production stub success, truthful transfer status and separate summary delivery versus staff acknowledgement.

Each mandatory language needs its own appropriate coverage; a single case label spanning languages is not three executed tests. Cases marked `DEFERRED` are intentionally not active for the first demo; active cases remain `NOT_RUN` until tested. Local config lint is separate evidence.

## Evidence record

Every acceptance case records ID, fixture/config version, expected outcome, actual tool result, spoken result, language, session/call reference, reviewer where applicable, verdict and unresolved issue. Use PASS/FAIL/BLOCKED/NOT RUN. Fictional demos and real-client acceptance have separate fixtures.

## Pilot approval

Freeze a client-specific acceptance set before execution. Every mandatory case must pass, with repeated critical action cases and no unresolved launch blockers. State sample sizes and limitations; passing a finite test set does not guarantee flawless operation. Agree monitoring, first-week review and a tested switch back to human routing.

No automatic declaration of launch readiness based on a provider score, vendor marketing or an untested specification.
