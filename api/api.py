import time
from flask import Flask
from flask import request, render_template
import places
from pprint import pprint
from scrapers.inventory import get_walmarts
from zipcoder import get_zipcode
import tomtom as tt

app = Flask(__name__, static_folder='build/static', template_folder="build")
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/nearby')
def get_nearby():
    lat = float(request.args.get('latitude'))
    lng = float(request.args.get('longitude'))
    rad = float(request.args.get('radius'))
    nearby = places.get_nearby_places(lat, lng, rad)
    # pprint(nearby)
    if "error" in nearby:
        return {'stores': []}
    else:
        return {'stores': nearby}


@app.route('/search')
def search_stores():
    lat = float(request.args.get('latitude'))
    lng = float(request.args.get('longitude'))
    item_name = str(request.args.get('item'))
    zipcode = get_zipcode(lat, lng)
    stores = get_walmarts(item_name, zipcode)
    locations = list()
    for store in stores:
        info = {}
        address = store['address'] + " " + \
            store['city'] + " " + store['zipcode']
        place = places.get_place_id(address)
        if 'error' in place:
            continue
        current_speed, free_flow_speed = tt.get_speeds(
            place['lat'], place['lng'])
        info['current_speed'] = current_speed
        info['free_flow_speed'] = free_flow_speed
        details = dict()
        info['id'] = place['place_id']
        info['place_id'] = place['place_id']
        info['name'] = store['storename']
        info['location'] = {
            'lat': place['lat'],
            'lng': place['lng']
        }
        info['popular'] = places.get_place_popularity_info(place['place_id'])

        # if "current_popularity" in data['popular']:
        #     data['safety'] = sum(
        #         current_speed/free_flow_speed*4+1, (100-data['popular'])/100*4+1)/2
        # else:
        #     data['safety'] = current_speed/free_flow_speed*4+1

        info['details'] = places.get_place_details(place['place_id'])
        info['details']["website"] = "https://www.walmart.com/"
        info['details']['icon'] = 'https://www.google.com/s2/favicons?domain=www.walmart.com'
        if 'photo_ref' in info['details']:
            info['photo'] = places.get_place_photo(
                info['details']['photo_ref'])
        locations.append(info)
    return {'stores': locations}


# {
#     current_speed: 26.0,
#     details: {
#         formatted_address: '8723 Cooper Rd D, Alexandria, VA 22309, USA',
#         formatted_phone_number: '(703) 799-8886',
#         website: 'www.google.com',
#         icon: 'https://www.google.com/s2/favicons?domain=www.walmart.com',
#         photo_ref:
#         'CmRaAAAADBmo1PSaRpIgW1SDA5ukWtI5DF1lhgDAI45BuhQ9ucBq9TS3ilFuYLzfTKxVTYk9gWpGXsAiYWuNCTjjeH6P7YXP0-qnz2glUxlG81l5PEGF7ja8Cwld4XKWZONmbAxxEhAG7HWN8XPj-hunllFrtzRDGhROOaDgR6qBw_0WbnhGiZsOgsQotA'
#     },
#     free_flow_speed: 32.0,
#     id: '8cbaf37e7f2468013bc2cfe365cb9cc2d804a00f',
#         location: {lat: 38.7202608, lng: -77.1241144},
#     name: 'AMIGOS DELI & SUPERMARKET',
#     photo:
#     'https://maps.googleapis.com/maps/api/place/photo?maxwidth=500&maxheight500&photoreference=CmRaAAAADBmo1PSaRpIgW1SDA5ukWtI5DF1lhgDAI45BuhQ9ucBq9TS3ilFuYLzfTKxVTYk9gWpGXsAiYWuNCTjjeH6P7YXP0-qnz2glUxlG81l5PEGF7ja8Cwld4XKWZONmbAxxEhAG7HWN8XPj-hunllFrtzRDGhROOaDgR6qBw_0WbnhGiZsOgsQotA&key=AIzaSyCl3oN8un11v0d7DGCJ9QQYEh7nf93Vu0Q',
#     place_id: 'ChIJizz_1xKtt4kRDlHkZc0O_vs',
#     popular: {
#           current_popularity: 0.8,
#           populartimes: [
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       2,
#                       17,
#                       37,
#                       51,
#                       45,
#                       28,
#                       8,
#                       2,
#                       8,
#                       22,
#                       37,
#                       40,
#                       28,
#                       11,
#                       2,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Monday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       8,
#                       31,
#                       31,
#                       25,
#                       37,
#                       40,
#                       31,
#                       17,
#                       11,
#                       17,
#                       25,
#                       31,
#                       25,
#                       14,
#                       2,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Tuesday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       2,
#                       14,
#                       28,
#                       40,
#                       42,
#                       37,
#                       25,
#                       17,
#                       14,
#                       17,
#                       22,
#                       22,
#                       17,
#                       8,
#                       2,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Wednesday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       8,
#                       20,
#                       28,
#                       34,
#                       34,
#                       25,
#                       14,
#                       11,
#                       17,
#                       25,
#                       34,
#                       37,
#                       31,
#                       20,
#                       8,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Thursday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       2,
#                       62,
#                       51,
#                       5,
#                       37,
#                       51,
#                       17,
#                       2,
#                       2,
#                       14,
#                       28,
#                       34,
#                       28,
#                       14,
#                       2,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Friday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       2,
#                       25,
#                       65,
#                       85,
#                       71,
#                       42,
#                       34,
#                       34,
#                       37,
#                       37,
#                       34,
#                       25,
#                       17,
#                       8,
#                       2,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Saturday'
#               },
#               {
#                   data: [
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       0,
#                       22,
#                       74,
#                       100,
#                       68,
#                       31,
#                       25,
#                       28,
#                       25,
#                       20,
#                       22,
#                       17,
#                       2,
#                       0,
#                       0,
#                       0,
#                       0
#                   ],
#                   name: 'Sunday'
#               }
#           ],
#             time_spent: 15,
#         time_wait: 15
#     },
#     safety: 4.25
# }
