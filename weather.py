import requests

API_KEY="d8217c48b2a7593cc5aa5159dc108e5c"
def get_weather(city):
    """Fetch weather data for a given city"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        return None

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"].title(),
    }
    return weather








