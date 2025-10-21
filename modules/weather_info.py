import requests
from modules.talk import talk

def get_current_city():
    """Get current city using IP geolocation."""
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("city")
    except requests.RequestException as e:
        print("Error fetching location:", e)
        return None


def get_weather(city: str = None):
    """Fetch weather information for the given city or current city."""
    if not city:
        city = get_current_city()
        if not city:
            talk("Sorry, I couldn’t detect your city.")
            return "Unable to determine current city."

    try:
        url = f"https://wttr.in/{city}?format=%C+%t+%w"
        response = requests.get(url, timeout=6)
        response.raise_for_status()
        weather_text = response.text.strip()
        talk(f"The weather in {city} is {weather_text}.")
        return weather_text
    except requests.RequestException as e:
        print("Error fetching the weather:", e)
        talk(f"Sorry, I couldn’t fetch the weather for {city}.")
        return f"Unable to get weather for {city}."
