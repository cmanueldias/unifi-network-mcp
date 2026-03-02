# Quick Start Guide - v0.2.0

## Installation

```bash
# Clone
git clone https://github.com/sirkirby/unifi-network-mcp.git
cd unifi-network-mcp

# Install
uv sync

# Configure
cat > .env << EOF_ENV
UNIFI_HOST=192.168.1.1
UNIFI_USERNAME=admin
UNIFI_PASSWORD=password
# UNIFI_TOOL_REGISTRATION_MODE=lazy  # default
EOF_ENV
```

## OpenAI Codex Setup

Edit your Codex config and add this MCP server block:

```toml
[mcp_servers.unifi]
command = "uv"
args = ["--directory", "/path/to/unifi-network-mcp", "run", "python", "-m", "src.main"]

[mcp_servers.unifi.env]
UNIFI_HOST = "192.168.1.1"
UNIFI_USERNAME = "admin"
UNIFI_PASSWORD = "password"
UNIFI_PORT = "443"
UNIFI_SITE = "default"
UNIFI_VERIFY_SSL = "false"
# UNIFI_TOOL_REGISTRATION_MODE = "lazy"
```

Ready-to-use templates:
- [`examples/codex_config.toml`](examples/codex_config.toml)
- [`examples/codex_meta_only.toml`](examples/codex_meta_only.toml)

Restart OpenAI Codex after editing `codex_config.toml`.

## Tool Registration Modes

| Mode | Default | Best for |
|------|---------|----------|
| `lazy` | Yes | Codex and production conversational usage |
| `meta_only` | No | Maximum context control |
| `eager` | No | Dev console and manual debugging |

## Smoke Test

Use these prompts in OpenAI Codex:
- `What UniFi tools are available?`
- `Show my top 10 wireless clients by traffic.`
- `List all UniFi devices that are offline.`

## Local Validation

```bash
# Run server directly
uv run python -m src.main

# Run tests
uv run pytest tests/ -v
```
