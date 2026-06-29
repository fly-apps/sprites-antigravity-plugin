# Sprites Services

Use Sprites services for long-running processes such as web servers, workers, daemons, and preview apps.

## Service Workflow

1. Inspect existing services before adding a new one.
2. Prefer stable service names based on the project or role, such as `web`, `worker`, or `preview`.
3. Set the command, working directory, environment, and port intentionally.
4. Start or restart the service.
5. Inspect status and recent logs.
6. If a URL is needed, confirm whether it should remain private/authenticated or become public.

## Debugging

- Read logs before changing code.
- Restart only the affected service.
- Include service name, port, URL/auth mode, and log summary in the final response.
