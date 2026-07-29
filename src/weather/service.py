from fastapi import HTTPException, status
from httpx import AsyncClient

from src.weather.config import WeatherConfig

settings = WeatherConfig()

GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


async def _get_coordinates(client: AsyncClient, city: str) -> tuple[float, float]:
    resp = await client.get(
        GEOCODING_URL,
        params={"q": city, "limit": 1, "appid": settings.API_KEY},
    )
    resp.raise_for_status()
    results = resp.json()
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City '{city}' not found.",
        )
    print(results)
    return results[0]["lat"], results[0]["lon"]


async def get_weather(client: AsyncClient, city: str) -> dict:
    lat, lon = await _get_coordinates(client, city)
    resp = await client.get(
        WEATHER_URL,
        params={"lat": lat, "lon": lon, "appid": settings.API_KEY, "units": "metric"},
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
