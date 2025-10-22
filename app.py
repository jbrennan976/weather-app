from fastapi import FastAPI, HTTPException
from utils.config import WEATHER_API_KEY
from utils.helper import unix_to_local
import requests
import math

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/weather")
async def get_weather(city: str):
    try:
    
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params={"q": city, "units": "imperial", "appid": WEATHER_API_KEY}, timeout=5)
        response.raise_for_status()
        data = response.json()


    except requests.exceptions.HTTPError as e:
        if e.response is not None:
            try:
                data = e.response.json()
            except ValueError:
                raise HTTPException(status_code=e.response.status_code, detail="Invalid response from weather API")
            
            raise HTTPException(status_code=int(data["cod"]), detail =data["message"])
    
    except requests.exceptions.ConnectionError as e:
        raise HTTPException(status_code=503, detail= "There was an error connecting with the weather API")

    except requests.exceptions.ReadTimeout as e:
        raise HTTPException(status_code=504, detail= "API request timeout")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail = "Internal server error")


    time = unix_to_local(data["dt"], data["timezone"])
    forcast = data["weather"][0]["description"]
    temp = math.ceil(data["main"]["temp"])

    res = {
        "location": city,
        "forecast": forcast,
        "temp": temp,
        "time": time
    }
    
    return res

    #Error codes:
    # - 404 for city name not found
    # - 401 for missing or incorrect API key
    # - 400 for issue w query string
