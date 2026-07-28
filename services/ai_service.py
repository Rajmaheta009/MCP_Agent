from __future__ import annotations

from config import GEMINI_API_KEY, GEMINI_MODEL


def generate_chat_response(message: str, system_instruction: str | None = None) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured. Add it to .env.")

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=GEMINI_API_KEY)
    config = None
    if system_instruction:
        config = types.GenerateContentConfig(system_instruction=system_instruction)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=message,
        config=config,
    )
    return response.text or ""
