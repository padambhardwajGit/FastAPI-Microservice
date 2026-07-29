from pydantic import BaseModel


class JokeResponse(BaseModel):
    category: str
    joke: str | None = None
    setup: str | None = None
    delivery: str | None = None
