import base64
import googlemaps
import populartimes
import tomtom as tt

GMAPS_API_KEY = "AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q"
GMAPS_CLIENT = googlemaps.Client(key=GMAPS_API_KEY)


def get_nearby_places(latitude, longitude, radius, types=['grocery_or_supermarket']):
    try:
        places = GMAPS_CLIENT.places_nearby(
            location=(latitude, longitude), radius=radius, type=types)  # open_now=True
        locations = list()
        for p in places['results']:
            data = dict()
            data['id'] = p['id']
            data['name'] = p['name']
            data['place_id'] = p['place_id']
            coords = p['geometry']['location']
            data['location'] = coords

            # factors to consider: average relative speed in a region, what else
            current_speed, free_flow_speed = tt.get_speeds(
                coords['lat'], coords['lng'])
            data['current_speed'] = current_speed
            data['free_flow_speed'] = free_flow_speed

            data['popular'] = get_place_popularity_info(p['place_id'])

            if "current_popularity" in data['popular']:
                data['safety'] = sum(
                    current_speed/free_flow_speed*4+1, (100-data['popular'])/100*4+1)/2
            else:
                data['safety'] = current_speed/free_flow_speed*4+1

            data['details'] = get_place_details(p['place_id'])
            if 'photo_ref' in data['details']:
                data['photo'] = get_place_photo(data['details']['photo_ref'])
            locations.append(data)
        return locations
    except googlemaps.exceptions.ApiError:
        return {'error': 'INVALID_REQUEST'}


def get_place_details(place_id, fields=['photo', 'website', 'formatted_address', 'icon', 'formatted_phone_number']):
    try:
        details = GMAPS_CLIENT.place(place_id, fields=fields)
        data = dict()
        if 'photos' in details['result']:
            data['photo_ref'] = details['result']['photos'][0]['photo_reference']
        if 'website' in details['result']:
            data['website'] = details['result']['website']
            data['icon'] = 'https://www.google.com/s2/favicons?domain=' + \
                data['website']
        if 'formatted_address' in details['result']:
            data['formatted_address'] = details['result']['formatted_address']
        if 'formatted_phone_number' in details['result']:
            data['formatted_phone_number'] = details['result']['formatted_phone_number']
        return data
    except googlemaps.exceptions.ApiError:
        return {'error': 'INVALID_REQUEST'}


def get_place_photo(photo_ref, max_height=200, max_width=200):
    try:
        # photo = GMAPS_CLIENT.places_photo(
        #     photo_ref, max_height=max_height, max_width=max_width)
        # buf = b''
        # for chunk in photo:
        #     if chunk:
        #         buf += chunk
        # encoded = base64.b64encode(buf)
        # return encoded
        url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth={}&maxheight{}&photoreference={}&key={}".format(
            max_width, max_height, photo_ref, GMAPS_API_KEY)
        return url
    except googlemaps.exceptions.ApiError:
        return {'error': 'INVALID_REQUEST'}


def get_place_popularity_info(place_id):
    try:
        data = populartimes.get_id(GMAPS_API_KEY, place_id)
        info = dict()
        if 'time_spent' in data:
            info['time_wait'] = data['time_spent'][0]
            info['time_spent'] = data['time_spent'][1]
        if "current_popularity" in data:
            info['current_popularity'] = data['current_popularity']  # 0 - 100\
        if 'populartimes' in data:
            info['populartimes'] = data['populartimes']
        return info
    except populartimes.crawler.PopulartimesException:
        return {'error': 'INVALID_REQUEST'}
