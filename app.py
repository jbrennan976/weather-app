from fastapi import FastAPI
from config import WEATHER_API_KEY
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}")
    data = response.json()
    return data["weather"]
    
