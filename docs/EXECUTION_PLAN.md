# Execution plan — draft for owner approval

Status: **DRAFT — no provider spend, account activation, telephone provisioning or live call is authorised by this document.**

Owner: Ismaël. Orchestrator: main Codex agent. The plan turns the pre-execution review into a bounded path to one automotive receptionist demonstration for Mauritius and the UAE.

## Decisions this plan assumes

- The first demo captures appointment requests. It does not book, reschedule, cancel or look up customers.
- Retell is the provisional first mapping target because it has the strongest documented starting position in the desk pass. It is not the final provider decision until the required route and quality evidence pass.
- Gate D is a Retell web-call smoke test for both markets. Retell's purchased-number path is not a Mauritius route; Mauritius telephony and warm-transfer testing move to Gate E with separate carrier approval. UAE remains a clearly labelled browser/test call until a customer-owned carrier path is verified.
- The repository is public only for the temporary external review. Return it to private after this review and before commercial material or further implementation work is published.

## Gates

| Gate | Work | Exit test | Owner approval |
|---|---|---|---|
| A — alignment repair | Apply D23–D25, extend config/validator, revise QA, record telephony facts and remove stale gate wording | Validator passes; 20 cases are categorised; Drift Guard is CLEAR | Complete after this draft is reviewed |
| B — offline provider mapping | Map the two fictional profiles, appointment-request action, FAQs, routing, the Make receipt path and unsupported-language fallback into Retell's native configuration model | Mapping covers the logical `request_destination_ref`, custom-function signature handling, every supported field, unknown and provider-specific limitation; Retell number limits are recorded; no push | Required |
| C — web-call access decision | Confirm fictional test data, Make route design, reviewers and initial test ceiling; do not provision a number | Retell web-call path is the only Gate D route; no phone or carrier cost is included | Required |
| D — lean web-call screen | Run only the approved Retell web-call smoke scenarios using fictional data and callback capture for handoff | No critical failure in facts, language, request capture, receipt delivery or truthful callback outcome | Required before start |
| E — human telephone review | Separately approve and test a Mauritius/customer-owned carrier route and warm transfer, then review MU EN/FR and UAE EN/AR naturalness, switching, interruption and fallback | Carrier route and human destination are reachable; required language reviewers pass; unresolved critical issue blocks progression | Required |
| F — master demo freeze | Freeze facts, prompts, native settings, config hash, action receipts and rollback procedure | One automotive dealership/service flow is repeatable and handover-ready | Required |
| G — customer pilot | Customer-owned facts, route, account and staff handoff; controlled acceptance and training | Client acceptance, tested human fallback and monitored pilot | Required |

## Proposed first live test budget

No spend is authorised yet. If approved, start with the smallest Retell **web-call-only** smoke test: existing credit first, then a maximum owner-approved ceiling of **USD 25** for provider usage. No number purchase, Mauritius carrier, SIP setup or warm-transfer charge is included. Stop immediately if the route, language, receipt or truthful callback gate fails. Any carrier charge, paid plan, number or additional test requires a new explicit approval.

## Lean smoke scenarios

Run the smallest set needed to decide whether the provisional mapping is viable:

1. MU EN: approved FAQ, service enquiry and appointment-request capture.
2. MU FR: the same request with a correction and read-back.
3. UAE EN: vehicle-sales or test-drive qualification.
4. UAE AR: appointment-request capture and human fallback.
5a. MU: interruption and language switching.
5b. UAE: unsupported-language fallback.
5c. MU or UAE: failed handoff through callback capture; a web call must not claim a transfer occurred.

Record a separate verdict for each scenario. Record provider, model, voice, route, language, config hash, exact action arguments, the Make receipt ID, staff email/Sheet delivery, spoken result, reviewer and cost. The first-demo duplicate key is Retell `call_id` plus intent; Make upserts the Sheet row on that key, so a replay cannot create a second row. A transcript alone cannot pass an action case.

## Stop conditions

Stop and return to the owner if the provider cannot support the required market route, language quality, appointment-request receipt, truthful handoff, customer ownership or data controls. Do not add a custom voice runtime, booking database, CRM, dashboard, new provider or extra vertical to work around a failed gate.

## Approval checklist

- [ ] Confirm appointment-request scope.
- [ ] Approve Retell as the provisional first mapping target.
- [ ] Approve or change the proposed USD 25 live-test ceiling.
- [ ] Approve Gate D as web-call-only; defer the Mauritius phone route and warm-transfer test to Gate E.
- [ ] Name the Gate E human handoff destination; keep the number in provider/secret storage, never Git.
- [ ] Confirm UAE browser/test route until customer-owned carrier support is verified.
- [ ] Confirm reviewers for MU EN/FR and UAE EN/AR.
- [ ] Return the repository to private after this review.

Approval authorises the next gate only. It does not authorise provider spend, credential entry or live calls unless those items are explicitly approved.
