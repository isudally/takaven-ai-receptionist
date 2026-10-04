# TAKAVEN AI Receptionist

Configure existing voice platforms into reliable, natural telephone receptionists for SMEs in Mauritius and the UAE. Sell a one-off implementation service; customers pay their own underlying platform and telephone charges.

**Current stage: documentation complete; Phase 0 desk qualification NOT STARTED.** No provider is selected. No benchmark, provider account, phone number or customer deployment has been created.

## Start here

1. Read [Project brief](docs/PROJECT_BRIEF.md) and [Decisions](docs/DECISIONS.md).
2. Follow [Phase 0 execution brief](docs/PHASE_0_BRIEF.md).
3. Record official-source evidence in [Provider qualification](docs/PROVIDER_QUALIFICATION.md).
4. Produce a desk recommendation and prerequisites. Stop before implementation or chargeable testing.

No API credentials are needed for Phase 0. Do not generate audio, write adapters or run calls at this stage.

## Documentation map

| File | Purpose |
|---|---|
| [AGENTS.md](AGENTS.md) | Operating instructions for Codex or another agent |
| [Project brief](docs/PROJECT_BRIEF.md) | Business objective, scope, offer and product boundaries |
| [Decisions](docs/DECISIONS.md) | Agreed decisions, superseded assumptions and unresolved points |
| [GitHub reuse review](docs/GITHUB_REUSE_REVIEW.md) | Existing code/templates, licence checks and recommended reuse path |
| [Phase 0 brief](docs/PHASE_0_BRIEF.md) | The next executable research task |
| [Provider qualification](docs/PROVIDER_QUALIFICATION.md) | Evidence template and five-candidate gate matrix |
| [Benchmark plan](docs/BENCHMARK_PLAN.md) | Lean, staged test design for a later authorised phase |
| [Acceptance](docs/ACCEPTANCE.md) | Reliability gates and customer launch requirements |
| [Master requirements](spec/MASTER_REQUIREMENTS.md) | Provider-neutral receptionist requirements |
| [Deployment playbook](docs/DEPLOYMENT_PLAYBOOK.md) | Repeatable customer configuration and handover |
| [Roadmap](docs/ROADMAP.md) | 30-day target, milestones and stop rules |
| [Status](docs/STATUS.md) | Current state, next work and handover checklist |
| [Manual actions](MANUAL_ACTIONS.md) | Human tasks, dependencies and outstanding actions |
| [Original blueprint](docs/reference/ORIGINAL_BLUEPRINT.txt) | Historical attachment; not the execution specification |

## Repository setup

GitHub repository: [isudally/takaven-ai-receptionist](https://github.com/isudally/takaven-ai-receptionist). Visibility: **private**. Documentation was published through the signed-in GitHub browser; the GitHub connection used in this session does not yet have access to the new repository.

The delivery archive contains the source folder and a Git bundle preserving its initial commit. To restore the repository locally:

```bash
git clone takaven-ai-receptionist.bundle takaven-ai-receptionist-work
cd takaven-ai-receptionist-work
git status
```

For ongoing work, clone the GitHub repository to retain its published commit history. The delivery archive and bundle preserve the original local documentation baseline; the browser upload creates separate GitHub commits. Do not push the bundle over the published branch or force-push. Make the repository accessible to the execution agent's GitHub connection when needed. Do not add credentials to Git.

## Source of truth

Latest explicit user instructions take precedence. The decision log captures the accepted changes to the attached historical blueprint. Vendor names, model identifiers, availability, prices and capabilities remain **unverified**, pending Phase 0. A name in the shortlist is not evidence that the named product exists or is accessible.

This repository initially contains documentation only. Add benchmark code only after the next phase is authorised; add production configuration only after selecting a deployable stack.
