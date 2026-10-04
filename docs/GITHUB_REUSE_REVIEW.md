# Quick GitHub reuse review

Reviewed: 2026-10-04. Scope: official repository pages, READMEs, visible structure and selected licence files. No cloning, installation, test execution, provider calls or end-to-end validation. Authors' production/test claims are not independently verified. No code has been imported.

## Recommendation

Keep TAKAVEN's documentation repository independent of a provider. The first community codebase worth inspecting for selective reuse is **dma-deploy-kit**, conditional on Retell surviving Phase 0. It uses per-client YAML configuration, deploy/diff tooling, post-call alerts and evaluation records. Its MIT licence permits reuse subject to retaining required notices.

Its existing scope is English/Spanish with separate language agents; SMS handling targets US phone numbers. The documented flow sends booking links, which does not establish our required live calendar actions. Dependency pinning and placeholder voice/routing packages also need inspection. It is a starting point, not a verified ready-to-sell EN/FR/AR receptionist.

Sources: [Repository](https://github.com/danielfmonzon/dma-deploy-kit), [MIT licence](https://github.com/danielfmonzon/dma-deploy-kit/blob/main/LICENSE).

## Shortlist

| Repository | Useful material | Licence evidence | Disposition |
|---|---|---|---|
| [danielfmonzon/dma-deploy-kit](https://github.com/danielfmonzon/dma-deploy-kit) | Repeatable client configuration, Retell deployment and post-call/evaluation tooling | MIT licence file checked | Closest factory fit; inspect selectively if Retell qualifies |
| [elevenlabs/cli](https://github.com/elevenlabs/cli) | Official agent templates, local config sync, tool/test registries and test commands | Repository identifies MIT; licence file not separately inspected | Use official tooling if ElevenLabs qualifies; a full fork is unnecessary |
| [elevenlabs/examples](https://github.com/elevenlabs/examples) | Official voice-agent and guardrail examples | MIT licence file checked | Reuse the smallest relevant example; browser demonstration alone is not telephone readiness |
| [twilio-samples/speech-assistant-openai-realtime-api-node](https://github.com/twilio-samples/speech-assistant-openai-realtime-api-node) | Official inbound OpenAI/Twilio bridge example with interruption handling | MIT licence file checked | Useful only if OpenAI's complete supported stack qualifies; still needs hosted integration and business actions |
| [kaa911-syp/ai-voice-receptionist](https://github.com/kaa911-syp/ai-voice-receptionist) | Retell/n8n/Google Calendar contracts and workflows | No licence found in inspected root/README; not conclusively cleared | Reference only until reuse permission is established; extra services may increase maintenance |
| [PilouZer/resto-voice-demo](https://github.com/PilouZer/resto-voice-demo) | French Retell restaurant demonstration | README expressly reserves rights and prohibits copying/deployment/commercial derivatives | Exclude from fork/copy candidates |

The [OpenAI/Twilio quickstart](https://github.com/openai/openai-realtime-twilio-demo/blob/main/README.md) is another official reference, but includes a web app and websocket server; the smaller Twilio sample is a leaner reference for this stage. Its licence was not checked here.

## Before importing code

For the selected component, pin an upstream commit, inspect actual source and current API compatibility, check dependency/service licences, preserve upstream notices and document modifications. Verify webhook authentication, secret handling, customer isolation, action validation, timezone handling, idempotency, rollback and supported carrier paths. Run appropriate tests only in an authorised implementation phase.

Do not equate GitHub visibility with reuse permission. The root licence does not automatically clear third-party assets, voice rights or hosted-service terms. Record attribution in `THIRD_PARTY_NOTICES.md` if code is actually imported; no attribution file is required yet because no code was copied.

## Next action

Complete Phase 0, then decide whether a qualifying provider's built-in tooling removes the need for custom code. If Retell qualifies and selective reuse saves work, inspect dma-deploy-kit before writing equivalent configuration tooling. No recommendation to adopt an entire community platform or replace the five-engine evaluation has been made.
