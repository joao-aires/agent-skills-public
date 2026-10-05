"""Local stdio adapter; session identity is configured outside model/tool arguments."""

import os

import httpx
from fastmcp import FastMCP

mcp = FastMCP("Project Notes")


@mcp.tool
async def list_my_notes() -> list[dict]:
    """Read notes belonging to the configured authenticated user."""
    async with httpx.AsyncClient(base_url=os.environ["NOTES_API_URL"], timeout=10) as client:
        response = await client.get(
            "/api/notes", cookies={"session": os.environ["NOTES_SESSION_TOKEN"]}
        )
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")
