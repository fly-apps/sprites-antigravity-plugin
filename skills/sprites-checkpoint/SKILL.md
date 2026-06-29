---
name: sprites-checkpoint
description: Creates, lists, inspects, or restores Sprite checkpoints. Use before risky changes or when the user asks for rollback, snapshots, or restore points.
---

# Sprites Checkpoint

Use the hosted `sprites` MCP server checkpoint tools.

1. Identify the target Sprite by exact name.
2. For creation, use a short reason-based checkpoint description.
3. For listing or inspection, summarize checkpoint IDs, names/descriptions, and timestamps if available.
4. For restore, force a clear confirmation that restoring rewinds filesystem state and discards newer changes.
5. After restore, inspect the Sprite state before continuing.
