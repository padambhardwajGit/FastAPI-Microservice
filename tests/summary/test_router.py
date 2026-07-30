from unittest.mock import AsyncMock, patch

from src.main import app
from src.summary.dependencies import verify_api_key


async def test_summary_success(client):
    app.dependency_overrides[verify_api_key] = lambda: "test-api-key"
    try:
        with patch("src.summary.service.groq_client") as mock_groq:
            mock_choice = AsyncMock()
            mock_choice.choices = [AsyncMock(message=AsyncMock(content="Short summary."))]
            mock_groq.chat.completions.create = AsyncMock(return_value=mock_choice.choices[0])
            mock_groq.chat.completions.create.return_value = mock_choice

            resp = await client.post("/summary", json={"text": "Some long text to summarize."})
        assert resp.status_code == 200
        assert resp.json() == {"summary": "Short summary."}
    finally:
        app.dependency_overrides.pop(verify_api_key, None)


async def test_summary_missing_api_key(client):
    resp = await client.post("/summary", json={"text": "Hello world."})
    assert resp.status_code == 422


async def test_summary_wrong_api_key(client):
    resp = await client.post(
        "/summary",
        json={"text": "Hello world."},
        headers={"X-Api-Key": "wrong-key"},
    )
    assert resp.status_code == 401


async def test_summary_empty_text(client):
    app.dependency_overrides[verify_api_key] = lambda: "test-api-key"
    try:
        resp = await client.post("/summary", json={"text": ""})
        assert resp.status_code == 422
    finally:
        app.dependency_overrides.pop(verify_api_key, None)
