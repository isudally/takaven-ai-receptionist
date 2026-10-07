# Receptionist operations and evidence

Use existing Retell and n8n execution history. No dashboard or custom observability service is required.

## Minimum event record

For each action, retain only what the approved customer policy permits:

- provider call reference (`call.call_id` where available);
- action name and configuration version/hash;
- request or callback reference;
- received timestamp and timezone;
- n8n execution success/failure and diagnostic code;
- Sheet/destination receipt evidence;
- safe caller-facing status (`RECEIVED` or `FAILED`).

Do not log API keys, header values, full secrets or unnecessary caller data. Recordings are off by default in the templates. The fictional demo release uses zero-day retention; a customer deployment must set retention and deletion ownership explicitly.

## Failure handling

- If the Sheet append succeeds, return `RECEIVED`.
- If the action fails or its outcome is unknown, return truthful fallback wording and create/route a callback request where configured.
- Never say booked, confirmed, reserved, available or staff-acknowledged without authoritative evidence.
- A staff notification or acknowledgement is separate from action success.

## Support checks

When a client reports a missed request, correlate the call reference with Retell logs, n8n execution history and the destination Sheet. Do not replay an unknown side effect blindly; inspect the records first.
