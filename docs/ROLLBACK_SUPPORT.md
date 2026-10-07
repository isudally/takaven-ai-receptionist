# Rollback and support

The customer retains control of the provider and existing phone route.

## Immediate rollback

1. Disable the Retell agent or remove its inbound route.
2. Route calls back to the existing human/business phone handling where practical.
3. Leave the customer’s number and provider account intact.
4. Preserve the failed call reference and n8n execution evidence.
5. Tell callers that the team will follow up only when a callback record exists; do not claim live transfer.

## Action failure

If appointment capture fails, use the callback path when configured. If callback capture also fails, provide the approved fallback contact wording and record the failure for manual follow-up through the customer’s existing process.

## Support ownership

The deployment record must name one customer operational owner and one TAKAVEN support contact. Changes are made from an approved configuration version; do not patch live prompts or credentials without recording the change and rollback point.

## Recovery evidence

Before an external demo, verify that the agent can be disabled, the fallback route is reachable, and the owner can identify the last known configuration and action references.
