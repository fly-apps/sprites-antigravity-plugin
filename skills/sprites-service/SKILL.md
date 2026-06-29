---
name: sprites-service
description: Manages long-running services in a Sprite. Use when the user wants to start, stop, restart, expose, inspect, or debug web servers and background services.
---

# Sprites Service

Use the hosted `sprites` MCP server service tools and read `../sprites/references/services.md` if the workflow is not trivial.

1. Identify the target Sprite and inspect existing services.
2. Prefer stable service names such as `web`, `worker`, or `preview`.
3. Configure command, working directory, environment, and port intentionally.
4. Start or restart the service and inspect recent logs.
5. Ask before making URLs public or widening network access.
6. Report service name, status, port, URL/auth mode, and log highlights.
