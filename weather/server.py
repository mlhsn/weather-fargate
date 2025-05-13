"""
Weather server module
"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"service_status": "OK"}


@app.get("/weather/{city_id}")
async def read_item(city_id: str = "Dhaka"):
    return {"city_id": city_id}