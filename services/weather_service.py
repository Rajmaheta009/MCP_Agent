from __future__ import annotations

import httpx
from config import HTTP_TIMEOUT, WEATHER_BASE_URL


async def get_weather(latitude: float, longitude: float) -> dict:
    """Get current weather from Open-Meteo."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,relative_humidity_2m,apparent_temperature,"
            "is_day,precipitation,rain,weather_code,cloud_cover,"
            "wind_speed_10m,wind_direction_10m"
        ),
        "timezone": "auto",
    }
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as client:
        response = await client.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "location": {
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
        },
        "current": data.get("current", {}),
        "units": data.get("current_units", {}),
        "source": "Open-Meteo",
    }
