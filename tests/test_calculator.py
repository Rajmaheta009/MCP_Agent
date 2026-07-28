from tools.calculator import register_calculator_tools
from mcp.server.fastmcp import FastMCP


def test_calculator_registration():
    mcp = FastMCP("test")
    register_calculator_tools(mcp)
    assert mcp is not None
