# Execution plan — frozen Gate 0A handoff

Status: **GATE 0A COMPLETE — no provider spend, account activation, telephone provisioning or live call is authorised by this document.**

Owner: Ismaël. Orchestrator: main Codex agent. The plan turns the pre-execution review into a bounded path to one automotive receptionist demonstration for Mauritius and the UAE.

## Decisions this plan assumes

- The first demo supports approved FAQs, service and vehicle-sales/test-drive qualification, lead capture, appointment-request capture, structured handoff, truthful escalation/callback fallback and post-call outcome summaries. It does not check availability, confirm bookings, reschedule, cancel or perform customer lookup.
- Retell is the accepted provisional first mapping target. It is not permanent vendor selection and provider comparison stays closed unless a demonstrated mandatory gate fails.
- Gate D is a Retell web-call smoke test for both markets. Retell's purchased-number path is not a Mauritius route; Mauritius telephony and warm-transfer testing move to Gate E with separate carrier approval. UAE remains a clearly labelled browser/test call until a customer-owned carrier path is verified.
- The repository is public only for the temporary external review. Return it to private after this review and before commercial material or further implementation work is published.

## Gates

| Gate | Work | Exit test | Owner approval |
|---|---|---|---|
| A — alignment repair | Apply accepted D23–D25, align scope/QA/privacy/actions and record telephony facts | Validator passes; active/deferred cases and seven smoke scenarios are consistent; Drift Guard is CLEAR | Complete |
| B — offline provider mapping | Map the two fictional profiles, appointment-request action, FAQs, routing, the Make receipt path and unsupported-language fallback into Retell's native configuration model | Mapping covers the logical `request_destination_ref`, custom-function signature handling, every supported field, unknown and provider-specific limitation; Retell number limits are recorded; no push | Required |
| C — web-call access decision | Confirm fictional test data, Make route design, reviewers and initial test ceiling; do not provision a number | Retell web-call path is the only Gate D route; no phone or carrier cost is included | Required |
| D — lean web-call screen | Run only the approved Retell web-call smoke scenarios using fictional data and callback capture for handoff | No critical failure in facts, language, request capture, receipt delivery or truthful callback outcome | Required before start |
| E — human telephone review | Separately approve and test a Mauritius/customer-owned carrier route and warm transfer, then review MU EN/FR and UAE EN/AR naturalness, switching, interruption and fallback | Carrier route and human destination are reachable; required language reviewers pass; unresolved critical issue blocks progression | Required |
| F — master demo freeze | Freeze facts, prompts, native settings, config hash, action receipts and rollback procedure | One automotive dealership/service flow is repeatable and handover-ready | Required |
| G — customer pilot | Customer-owned facts, route, account and staff handoff; controlled acceptance and training | Client acceptance, tested human fallback and monitored pilot | Required |

## Proposed first live test budget

No spend is authorised yet. If approved, start with the smallest Retell **web-call-only** smoke test: existing credit first, then a maximum owner-approved ceiling of **USD 25** for provider usage. No number purchase, Mauritius carrier, SIP setup or warm-transfer charge is included. Stop immediately if the route, language, receipt or truthful callback gate fails. Any carrier charge, paid plan, number or additional test requires a new explicit approval.

## Seven smoke scenarios

These are seven logical scenarios with separate verdicts. Actual language variants and calls are recorded as separate sessions; they do not change the scenario count.

1. Approved facts and unknown handling.
2. Mauritius service enquiry and lead capture.
3. UAE vehicle-sales/test-drive qualification.
4. Appointment request, correction and read-back.
5. Structured handoff, callback fallback and post-call outcome.
6. Language switching and unsupported-language fallback.
7. Natural-conversation recovery: interruption, hesitation/silence, difficult names/numbers, background noise, changing intent and upset caller.

Record a separate verdict for each scenario. Record provider, model, voice, route, language, config hash, exact action arguments, receipt reference, staff email/Sheet delivery, spoken result, reviewer and cost. Gate B must define and verify signature checking, replay serialization, stored receipt/payload comparison and separately deduplicated email delivery. The first demo permits at most one committed request per intent per call; within that limit, the duplicate key is trusted Retell `call_id` plus intent and Gate D must prove that a replay creates no second Sheet row or email. A second same-intent request routes to human follow-up. A transcript alone cannot pass an action case.

## Stop conditions

Stop and return to the owner if the provider cannot support the required market route, language quality, appointment-request receipt, truthful handoff, customer ownership or data controls. Do not add a custom voice runtime, booking database, CRM, dashboard, new provider or extra vertical to work around a failed gate.

## Gate 0A completion checklist

- [x] Freeze D23 first-demo scope.
- [x] Freeze D24 Retell provisional mapping target.
- [x] Freeze D25 staged market routes.
- [x] Keep Gate B unopened; preserve provider, route, data and reviewer unknowns for the next gate.

Gate B offline Retell mapping is the next project gate. It has not been started by this task and requires the owner's instruction to proceed.
