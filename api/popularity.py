import sys
import time
import json
import googlemaps
import populartimes
from pprint import pprint
from datetime import datetime


API_KEY = sys.argv[1]

gmaps = googlemaps.Client(key=API_KEY)

location = (38.85200277,-77.400724)

API_KEY = sys.argv[1]

def getAvailableLocations(latitude, longitude, radius, types=["grocery_or_supermarket"]):
    places = gmaps.places_nearby(location=location, radius=radius, type=types, open_now=True)
    locations = list()
    for p in places["results"]:
        data = dict()
        data["id"] = p["id"]
        data["name"] = p["name"]
        data["place_id"] = p["place_id"]
        data["address"] = p["vicinity"]
        locations.append(data)
    return locations

def getLocationPopularityInfo(place_id):
    data = populartimes.get_id(API_KEY, place_id)
    info = dict()
    info["time_wait"] = data["time_spent"][0]
    info["time_spent"] = data["time_spent"][1]
    info["current_popularity"] = data["current_popularity"]
    info["populartimes"] = data["populartimes"]
    return info
    




#result = getAvailableLocations(location[0], location[1], 1000)
result = getLocationPopularityInfo("ChIJmw3Qq5ZFtokR110Yscnc6hA")
pprint(result)
