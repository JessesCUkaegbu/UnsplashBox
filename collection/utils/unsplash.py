import requests
from django.conf import settings

UNSPLASH_BASE_URL = "https://api.unsplash.com"


def search_unsplash(query, per_page=10, page=1):
    url = f"{UNSPLASH_BASE_URL}/search/photos"
    params = {
        "query": query,
        "per_page": per_page,
        "page": page,
        "client_id": settings.UNSPLASH_ACCESS_KEY,  # Access key
    }
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else {}


# Fetch image details from Unsplash API
def get_unsplash_image_detail(image_id):
    url = f"{UNSPLASH_BASE_URL}/photos/{image_id}"
    params = {
        "client_id": settings.UNSPLASH_ACCESS_KEY,
    }
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None
