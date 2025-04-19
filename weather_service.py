import requests
from config import API_KEYS
from datetime import datetime

def get_weather_data(location):
    """Get weather data from OpenWeatherMap API with fallback defaults"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': API_KEYS['openweathermap'],
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return {
            'temperature': data['main']['temp'],
            'conditions': data['weather'][0]['main'],
            'humidity': data['main']['humidity'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            'clouds': data['clouds']['all']
        }
    except Exception as e:
        print(f"Weather API error: {e}")
        # Return sensible defaults if API fails
        return {
            'temperature': 20,
            'conditions': 'Clear',
            'humidity': 50,
            'sunrise': datetime.now().timestamp() - 3600,
            'sunset': datetime.now().timestamp() + 3600,
            'clouds': 20
        }

def generate_weather_tips(weather):
    """Generate exactly 5 photography tips based on weather conditions"""
    tips = []
    conditions = weather['conditions'].lower()
    
    # Condition-specific tips
    if 'clear' in conditions:
        tips.append("Clear skies perfect for landscape and astrophotography")
    elif 'rain' in conditions:
        tips.append("Rain creates beautiful reflections - look for puddles!")
    elif 'cloud' in conditions:
        tips.append("Cloudy weather provides soft, even lighting for portraits")
    
    # Time-based tips
    now = datetime.now().timestamp()
    if abs(now - weather['sunrise']) < 3600:
        tips.append("Golden hour at sunrise - warm, directional light perfect for landscapes")
    elif abs(now - weather['sunset']) < 3600:
        tips.append("Sunset golden hour - capture vibrant colors and long shadows")
    
    # Temperature-based tips
    if weather['temperature'] < 10:
        tips.append("Cold weather: Keep batteries warm and watch for condensation")
    elif weather['temperature'] > 30:
        tips.append("Hot weather: Shoot in RAW to recover highlights from harsh sun")
    
    # Always include these general photography tips
    general_tips = [
        "Use the rule of thirds for more compelling compositions",
        "Look for leading lines to draw viewers into your image",
        "Include human elements for scale and storytelling",
        "Try different perspectives - get low or find a high vantage point",
        "Capture details that tell the story of the place"
    ]
    
    # Combine and return exactly 5 tips
    return (tips + general_tips)[:5]