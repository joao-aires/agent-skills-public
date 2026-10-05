"""Actual API/PostgreSQL plus stdio MCP with synthetic isolated sessions."""

import asyncio
import os
import subprocess
import time
from pathlib import Path
from uuid import uuid4

import httpx
from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def check(token: str, expected_title: str):
    transport = StdioTransport(
        command="uv",
        args=["run", "--frozen", "--group", "mcp", "python", "-m", "notes.mcp"],
        cwd=str(Path(__file__).resolve().parents[1]),
        env={
            **os.environ,
            "PYTHONPATH": "src",
            "NOTES_API_URL": "http://127.0.0.1:8010",
            "NOTES_SESSION_TOKEN": token,
        },
    )
    async with Client(transport) as client:
        assert [t.name for t in await client.list_tools()] == ["list_my_notes"]
        result = await client.call_tool("list_my_notes", {})
        assert not result.is_error
        assert [n["title"] for n in result.data] == [expected_title]


server = subprocess.Popen(
    [
        "uv",
        "run",
        "--frozen",
        "--group",
        "mcp",
        "uvicorn",
        "notes.main:app",
        "--app-dir",
        "src",
        "--host",
        "127.0.0.1",
        "--port",
        "8010",
    ],
    cwd=Path(__file__).resolve().parents[1],
)
try:
    with httpx.Client(base_url="http://127.0.0.1:8010", timeout=10) as http:
        for _ in range(100):
            try:
                if http.get("/api/health").status_code == 200:
                    break
            except httpx.ConnectError:
                pass
            if server.poll() is not None:
                raise RuntimeError("API exited before MCP integration")
            time.sleep(0.1)
        else:
            raise RuntimeError("API readiness timeout")
        for index in range(2):
            http.cookies.clear()
            origin = {"origin": "http://localhost:3000"}
            assert (
                http.post(
                    "/api/auth/register",
                    json={"email": f"{uuid4()}@example.com", "password": "test-password-123"},
                    headers=origin,
                ).status_code
                == 201
            )
            title = f"MCP user {index} {uuid4()}"
            assert http.post("/api/notes", json={"title": title}, headers=origin).status_code == 201
            asyncio.run(check(http.cookies["session"], title))
    print("Real stdio MCP authorization/persistence passed for two isolated identities")
finally:
    server.terminate()
    server.wait(timeout=15)
