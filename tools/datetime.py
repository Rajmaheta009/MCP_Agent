from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from mcp.server.fastmcp import FastMCP


def _now(timezone: str) -> datetime:
    try:
        return datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError as exc:
        raise ValueError(f"Unknown timezone: {timezone}") from exc


def register_datetime_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def current_datetime(timezone: str = "Asia/Kolkata") -> str:
        """Get current date and time for an IANA timezone."""
        return _now(timezone).strftime("%Y-%m-%d %H:%M:%S %Z")

    @mcp.tool()
    def current_time(timezone: str = "Asia/Kolkata") -> str:
        """Get current time for an IANA timezone."""
        return _now(timezone).strftime("%H:%M:%S %Z")

    @mcp.tool()
    def current_date(timezone: str = "Asia/Kolkata") -> str:
        """Get current date for an IANA timezone."""
        return _now(timezone).strftime("%Y-%m-%d")
