from unittest.mock import AsyncMock

import httpx

from src.joke.service import get_joke


async def test_get_joke_single():
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    mock_client.get.return_value = httpx.Response(
        200,
        json={"type": "single", "category": "Programming", "joke": "A bug walks into a bar."},
        request=httpx.Request("GET", "https://v2.jokeapi.dev/joke/Any"),
    )

    result = await get_joke(mock_client)
    assert result == {"category": "Programming", "joke": "A bug walks into a bar."}


async def test_get_joke_twopart():
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    mock_client.get.return_value = httpx.Response(
        200,
        json={
            "type": "twopart",
            "category": "Dark",
            "setup": "What's the deal?",
            "delivery": "No deal.",
        },
        request=httpx.Request("GET", "https://v2.jokeapi.dev/joke/Any"),
    )

    result = await get_joke(mock_client)
    assert result == {
        "category": "Dark",
        "setup": "What's the deal?",
        "delivery": "No deal.",
    }
