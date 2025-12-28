from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.config import WEATHER_API_KEY
from utils.helper import parse_response, validate_city_name
import requests, time

START_TIME = time.time()

app = FastAPI()

origins = [
    "https://jbweather-appv1.netlify.app",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def get_health():
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"q": "London", "units": "imperial", "appid": WEATHER_API_KEY}, timeout=3)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail = "Server error")


    return JSONResponse(
        status_code=200, 
        content={"status": "ok",
                 "uptime": str(int(time.time() - START_TIME))+ " seconds"}
        )

@app.get("/weather")
async def get_weather(city: str):
    city = validate_city_name(city)
    if city is False:
        raise HTTPException(status_code=400, detail="Invalid city name")
    
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"q": city, "units": "imperial", "appid": WEATHER_API_KEY}, timeout=5)
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

    try:
        result = parse_response(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error parsing weather API response")
    
    return result
