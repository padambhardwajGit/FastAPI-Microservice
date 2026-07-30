from unittest.mock import AsyncMock, patch

from src.summary.service import summarize


async def test_summarize_returns_content():
    mock_message = AsyncMock(content="This is the summary.")
    mock_choice = AsyncMock(message=mock_message)
    mock_response = AsyncMock(choices=[mock_choice])

    with patch("src.summary.service.groq_client") as mock_groq:
        mock_groq.chat.completions.create = AsyncMock(return_value=mock_response)
        result = await summarize("A long text that needs summarizing.")

    assert result == "This is the summary."
