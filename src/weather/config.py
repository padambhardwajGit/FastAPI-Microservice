from pydantic_settings import BaseSettings, SettingsConfigDict


class WeatherConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="WEATHER_", env_file=".env", extra="ignore")

    API_KEY: str
