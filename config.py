"""Application configuration loaded from environment variables."""
from __future__ import annotations
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "Raj Assistant MCP")
VERSION = os.getenv("VERSION", "1.0.0")

WEATHER_BASE_URL = os.getenv(
    "WEATHER_BASE_URL",
    "https://api.open-meteo.com/v1/forecast",
)
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
NEWS_BASE_URL = os.getenv("NEWS_BASE_URL", "https://newsdata.io/api/1/latest")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

CURRENCY_BASE_URL = os.getenv("CURRENCY_BASE_URL", "https://api.frankfurter.app")

RAG_PERSIST_DIR = os.getenv("RAG_PERSIST_DIR", "./data/chroma")
RAG_COLLECTION = os.getenv("RAG_COLLECTION", "raj_assistant_documents")
RAG_CHUNK_SIZE = int(os.getenv("RAG_CHUNK_SIZE", "1000"))
RAG_CHUNK_OVERLAP = int(os.getenv("RAG_CHUNK_OVERLAP", "150"))
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "20"))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
