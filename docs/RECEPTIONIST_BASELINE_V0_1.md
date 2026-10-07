# TAKAVEN Receptionist v0.1 baseline

Status: **technical baseline functional; human voice acceptance deferred; production readiness not established**.

This package is a sanitized, TAKAVEN-owned representation of the current fictional baseline:

```text
capture_appointment_request
  -> n8n webhook
  -> Google Sheets append
  -> synchronous RECEIVED response
```

It is concrete Receptionist implementation packaging, not a generic shared-agent framework. Sales and Admin/Support are out of scope.

## Package map

- [`retell/agent-config.example.json`](../retell/agent-config.example.json): sanitized agent, knowledge, tool, response and placeholder configuration.
- [`retell/tools/capture_appointment_request.schema.json`](../retell/tools/capture_appointment_request.schema.json): authoritative tool contract.
- [`n8n/capture_appointment_request.sanitized.workflow.json`](../n8n/capture_appointment_request.sanitized.workflow.json): sanitized four-node workflow blueprint matching the current path.
- [`n8n/sheet-schema.example.csv`](../n8n/sheet-schema.example.csv): fictional Sheet header and example row.
- [`n8n/environment.example.env`](../n8n/environment.example.env): placeholders only; never populate this file with secrets.
- [`config/mauritius.example.json`](../config/mauritius.example.json) and [`config/uae.example.json`](../config/uae.example.json): fictional market knowledge/configuration.

## Tool contract

Required caller-confirmed fields:

`caller_name`, `caller_contact`, `vehicle`, `service`, `preferred_date`, `preferred_time_window`.

Optional fields in the current Retell representation are `urgency` and `opportunity_classification`; the v0.1 Sheet path does not use them as booking or scoring authority.

`RECEIVED` means the appointment request was sent to the team for confirmation. It does not mean booked, confirmed, reserved, available or staff-acknowledged. `FAILED` requires truthful fallback wording. No booking, calendar, CRM, Data Store, notification or post-call module belongs in this v0.1 path.

## Reproduction outline

1. Import the sanitized n8n blueprint into an owner-controlled n8n workspace.
2. Set the webhook path and attach an owner-controlled Google Sheets credential outside Git.
3. Create a fictional Sheet using the committed header schema.
4. Configure the Retell function using the committed tool schema, owner-controlled n8n endpoint placeholder, native header credential and `max_retries = 0`.
5. Keep the standard Retell envelope available so `call.call_id` can be mapped to `Call Reference`; do not use caller ID as identity authority.
6. Send one fictional direct action test and confirm one Sheet row plus the synchronous response.
7. Record results in the existing QA evidence format. Human Voice Acceptance remains a separate future gate.

The actual n8n export was inspected in the owner workspace but is not committed raw because it contains environment-specific URLs, credential references and account configuration. The committed JSON is a sanitized TAKAVEN-owned blueprint of the observed four-node shape, with placeholders replacing those values. The launch-preparation callback template is separate and does not change this known-good appointment path.

## Safety and scope

- Fictional data only; no customer data.
- No API keys, tokens, credential IDs, private webhook URLs or provider account identifiers are committed.
- Real credentials belong only in Retell/n8n credential stores.
- The working external runtime was not changed by packaging this baseline.
- Human voice acceptance is **DEFERRED**.
- Production readiness is **NOT ESTABLISHED**.

## Provenance

The package is independently authored TAKAVEN material. It adapts permitted architectural lessons from the MIT-licensed `dom-ran/voice-receptionist-ai` and `Sarthak0521/quensultingai-dental-voice-agent` repositories. The official `RetellAI/n8n-nodes-retellai` repository was reviewed as a possible integration dependency but is not required by this baseline. No source or configuration was copied from the unlicensed/uncertain Muhammad reference.

## Validation

From the repository root:

```text
python scripts/validate_config.py
python scripts/validate_config.py --self-test
python scripts/validate_receptionist_baseline.py
python -m py_compile scripts/validate_config.py scripts/validate_receptionist_baseline.py
git diff --check
```
