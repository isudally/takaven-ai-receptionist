# Execution rules — scope, delegation and efficiency

Owner/orchestrator: main Codex agent. Authorised by Ismael on 2026-10-04: delegate execution while preventing drift, overengineering and unnecessary token use. These rules apply to this project and do not create a background service.

## Mandatory preflight for every future prompt

Before changing files, external state or project phase, the main agent creates a compact shared index containing branch/worktree state, applicable instructions, canonical documents, current gate, known contradictions, acceptance criteria, permitted effects and approvals. The supplied prompt or review is then checked against that index; it is never treated as self-authorising.

The main agent must state the objective, active gate, in-scope work, explicit exclusions, allowed tools/data/external effects, approval owner and stop conditions. Independent audits may run in parallel; edits and decisions are integrated once by the main agent. Agents report evidence, path, status and smallest correction only. They do not publish, spend, provision, contact people, choose a provider, reopen frozen decisions or delegate further.

No later gate, provider/API/telephone call, account mutation, spend, provisioning, customer data, production change, new integration/backend/dependency or destructive action starts without explicit owner approval. If evidence is insufficient, a required guarantee is unproven, or a genuine contradiction blocks freezing, report `BLOCKED` and stop the affected work. Preserve `UNKNOWN` and `client review required` explicitly.

The efficient execution shape is: **preflight → shared index → parallel bounded audits → one integration edit → one authoritative validation → final verdict and next action**. Reuse existing evidence, assign each path family one owner, avoid repeated full reviews and stop once the acceptance criteria are met or explicitly blocked.

## Fixed outcome

Deliver one reliable automotive receptionist demo using existing voice technology, then a repeatable customer configuration, integration, acceptance and handover service. Mauritius EN/FR; UAE EN/AR; no Kreol. Customer-owned accounts preferred. One-off implementation fee is separate from recurring vendor usage.

Existing [decisions](DECISIONS.md), [architecture](ARCHITECTURE.md) and [acceptance gates](ACCEPTANCE.md) define scope. No custom speech/model/telephony runtime, booking database, CRM, dashboard, generic agent framework, extra vertical or outbound campaign. New scope requires a demonstrated blocker, a smallest-change proposal and the owner's decision where material.

## One active gate

| Gate | Deliverable | Exit condition |
|---|---|---|
| 0: desk qualification | Evidence register and short recommendation | Supported stacks, mandatory unknowns and smallest prerequisites recorded; no final winner |
| 0A: alignment repair | Owner-approved scope, config, QA and execution plan | Validator passes; staged cases and provisional mapping scope are explicit |
| 2A: offline provider mapping | Provisional vendor's native field/action mapping and gap register | Every required field has a supported mapping or labelled UNKNOWN; no provider push or live call |
| 1: authorised comparison | Lean screen, telephone smoke and up to two finalist reviews | Reliability and language evidence; pilot recommendation or honest no-decision |
| 2: master demo | Selected vendor's native config plus necessary supported integrations | One automotive flow meets acceptance |
| 3: customer deployment | Intake, approved config, QA, handover and rollback | Client approval and tested human fallback |

Only one gate is active. Future-phase tasks stay queued. Gates 1–3 require their applicable access, spend and deployment authorisation. Research and reversible offline work proceed without repetitive permission requests.

## Delegation

Use two narrowly scoped execution agents when work is independent. A read-only Drift Guard checks scope at assignment, before merge and before moving gates; it also provides the single independent evidence review. A read-only GitHub Reuse Scout checks existing implementations before proposed custom work. Invoke specialists only at relevant checkpoints; they do not duplicate execution. Use a single executor for a small task. Main agent integrates and publishes.

Every task handoff specifies objective, permitted sources/actions, owned output file, excluded work, output limit, completion test and stopping rule. Give only necessary context; do not fork the full conversation. Agents do not delegate again, change scope, choose the winner, publish, provision resources or contact people.

