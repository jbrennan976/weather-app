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
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={WEATHER_API_KEY}", timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError:

    except requests.exceptions.RequestException:
        raise ()


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

    #Error codes:
    # - 404 for city name not found
    # - 401 for missing or incorrect API key
    # - 400 for issue w query string
