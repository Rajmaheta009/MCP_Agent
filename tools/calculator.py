from mcp.server.fastmcp import FastMCP


def register_calculator_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @mcp.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    @mcp.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @mcp.tool()
    def divide(a: float, b: float) -> float:
        """Divide a by b. Raises an error when b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @mcp.tool()
    def percentage(value: float, percent: float) -> float:
        """Calculate a percentage of a value."""
        return value * percent / 100
