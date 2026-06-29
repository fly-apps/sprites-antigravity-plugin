# Sprites Deployment And Sync

Use this reference for workflows that copy local project state into a Sprite, build inside a Sprite, or run a preview service.

## Recommended Flow

1. Confirm the target Sprite and remote working directory.
2. Create or verify a checkpoint before overwriting remote files.
3. Sync selected paths, not the entire workspace by default.
4. Install dependencies or build inside the Sprite only when needed.
5. Run tests or smoke checks inside the Sprite.
6. Start or update a service for long-running previews.
7. Inspect logs and report URLs, auth mode, and any remaining manual steps.

## Sync Boundaries

Avoid syncing:

- `.git/`
- dependency caches such as `node_modules/`, `_build/`, `.venv/`, `target/`, or `dist/` unless explicitly requested
- local secrets such as `.env`, key files, token caches, and credential stores
- large generated artifacts unless they are the intended deployment payload
