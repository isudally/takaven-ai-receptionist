# Offline validation — 2026-10-04 (alignment repair)

Scope: original TAKAVEN draft configuration and repository consistency only. No vendor APIs, source-repository tests, generated audio, telephone sessions, provisioning or paid activity.

## Checks

| Check | Result | Meaning |
|---|---|---|
| Mauritius and UAE profile lint | VALID_DRAFT (2 profiles) | Fixed v1 structure and local safety policies conform; unresolved prerequisites remain |
| Unsafe/invalid variants | PASS (23 rejected) | Wrong types/keys, market/timezone/language mismatch, duplicate services, localized FAQ mismatch, empty intent fields, unsafe handoff, false confirmation, unsafe binding, recording and consent errors rejected |
| Deterministic configuration hash | PASS | Repeated validation of the same profile produces the same digest |
| Python syntax | PASS | Local validator parses |
| JSON artifacts | PASS | Examples and source inventory parse |
| QA catalogue | PASS | 20 unique staged cases; booking-lifecycle cases DEFERRED and provider cases NOT_RUN |
| Source inventory | PASS | 42 pinned blobs across 6 repositories |
| Relative documentation links | PASS | Referenced local documentation files exist |
| Git whitespace check | PASS | No diff whitespace errors |

Commands: `python scripts/validate_config.py`, `python scripts/validate_config.py --self-test`, `git diff --check`; stdlib checks for syntax/JSON/CSV/source inventory and local link targets.

## Draft hashes

- Mauritius: `27ced26e933769960f30d36321d807845add5fe93281ec5a0d59e4fa350fe18a`
- UAE: `9b27dc4b1d28472546cc221257491b47bed68f2aef1409cde5b79c0ba5daba65`

Both report `deployment_ready: false`. Each has 9 unresolved first-demo prerequisites: provider, agent, identity policy, rollback, handoff destination, retention, two voice references and fact approval. The booking authority is reported separately as one deferred prerequisite.

## Limits

Static source review establishes inspected code behavior and reasoned risks only. The lint is a small dedicated check for our fixed draft format; it does not establish provider capability, authentication correctness, concurrency, action commitment, naturalness, regulatory suitability or launch readiness.

No provider result exists. The desk pass is complete. The next gate is owner approval of `docs/EXECUTION_PLAN.md`, followed by offline Retell mapping and a separately authorised testing phase with route, reviewer and spend limits.
