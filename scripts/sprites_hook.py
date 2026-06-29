#!/usr/bin/env python3
"""Antigravity hook helpers for the Sprites Plugin.

The hook contract is JSON on stdin and JSON on stdout. Keep this script
dependency-free so the Sprites Plugin works immediately after installation.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


DESTRUCTIVE_PATTERNS = [
    r"destroy[_-]?sprite",
    r"delete[_-]?sprite",
    r"restore[_-]?(sprite|checkpoint)",
    r"delete[_-]?checkpoint",
    r"update[_-]?network[_-]?policy",
    r"set[_-]?network[_-]?policy",
    r"make[_-]?public",
    r"public[_-]?url",
    r"expose[_-]?(service|port|url)",
    r"privilege[_-]?policy",
    r"resource[_-]?policy",
]

CHECKPOINT_PATTERNS = [
    r"\brm\s+-rf\b",
    r"\bdrop\s+database\b",
    r"\btruncate\s+table\b",
    r"\bdelete\s+from\b",
    r"\b(db:)?migrate\b",
    r"\bprisma\s+migrate\b",
    r"\balembic\s+upgrade\b",
    r"\brails\s+db:migrate\b",
    r"\bnpm\s+(install|update|audit\s+fix)\b",
    r"\bpnpm\s+(install|update|add|up)\b",
    r"\byarn\s+(install|upgrade|add)\b",
    r"\bpip\s+install\b",
    r"\buv\s+(pip\s+)?install\b",
    r"\bapt(-get)?\s+(install|upgrade|dist-upgrade)\b",
    r"\bdnf\s+(install|upgrade)\b",
    r"\bapk\s+add\b",
]

TEST_PATTERNS = [
    r"\bnpm\s+(run\s+)?test\b",
    r"\bpnpm\s+(run\s+)?test\b",
    r"\byarn\s+(run\s+)?test\b",
    r"\bpytest\b",
    r"\bpython\s+-m\s+pytest\b",
    r"\bgo\s+test\b",
    r"\bcargo\s+test\b",
    r"\bmix\s+test\b",
    r"\bbundle\s+exec\s+rspec\b",
    r"\brspec\b",
]


def read_payload() -> dict[str, Any]:
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        return {}


def searchable_text(payload: dict[str, Any]) -> str:
    tool_call = payload.get("toolCall") or {}
    return json.dumps(
        {
            "name": tool_call.get("name", ""),
            "args": tool_call.get("args", {}),
        },
        sort_keys=True,
    ).lower()


def command_line(payload: dict[str, Any]) -> str:
    args = (payload.get("toolCall") or {}).get("args") or {}
    for key in ("CommandLine", "commandLine", "command", "cmd"):
        value = args.get(key)
        if isinstance(value, str):
            return value.lower()
    return searchable_text(payload)


def matches_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def respond(obj: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(obj))


def allow() -> None:
    respond({"allow_tool": True})


def deny(reason: str) -> None:
    respond({"allow_tool": False, "deny_reason": reason})


def safety(payload: dict[str, Any]) -> None:
    text = searchable_text(payload)
    if matches_any(text, DESTRUCTIVE_PATTERNS):
        deny(
            "This Sprites action may destroy state, restore over newer work, "
            "or expose a service/network policy. Confirm the exact Sprite, "
            "scope, and rollback plan before continuing."
        )
        return
    allow()


def checkpoint(payload: dict[str, Any]) -> None:
    text = command_line(payload)
    if matches_any(text, CHECKPOINT_PATTERNS):
        deny(
            "This looks like a high-risk Sprite change. Create or verify a "
            "recent checkpoint before proceeding."
        )
        return
    allow()


def remote_test(payload: dict[str, Any]) -> None:
    text = command_line(payload)
    if matches_any(text, TEST_PATTERNS):
        deny(
            "Remote Sprite test routing is enabled. Run this test inside the "
            "selected Sprite with the Sprites MCP exec tool unless the user "
            "explicitly wants a local run."
        )
        return
    allow()


def auto_sync(_: dict[str, Any]) -> None:
    # PostToolUse hooks cannot directly call MCP tools. Keep this disabled by
    # default and use it as a visible reminder when a workspace opts in.
    allow()


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "safety"
    payload = read_payload()

    if mode == "safety":
        safety(payload)
    elif mode == "checkpoint":
        checkpoint(payload)
    elif mode == "remote-test":
        remote_test(payload)
    elif mode == "auto-sync":
        auto_sync(payload)
    else:
        allow()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
