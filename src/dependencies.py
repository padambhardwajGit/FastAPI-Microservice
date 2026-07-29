from typing import Annotated

from fastapi import Depends, Request
from httpx import AsyncClient


def get_http_client(request: Request) -> AsyncClient:
    return request.app.state.http_client


HttpClientDep = Annotated[AsyncClient, Depends(get_http_client)]
