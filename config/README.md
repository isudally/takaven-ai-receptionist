# Client configuration pack v1

`mauritius.example.json` and `uae.example.json` are fictional draft automotive profiles for specification and offline lint. They are not provider payloads, approved client facts or runnable agents. Rates/hours are invented demo facts and not a commercial price recommendation. Contacts, provider IDs and authority remain null.

Copy a profile, replace facts with approved customer information, keep credentials in the vendor's supported secret store and map only after provider qualification. Preserve one config per customer/market. Mauritius uses EN/FR, MUR and Indian/Mauritius; UAE uses EN/AR, AED and Asia/Dubai. Do not mix calendars or currencies.

Run from the repository root with Python 3.11+:

```bash
python scripts/validate_config.py
python scripts/validate_config.py --self-test
python scripts/validate_config.py config/mauritius.example.json
```

The dedicated validator enforces its documented fixed v1 structure, rejects unknown/missing keys, checks market and timezone consistency, services, localized FAQs, intent qualification, escalation, handoff settings and safety policies. It outputs a deterministic config hash and lists unresolved deployment prerequisites. It makes no network requests, reads no credentials and never changes vendor state. This is not a general JSON Schema engine or a provider capability test.

## Fields

| Section | Purpose |
|---|---|
| schema_version, stage, client | Fixed v1 draft, fictional name/ID, market, currency, timezone |
| conversation | Required language pair, default, explicit AI disclosure and voice references |
| facts | Approved-content state, address, localized FAQs, services with stable IDs/durations/prices, hours and closures |
| routing | Intent IDs with required qualification fields and explicit escalation triggers/actions |
| integration | Selected provider/agent and existing booking authority; null until qualified |
| safety | Mandatory confirmation, identity, replay, committed-result and fail-closed policies |
| operations | Reception mode, trusted customer binding, handoff destination/hours/fallback and rollback reference |
| privacy | Recording off; optional messaging consent; client-approved retention prerequisite |

Local validation deliberately permits documented null prerequisites in draft templates. Provider, agent, approvals, handoff destination, rollback, voices, identity policy and retention are still needed for the first demo deployment. Booking authority is a deferred prerequisite for a later scheduling lifecycle. The first demo uses a staff/queue appointment-request receipt rather than a booking authority. No `production` stage is supported by this pack. Future stages require a separately reviewed provider mapping and acceptance evidence.
