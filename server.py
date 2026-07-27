"""
=========================================
Raj Assistant - MCP Server
=========================================

This is the main entry point of our MCP project.

Responsibilities:
1. Create MCP Server
2. Register all tools
3. Start the server

"""

from mcp.server.fastmcp import FastMCP

# Project Configuration
from config import PROJECT_NAME

# Import Tool Registration Functions
from tools.calculator import register_calculator_tools
from tools.datetime import register_datetime_tools
from tools.chat import register_chat_tools
from tools.news import register_news_tools
from tools.weather import register_weather_tools
from tools.currency import register_currency_tools

# ---------------------------------------
# Create MCP Server
# ---------------------------------------

mcp = FastMCP(PROJECT_NAME)

# ---------------------------------------
# Register All Tools
# ---------------------------------------
register_calculator_tools(mcp)
register_weather_tools(mcp)
register_news_tools(mcp)
register_chat_tools(mcp)
register_datetime_tools(mcp)
register_currency_tools(mcp)

# ---------------------------------------
# Start Server
# ---------------------------------------

if __name__ == "__main__":
    print(f"{PROJECT_NAME} Started Successfully...")
    mcp.run()