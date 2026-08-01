#!/usr/bin/env python3
"""Validate an orchestrate-dev completion evidence JSON document."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


VALID_MODES = {"compact", "coordinated", "critical"}
VALID_STATUSES = {"passed", "failed", "blocked"}
VALID_VERDICTS = {"pass", "revise", "blocked"}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(data: Any, require_complete: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["document must be a JSON object"]

    if data.get("mode") not in VALID_MODES:
        errors.append("mode must be compact, coordinated, or critical")
    if not nonempty_string(data.get("outcome")):
        errors.append("outcome must be a non-empty string")

    criteria = data.get("acceptance_criteria")
    if not isinstance(criteria, list) or not criteria:
        errors.append("acceptance_criteria must be a non-empty list")
        criteria = []
    for index, item in enumerate(criteria):
        prefix = f"acceptance_criteria[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in ("criterion", "artifact", "verification"):
            if not nonempty_string(item.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string")
        if item.get("status") not in VALID_STATUSES:
            errors.append(f"{prefix}.status must be passed, failed, or blocked")

    checks = data.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("checks must be a non-empty list")
        checks = []
    for index, item in enumerate(checks):
        prefix = f"checks[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if not nonempty_string(item.get("command")):
            errors.append(f"{prefix}.command must be a non-empty string")
        if not nonempty_string(item.get("result")):
            errors.append(f"{prefix}.result must be a non-empty string")

    for field in ("review_verdict", "qa_verdict"):
        if data.get(field) not in VALID_VERDICTS:
            errors.append(f"{field} must be pass, revise, or blocked")
    if not isinstance(data.get("residual_risks"), list):
        errors.append("residual_risks must be a list")
    if not isinstance(data.get("required_work_remaining"), bool):
        errors.append("required_work_remaining must be a boolean")

    if require_complete:
        if any(item.get("status") != "passed" for item in criteria if isinstance(item, dict)):
            errors.append("completion requires every acceptance criterion to pass")
        if data.get("review_verdict") != "pass":
            errors.append("completion requires review_verdict=pass")
        if data.get("qa_verdict") != "pass":
            errors.append("completion requires qa_verdict=pass")
        if data.get("required_work_remaining") is not False:
            errors.append("completion requires required_work_remaining=false")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="Path to evidence JSON")
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()

    try:
        data = json.loads(args.evidence.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid evidence file: {exc}", file=sys.stderr)
        return 2

    errors = validate(data, args.require_complete)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Evidence is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
