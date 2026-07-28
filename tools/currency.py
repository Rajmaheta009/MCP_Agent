from mcp.server.fastmcp import FastMCP
from services.currency_service import convert_currency as service_convert_currency


def register_currency_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    async def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
        """Convert an amount using current Frankfurter exchange-rate data."""
        return await service_convert_currency(amount, from_currency, to_currency)
