from fastapi import APIRouter

from src.summary.dependencies import ApiKeyDep
from src.summary.schemas import SummaryRequest, SummaryResponse
from src.summary.service import summarize

router = APIRouter(tags=["summary"])


@router.post(
    "/summary",
    response_model=SummaryResponse,
    summary="Summarize text",
    description="Generate an LLM-powered summary of the provided text. Requires API key auth.",
)
async def summary(_api_key: ApiKeyDep, payload: SummaryRequest) -> dict:
    result = await summarize(payload.text)
    return {"summary": result}
