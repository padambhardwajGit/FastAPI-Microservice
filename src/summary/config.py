from pydantic_settings import BaseSettings, SettingsConfigDict


class SummaryConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SUMMARY_", env_file=".env", extra="ignore")

    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.1-8b-instant"
