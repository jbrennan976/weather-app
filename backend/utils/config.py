from dotenv import load_dotenv
import os

load_dotenv(".env")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise RuntimeError("WEATHER_API_KEY is not set")

