from mcp.server.fastmcp import FastMCP


def register_weather_tools(mcp: FastMCP):

    @mcp.tool()
    def get_weather(city: str) -> str:
        """
        Get weather information.
        (Implementation coming next)
        """
        return f"Weather tool is under development. Requested city: {city}"