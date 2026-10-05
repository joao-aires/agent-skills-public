"""Exercise actual stdio MCP against a running API with an explicit session token."""

import asyncio
import os
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def main():
    transport = StdioTransport(
        command="uv",
        args=["run", "--frozen", "--group", "mcp", "python", "-m", "notes.mcp"],
        cwd=str(Path(__file__).resolve().parents[1]),
        env={**os.environ, "PYTHONPATH": "src"},
    )
    async with Client(transport) as client:
        tools = await client.list_tools()
        assert [t.name for t in tools] == ["list_my_notes"]
        result = await client.call_tool("list_my_notes", {})
        assert not result.is_error
        print("Authenticated read-only MCP round trip passed")


asyncio.run(main())
