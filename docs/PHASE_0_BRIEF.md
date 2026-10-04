# Phase 0 — desk qualification execution brief

## Task

When instructed to begin Phase 0, qualify the five candidate families below using official public documentation. Recommend which deployable stacks deserve a small benchmark. Do not choose a final engine without testing.

1. OpenAI realtime/live candidate, previously labelled GPT-Live-1, plus existing supported telephony integration.
2. Google Gemini live candidate, previously labelled Gemini 3.8 Live, plus existing supported telephony integration.
3. Retell AI.
4. ElevenLabs agent/receptionist offering; verify ElevenAgents and Reception.ai product boundaries.
5. Synthflow.

These labels are unverified. First confirm the exact offered product, supported model identifier, plan, availability and official documentation. If a supplied version cannot be verified, record that explicitly and identify the current official equivalent for review; do not silently replace the shortlist or invent a product.

## Constraints

Read the repository before researching. Public-document research only: no provider API calls, account creation, credentials, telephone provisioning, test sessions, audio generation, benchmark code or paid activity. Keep research focused on the fixed shortlist. Do not contact vendors or other people without instructions.

Timebox the first desk pass to approximately 2–4 hours of executor work. Report unresolved gates rather than extending research indefinitely. This is a planning allowance, not an assertion that every gate can be verified in that time.

## Qualification gates

For each exact proposed stack, document:

1. Product existence/access: generally available, preview or restricted; required plan and official interface.
2. Complete telephone path: existing-number routing/forwarding/SIP, inbound operation, outbound callback/transfer if needed; separate Mauritius and UAE feasibility. A country listed for number purchase does not prove compatibility with a customer's existing carrier.
3. Language capability: EN/FR/AR documented; automatic detection/switching support. Documented support does not establish native-quality performance.
4. Conversation controls: interruption/barge-in, turn detection and relevant configuration.
5. Business actions: supported tools/webhooks/calendar integration for availability, booking, changes and cancellation.
6. Human handoff: transfer path, failure handling and callback fallback. Define whether urgent live transfer is available for the chosen client path.
7. Evidence access: supported recordings, transcripts, tool logs, timestamps and export/retention constraints.
8. Configuration access: official API or supported UI; minimal steps; limitations. An adequate supported UI can be viable even without a configuration API.
9. Customer ownership: separate client accounts, access delegation, data/config export and practical handover. Do not describe proprietary vendor dependence as zero lock-in.
10. Deployment/commercial feasibility: supported integration fits buy/configure/integrate boundaries and a 30-day launch target; costs, minimums and ongoing dependencies.
11. Data/contract prerequisites: processing locations, retention controls, recording/AI disclosure requirements and any relevant customer/carrier verification. Use authoritative sources for legal assertions; mark unresolved interpretation for review.

## Evidence method

Use `PROVIDER_QUALIFICATION.md`. Store the source URL, date checked, exact plan/region, concise finding and limitation. Prefer vendor documentation, official pricing, terms and carrier documentation. Marketing language alone is insufficient for a technical pass.

Use PASS, FAIL or UNKNOWN per requirement. A documented blocker can eliminate a stack. UNKNOWN means unresolved, not rejected and not qualified. A viable supported workaround must show its extra cost and manual work. Do not write an adapter to prove a desk assumption.

## Outputs

Update the gate matrix and evidence records; update `MANUAL_ACTIONS.md` and `STATUS.md`. Produce a concise `reports/PHASE_0_RECOMMENDATION.md` containing:

- verified products and complete proposed stacks;
- survivors, eliminated candidates and unresolved requirements, with reasons;
- minimum human actions and account/access prerequisites;
- verified cost components and unknowns;
- recommended lean test scope for survivors;
- market-specific constraints and whether separate market choices may be needed;
- exact next action and any spend/access decisions.

Stop after the desk report. No promise of three survivors and no forced winner. If none qualifies, explain the blockers before reopening discovery or changing scope.
