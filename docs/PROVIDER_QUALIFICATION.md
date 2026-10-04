# Provider qualification register

Checked 2026-10-04. **Bounded first desk pass complete; every full stack UNRESOLVED.** PASS means a specific documented capability, not tested performance. No account/call/audio/API execution or spend. EN/FR/AR telephone quality, customer carrier paths and safe booking have not been demonstrated.

## Gate matrix

| Candidate / proposed existing stack | Product identity | MU telephone | UAE telephone | EN/FR/AR switching | Turn control | Complete actions | Route-specific handoff | Evidence / ownership / total cost | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| GPT-Live 1 `gpt-live-1` + Twilio Agent Connect | PASS [O1,O2] | UNKNOWN | UNKNOWN | UNKNOWN | Model documented; partner UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNRESOLVED |
| Gemini 3.8 Live `gemini-3.8-live` + Voximplant Gemini Live API Client | PASS model [G1]; pairing UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Model documented; partner UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNRESOLVED |
| Retell AI Voice Agents + supported elastic SIP + existing booking authority | PASS [R1,R2] | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN in bounded pass | UNKNOWN | Tool documented; exact route UNKNOWN [R3] | Partial evidence; ownership / total cost UNKNOWN | UNRESOLVED; first to resolve |
| ElevenLabs ElevenAgents + native Twilio or supported SIP + existing booking authority | PASS [E1] | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN pending exact setting evidence | UNKNOWN | UNKNOWN | Partial platform support; pricing / handover UNKNOWN | UNRESOLVED |
| Synthflow AI Voice Agents + approved SIP/native telephony + Cal.com | PASS [S1,S2] | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Booking documented; change/cancel UNKNOWN [S4] | Warm-transfer features documented; exact route UNKNOWN [S3] | CSV documented; full ownership / total cost UNKNOWN | UNRESOLVED; commercial concern |

## Findings and limitations

**OpenAI:** exact model verified; official partner page names Twilio Agent Connect for incoming/outgoing GPT-Live calls. Exact partner package, supported setup and all business/market gates remain unresolved. An existing Realtime connection is not proof of GPT-Live compatibility. Direct SIP requires application control/integration duties [O3]; it is not recommended for the first demo until burden and supported path are established. Small business-integration glue is not automatically a prohibited voice runtime.

**Google:** exact model verified in pricing; official Live overview names Voximplant for inbound/outbound calls. Its product page advertises native connectivity [G3], but exact 3.8 compatibility and complete supported deployment remain UNKNOWN. Function calling alone does not establish authorised calendar mutations or handover.

**Retell:** elastic SIP documents own-number inbound/outbound operation and transfers conditional on carrier capabilities. Dial-to-SIP documents integration code and loss of built-in transfer; record a route limitation, not rejection merely because code exists. Warm/agentic transfer configuration is documented; customer-specific transfer/failure/callback remains unverified. Transcripts/analytics are listed. Full booking lifecycle, fluent language quality, delegation, export/retention, local account acceptance and complete MU/UAE routes are UNKNOWN.

**ElevenLabs:** current documented product is ElevenAgents. Native Twilio and SIP connections are documented at overview level. Navigation/calendar listings are discovery leads, not proven complete integrations. Exact plan/pricing, language switching, transfer fallback, action authority and ownership remain UNKNOWN. Reception.ai relationship/capabilities are not established by this pass; homepage retrieval failed.

**Synthflow:** supported agent setup, enterprise telephony/integrations, real-time Cal.com booking, warm-transfer options and CSV call export are documented. No proof of reschedule/cancel correctness, local carrier viability, bilingual quality or full handover. Current pricing takes precedence over older conflicting blog claims. Without an approved spend ceiling, high cost is a concern rather than a formal FAIL.

For all stacks: recording/disclosure approach, processing locations, retention/deletion, DPA/terms and customer/carrier verification remain prerequisites. No legal suitability verdict is made. No provider is eliminated solely for an UNKNOWN or small supported integration.

## Published cost components — USD, excluding unknown charges

| Component | Verified unit | 500 / 1,500 minute illustration | Missing from total |
|---|---|---|---|
| GPT-Live 1 | $0.05/session minute, billed per second [O2] | $25 / $75 voice component | Backend/tools, partner, carrier, numbers, transfer legs, integrations, taxes |
| Gemini 3.8 Live audio | $3 input and $12 output per million tokens; published $0.005/input audio minute and $0.018/output audio minute [G1] | Not a connected-minute total: input/output duration ratio unverified | Text/thinking/other usage, partner/carrier and integrations |
| Retell | Advertised $0.07–$0.31/AI minute [R1] | $35–$155 / $105–$465 headline AI component only | Model/voice selection, carrier, add-ons and number fees; some listed models exceed headline range |
| ElevenAgents | UNKNOWN | UNKNOWN | Exact plan, allowances and rate inclusions |
| Synthflow | Enterprise contracts start $30,000 annually [S2] | Minute allowance/rate UNKNOWN | Quoted telephony/integration/support inclusions |

Retell's custom SIP has no Retell telephony charge; customer carrier fees remain. Number rental is listed at $2/month. Do not double count included model/TTS charges. These are desk arithmetic/components, not quotes, observed usage or TAKAVEN implementation prices.

## Official evidence

All checked 2026-10-04; sources may change. Not all linked subpages were inspected.

- O1 [GPT-Live partner integrations](https://developers.openai.com/api/docs/guides/live-partner-integrations)
- O2 [GPT-Live 1 model and billing](https://developers.openai.com/api/docs/models/gpt-live-1)
- O3 [OpenAI telephone/SIP guide](https://developers.openai.com/api/docs/guides/voice-sip)
- G1 [Google API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- G2 [Google Live overview](https://ai.google.dev/gemini-api/docs/live-api)
- G3 [Voximplant Gemini client](https://voximplant.com/products/gemini-client)
- R1 [Retell pricing](https://www.retellai.com/pricing)
- R2 [Retell custom telephone routes](https://docs.retellai.com/deploy/custom-telephony)
- R3 [Retell transfer configuration](https://docs.retellai.com/build/single-multi-prompt/transfer-call)
- E1 [ElevenAgents overview](https://elevenlabs.io/docs/eleven-agents/overview)
- S1 [Synthflow setup](https://docs.synthflow.ai/getting-started)
- S2 [Synthflow current pricing](https://synthflow.ai/pricing)
- S3 [Synthflow call transfers](https://docs.synthflow.ai/call-transfers)
- S4 [Synthflow real-time booking](https://docs.synthflow.ai/configure-real-time-booking-node)
- S5 [Synthflow call export](https://docs.synthflow.ai/export-call-data)

Failed retrievals: ElevenLabs attempted pricing URL and Reception.ai homepage. They remain UNKNOWN; retrieval failure does not mean unavailable. Naturalness, mutation safety and telephone reliability remain NOT_RUN.

See [desk recommendation](../reports/PHASE_0_RECOMMENDATION.md). No complete stack yet qualifies for paid comparison.
