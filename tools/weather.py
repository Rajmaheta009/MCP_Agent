from mcp.server.fastmcp import FastMCP
from services.weather_service import get_weather


def register_weather_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    async def get_current_weather(latitude: float, longitude: float) -> dict:
        """Get current weather using latitude and longitude."""
        return await get_weather(latitude, longitude)
