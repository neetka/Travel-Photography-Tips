# tip_generator.py
from weather_service import get_weather_data
from location_service import find_photogenic_spots
from photo_inspiration_service import get_inspiration_photos
from datetime import datetime

def generate_tips(location, user_preferences):
    # Fetch data from all APIs
    weather = get_weather_data(location)
    spots = find_photogenic_spots(location)
    photos = get_inspiration_photos(f"{location} travel photography")
    
    # Generate tips based on weather
    weather_tips = []
    if weather:
        if weather['conditions'].lower() == 'clear':
            weather_tips.append("Perfect clear skies for landscape shots!")
        elif weather['conditions'].lower() == 'rain':
            weather_tips.append("Rain can create great reflections - look for puddles!")
        
        # Golden hour recommendation
        now = datetime.now().timestamp()
        if abs(now - weather['sunrise']) < 3600:
            weather_tips.append("Shooting during sunrise golden hour - perfect lighting!")
        elif abs(now - weather['sunset']) < 3600:
            weather_tips.append("Shooting during sunset golden hour - perfect lighting!")
    
    # Generate location tips
    location_tips = []
    if spots:
        top_spot = sorted(spots, key=lambda x: x['rating'], reverse=True)[0]
        location_tips.append(f"Top rated photogenic spot nearby: {top_spot['name']}")
    
    # Combine all tips
    all_tips = {
        'weather_tips': weather_tips,
        'location_tips': location_tips,
        'inspiration_photos': photos,
        'gear_recommendations': get_gear_recommendations(weather, user_preferences)
    }
    
    return all_tips

def get_gear_recommendations(weather, preferences):
    gear = []
    
    if weather and weather['conditions'].lower() in ['rain', 'snow']:
        gear.append("Weather protection for your camera")
    
    if preferences.get('tripod', False):
        gear.append("Tripod for long exposures")
    
    # Add more gear logic based on weather and preferences
    return gear