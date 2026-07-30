from unittest.mock import AsyncMock

import httpx

from src.weather.service import get_weather


async def test_get_weather_returns_mapped_fields():
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    mock_client.get.return_value = httpx.Response(
        200,
        json={
            "name": "Paris",
            "main": {"temp": 22.3, "feels_like": 21.0, "humidity": 55},
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 3.2},
        },
        request=httpx.Request("GET", "https://api.openweathermap.org/data/2.5/weather"),
    )

    result = await get_weather(mock_client, "Paris")
    assert result == {
        "city": "Paris",
        "temperature": 22.3,
        "feels_like": 21.0,
        "description": "clear sky",
        "humidity": 55,
        "wind_speed": 3.2,
    }
