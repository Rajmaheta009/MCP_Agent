from __future__ import annotations

import httpx
from config import CURRENCY_BASE_URL, HTTP_TIMEOUT


async def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    base = from_currency.upper().strip()
    target = to_currency.upper().strip()

    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if len(base) != 3 or len(target) != 3:
        raise ValueError("Currencies must be 3-letter ISO codes, e.g. USD, INR.")

    if base == target:
        return {
            "amount": amount,
            "from": base,
            "to": target,
            "rate": 1.0,
            "converted": amount,
            "source": "Frankfurter",
        }

    url = f"{CURRENCY_BASE_URL.rstrip('/')}/latest"
    params = {"amount": amount, "from": base, "to": target}
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    converted = data.get("rates", {}).get(target)
    if converted is None:
        raise ValueError(f"Currency pair {base}->{target} was not returned.")

    return {
        "amount": amount,
        "from": base,
        "to": target,
        "rate": converted / amount if amount else None,
        "converted": converted,
        "date": data.get("date"),
        "source": "Frankfurter",
    }
