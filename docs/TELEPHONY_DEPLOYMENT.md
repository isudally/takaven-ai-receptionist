# Telephony deployment — Mauritius and UAE

This runbook documents the selected Retell-based route without reopening provider selection. Numbers and paid carrier services remain customer-owned and require owner approval before purchase.

## Common ownership model

- The customer owns the Retell workspace, phone/SIP/carrier account and billing relationship.
- TAKAVEN configures the agent, approved knowledge, action endpoints, routing and acceptance checks.
- The customer approves caller-ID, recording, retention, forwarding and fallback behaviour.
- The demo can use a browser/web-call route until a customer-owned phone route is ready.

## Mauritius

Minimum launch arrangement: a customer-owned telephony number or SIP/carrier route supported by the selected Retell account and available for the intended Mauritius caller path. Confirm country availability, caller-ID presentation, inbound routing, recording rules and warm-transfer support with Retell/carrier documentation before purchase.

TAKAVEN configures the Retell phone/route, webhook/action references, business hours, callback destination and rollback route. The existing business line should remain the fallback where practical.

Known limitation: this repository does not claim that a Mauritius number, SIP trunk or warm transfer is currently provisioned or proven. Do not present browser-call evidence as Mauritius carrier readiness.

## UAE

Minimum launch arrangement: a customer-owned UAE-compatible number or SIP/carrier route supported by the selected Retell account and local requirements. Confirm number availability, caller-ID, recording/consent, inbound routing and transfer support before purchase.

TAKAVEN configures the same agent/action path and documents the customer-owned route. Until that route is accepted, use a labelled browser/web-call demo only.

Known limitation: this repository does not claim that a UAE number, SIP trunk or warm transfer is currently provisioned or proven.

## Cost treatment

Retell, carrier, number, SIP and usage charges vary by account, market and date. The customer must check the current provider quote before committing. No numeric recurring price is treated as a repository fact here; prototype cash spend remains `$0` and no purchase is authorised by this package.

## Cutover checklist

1. Customer account and billing owner confirmed.
2. Number/SIP route and caller-ID accepted by the customer.
3. Privacy, recording and retention choices approved.
4. Authenticated appointment and callback actions pass.
5. Existing human route and rollback owner confirmed.
6. One release human acceptance call completed before external demonstration.
