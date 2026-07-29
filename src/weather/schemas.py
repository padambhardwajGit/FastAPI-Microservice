from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    description: str
    humidity: int
    wind_speed: float
