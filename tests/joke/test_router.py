import httpx


async def test_joke_single(client, mock_http_client):
    mock_http_client.get.return_value = httpx.Response(
        200,
        json={"type": "single", "category": "Pun", "joke": "A funny joke"},
        request=httpx.Request("GET", "http://test/joke"),
    )
    resp = await client.get("/joke")
    assert resp.status_code == 200
    data = resp.json()
    assert data["category"] == "Pun"
    assert data["joke"] == "A funny joke"
    assert data["setup"] is None
    assert data["delivery"] is None


async def test_joke_twopart(client, mock_http_client):
    mock_http_client.get.return_value = httpx.Response(
        200,
        json={
            "type": "twopart",
            "category": "Misc",
            "setup": "Why?",
            "delivery": "Because.",
        },
        request=httpx.Request("GET", "http://test/joke"),
    )
    resp = await client.get("/joke")
    assert resp.status_code == 200
    data = resp.json()
    assert data["category"] == "Misc"
    assert data["setup"] == "Why?"
    assert data["delivery"] == "Because."
    assert data["joke"] is None
