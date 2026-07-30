import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from httpx import HTTPStatusError
from groq import APIError

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPStatusError)
    async def httpx_error_handler(request: Request, exc: HTTPStatusError) -> JSONResponse:
        logger.error("Upstream HTTP error: %s %s", exc.response.status_code, exc.request.url)
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={"detail": "Upstream service returned an error."},
        )

    @app.exception_handler(APIError)
    async def groq_error_handler(request: Request, exc: APIError) -> JSONResponse:
        logger.error("Groq API error: %s", exc.message)
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={"detail": "AI service returned an error."},
        )
