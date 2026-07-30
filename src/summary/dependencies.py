import secrets
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status

from src.config import AppConfig

app_settings = AppConfig()


async def verify_api_key(
    x_api_key: Annotated[str, Header(description="API key for authentication")],
) -> str:
    if not secrets.compare_digest(x_api_key, app_settings.APP_API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key.",
        )
    return x_api_key


ApiKeyDep = Annotated[str, Depends(verify_api_key)]
