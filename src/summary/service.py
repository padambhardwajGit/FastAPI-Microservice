from groq import AsyncGroq

from src.summary.config import SummaryConfig

settings = SummaryConfig()

groq_client = AsyncGroq(api_key=settings.GROQ_API_KEY)


async def summarize(text: str) -> str:
    response = await groq_client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {"role": "system", "content": "Summarize the following text concisely. The summary should be clear, accurate, and capture the main points of the text. The final result should not exceed 2 paragraphs."},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content or ""
