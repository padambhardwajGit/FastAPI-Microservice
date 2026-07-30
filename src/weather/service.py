from fastapi import HTTPException, status
from httpx import AsyncClient

from src.weather.config import WeatherConfig

settings = WeatherConfig()

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"



async def get_weather(client: AsyncClient, city: str) -> dict:
    resp = await client.get(
        WEATHER_URL,
        params={"q": city, "appid": settings.API_KEY, "units": "metric"},
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
