from weather_service import get_weather_data, generate_weather_tips
from location_service import find_photogenic_spots
from photo_inspiration_service import get_inspiration_photos
from datetime import datetime

def get_gear_recommendations(weather, preferences):
    """Generate at least 3 gear recommendations based on conditions and preferences"""
    gear = []
    
    # Weather-based gear
    if weather['temperature'] < 10:
        gear.append("Insulated camera gloves")
    if weather['temperature'] > 30:
        gear.append("Lens hood to prevent flare")
    if 'rain' in weather['conditions'].lower():
        gear.append("Rain cover for your camera")
    
    # Time-based gear
    now = datetime.now().timestamp()
    if abs(now - weather['sunrise']) < 7200 or abs(now - weather['sunset']) < 7200:
        gear.append("Tripod for golden hour photography")
    
    # Preference-based gear
    if preferences.get('tripod', False):
        gear.append("Compact travel tripod")
    if preferences.get('filters', False):
        gear.append("ND filter for long exposures")
    
    # Essential gear that always applies
    essential_gear = [
        "Spare memory cards",
        "Extra batteries",
        "Lens cleaning kit",
        "Polarizing filter",
        "Comfortable camera strap"
    ]
    
    return (gear + essential_gear)[:5]

def generate_location_tips(location, spots=None):
    """Generate exactly 5 location recommendations"""
    city = location.split(',')[0].strip().lower()
    
    # Specific recommendations for known locations
    if 'punjab' in city:
        return [
            "Golden Temple, Amritsar - Stunning architecture and reflections",
            "Wagah Border - Vibrant flag ceremony between India and Pakistan",
            "Jallianwala Bagh - Historical memorial with poignant atmosphere",
            "Anandpur Sahib - Spiritual center with beautiful gurudwaras",
            "Ranjit Sagar Dam - Scenic lake views and surrounding hills"
        ]
    
    # Use API results if available
    if spots:
        sorted_spots = sorted(spots, key=lambda x: x.get('rating', 0), reverse=True)
        return [f"📍 {spot['name']} (Rating: {spot.get('rating', '?')}/5)" 
               for spot in sorted_spots[:5]]
    
    # Generic fallback recommendations
    return [
        f"Explore {city}'s main square for street photography",
        f"Visit {city}'s historic district for architectural shots",
        f"Find {city}'s highest viewpoint for panoramas",
        f"Photograph daily life at local markets",
        f"Capture the city's most famous landmark at different times of day"
    ]

def generate_tips(location, preferences):
    """Main function that coordinates all tip generation"""
    weather = get_weather_data(location)
    spots = find_photogenic_spots(location)
    photos = get_inspiration_photos(f"{location} travel photography")
    
    return {
        'weather_tips': generate_weather_tips(weather),
        'location_tips': generate_location_tips(location, spots),
        'inspiration_photos': photos[:8] if photos else [],
        'gear_recommendations': get_gear_recommendations(weather, preferences)
    }