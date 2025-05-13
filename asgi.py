"""
Weather server module
"""
import httpx
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openapi_url: str
    weatherapi_key: str
    weatherapi_url: str = "http://api.weatherapi.com/v1/current.json"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI(
    openapi_url=settings.openapi_url,  # disable API doc
)


@app.get("/")
async def read_root():
    return {"service_status": "OK"}


@app.get("/weather/{city_id}")
async def read_item(city_id: str = "Dhaka"):
    async with httpx.AsyncClient() as cli:
        response: httpx.Response = await cli.get(settings.weatherapi_url, params={
            "key": settings.weatherapi_key,
            "q": city_id,
            "lang": "bn",
        })

        response.raise_for_status()

        if response.status_code == 200:
            return response.json()
