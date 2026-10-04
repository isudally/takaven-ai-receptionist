# Lean benchmark plan — future phase

**Design only. Not executed or authorised by repository setup.** Reconfirm the provisional Retell mapping, route, access and spend limit after owner approval. Compare complete deployable receptionist stacks only if the provisional path hits a demonstrated blocker, with reliability first and human telephone experience second.

## Stages

| Stage | Scope | Decision |
|---|---|---|
| 0: desk qualification | Fixed five candidate families | Qualified stacks, blockers, unknowns |
| 1: minimal functional screening | Five approved smoke scenarios for the provisional stack | Eliminate reproduced critical failures or unsupported mandatory functions |
| 2: human telephone smoke | About 2–3 calls per survivor | Select up to two finalists; do not rely solely on lab rankings |
| 3: finalist stress testing | About 12–15 cases per finalist, targeted repeats | Reliability gates, blind human preference, commercial viability |

Counts are initial allowances, not statistical proof. For three survivors, roughly 30 core sessions plus 24–30 finalist sessions and repeats is a starting budget, not a promise. A scenario becomes multiple sessions if languages/runs are duplicated; count actual sessions. Account for smoke calls and finalist telephone calls separately to avoid double counting. No validated cost exists yet.

## Core screening cases

FAQ; availability; confirmed booking; corrected booking/date; reschedule; cancellation; contact plus registration capture; unknown question; explicit human request; interruption with language switching. Distribute EN/FR/AR across screening; require meaningful coverage of every mandatory language before choosing finalists. Later stress calls deepen each language; no Kreol.

## Finalist cases

Hesitation and silence; overlapping speech/barge-in; multiple corrections; difficult names; phone/email/plate spelling; VIN when the client actually requires it; natural Gulf/UAE-relevant Arabic; EN/FR and EN/AR switching; background noise; prolonged interaction; upset caller; unavailable slot; tool timeout/failure; duplicate booking attempt; failed transfer; after-hours fallback; brief concurrency smoke.

For each action, verify that the tool executed, its arguments were correct and the final spoken confirmation matches the committed result. A convincing transcript does not prove a booking happened. Test retries/idempotency and authentication for changes; avoid using recognition alone as identity verification.

## Source-review case catalogue

The [QA catalogue](../qa/README.md) turns inspected failure modes into acceptance expectations. The first screen uses request capture, lead qualification, handoff, language and interruption cases. Booking/reschedule/cancellation/lookup cases remain deferred until a customer-owned booking authority exists. These are design, not run results; count sessions and language variants explicitly.

## Minimum implementation after authorisation

Use small scripts, one frozen business fixture, deterministic benchmark-only action mocks, common result JSON and a CSV/Markdown comparison. Prefer supported built-in testing/configuration tools where they satisfy the design. Implement only surviving interfaces; no universal framework or cloud review app. Blind review can use shuffled local recordings and a spreadsheet.

## Fairness controls

Freeze business facts, semantic rules, expected tool outcomes and scenario versions. Allow minimal provider-specific translation into supported settings and track every change. Set the same tuning time allowance before testing, provisionally 60 minutes per candidate, then document any justified exception and sensitivity.

Use common recordings for fixed utterances where supported. Replay cannot fairly reproduce adaptive live turn-taking; humans follow equivalent intent scripts and branch based on replies. Randomise provider order. Use comparable carrier paths, devices, call destinations and network conditions; record unavoidable differences. Do not penalise a platform merely because its API exposes fewer timing fields.

Choose a supported, representative voice per language under the same selection rule. Voice preference and recognisable provider voices can prevent perfect blinding; record that limitation. Disclose model, voice, settings and config hash in the private evidence key.

## Measurement and human judgement

Machine evidence: exact action arguments/results, business facts, corrections retained, errors, disconnects, speech-end/first-output timestamps when available and usage. Keep API latency separate from caller-perceived telephone latency. Report timing sample count with median/max; p90/p95 from small samples are exploratory, not dependable guarantees. Fillers alone are not meaningful answers.

Human evidence: natural wording/rhythm, voice quality, pronunciation, helpfulness, interruption recovery and emotional appropriateness. Use anonymised IDs, mixed order, 1–5 anchored ratings and pairwise preference on matched tasks. Listen before revealing transcripts. Have at least one fluent reviewer per required language; use a second reviewer on close results where possible. Review approximately 6–9 selected full calls per finalist, balanced across languages and critical situations, then targeted extras for ties/failures.

Repeat a critical failure using a fresh session and frozen scenario. If caused by a verified configuration error, fix it and rerun the impacted cases for all affected stacks where appropriate. Preserve both outcomes. Any unresolved critical failure blocks launch; repeated failures override average ratings.

## Selection

First pass reliability and language gates. Then compare human telephone experience. If practically tied, compare total cost, implementation burden, handover and integrations. The historical 100-point weighting may remain a secondary summary: naturalness 25, accuracy 20, turn-taking 15, language 15, messy speech 10, setup 5, telephony 5, cost 5. Never fill unavailable measurements with guessed scores or treat an incomplete total as final.

Do not force a winner by Day 3 if mandatory access or evidence is missing. Report no decision and the smallest next step. A three-day comparison selects a paid-pilot candidate, not proof of universal production reliability.
