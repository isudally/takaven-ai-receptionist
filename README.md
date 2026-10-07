# TAKAVEN AI Receptionist

Configure existing voice technology into reliable telephone receptionists for SMEs in Mauritius and the UAE. Sell a one-off implementation and handover; customers own accounts and pay their underlying platform/telephone charges.

**Current stage: Receptionist launch preparation.** The technical prototype is functional and has been exercised through Retell, n8n and Google Sheets using fictional data. Human voice evidence is completed, automated regression A–H passes, and final human release acceptance is deferred until the first external-demo candidate is frozen. Production readiness is not established.

## What is implemented

- [Source review](docs/GITHUB_REUSE_REVIEW.md): 42 inspected files across six repositories, with adopt/skip decisions and [pinned provenance](docs/SOURCE_INVENTORY.json).
- [Implementation architecture](docs/ARCHITECTURE.md): vendor-neutral receptionist standard, structured handoff/outcomes, proposed receipt path, deferred booking authority and human fallback.
- [Client configuration pack](config/README.md): separate fictional Mauritius EN/FR and UAE EN/AR draft profiles.
- [Action contracts](spec/ACTION_CONTRACTS.md) and [conversation policy](spec/CONVERSATION_POLICY.md): committed results, identity, corrections, retries and escalation.
- [Offline validator](scripts/validate_config.py): strict v1 configuration checks and deterministic hashes; no network or provider credentials.
- [Acceptance catalogue](qa/README.md): staged cases covering facts, qualification, lead/request receipts, handoff, outcomes and natural-conversation risks; booking-lifecycle cases remain DEFERRED.

No external repository code, prompts, workflow files or migrations were imported. Restricted repositories informed independently written requirements. Native vendor tooling will be used where it fits the qualified stack.

## Local verification

Python 3.11+; no packages to install:

```bash
python scripts/validate_config.py
python scripts/validate_config.py --self-test
```

Both example profiles validate as drafts. The self-test rejects 23 unsafe/invalid variants and checks stable hashes. **Validation does not establish deployment readiness or receptionist performance.**

## Next gate

Follow the owner-review [execution plan](docs/EXECUTION_PLAN.md) and [Execution rules](docs/EXECUTION_RULES.md): main Codex orchestrates two bounded executors, a Drift Guard and a GitHub Reuse Scout. Checkpoints prevent scope expansion and duplicated custom work.

The [launch-preparation plan](docs/EXECUTION_PLAN.md) records the remaining work before a controlled external demo. The active runtime is Retell → dedicated `capture_appointment_request` → n8n → Google Sheets → synchronous `RECEIVED`. It does not book, confirm availability, reschedule, cancel, or perform customer lookup. Do not build adapters, a voice engine, a booking database, CRM or dashboard.

Launch preparation is consolidated in [docs/LAUNCH_PREPARATION.md](docs/LAUNCH_PREPARATION.md). It is intentionally single-client and customer-owned: configuration, native credential stores, callback destination, telephony route, operational evidence and rollback are prepared per deployment.

## Documentation

| Document | Purpose |
|---|---|
| [Project brief](docs/PROJECT_BRIEF.md) | Commercial offer and scope |
| [Decisions](docs/DECISIONS.md) | Accepted choices and superseded assumptions |
| [Architecture](docs/ARCHITECTURE.md) | How the selected parts fit together |
| [Source review](docs/GITHUB_REUSE_REVIEW.md) | Code findings, licences and adoption decisions |
| [Master requirements](spec/MASTER_REQUIREMENTS.md) | Product requirements |
| [Acceptance](docs/ACCEPTANCE.md) | Mandatory launch gates |
| [Benchmark plan](docs/BENCHMARK_PLAN.md) | Lean staged test design |
| [Deployment playbook](docs/DEPLOYMENT_PLAYBOOK.md) | Plan, apply, read-back, acceptance and handover |
| [Roadmap](docs/ROADMAP.md) | Execution milestones |
| [Validation report](reports/OFFLINE_VALIDATION.md) | Checks actually run and limitations |
| [Status](docs/STATUS.md) / [Manual actions](MANUAL_ACTIONS.md) | Handover and dependencies |
| [AGENTS.md](AGENTS.md) | Agent operating boundaries |
| [Original blueprint](docs/reference/ORIGINAL_BLUEPRINT.txt) | Historical reference |

## Repository

This repository may remain public for development and independent audit while it contains only fictional data, placeholders and sanitised workflow templates. Make it private before introducing customer information, production secrets, recordings or private configuration. Earlier Gate 0A/Gate B design documents remain historical evidence where marked superseded; they are not the active runtime description.

Latest explicit user instructions and [decision log](docs/DECISIONS.md) govern work. Use the qualification register to distinguish verified public facts from unresolved access, integration and performance. A repository demonstration is not launch evidence.
