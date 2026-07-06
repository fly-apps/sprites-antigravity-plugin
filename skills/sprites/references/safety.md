# Sprites Safety

## Confirm Before These Actions

- Destroying a Sprite.
- Restoring a checkpoint.
- Updating outbound network policy.
- Making a service public or exposing a new URL.
- Changing privilege/resource policy.
- Overwriting broad filesystem paths.

## Checkpoint Guidance

Create a checkpoint before:

- Package upgrades or dependency lockfile churn.
- Database migrations.
- Bulk file moves, deletes, or generated rewrites.
- Service command changes.
- Network policy changes.
- Experiments with untrusted code.

Use checkpoint names or descriptions that include the reason, such as `before-node-upgrade` or `before-db-migration`.

## Recovery

Before restoring, explain that restore rewinds filesystem state and discards work after the checkpoint. List newer checkpoints or relevant files first when possible.

There is no tool to delete an individual checkpoint. Checkpoints are removed only by destroying the Sprite.
