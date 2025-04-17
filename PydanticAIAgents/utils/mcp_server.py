from pydantic_ai.mcp import MCPServerStdio



fetch_server = MCPServerStdio(
    'python',  ["-m", "mcp_server_fetch"]
)

