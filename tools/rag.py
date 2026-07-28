from mcp.server.fastmcp import FastMCP
from services.rag_service import search_documents


def register_rag_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def search_knowledge(query: str, top_k: int = 5) -> list[dict]:
        """Search documents previously indexed with index_document."""
        return search_documents(query, top_k)
