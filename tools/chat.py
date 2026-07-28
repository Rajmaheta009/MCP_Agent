from mcp.server.fastmcp import FastMCP
from services.ai_service import generate_chat_response


def register_chat_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def chat(message: str, system_instruction: str = "") -> str:
        """Generate an AI response using Gemini."""
        return generate_chat_response(message, system_instruction or None)
