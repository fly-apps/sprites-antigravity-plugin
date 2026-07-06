---
name: sprites-cleanup
description: Finds and safely cleans up stale Sprites, services, and exec sessions. Use when the user asks to tidy, prune, delete old environments, or reduce Sprite clutter.
---

# Sprites Cleanup

Use the hosted `sprites` MCP server.

1. List Sprites and identify likely cleanup candidates, especially old `mcp-` prefixed environments.
2. Inspect services, checkpoints, and exec sessions to understand each candidate before proposing cleanup.
3. Present a cleanup plan with exact Sprite names and destructive effects.
4. Ask for confirmation before destroying Sprites, stopping services, or killing exec sessions.
5. Prefer stopping services before destroying a Sprite when that makes the action clearer.
6. Report what was cleaned up and what was intentionally kept.

Checkpoints cannot be deleted individually; a Sprite's checkpoints are removed only when the Sprite is destroyed. Note that when listing what a `destroy_sprite` will remove.
