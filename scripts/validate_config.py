#!/usr/bin/env python3
"""Offline lint for TAKAVEN's fixed draft client configuration v1. No network."""
import argparse
import copy
import hashlib
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
NULL_STRING = ("string", "null")
SHAPE = {
    "schema_version": "integer", "stage": "string",
    "client": {k: "string" for k in ("id", "name", "market", "timezone", "currency")},
    "conversation": {
        "languages": ["string"], "default_language": "string",
        "ai_disclosure": "boolean", "voice_refs": "voices"
    },
    "facts": {
        "approved": "boolean",
        "address": "string",
        "faqs": [{"id": "string", "text": "localized"}],
        "services": [{
            "id": "string", "name": "string", "duration_minutes": "integer",
            "price_amount": NULL_STRING, "price_basis": "string", "tax_wording": "string"
        }],
        "hours": [{"day": "string", "open": "string", "close": "string"}],
        "closures": ["string"]
    },
    "routing": {
        "intents": [{"id": "string", "qualification_fields": ["string"], "action": "string"}],
        "escalation": [{"id": "string", "trigger": "string", "action": "string"}]
    },
    "integration": {k: NULL_STRING for k in ("provider", "agent_ref", "booking_authority")},
    "safety": {
        "explicit_confirmation": "boolean", "identity_policy_ref": NULL_STRING,
        **{k: "string" for k in (
            "idempotency", "availability", "confirmation", "unknown_outcome",
            "reschedule", "missing_config", "retries"
        )}
    },
    "operations": {
        "mode": "string", "customer_binding": "string", "request_destination_ref": "string",
        "handoff": {"destination_ref": NULL_STRING, "hours": "string", "fallback": "string"},
        "rollback_ref": NULL_STRING
    },
    "privacy": {
        "recording_enabled": "boolean", "messaging_requires_consent": "boolean",
        "retention_days": ("integer", "null")
    }
}
POLICIES = {
    "idempotency": "durable_operation_and_payload",
    "availability": "authoritative_only", "confirmation": "committed_receipt_only",
    "unknown_outcome": "reconcile_before_retry", "reschedule": "atomic_or_human",
    "missing_config": "fail_closed", "retries": "bounded_then_manual_review"
}
MARKETS = {
    "MU": ("Indian/Mauritius", "MUR", {"en", "fr"}),
    "AE": ("Asia/Dubai", "AED", {"en", "ar"})
}
TYPES = {"string": str, "integer": int, "boolean": bool, "null": type(None)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_shape(value, shape, path="config"):
    if isinstance(shape, dict):
        require(type(value) is dict, f"{path}: expected object")
        require(set(value) == set(shape), f"{path}: unknown or missing keys")
        for key, subshape in shape.items():
            check_shape(value[key], subshape, f"{path}.{key}")
    elif isinstance(shape, list):
        require(type(value) is list, f"{path}: expected array")
        for index, item in enumerate(value):
            check_shape(item, shape[0], f"{path}[{index}]")
    elif shape == "voices":
        require(type(value) is dict, f"{path}: expected language object")
        for key, item in value.items():
            check_shape(key, "string", path)
            check_shape(item, NULL_STRING, f"{path}.{key}")
    elif shape == "localized":
        require(type(value) is dict, f"{path}: expected localized object")
        for key, item in value.items():
            check_shape(key, "string", path)
            check_shape(item, "string", f"{path}.{key}")
    else:
        allowed = shape if isinstance(shape, tuple) else (shape,)
        require(any(type(value) is TYPES[t] for t in allowed), f"{path}: invalid type")
        if type(value) is str:
            require(bool(value.strip()), f"{path}: blank string")


def lint(config):
    check_shape(config, SHAPE)
    require(config["schema_version"] == 1 and config["stage"] == "draft",
            "Only v1 draft configuration is supported; this tool cannot approve deployment")
    c = config["client"]
    require(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", c["id"])), "Invalid client ID")
    require(c["market"] in MARKETS, "Market must be MU or AE")
    timezone, currency, languages = MARKETS[c["market"]]
    require(c["timezone"] == timezone and c["currency"] == currency, "Market/timezone/currency mismatch")
    ZoneInfo(c["timezone"])
    conv = config["conversation"]
    require(set(conv["languages"]) == languages and len(conv["languages"]) == 2,
            "Required language pair mismatch")
    require(conv["default_language"] in languages, "Invalid default language")
    require(set(conv["voice_refs"]) == languages, "Voice references must match languages")
    require(conv["ai_disclosure"], "AI disclosure is required")
    facts = config["facts"]
    require(facts["address"].strip(), "Address is required")
    faq_ids = set()
    for faq in facts["faqs"]:
        require(faq["id"] not in faq_ids, "Duplicate FAQ ID")
        faq_ids.add(faq["id"])
        require(set(faq["text"]) == languages, "FAQ languages must match market")
        require(all(text.strip() for text in faq["text"].values()), "FAQ text cannot be blank")
    require(bool(facts["services"]), "Service catalogue is empty")
    ids = set()
    for service in facts["services"]:
        require(bool(re.fullmatch(r"[a-z][a-z0-9_]*", service["id"])), "Invalid service ID")
        require(service["id"] not in ids, "Duplicate service ID")
        ids.add(service["id"])
        require(1 <= service["duration_minutes"] <= 480, "Invalid service duration")
        amount = service["price_amount"]
        require(service["price_basis"] in ("fixed_demo", "fixed", "from", "human_quote"), "Invalid price basis")
        require((amount is None) == (service["price_basis"] == "human_quote"),
                "Unknown prices must require human quotation")
        if amount is not None:
            require(bool(re.fullmatch(r"[0-9]+(?:\.[0-9]{1,2})?", amount)), "Invalid decimal price")
            price = Decimal(amount)
            require(price.is_finite() and price >= 0, "Price must be finite and nonnegative")
        require(not facts["approved"] or service["price_basis"] != "fixed_demo",
                "Demo prices cannot be marked client-approved")
    routing = config["routing"]
    intent_ids = set()
    for intent in routing["intents"]:
        require(intent["id"] not in intent_ids, "Duplicate intent ID")
        intent_ids.add(intent["id"])
        require(intent["qualification_fields"], "Intent qualification fields are empty")
        require(len(intent["qualification_fields"]) == len(set(intent["qualification_fields"])), "Duplicate intent qualification field")
        require(intent["action"] in ("create_lead", "capture_appointment_request", "escalate_to_human"), "Invalid intent action")
    escalation_ids = set()
    for rule in routing["escalation"]:
        require(rule["id"] not in escalation_ids, "Duplicate escalation ID")
        escalation_ids.add(rule["id"])
        require(rule["action"] in ("human", "callback_capture"), "Invalid escalation action")
    days = set()
    require(bool(facts["hours"]), "Opening hours are empty")
    for window in facts["hours"]:
        require(window["day"] in ("mon", "tue", "wed", "thu", "fri", "sat", "sun"), "Invalid weekday")
        require(window["day"] not in days, "Duplicate weekday; v1 supports one window per day")
        days.add(window["day"])
        for field in ("open", "close"):
            require(bool(re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", window[field])), "Invalid opening time")
        require(window["open"] < window["close"], "Opening window must end later on same day")
    require(len(facts["closures"]) == len(set(facts["closures"])), "Duplicate closure date")
    for closure in facts["closures"]:
        require(date.fromisoformat(closure).isoformat() == closure, "Closure must be YYYY-MM-DD")
    safety = config["safety"]
    require(safety["explicit_confirmation"], "Explicit intent confirmation is required")
    for key, expected in POLICIES.items():
        require(safety[key] == expected, f"Unsafe policy: {key}")
    ops = config["operations"]
    require(ops["mode"] in ("primary", "overflow", "after_hours"), "Invalid reception mode")
    require(ops["customer_binding"] == "trusted_destination_and_agent", "Unsafe customer binding")
    require(ops["request_destination_ref"] == "n8n:webhook:appointment-request",
            "Request destination must be the documented n8n appointment route")
    require(ops["handoff"]["hours"] in ("business", "always", "configured"), "Invalid handoff hours")
    require(ops["handoff"]["fallback"] == "callback_capture", "Unsafe handoff fallback")
    privacy = config["privacy"]
    require(not privacy["recording_enabled"], "Draft pack does not authorise recordings")
    require(privacy["messaging_requires_consent"], "Messaging consent is required")
    require(privacy["retention_days"] is None or 1 <= privacy["retention_days"] <= 365,
            "Invalid retention; value requires client approval before deployment")
    prerequisites = []
    for section, fields in {
        "integration": ("provider", "agent_ref"),
        "safety": ("identity_policy_ref",),
        "operations": ("rollback_ref", "handoff.destination_ref"),
        "privacy": ("retention_days",)
    }.items():
        for field in fields:
            value = config[section]
            for part in field.split("."):
                value = value[part]
            if value is None:
                prerequisites.append(f"{section}.{field}")
    prerequisites.extend(f"conversation.voice_refs.{lang}" for lang, ref in conv["voice_refs"].items() if ref is None)
    if not facts["approved"]:
        prerequisites.append("facts.client_approval")
    raw = json.dumps(config, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return {"status": "VALID_DRAFT", "config_sha256": hashlib.sha256(raw).hexdigest(),
            "unresolved_prerequisites": prerequisites,
            "deferred_prerequisites": ["integration.booking_authority"],
            "deployment_ready": False}


def read_config(path):
    def unique_pairs(pairs):
        value = {}
        for key, item in pairs:
            require(key not in value, f"Duplicate JSON key: {key}")
            value[key] = item
        return value
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def self_test():
    base = read_config(ROOT / "config/mauritius.example.json")
    lint(base)
    lint(read_config(ROOT / "config/uae.example.json"))
    cases = [
        ("production stage", lambda c: c.update(stage="production")),
        ("unknown key", lambda c: c["safety"].update(bypass=True)),
        ("missing key", lambda c: c["safety"].pop("confirmation")),
        ("wrong type", lambda c: c["safety"].update(explicit_confirmation="true")),
        ("boolean version", lambda c: c.update(schema_version=True)),
        ("currency mismatch", lambda c: c["client"].update(currency="AED")),
        ("timezone mismatch", lambda c: c["client"].update(timezone="UTC")),
        ("language mismatch", lambda c: c["conversation"].update(languages=["en", "ar"])),
        ("voice mismatch", lambda c: c["conversation"].update(voice_refs={"en": None})),
        ("duplicate service", lambda c: c["facts"]["services"].append(copy.deepcopy(c["facts"]["services"][0]))),
        ("invented unknown price", lambda c: c["facts"]["services"][1].update(price_amount="1.00")),
        ("NaN price", lambda c: c["facts"]["services"][0].update(price_amount="NaN")),
        ("invalid time", lambda c: c["facts"]["hours"][0].update(open="25:00")),
        ("reverse hours", lambda c: c["facts"]["hours"][0].update(close="08:00")),
        ("invalid date", lambda c: c["facts"].update(closures=["2026-02-30"])),
        ("unsafe confirmation", lambda c: c["safety"].update(confirmation="stub_success")),
        ("unsafe binding", lambda c: c["operations"].update(customer_binding="caller_number")),
        ("recording", lambda c: c["privacy"].update(recording_enabled=True)),
        ("no message consent", lambda c: c["privacy"].update(messaging_requires_consent=False)),
        ("approved demo facts", lambda c: c["facts"].update(approved=True)),
        ("FAQ language mismatch", lambda c: c["facts"]["faqs"][0].update(text={"en": "Only English"})),
        ("empty intent fields", lambda c: c["routing"]["intents"][0].update(qualification_fields=[])),
        ("unsafe handoff fallback", lambda c: c["operations"]["handoff"].update(fallback="pretend_connected")),
    ]
    for label, change in cases:
        candidate = copy.deepcopy(base)
        change(candidate)
        try:
            lint(candidate)
        except (ValueError, InvalidOperation):
            continue
        raise AssertionError(f"Unsafe configuration accepted: {label}")
    require(lint(base)["config_sha256"] == lint(copy.deepcopy(base))["config_sha256"], "Hash is unstable")
    print(json.dumps({"status": "PASS", "valid_profiles": 2, "rejected_negative_cases": len(cases),
                      "deterministic_hash": True, "scope": "offline configuration lint only"}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    paths = args.paths or sorted((ROOT / "config").glob("*.example.json"))
    failed = False
    for path in paths:
        try:
            print(json.dumps({"file": str(path), **lint(read_config(path))}))
        except (ValueError, OSError, InvalidOperation) as error:
            print(json.dumps({"file": str(path), "status": "INVALID", "error": str(error)}))
            failed = True
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
