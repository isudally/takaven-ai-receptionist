# Decision log

Baseline recorded: 2026-10-04. Owner: Ismaël. Executor selected in prior discussion: Codex. No benchmark execution is authorised by the creation of this repository.

| ID | Accepted decision | Consequence |
|---|---|---|
| D01 | Configure existing technology; do not build a voice platform | Evaluate complete deployable stacks and their integration burden |
| D02 | Five candidate labels from prior discussion | Verify exact names, access and capabilities before integrations |
| D03 | Phase 0 desk qualification comes first | No adapters, audio generation, test calls or provider API activity yet |
| D04 | EN/FR for Mauritius; EN/AR for UAE | No Kreol implementation or stress testing |
| D05 | Codex is the planned execution agent | Incorporate useful methodology safeguards; no new agent comparison needed |
| D06 | Lean staged benchmark | Screen broadly, test deeply only for finalists |
| D07 | Reliability gates override scores | A pleasant voice cannot compensate for incorrect business actions |
| D08 | One automotive demo initially | Do not build three vertical demos before proving one |
| D09 | Customer-owned accounts preferred | Separate implementation fee from ongoing vendor/telephone costs |
| D10 | Subjective quality judged by fluent humans over telephone | Do not select a winner from synthetic API tests alone |
| D11 | Fixed tuning budgets and comparable test conditions | Track configuration versions and avoid unequal tuning |
| D12 | Record unknowns honestly | No fabricated model names, pricing, support claims or results |
| D13 | Review existing GitHub work before writing equivalent code | Source-level review completed across six repositories; 42 files inventoried; no code copied |
| D14 | Use browser fallback for GitHub setup when connector lacks creation | User authorised opening GitHub and providing access; continue setup after sign-in |
| D15 | 2026-10-04: rebuild independently using useful patterns from each reference | Authorised offline client configuration, action contracts, QA design and lint; no live providers or paid tests |
| D16 | Truthful outcomes require authoritative committed receipts | Reject stub confirmation, fake escalation and unverified success after timeout |
| D17 | Keep the implementation a customer configuration/integration pack | Native voice runtime and existing booking/CRM authority; no custom platform or booking database |
| D18 | Preserve operation history; atomically protect both create and reschedule | Safe replay after cancellation, outcome reconciliation and bounded terminal retry states |
| D19 | 2026-10-04: main Codex agent orchestrates bounded sub-agents | Fixed scope, one active gate, minimal handoffs, separate drafts, one review and explicit stopping rules in EXECUTION_RULES.md |
| D20 | 2026-10-04: dedicated read-only Drift Guard | Checks assignment, merge and phase transitions; CLEAR/FLAG/STOP verdict; main agent resolves STOP before proceeding |
| D21 | 2026-10-04: bounded desk pass completed; no final engine selected | All complete stacks unresolved; resolve Retell first, ElevenAgents next; no automatic exclusion for small supported business-integration glue |
| D22 | 2026-10-04: dedicated GitHub Reuse Scout | Checks close existing implementations before custom code; flags overlap, provenance, licence and gaps without changing scope or copying restricted code |
| D23 (proposed) | 2026-10-04: first demo captures appointment requests only | Owner approval pending; no committed booking, rescheduling, cancellation or customer lookup until a customer-owned booking authority is selected and tested |
| D24 (proposed) | 2026-10-04: Retell is the provisional first mapping target | Owner approval pending; complete an offline native mapping and evidence plan first; no provider spend, account activation or live calls without separate approval |
| D25 (proposed) | 2026-10-04: market route is staged | Owner approval pending; Mauritius may use a real customer/owner telephone route after carrier checks; UAE starts as a labelled browser/test call until a customer-owned carrier path is verified |

## Superseded material

The attached original blueprint is preserved in `reference/ORIGINAL_BLUEPRINT.txt`. Its two-provider contest, mandatory 80-scenario starting suite, three initial demos and feature claims are historical. Later discussion replaces these with five-candidate desk qualification, a lean staged benchmark and one automotive demo. The earlier large execution prompt requiring five adapters and roughly 60 tests per provider is also superseded.

Names such as `GPT-Live-1`, `Gemini 3.8 Live`, `ElevenAgents` and `Reception.ai` were supplied in prior discussion. The 2026-10-04 desk pass verified `gpt-live-1`, `gemini-3.8-live` and ElevenAgents in official documentation. Full stack/market suitability remains unresolved. Reception.ai and ElevenAgents must not be assumed interchangeable.

## Open decisions

- Exact available product/model/plan for each candidate; no silent substitutions.
- Complete supported telephone route for each target market and customer-number setup.
- Accounts, trial access, reviewer availability, spend cap and execution start date.
- Appointment-request capture is the first action scope; a booking authority is deferred.
- Retell is the provisional first mapping target; the initial live-test spend ceiling remains owner approval.
- Mauritius and UAE demo route, human handoff destination and callback fallback.
- Final benchmark count, tied to qualified survivors and available access.
- Launch prices, support boundaries and optional care scope.
- Data handling, recording/AI disclosure and contractual requirements for the specific deployment.

The owner must approve the execution plan in `docs/EXECUTION_PLAN.md` before any provider account, telephone route, paid test or live call is activated.

Record future changes here with date, reason, evidence and user decision where required. The historical attachment never overrides this log or newer user instructions.
