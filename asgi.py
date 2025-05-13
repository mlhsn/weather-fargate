"""
Weather server module
"""
import icecream
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openapi_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
app = FastAPI(
    openapi_url=settings.openapi_url, # disable API doc
)


@app.get("/")
async def read_root():
    return {"service_status": "OK"}


@app.get("/weather/{city_id}")
async def read_item(city_id: str = "Dhaka"):
    return {"city_id": city_id}
