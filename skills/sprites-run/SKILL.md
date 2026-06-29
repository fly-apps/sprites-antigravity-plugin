---
name: sprites-run
description: Runs commands inside a Sprite with clear confirmation and result summaries. Use when the user asks to execute, test, inspect, install, or debug inside a Sprite.
---

# Sprites Run

Use the hosted `sprites` MCP server exec tools.

1. Identify the target Sprite by exact name. List Sprites first if ambiguous.
2. For high-risk commands, create or verify a checkpoint before running.
3. Run the command in the intended working directory.
4. For long-running processes, prefer creating a Sprites service instead of an exec command.
5. Summarize command, exit status, key output, and follow-up steps.
