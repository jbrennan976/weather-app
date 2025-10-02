from fastapi import FastAPI
from config import WEATHER_API_KEY
import requests
import math

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={WEATHER_API_KEY}")
    data = response.json()
    res = {
        "location": city,
        "forcast": data["weather"][0]["description"],
        "temp": math.ceil(data["main"]["temp"]),
        "time": data["dt"]
    }
    return res
