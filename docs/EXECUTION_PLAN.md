# Execution plan — draft for owner approval

Status: **DRAFT — no provider spend, account activation, telephone provisioning or live call is authorised by this document.**

Owner: Ismaël. Orchestrator: main Codex agent. The plan turns the pre-execution review into a bounded path to one automotive receptionist demonstration for Mauritius and the UAE.

## Decisions this plan assumes

- The first demo captures appointment requests. It does not book, reschedule, cancel or look up customers.
- Retell is the provisional first mapping target because it has the strongest documented starting position in the desk pass. It is not the final provider decision until the required route and quality evidence pass.
- Mauritius may use a real telephone route after carrier and handoff details are confirmed. UAE begins as a clearly labelled browser/test call until a customer-owned carrier path is verified.
- The repository is public only for the temporary external review. Return it to private after this review and before commercial material or further implementation work is published.

## Gates

| Gate | Work | Exit test | Owner approval |
|---|---|---|---|
| A — alignment repair | Apply D23–D25, extend config/validator, revise QA, record telephony facts and remove stale gate wording | Validator passes; 20 cases are categorised; Drift Guard is CLEAR | Complete after this draft is reviewed |
| B — offline provider mapping | Map the two fictional profiles, appointment-request action, FAQs, routing, handoff and unsupported-language fallback into Retell's native configuration model | Mapping document identifies every supported field, unknown and provider-specific limitation; no push | Required |
| C — route and access decision | Confirm demo route, human destination, customer-owned account, reviewer languages and initial test ceiling | One reachable route per approved market, or UAE explicitly remains browser/test only | Required |
| D — lean functional screen | Run only the approved Retell smoke scenarios using fictional data and the approved route | No critical failure in facts, language, request capture, handoff or truthful outcomes | Required before start |
| E — human telephone review | Fluent Mauritius EN/FR and UAE EN/AR review of naturalness, switching, interruption and fallback | Required language reviewers pass the acceptance gates; unresolved critical issue blocks progression | Required |
| F — master demo freeze | Freeze facts, prompts, native settings, config hash, action receipts and rollback procedure | One automotive dealership/service flow is repeatable and handover-ready | Required |
| G — customer pilot | Customer-owned facts, route, account and staff handoff; controlled acceptance and training | Client acceptance, tested human fallback and monitored pilot | Required |

## Proposed first live test budget

No spend is authorised yet. If approved, start with the smallest Retell smoke test: existing credit first, then a maximum owner-approved ceiling of **USD 25** for provider usage and no number purchase. Stop immediately if the route, language, handoff or truthful receipt gate fails. Any carrier charge, paid plan or additional test requires a new explicit approval.

## Lean smoke scenarios

Run the smallest set needed to decide whether the provisional mapping is viable:

1. MU EN: approved FAQ, service enquiry and appointment-request capture.
2. MU FR: the same request with a correction and read-back.
3. UAE EN: vehicle-sales or test-drive qualification.
4. UAE AR: appointment-request capture and human fallback.
5. MU or UAE: interruption, unsupported-language fallback and failed handoff.

Record provider, model, voice, route, language, config hash, exact action arguments, staff/queue receipt, spoken result, reviewer and cost. A transcript alone cannot pass an action case.

## Stop conditions

Stop and return to the owner if the provider cannot support the required market route, language quality, appointment-request receipt, truthful handoff, customer ownership or data controls. Do not add a custom voice runtime, booking database, CRM, dashboard, new provider or extra vertical to work around a failed gate.

## Approval checklist

- [ ] Confirm appointment-request scope.
- [ ] Approve Retell as the provisional first mapping target.
- [ ] Approve or change the proposed USD 25 live-test ceiling.
- [ ] Confirm Mauritius route and human handoff destination.
- [ ] Confirm UAE browser/test route until customer-owned carrier support is verified.
- [ ] Confirm reviewers for MU EN/FR and UAE EN/AR.
- [ ] Return the repository to private after this review.

Approval authorises the next gate only. It does not authorise provider spend, credential entry or live calls unless those items are explicitly approved.
