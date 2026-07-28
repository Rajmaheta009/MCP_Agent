"""Raj Assistant MCP server entry point."""
from mcp.server.fastmcp import FastMCP

from config import PROJECT_NAME
from tools import register_all_tools

mcp = FastMCP(PROJECT_NAME)
register_all_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
