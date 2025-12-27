from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.config import WEATHER_API_KEY, API_BASE_URL
from utils.helper import parse_response, validate_city_name
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/config")
async def get_config():
    return {"API_BASE_URL": API_BASE_URL}


@app.get("/weather")
async def get_weather(city: str):
    city = validate_city_name(city)
    if city is False:
        raise HTTPException(status_code=400, detail="Invalid city name")
    
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

    try:
        result = parse_response(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error parsing weather API response")
    
    return result
