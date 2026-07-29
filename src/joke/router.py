from fastapi import APIRouter

from src.dependencies import HttpClientDep
from src.joke.schemas import JokeResponse
from src.joke.service import get_joke

router = APIRouter(tags=["joke"])


@router.get(
    "/joke",
    response_model=JokeResponse,
    summary="Get a random joke",
    description="Fetch a random safe joke from JokeAPI.",
)
async def joke(client: HttpClientDep) -> dict:
    return await get_joke(client)
