import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")


def get_lat_lng(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{requests.utils.quote(place_name)}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1,
        "bbox": "-71.9,42.0,-70.5,42.7",
    }
    data = requests.get(url, params=params).json()
    coords = data["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]


def get_nearest_stops(lat, lng):
    params = {
        "api_key": MBTA_API_KEY,
        "filter[latitude]": lat,
        "filter[longitude]": lng,
        "filter[route_type]": "0,1,2",
        "sort": "distance",
        "page[limit]": 10,
    }
    data = requests.get("https://api-v3.mbta.com/stops", params=params).json()
    stops = []
    seen = set()
    for stop in data["data"]:
        attrs = stop["attributes"]
        name = attrs["name"]
        if name not in seen:
            seen.add(name)
            stops.append({
                "name": name,
                "wheelchair": attrs["wheelchair_boarding"] == 1,
                "lat": attrs["latitude"],
                "lng": attrs["longitude"],
            })
        if len(stops) == 3:
            break
    return stops


def find_stops_near(place_name):
    lat, lng = get_lat_lng(place_name)
    stops = get_nearest_stops(lat, lng)
    return stops, lat, lng


if __name__ == "__main__":
    stops, lat, lng = find_stops_near("Fenway Park")
    print(f"Coordinates: ({lat}, {lng})\n")
    for i, stop in enumerate(stops, 1):
        accessible = "Yes" if stop["wheelchair"] else "No"
        print(f"{i}. {stop['name']} — Wheelchair accessible: {accessible}")