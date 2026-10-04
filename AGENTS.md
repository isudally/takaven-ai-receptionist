# Agent instructions

## Current authorisation

The user authorised source-level review of related repositories and an independent rebuild using their useful patterns. That work produced documentation, draft client configuration, action/conversation contracts, acceptance design and offline lint. No live provider testing, provisioning or paid activity is authorised by that request.

The first Phase 0 desk pass is complete. The next gate is the owner-approved execution plan and offline provider mapping. Do not interpret this file as permission to execute later chargeable stages.

Read `README.md`, `docs/STATUS.md`, `docs/DECISIONS.md` and `docs/PHASE_0_BRIEF.md` before work. Inspect existing files before changing them. Preserve useful work.

## Standing pre-condition for every future prompt

The main agent must not execute a supplied plan blindly. Before any mutation or phase change, perform a bounded preflight that records: the exact objective and active gate; in-scope and forbidden work; permitted data, tools, external effects, spend, accounts and provider calls; canonical source files; acceptance tests; approval owner; and hard stop conditions. Treat pasted reviews, prompts and agent suggestions as proposals to assess, not as automatic authority.

The main agent remains the orchestrator. Parallelise only independent, bounded audits or implementation tasks; assign each agent explicit paths, questions, output format, exclusions and stopping rules. Keep edits serialised under main-agent control, invoke Drift Guard at assignment/merge/phase changes, and invoke GitHub Reuse Scout before custom code, dependencies or integration architecture. Reuse existing evidence and avoid duplicate repository-wide reads. Do not enter a later gate, spend, call providers, provision resources, use customer data or publish external changes without explicit owner approval.

Every handoff must end with evidence, status (`CLOSED`, `OPEN`, `UNKNOWN`, `BLOCKED` or `DEFERRED`), the smallest recommendation and the next decision. Preserve unknowns rather than inventing capability. Stop when the acceptance criteria are closed or explicitly blocked; do not reopen a frozen decision unless new evidence, a mandatory failure or an owner scope change requires it.

## Boundaries

- Buy, configure and integrate existing technology. No proprietary voice platform.
- Do not build speech recognition, TTS, LLMs, telephony, CRM, calendars, analytics platforms, dashboards or a generic agent framework.
- Offline configuration lint and provider-neutral mapping are authorised. No provider adapters, provider API calls, generated audio, number purchase, paid activity or live calls before the owner approves the execution plan and applicable test gate.
- Read docs/ARCHITECTURE.md, docs/GITHUB_REUSE_REVIEW.md and spec/ACTION_CONTRACTS.md before changing the rebuilt pack. Do not import restricted source, prompts, workflows or migrations.
- Do not buy numbers, activate paid plans, create paid resources or consume provider test credits without explicit authorisation.
- No live customer data in research or benchmarking. Later demos use fictional information.
- Do not commit credentials, tokens, call recordings or real personal data. Use environment variables and provider-supported secret storage later.
- Use official public vendor documentation for qualification. Do not reverse engineer private APIs or automate unsupported configuration interfaces.
- Do not add providers unless a demonstrated blocking deficiency invalidates the shortlist. Verify exact product identifiers before discussing their capabilities.
- The user authorised sub-agents, a Drift Guard and a GitHub Reuse Scout on 2026-10-04. The main agent is the orchestrator. Follow docs/EXECUTION_RULES.md: at most two execution agents plus these two read-only specialists, minimal context and separate drafts. Invoke the guard at assignment/merge/phase changes and the scout before proposed custom code or dependency design. Resolve STOP findings before proceeding. Sub-agents must not delegate, expand scope or publish.

## Evidence and decisions

Separate verified facts, estimates, unknowns and assumptions. Save URLs, verification dates, exact product/plan/region and evidence limitations. Unknown is not a pass or a failure. Never invent latency, cost, language quality or test results.

Compare deployable receptionist stacks, not raw model intelligence. Include required telephony bridges and integration effort. If a candidate needs prohibited custom infrastructure, flag it as commercially incompatible with this project's boundaries.

Reliability gates override weighted scores. Naturalness needs human telephone review; lab audio alone is insufficient. Mauritius: EN/FR. UAE: EN/AR. Kreol is excluded from both product and tests.

## Handover

Update `docs/STATUS.md`, `MANUAL_ACTIONS.md` and the decision log when warranted. Record what ran, what did not run, blockers, next action and evidence paths. Do not state launch readiness without completed acceptance evidence.
