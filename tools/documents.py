from mcp.server.fastmcp import FastMCP
from services.document_service import extract_text
from services.rag_service import add_document


def register_document_tools(mcp: FastMCP) -> None:
    @mcp.tool()
    def read_document(path: str) -> dict:
        """Read supported local files: PDF, DOCX, TXT, MD, CSV, XLSX, JSON and images."""
        text = extract_text(path)
        return {"path": path, "characters": len(text), "text": text[:50000]}

    @mcp.tool()
    def index_document(path: str) -> dict:
        """Read a local document and add its text chunks to the local RAG vector store."""
        text = extract_text(path)
        count = add_document(text, path)
        return {"path": path, "chunks_added": count}
