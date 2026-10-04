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
| QA catalogue | PASS | 26 unique staged cases; active cases NOT_RUN and booking-lifecycle cases DEFERRED |
| Source inventory | PASS | 42 pinned blobs across 6 repositories |
| Relative documentation links | PASS | Referenced local documentation files exist |
| Git whitespace check | PASS | No diff whitespace errors |

Commands: `python scripts/validate_config.py`, `python scripts/validate_config.py --self-test`, `git diff --check`; stdlib checks for syntax/JSON/CSV/source inventory and local link targets.

## Draft hashes

- Mauritius: `55fead02611723fb156a6a73ee076778d8244a5be80db79c10b114c4040746fa`
- UAE: `8b6dca4412746ed7c5c252b453c8318a8d4a085847349dbccfa181ae60b1e994`

Both report `deployment_ready: false`. Each has 9 unresolved first-demo prerequisites: provider, agent, identity policy, rollback, handoff destination, retention, two voice references and fact approval. The booking authority is reported separately as one deferred prerequisite.

## Limits

Static source review establishes inspected code behavior and reasoned risks only. The lint is a small dedicated check for our fixed draft format; it does not establish provider capability, authentication correctness, concurrency, action commitment, naturalness, regulatory suitability or launch readiness.

No provider result exists. Gate 0A alignment is complete. Gate B offline Retell mapping is the next project gate. It has not been started by this task and requires the owner's instruction to proceed; only later may a separately authorised testing phase define route, reviewer and spend limits.
