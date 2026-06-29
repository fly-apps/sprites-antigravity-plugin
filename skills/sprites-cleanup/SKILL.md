---
name: sprites-cleanup
description: Finds and safely cleans up stale Sprites, checkpoints, services, and exec sessions. Use when the user asks to tidy, prune, delete old environments, or reduce Sprite clutter.
---

# Sprites Cleanup

Use the hosted `sprites` MCP server.

1. List Sprites and identify likely cleanup candidates, especially old `mcp-` prefixed environments.
2. Inspect services and checkpoints before proposing deletion.
3. Present a cleanup plan with exact Sprite names and destructive effects.
4. Ask for confirmation before destroying Sprites or deleting checkpoints.
5. Prefer stopping services before destroying a Sprite when that makes the action clearer.
6. Report what was deleted and what was intentionally kept.
