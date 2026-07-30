async def test_root_not_found(client):
    resp = await client.get("/")
    assert resp.status_code == 404
