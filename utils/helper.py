from datetime import datetime, timezone, timedelta
import re

def validate_city_name(city: str) -> bool | str:
    city = city.strip().lower()

    if len(city) < 1 or len(city) > 168:
        return False
    
    match = re.search(r'^[a-z\s-]+$', city)
    if match:
        return city
    else:
        return False


def unix_to_local(dt, offset):
    utc_time = datetime.fromtimestamp(dt, tz=timezone.utc)
    local_time = utc_time + timedelta(seconds=offset)

    if local_time.second >= 30:
        local_time = local_time + timedelta(minutes=1)
    
    local_time = local_time.strftime("%I:%M %p").lstrip("0")

    return local_time


def parse_response(data):
    city_name = data["name"]
    country = data["sys"]["country"]
    location = f"{city_name}, {country}"
    time = unix_to_local(data["dt"], data["timezone"])
    temp = round(data["main"]["temp"])
    forecast = data["weather"][0]["description"].capitalize()
    icon_id = data["weather"][0]["icon"]

    res = {
        "location": location,
        "time": time,
        "temp": temp,
        "forecast": forecast,
        "icon-id": icon_id
    }
    
    return res