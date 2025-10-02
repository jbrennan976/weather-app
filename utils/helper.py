from datetime import datetime, timezone, timedelta

def unix_to_local(dt, offset):
    utc_time = datetime.fromtimestamp(dt, tz=timezone.utc)
    local_time = utc_time + timedelta(seconds=offset)

    if local_time.second >= 30:
        local_time = local_time + timedelta(minutes=1)
    
    local_time = local_time.strftime("%I:%M %p").lstrip("0")

    return local_time
