import googlemaps

API_KEY = "AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q"
GMAPS_CLIENT = googlemaps.Client(key=API_KEY)


def get_nearby_places(lat, lng, radius):
    raw = GMAPS_CLIENT.places_nearby(
        (lat, lng), radius, type='grocery_or_supermarket')
    places = []
    for place in raw['results']:
        temp = {
            'name': place['name'],
            'place': place['place_id'],
            'location': place['geometry']['location']
        }
        places.append(temp)
    return places
