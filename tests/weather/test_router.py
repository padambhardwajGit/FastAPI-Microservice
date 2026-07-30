import httpx


async def test_weather_valid_city(client, mock_http_client):
    mock_http_client.get.return_value = httpx.Response(
        200,
        json={
            "name": "London",
            "main": {"temp": 15.0, "feels_like": 13.5, "humidity": 72},
            "weather": [{"description": "overcast clouds"}],
            "wind": {"speed": 4.1},
        },
        request=httpx.Request("GET", "http://test/weather"),
    )
    resp = await client.get("/weather", params={"city": "London"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["city"] == "London"
    assert data["temperature"] == 15.0
    assert data["feels_like"] == 13.5
    assert data["description"] == "overcast clouds"
    assert data["humidity"] == 72
    assert data["wind_speed"] == 4.1


async def test_weather_missing_city(client, mock_http_client):
    resp = await client.get("/weather")
    assert resp.status_code == 422


async def test_weather_empty_city(client, mock_http_client):
    resp = await client.get("/weather", params={"city": ""})
    assert resp.status_code == 422
