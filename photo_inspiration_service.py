# photo_inspiration_service.py
import requests
from config import API_KEYS

def get_inspiration_photos(query, count=5):
    base_url = "https://api.unsplash.com/search/photos"
    headers = {
        'Authorization': f'Client-ID {API_KEYS["unsplash"]}'
    }
    params = {
        'query': query,
        'per_page': count
    }
    
    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        photos = []
        for item in data['results']:
            photos.append({
                'url': item['urls']['regular'],
                'description': item.get('description', ''),
                'photographer': item['user']['name']
            })
        return photos
    except requests.exceptions.RequestException as e:
        print(f"Unsplash API error: {e}")
        return None