#!/usr/bin/env python3
"""Offline validation for the sanitized TAKAVEN Receptionist v0.1 package."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = [
    "caller_name",
    "caller_contact",
    "vehicle",
    "service",
    "preferred_date",
    "preferred_time_window",
]
SHEET_FIELDS = [
    "Caller Name",
    "Caller Contact",
    "Vehicle",
    "Service",
    "Preferred Date",
    "Preferred Time Window",
    "Call Reference",
    "Status",
]
FORBIDDEN_LIVE_MARKERS = (
    "takaven.app.n8n.cloud",
    "eu1.make.com",
    "api_key=",
    "Bearer ",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    agent_path = ROOT / "retell/agent-config.example.json"
    schema_path = ROOT / "retell/tools/capture_appointment_request.schema.json"
    workflow_path = ROOT / "n8n/capture_appointment_request.sanitized.workflow.json"
    sheet_path = ROOT / "n8n/sheet-schema.example.csv"

    agent = read_json(agent_path)
    schema = read_json(schema_path)
    workflow = read_json(workflow_path)
    schema_fields = schema["properties"]
    require(schema["type"] == "object", "tool schema must be an object")
    require(schema["required"] == REQUIRED_FIELDS, "tool required fields changed")
    require(set(REQUIRED_FIELDS).issubset(schema_fields), "tool field missing")
    require(agent["tool"]["name"] == "capture_appointment_request", "agent tool mismatch")
    require(agent["tool"]["schema_file"].endswith("capture_appointment_request.schema.json"), "agent schema reference mismatch")
    require(agent["tool"]["max_retries"] == 0, "automatic retries must remain disabled")

    nodes = workflow["nodes"]
    node_names = {node["name"] for node in nodes}
    require(len(nodes) == 4, "baseline must contain exactly four nodes")
    require(
        node_names
        == {
            "Retell Function - Capture Appointment Request",
            "Save Appointment Request",
            "Respond - Request Received",
            "Respond - Request Failed",
        },
        "unexpected baseline node set",
    )
    workflow_text = json.dumps(workflow, ensure_ascii=False)
    for field in REQUIRED_FIELDS:
        require(field in workflow_text, f"workflow does not map {field}")
    require("status\\\":\\\"RECEIVED" in workflow_text, "RECEIVED response missing")
    require("status\\\":\\\"FAILED" in workflow_text, "FAILED response missing")
    require("booking" not in workflow_text.lower(), "booking action leaked into workflow")
    require("calendar" not in workflow_text.lower(), "calendar action leaked into workflow")

    with sheet_path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.reader(stream))
    require(rows and rows[0] == SHEET_FIELDS, "Sheet schema mismatch")
    require(len(rows) == 2, "Sheet example must contain one fictional row")
    require(rows[1][-1] == "RECEIVED", "Sheet example status mismatch")

    package_text = "\n".join(path.read_text(encoding="utf-8") for path in (agent_path, schema_path, workflow_path, sheet_path))
    for marker in FORBIDDEN_LIVE_MARKERS:
        require(marker not in package_text, f"live secret or endpoint marker found: {marker}")
    urls = re.findall(r"https?://[^<>\s\"]+", package_text)
    require(
        urls == ["https://json-schema.org/draft/2020-12/schema"],
        "non-placeholder URL found in baseline package",
    )

    print(json.dumps({"status": "PASS", "nodes": len(nodes), "required_fields": REQUIRED_FIELDS, "live_values": False}))


if __name__ == "__main__":
    main()
