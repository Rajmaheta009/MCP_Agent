"""
Calculator Tools
----------------
This file contains all calculator-related MCP tools.

Workflow:
Inspector
    ↓
MCP Server
    ↓
Calculator Tool
    ↓
Return Result
"""

from mcp.server.fastmcp import FastMCP

# This function registers all calculator tools
def register_calculator_tools(mcp: FastMCP):

    @mcp.tool()
    def add(a: float, b: float) -> float:
        """
        Add two numbers.
        """
        return a + b

    @mcp.tool()
    def subtract(a: float, b: float) -> float:
        """
        Subtract two numbers.
        """
        return a - b

    @mcp.tool()
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.
        """
        return a * b

    @mcp.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide two numbers.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b