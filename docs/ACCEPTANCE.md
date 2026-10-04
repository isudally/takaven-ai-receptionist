# Acceptance and launch gates

**No gate has been tested.** These are acceptance requirements for later execution, not achieved performance or statistical guarantees.

## Reliability blockers

Any unresolved wrong appointment/date/time, fabricated price/policy, restricted action, disclosure to an unauthorised caller, lost material correction, failed explicit escalation without a truthful fallback, or unreliable telephone path blocks launch. Do not average these away.

| Area | Required evidence before a paid pilot |
|---|---|
| Knowledge | Exact approved facts; unknowns acknowledged and routed without invention |
| Booking | Availability checked; explicit confirmation before mutation; correct committed slot/timezone; no duplicate mutation on retries |
| Changes/cancellation | Appropriate identity check; correct booking targeted; committed result matches spoken response |
| Contact capture | Correct name/phone; confirm ambiguous spelling/numbers; accurate actionable handoff |
| Corrections | Final details replace earlier details in both tool arguments and summary |
| Escalation | Explicit human requests respected; urgent path and transfer-failure/callback fallback verified |
| Language | Fluent-reviewer pass in EN/FR/AR; natural required switching; no Kreol testing |
| Telephone | Actual customer-like phone route tested, including disconnect, noise, interruption and call ending |
| Tool failure | No success claim when action fails; safe retry/fallback; clear staff action |
| Data handling | Client-approved access, disclosure/recording approach, retention and handover controls |
| Operations | Mode/routing/after-hours, rollback and human backup demonstrated |

## Evidence record

Every acceptance case records ID, fixture/config version, expected outcome, actual tool result, spoken result, language, session/call reference, reviewer where applicable, verdict and unresolved issue. Use PASS/FAIL/BLOCKED/NOT RUN. Fictional demos and real-client acceptance have separate fixtures.

## Pilot approval

Freeze a client-specific acceptance set before execution. Every mandatory case must pass, with repeated critical action cases and no unresolved launch blockers. State sample sizes and limitations; passing a finite test set does not guarantee flawless operation. Agree monitoring, first-week review and a tested switch back to human routing.

No automatic declaration of launch readiness based on a provider score, vendor marketing or an untested specification.
