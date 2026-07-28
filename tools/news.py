from mcp.server.fastmcp import FastMCP
from services.news_service import get_news


def register_news_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    async def top_news(topic: str = "general", country: str = "in", limit: int = 5) -> dict:
        """Get latest news. Uses NewsData.io and requires NEWS_API_KEY."""
        return await get_news(topic, country, limit)
