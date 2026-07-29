from httpx import AsyncClient

JOKEAPI_URL = "https://v2.jokeapi.dev/joke/Any"


async def get_joke(client: AsyncClient) -> dict:
    resp = await client.get(JOKEAPI_URL, params={"safe-mode":"true"})
    resp.raise_for_status()
    data = resp.json()

    result: dict = {"category": data["category"]}
    if data["type"] == "single":
        result["joke"] = data["joke"]
    else:
        result["setup"] = data["setup"]
        result["delivery"] = data["delivery"]
    return result
