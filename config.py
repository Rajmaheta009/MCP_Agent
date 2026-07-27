from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -----------------------------
# API Keys
# -----------------------------

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# -----------------------------
# Project
# -----------------------------

PROJECT_NAME = "Raj Assistant"

VERSION = "1.0.0"