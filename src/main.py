from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from src.config import AppConfig
from src.exceptions import register_exception_handlers
from src.joke.router import router as joke_router
from src.weather.router import router as weather_router

app_settings = AppConfig()

SHOW_DOCS_IN = {"local", "staging"}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.http_client = httpx.AsyncClient(timeout=10.0)
    yield
    await app.state.http_client.aclose()


app_kwargs: dict = {"title": "FastAPI Microservice", "lifespan": lifespan}
if app_settings.ENVIRONMENT not in SHOW_DOCS_IN:
    app_kwargs["openapi_url"] = None

app = FastAPI(**app_kwargs)

register_exception_handlers(app)

app.include_router(weather_router)
app.include_router(joke_router)
