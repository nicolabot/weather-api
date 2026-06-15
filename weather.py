import random
from datetime import datetime, timedelta

CITIES = {
    "stockholm": {"lat": 59.33, "lon": 18.07},
    "oslo": {"lat": 59.91, "lon": 10.75},
    "helsinki": {"lat": 60.17, "lon": 24.94},
    "copenhagen": {"lat": 55.68, "lon": 12.57},
}

def get_weather(city):
    city = city.lower()
    if city not in CITIES:
        return None
    return {
        "city": city,
        "temperature": round(random.uniform(-5, 25), 1),
        "humidity": random.randint(40, 90),
        "wind_speed": round(random.uniform(0, 20), 1),
        "timestamp": datetime.utcnow().isoformat(),
    }

def get_forecast(city, days=3):
    city = city.lower()
    if city not in CITIES:
        return {"error": "City not found", "forecast": []}
    forecast = []
    for i in range(days):
        date = datetime.utcnow() + timedelta(days=i + 1)
        forecast.append({
            "date": date.strftime("%Y-%m-%d"),
            "high": round(random.uniform(10, 28), 1),
            "low": round(random.uniform(-2, 15), 1),
            "condition": random.choice(["sunny", "cloudy", "rain", "snow"]),
        })
    return {"city": city, "forecast": forecast}
