# FastAPI Microservice

A lightweight FastAPI application that aggregates three services: jokes, weather, and AI-powered text summarization.

## Setup

**Python 3.13+** required.

```bash
pip install -e .
```

Create a `.env` file in the project root:

```
ENVIRONMENT=local
APP_API_KEY=your-secret-api-key
WEATHER_API_KEY=your-openweather-api-key
SUMMARY_GROQ_API_KEY=your-groq-api-key
```

## Running

```bash
uvicorn src.main:app --reload
```

API docs available at `http://localhost:8000/docs` (local/staging only).

## Endpoints

### `GET /joke`

Returns a random joke from [JokeAPI](https://v2.jokeapi.dev/).

### `GET /weather?city={city_name}`

Returns current weather for a city using the [OpenWeather API](https://openweathermap.org/api). Requires `WEATHER_API_KEY`.

### `POST /summary`

Summarizes text using Groq's LLM API. Requires `X-API-Key` header matching `APP_API_KEY`.

**Request body:**
```json
{ "text": "Your text here (up to 10,000 characters)" }
```
