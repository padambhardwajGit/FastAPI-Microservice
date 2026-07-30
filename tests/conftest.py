import os

os.environ.setdefault("APP_API_KEY", "test-api-key")
os.environ.setdefault("WEATHER_API_KEY", "fake-weather-key")
os.environ.setdefault("SUMMARY_GROQ_API_KEY", "fake-groq-key")

from unittest.mock import AsyncMock

import httpx
import pytest
from httpx import ASGITransport, AsyncClient

from src.dependencies import get_http_client
from src.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def mock_http_client():
    mock = AsyncMock(spec=httpx.AsyncClient)
    app.dependency_overrides[get_http_client] = lambda: mock
    yield mock
    app.dependency_overrides.pop(get_http_client, None)
