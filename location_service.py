# location_service.py
import requests
from config import API_KEYS

def find_photogenic_spots(location, radius=20000):
    """Find photogenic spots using Google Maps API"""
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    lat_lng = get_lat_lng(location)
    
    if not lat_lng:
        return None
    
    params = {
        'location': lat_lng,
        'radius': radius,
        'keyword': 'photography spot scenic viewpoint',
        'key': API_KEYS['google_maps']
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        spots = []
        for item in data.get('results', []):
            spots.append({
                'name': item['name'],
                'location': item['geometry']['location'],
                'rating': item.get('rating', 3.0),
                'types': item.get('types', [])
            })
        return spots
    except requests.exceptions.RequestException as e:
        print(f"Google Maps API error: {e}")
        return None

def get_lat_lng(location):
    """Convert location name to latitude/longitude coordinates"""
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': location,
        'key': API_KEYS['google_maps']
    }
    
    try:
        response = requests.get(geocode_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            loc = data['results'][0]['geometry']['location']
            return f"{loc['lat']},{loc['lng']}"
    except Exception as e:
        print(f"Geocoding error: {e}")
    
    return None