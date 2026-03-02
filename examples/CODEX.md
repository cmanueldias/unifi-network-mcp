# Using UniFi Network MCP with OpenAI Codex

This guide shows the recommended codex-first usage pattern for this server.

## Recommended Flow

1. Call `unifi_tool_index` to discover tool schemas.
2. Call `unifi_execute` for a single operation.
3. Use `unifi_batch` + `unifi_batch_status` for parallel work.

This pattern minimizes context usage and keeps calls explicit.

## Example Prompts

- `What UniFi tools are available for client analysis?`
- `Show top 10 wireless clients by traffic.`
- `List all offline UniFi devices and summarize by model.`
- `Prepare a change preview to block client aa:bb:cc:dd:ee:ff.`

## Mutation Safety

Mutating tools require explicit confirmation:
- Preview call: omit `confirm` or set `confirm=false`
- Execute call: set `confirm=true`

For automation workflows, you can use `UNIFI_AUTO_CONFIRM=true`.

## Config Templates

Use one of these templates:
- [`codex_config.toml`](codex_config.toml) for default `lazy` mode
- [`codex_meta_only.toml`](codex_meta_only.toml) for explicit discovery mode

## Practical Pattern

1. Discover candidates with `unifi_tool_index`.
2. Pick exact tool and required arguments from schema.
3. Execute via `unifi_execute`.
4. For bulk tasks, dispatch with `unifi_batch` and poll `unifi_batch_status`.
