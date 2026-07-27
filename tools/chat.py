from mcp.server.fastmcp import FastMCP


def register_chat_tools(mcp: FastMCP):

    @mcp.tool()
    def chat(message: str) -> str:
        """
        AI Chat Tool
        (Gemini/OpenAI coming later)
        """
        return f"You said: {message}"