# TAKAVEN Receptionist commercial demo package

## Demo position

This package presents the frozen TAKAVEN Receptionist technical release candidate through a browser/web call. The fictional business is **Moka Motor Service Centre**. The demo uses fictional information only and does not claim that production telephony, booking, live availability or customer deployment is ready.

## Presenter introduction

> I’ll show a short fictional example of TAKAVEN Receptionist handling a normal automotive enquiry in English or French. It can answer approved questions, capture a request for the team and arrange a callback request when it cannot complete something. It does not claim to book an appointment or transfer a caller unless those capabilities are separately deployed.

## Demo script: 3–5 minutes

Use the flow naturally; the presenter should not read every line as a test script.

### 1. Greeting and FAQ

Caller, in French: “Bonjour, j’aimerais savoir quand vous êtes ouverts et où vous vous trouvez.”

The agent should answer from the approved Moka Motor Service Centre facts, then pause for the caller’s next need.

### 2. Service enquiry

Caller: “Je voudrais faire inspecter ma voiture. Combien coûte l’inspection ?”

The agent should answer the approved fictional price or explain that a quote is needed, without inventing a price or implying that an appointment is available.

### 3. Appointment request and correction

The caller requests an appointment and provides fictional details such as a name, telephone number, service, vehicle and preferred time window. If useful for the demo, initially say “Toyota Corolla”, then correct it naturally: “Ce n’est pas une Toyota Corolla, c’est une Hyundai i20.”

The agent should keep the latest value, avoid restarting the conversation, give a short final summary and say that the request has been sent to the team for confirmation. It must not say booked, confirmed, reserved or available.

### 4. Optional callback branch

Caller: “J’ai aussi une question sur un devis de flotte. Je préfère parler à quelqu’un.”

The agent should capture the caller’s contact and reason, create a callback request and explain that the team will follow up. It must not claim a live transfer or promise a response time that has not been configured.

### Presenter close

Explain that the caller’s request and any callback are recorded in the customer-owned destination, while the agent stays within the approved business facts and gives a truthful request acknowledgement.

## What the prospect should notice

- The agent answers a simple business question before collecting information.
- It can work in English or French for the Mauritius first version.
- It captures an appointment **request**, not a booking.
- A correction replaces the earlier value instead of restarting the conversation.
- A difficult or human-only request becomes a callback/handoff request.
- The customer owns the connected accounts, records and telephony route.

## What to explain after the call

The demo uses fictional data. Business facts, languages, tone, action permissions and callback destinations are configured per customer. The first version does not include confirmed booking, live availability, rescheduling, cancellation, CRM replacement, customer lookup or guaranteed live transfer/response time.

## Customer-facing capabilities

### Available now in the Receptionist release candidate

- 24/7 call answering once the customer’s telephony route is deployed;
- approved FAQs and business information;
- English and French conversation for the Mauritius first version;
- caller, vehicle and service-context capture;
- appointment-request capture with truthful wording;
- correction handling during a conversation;
- callback and human-handoff requests;
- structured request records in the configured customer-owned destination;
- customer-owned accounts, data and deployment configuration.

### Not included in this version

- confirmed booking or reservation;
- live calendar availability;
- reschedule or cancellation workflows;
- CRM replacement or customer lookup;
- guaranteed live transfer or response time;
- UAE Arabic runtime acceptance before that version is separately prepared and accepted.

## Implementation and handover flow

1. **Discover** — collect business facts, services, FAQs, languages, escalation rules and privacy choices.
2. **Connect customer-owned accounts** — connect the approved Retell, n8n, Google and telephony accounts without taking ownership of customer data.
3. **Configure** — TAKAVEN prepares the agent, knowledge, action contracts, destinations and fallback wording.
4. **Automated QA** — run the agreed conversation and integration checks using fictional or approved test data.
5. **Customer demo and acceptance** — review facts, wording, callback behaviour and safe outcome language.
6. **Telephony cutover** — connect the customer-owned number/SIP route, or keep browser/web-call mode for a demo.
7. **Monitored pilot** — operate for an agreed short period with a named support contact and rollback route.
8. **Handover and support** — provide configuration references, operating notes, support contact and rollback instructions.

## One-pager content

### Stop losing good enquiries after hours

Missed calls and repetitive questions cost service businesses time and opportunities. TAKAVEN Receptionist gives customers a professional first response while keeping the business in control of its facts, accounts and follow-up.

### What it does

TAKAVEN Receptionist answers approved FAQs, speaks English and French, collects caller and service details, captures appointment requests, handles corrections and sends human follow-up requests when the conversation needs a person.

It is deliberately truthful: a request is not presented as a confirmed booking, and the agent does not invent availability or business facts.

### How deployment works

TAKAVEN collects the business information, configures the receptionist in customer-owned accounts, runs automated QA, demonstrates the result, connects the approved telephony route and supports a short monitored pilot.

### Customer ownership

The customer owns the connected accounts, business data and telephony relationship. TAKAVEN provides configuration, implementation, QA and handover rather than forcing the customer into a proprietary platform.

### Languages and fallback

The first Mauritius version supports English and French. When the agent cannot safely complete a request, it captures a callback or handoff request for the configured team. It does not pretend to have transferred the caller unless a real transfer route is deployed.

### Call to action

**Book a TAKAVEN demo or discuss a customer-owned deployment.**

## Demo-to-pilot path

When a prospect says “I want this”, collect the business name, locations, timezone, hours, services, prices or quote rules, FAQs, preferred languages, tone, callback destination, fallback process, account ownership, telephony details, privacy choices and named acceptance owner. Then:

1. confirm the smallest pilot scope and approved facts;
2. connect customer-owned accounts and destinations;
3. configure one Receptionist deployment;
4. run automated QA and resolve only material defects;
5. conduct the customer demo and record acceptance;
6. connect the customer-owned telephony route or agree browser/web-call pilot mode;
7. run a short monitored pilot with a rollback contact;
8. hand over operating and support notes.

## Shared-base labels

The following are **FUTURE SHARED-BASE CANDIDATES**, not abstractions introduced by this package:

- customer configuration structure;
- provider and action-contract conventions;
- authenticated n8n integration pattern;
- truthful callback/handoff contract;
- automated QA and handover methodology.

Receptionist remains Agent #1. Sales and Admin/Support remain deferred.
