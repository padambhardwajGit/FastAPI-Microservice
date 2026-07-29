from typing import Annotated

from fastapi import APIRouter, Query

from src.dependencies import HttpClientDep
from src.weather.schemas import WeatherResponse
from src.weather.service import get_weather

router = APIRouter(tags=["weather"])


@router.get(
    "/weather",
    response_model=WeatherResponse,
    summary="Get current weather",
    description="Query current weather for a city using the OpenWeather API.",
)
async def weather(
    client: HttpClientDep,
    city: Annotated[str, Query(min_length=1, max_length=100, description="City name")],
) -> dict:
    return await get_weather(client, city)
