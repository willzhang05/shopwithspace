import sys
import time
import json
import googlemaps
import populartimes
from pprint import pprint
from datetime import datetime
import base64

GMAPS_API_KEY = sys.argv[1]

GMAPS_CLIENT = googlemaps.Client(key=GMAPS_API_KEY)

location = (38.85200277, -77.400724)


def get_nearby_places(latitude, longitude, radius, types=['grocery_or_supermarket']):
    try:
        places = GMAPS_CLIENT.places_nearby(
            location=(latitude, longitude), radius=radius, type=types, open_now=True)
        locations = list()
        for p in places['results']:
            data = dict()
            data['id'] = p['id']
            data['name'] = p['name']
            data['place_id'] = p['place_id']
            coords = p['geometry']['location']
            data['location'] = coords

            # factors to consider: average relative speed in a region, what else
            data['safety'] = tt.get_region_speed(
                coords['lat'], coords['lng'])*5/64
            locations.append(data)
        return locations
    except googlemaps.exceptions.ApiError:
        return {"error": "INVALID_REQUEST"}


def get_place_details(place_id, fields=['photo", "website']):
    try:
        details = GMAPS_CLIENT.place(place_id, fields=fields)
        data = dict()
        data['photo_ref'] = details['result']['photos'][0]['photo_reference']
        data['photo_attr'] = details['result']['photos'][0]['html_attributions']
        data['website'] = details['result']['website']
        return data
    except googlemaps.exceptions.ApiError:
        return {'error': 'INVALID_REQUEST'}


def get_place_photo(photo_ref, max_height=500, max_width=500):
    try:
        photo = GMAPS_CLIENT.places_photo(
            photo_ref, max_height=max_height, max_width=max_width)
        buf = b''
        for chunk in photo:
            if chunk:
                buf += chunk
        encoded = base64.b64encode(buf)
        return encoded
    except googlemaps.exceptions.ApiError:
        return {'error': 'INVALID_REQUEST'}


def get_place_popularity_info(place_id):
    try:
        data = populartimes.get_id(GMAPS_API_KEY, place_id)
        info = dict()
        info['time_wait'] = data['time_spent'][0]
        info['time_spent'] = data['time_spent'][1]
        if "current_popularity" in data:
            info['current_popularity'] = data['current_popularity']
        else:
            info['current_popularity'] = -1
        info['populartimes'] = data['populartimes']
        return info
    except populartimes.crawler.PopulartimesException:
        return {'error': 'INVALID_REQUEST'}


#result = getAvailableLocations(location[0], location[1], 2000)
#result = get_place_popularity_info("aChIJmw3Qq5ZFtokR110Yscnc6hA")
# result = get_place_details("ChIJmw3Qq5ZFtokR110Yscnc6hA")
# pprint(result)
# photo = get_place_photo(result["photo_ref"])
# print(encoded)
