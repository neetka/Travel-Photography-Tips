# weather_service.py
import requests
from config import API_KEYS

def get_weather_data(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': API_KEYS['openweathermap'],
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract relevant weather information
        weather_info = {
            'temperature': data['main']['temp'],
            'conditions': data['weather'][0]['main'],
            'humidity': data['main']['humidity'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            'clouds': data['clouds']['all']
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        print(f"Weather API error: {e}")
        return None