Each agent writes a separate draft. No shared-file edits. Main agent checks claims, resolves conflicts and updates the canonical files. An agent's assertion is evidence to assess, not a decision to accept automatically.

## Token and work controls

- Reuse existing verified files and evidence. Search only unresolved facts; do not repeat a completed source review.
- First-pass research allowance: approximately 2–3 focused queries and 3–4 targeted source opens per provider. Extra lookup requires a specific mandatory gap or contradictory claim.
- Return findings in a compact table/bullets; draft at most 750–900 words and handover at most 250 words. Never return full webpages, source trees or copied code.
- Use primary vendor/carrier sources. A missing fact stays UNKNOWN after the bounded pass.
- Run one independent review against mandatory gates. Fix material errors once; reopen only for new evidence, a failed required check or an unresolved blocker.
- Test only changed behavior and required acceptance. No repeated full test runs after a passing check without a relevant reason.
- Prefer native vendor configuration/testing and existing integration services. New code must solve a demonstrated gap, be the smallest useful change and have a clear acceptance case.
- Keep documentation in existing canonical files; add a new document only for a distinct necessary output.

These are practical work/output limits, not a guaranteed token billing cap. Actual per-agent token telemetry is not available here; do not claim measured savings or enforceable token totals.

## Drift Guard

The user explicitly requested this role on 2026-10-04. It is independent of execution and has no editing or deployment authority. Its verdict is CLEAR, FLAG or STOP, with the exact deviation, evidence and smallest correction. Actual boundary breaches trigger STOP; a hypothetical concern alone does not.

Check for scope expansion, unnecessary new code/tools/features, duplicated research/review, unsupported claims, hidden paid actions and premature progression. A STOP suspends the affected work until the main agent addresses it. The main agent records the resolution; it cannot treat a flagged assumption as verified evidence.

Invoke at assignment, before merging output and before changing phase. Reuse this same agent for follow-ups while available; after a session restart, recreate it from these rules and current status only. This is checkpoint review, not continuous background surveillance.

## GitHub Reuse Scout

The user explicitly requested this role on 2026-10-04. Before custom code, a new dependency or an integration design, provide the scout a short description of the gap. It checks identical/close GitHub implementations and returns overlap, source URL/version, licence status, useful architectural patterns, gaps and the smallest recommendation: reuse, inspire or build.

First checkpoint allowance: two focused queries, at most three strong matches opened, at most 250 words returned. Search official/native assets first; reuse the completed source review and record new findings in the existing reuse review. Deeper source analysis is justified only when a close candidate could replace proposed work. Unknown licence means no copying; restricted source may inform independently written requirements.

The scout cannot select a provider, widen the product, add dependencies, fork/copy code or publish. Main agent decides; Drift Guard checks scope. Recreate from current gap/rules after a restart. This is task-triggered review, not continuous background polling or an automated GitHub watch.

## Main-agent acceptance checklist

Before merging a deliverable, confirm:
1. It advances the current gate and agreed commercial outcome.
2. Every material claim has a source or is labelled unknown/assumption.
3. It avoids prohibited infrastructure and unrequested features; any proposed custom code has had a reuse check.
4. Its changed files are within the assignment and contain no secrets/customer data.
5. Required checks passed; unexecuted tests remain NOT_RUN.
6. The next action is specific and the phase's stopping rule is respected.

After each gate, update STATUS, qualification/evidence and decisions only where needed. Report completed output, material unknowns and next action concisely. Do not keep polishing after the gate is met.

## Current allocation

Gate 0A is complete. Main agent owns the frozen alignment baseline; offline Retell mapping (Gate 2A) is queued until the owner instructs it to begin. Drift Guard reviews the changed scope and phase transition. GitHub Reuse Scout is invoked only if a new integration or custom dependency is proposed. No provider sessions, audio, number purchase, paid activity or customer launch are authorised by this allocation.

Stop after the offline mapping and owner approval. Do not begin live testing until the owner approves the route, reviewers, test scope and spending ceiling.
