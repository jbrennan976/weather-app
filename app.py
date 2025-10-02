from fastapi import FastAPI
from utils.config import WEATHER_API_KEY
from utils.helper import unix_to_local
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

    time = unix_to_local(data["dt"], data["timezone"])
    forcast = data["weather"][0]["description"]
    temp = math.ceil(data["main"]["temp"])

    res = {
        "location": city,
        "forcast": forcast,
        "temp": temp,
        "time": time
    }
    
    return res
