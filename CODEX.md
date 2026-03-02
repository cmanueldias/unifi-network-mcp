# unifi-network-mcp Development Guidelines (Codex)

This repository is optimized for OpenAI Codex workflows.

## Source of Truth

Read the project constitution first:
- [`oak/constitution.md`](oak/constitution.md)

All implementation and review decisions must follow the constitution.

## Codex-First MCP Workflow

1. Discover tools with `unifi_tool_index`.
2. Execute a single operation with `unifi_execute`.
3. Execute bulk/parallel operations with `unifi_batch` and poll with `unifi_batch_status`.
4. Use `confirm=true` only for intended mutations.

## Runtime Recommendation

- Default mode: `UNIFI_TOOL_REGISTRATION_MODE=lazy`
- Maximum control mode: `UNIFI_TOOL_REGISTRATION_MODE=meta_only`

Both modes are optimized for small context usage. In `meta_only`, discover tools first, then execute.

## Local Validation

```bash
# Unit/integration tests
uv run pytest tests/ -v

# Lint and format
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
```

## MCP Config Templates

Use the ready-made examples:
- [`examples/codex_config.toml`](examples/codex_config.toml)
- [`examples/codex_meta_only.toml`](examples/codex_meta_only.toml)
