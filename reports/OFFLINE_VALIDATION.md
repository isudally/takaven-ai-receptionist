# Offline validation — 2026-10-04

Scope: original TAKAVEN draft configuration and repository consistency only. No vendor APIs, source-repository tests, generated audio, telephone sessions, provisioning or paid activity.

## Checks

| Check | Result | Meaning |
|---|---|---|
| Mauritius and UAE profile lint | VALID_DRAFT (2 profiles) | Fixed v1 structure and local safety policies conform; unresolved prerequisites remain |
| Unsafe/invalid variants | PASS (20 rejected) | Wrong types/keys, market/timezone/language mismatch, duplicate services, false confirmation, unsafe binding, recording and consent errors rejected |
| Deterministic configuration hash | PASS | Repeated validation of the same profile produces the same digest |
| Python syntax | PASS | Local validator parses |
| JSON artifacts | PASS | Examples and source inventory parse |
| QA catalogue | PASS | 15 unique cases; every provider case NOT_RUN |
| Source inventory | PASS | 42 pinned blobs across 6 repositories |
| Relative documentation links | PASS | Referenced local documentation files exist |
| Git whitespace check | PASS | No diff whitespace errors |

Commands: `python scripts/validate_config.py`, `python scripts/validate_config.py --self-test`, `git diff --check`; stdlib checks for syntax/JSON/CSV/source inventory and local link targets.

## Draft hashes

- Mauritius: `3e03a9ac6dc249c22995f6b3eb10264cc5c2202f0d94221b435fff2d672aaad7`
- UAE: `b9a9b105088257e212599a0b337cb5230bb8af6e6800fc67d28dd3fba5a9326f`

Both report `deployment_ready: false`. Each has 10 unresolved prerequisites: provider, agent, booking authority, identity policy, human fallback, rollback, retention, two voice references and fact approval.

## Limits

Static source review establishes inspected code behavior and reasoned risks only. The lint is a small dedicated check for our fixed draft format; it does not establish provider capability, authentication correctness, concurrency, action commitment, naturalness, regulatory suitability or launch readiness.

No provider result exists. The next gate is official-source desk qualification, followed by a separately authorised mapping/testing phase with session and spend limits.
