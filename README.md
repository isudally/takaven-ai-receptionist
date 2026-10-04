# TAKAVEN AI Receptionist

Configure existing voice technology into reliable telephone receptionists for SMEs in Mauritius and the UAE. Sell a one-off implementation and handover; customers own accounts and pay their underlying platform/telephone charges.

**Current stage: source review complete; independent configuration pack rebuilt and validated offline.** No provider is selected, no live agent is deployed, and no provider tests, audio generation or paid calls have run.

## What is implemented

- [Source review](docs/GITHUB_REUSE_REVIEW.md): 42 inspected files across six repositories, with adopt/skip decisions and [pinned provenance](docs/SOURCE_INVENTORY.json).
- [Implementation architecture](docs/ARCHITECTURE.md): existing voice runtime and customer booking authority, supported integrations and human fallback.
- [Client configuration pack](config/README.md): separate fictional Mauritius EN/FR and UAE EN/AR draft profiles.
- [Action contracts](spec/ACTION_CONTRACTS.md) and [conversation policy](spec/CONVERSATION_POLICY.md): committed results, identity, corrections, retries and escalation.
- [Offline validator](scripts/validate_config.py): strict v1 configuration checks and deterministic hashes; no network or provider credentials.
- [Acceptance catalogue](qa/README.md): 15 cases covering the source review's failure modes; every provider case is NOT_RUN.

No external repository code, prompts, workflow files or migrations were imported. Restricted repositories informed independently written requirements. Native vendor tooling will be used where it fits the qualified stack.

## Local verification

Python 3.11+; no packages to install:

```bash
python scripts/validate_config.py
python scripts/validate_config.py --self-test
```

Both example profiles validate as drafts. The self-test rejects 20 unsafe/invalid variants and checks stable hashes. **Validation does not establish deployment readiness or receptionist performance.**

## Next gate

Follow [Phase 0 brief](docs/PHASE_0_BRIEF.md) and record official-source evidence in [Provider qualification](docs/PROVIDER_QUALIFICATION.md). Verify the five candidate families, exact products, supported MU/UAE telephone paths and existing booking/CRM integrations. Then map the pack only to survivors and conduct the separately authorised lean benchmark. Do not build five adapters, a voice engine, a booking database or a dashboard.

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

Private repository: [isudally/takaven-ai-receptionist](https://github.com/isudally/takaven-ai-receptionist). Use its published history for ongoing work. Earlier delivered bundle/archive represents the original documentation baseline and is superseded by this rebuild; do not force-push it over GitHub.

Latest explicit user instructions and [decision log](docs/DECISIONS.md) govern work. Candidate names, access, prices and performance remain unverified until qualification. A repository demonstration is not provider capability or launch evidence.
