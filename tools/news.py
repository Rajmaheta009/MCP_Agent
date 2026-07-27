from mcp.server.fastmcp import FastMCP


def register_news_tools(mcp: FastMCP):

    @mcp.tool()
    def top_news(topic: str = "general") -> str:
        """
        Get latest news.
        (Implementation coming next)
        """
        return f"News tool is under development. Topic: {topic}"