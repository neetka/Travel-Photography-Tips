# location_service.py
import requests
from config import API_KEYS

def find_photogenic_spots(location, radius=5000):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,  # Should be in 'lat,lng' format
        'radius': radius,
        'keyword': 'photography spot scenic viewpoint',
        'key': API_KEYS['google_maps']
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        spots = []
        for item in data['results']:
            spots.append({
                'name': item['name'],
                'location': item['geometry']['location'],
                'rating': item.get('rating', 'N/A'),
                'photos': item.get('photos', [])
            })
        return spots
    except requests.exceptions.RequestException as e:
        print(f"Google Maps API error: {e}")
        return None