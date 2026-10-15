# MCP (Model Context Protocol)

RedPilot speaks MCP in both directions.

## Expose RedPilot as tools (server)

Drive RedPilot from Claude Desktop or any MCP host as native tools:

```bash
pip install "redpilot[mcp]"
redpilot mcp          # stdio MCP server
```

Add it to your MCP host config (Claude Desktop shape):

```json
{
  "mcpServers": {
    "redpilot": { "command": "redpilot", "args": ["mcp"] }
  }
}
```

Exposed tools include `recon`, `toolkit`, `scan`, `webscan`, `crawl`,
`agent_run`, `scope_show`, `scope_add`, and `tools_status`. Scope is enforced
inside every tool, `agent_run` defaults to **plan-only** (dry-run), and every
active action is audit-logged.

> The MCP transport is stdio, so the server keeps stdout clean — logs go to stderr.

## Consume external MCP servers (client)

Point RedPilot at other MCP servers (CVE/OSINT feeds, your own tools) in
Claude-Desktop shape:

```bash
# mcp_servers.json  (or set REDPILOT_MCP_SERVERS)
redpilot mcp-tools    # list the tools exposed by the configured servers
```

External MCP tools run through the service — they are **not** auto-added to the
autonomous agent's fixed, curated action set.
