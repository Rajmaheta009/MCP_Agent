from datetime import datetime
from mcp.server.fastmcp import FastMCP


def register_datetime_tools(mcp: FastMCP):

    @mcp.tool()
    def current_datetime() -> str:
        """Get current date and time"""
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @mcp.tool()
    def current_time() -> str:
        """Get current time"""
        return datetime.now().strftime("%H:%M:%S")

    @mcp.tool()
    def current_date() -> str:
        """Get current date"""
        return datetime.now().strftime("%d-%m-%Y")