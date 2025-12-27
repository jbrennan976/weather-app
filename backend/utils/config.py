from dotenv import load_dotenv
import os

load_dotenv(".env-dev")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

if not WEATHER_API_KEY:
    raise RuntimeError("WEATHER_API_KEY is not set")

if not API_BASE_URL:
    raise RuntimeError("API_BASE_URL is not set")
