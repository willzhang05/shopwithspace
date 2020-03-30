import time
from flask import Flask
from flask import request, render_template
import places
from pprint import pprint
from scrapers.inventory import get_walmarts
from zipcoder import get_zipcode
import tomtom as tt

app = Flask(__name__, static_folder="build/static", template_folder="build")
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


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
