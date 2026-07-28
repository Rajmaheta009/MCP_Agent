from __future__ import annotations

import httpx
from config import HTTP_TIMEOUT, NEWS_API_KEY, NEWS_BASE_URL


async def get_news(topic: str = "general", country: str = "in", limit: int = 5) -> dict:
    if not NEWS_API_KEY:
        raise RuntimeError("NEWS_API_KEY is not configured. Add it to .env.")

    params = {
        "apikey": NEWS_API_KEY,
        "country": country,
        "language": "en",
        "size": max(1, min(limit, 10)),
    }
    if topic and topic.lower() != "general":
        params["q"] = topic

    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as client:
        response = await client.get(NEWS_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

    articles = []
    for item in data.get("results", [])[:limit]:
        articles.append({
            "title": item.get("title"),
            "description": item.get("description"),
            "url": item.get("link"),
            "source": item.get("source_name") or item.get("source_id"),
            "published_at": item.get("pubDate"),
        })

    return {"topic": topic, "country": country, "articles": articles}
