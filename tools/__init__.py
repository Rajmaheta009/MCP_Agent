from mcp.server.fastmcp import FastMCP

from .calculator import register_calculator_tools
from .datetime import register_datetime_tools
from .weather import register_weather_tools
from .news import register_news_tools
from .chat import register_chat_tools
from .currency import register_currency_tools
from .documents import register_document_tools
from .rag import register_rag_tools


def register_all_tools(mcp: FastMCP) -> None:
    register_calculator_tools(mcp)
    register_datetime_tools(mcp)
    register_weather_tools(mcp)
    register_news_tools(mcp)
    register_chat_tools(mcp)
    register_currency_tools(mcp)
    register_document_tools(mcp)
    register_rag_tools(mcp)
