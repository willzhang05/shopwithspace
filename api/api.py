import time
from flask import Flask
from flask import request
import places
from pprint import pprint
from .scrapers.inventory import get_walmarts
from zipcoder import get_zipcode

app = Flask(__name__)


@app.route('/nearby')
def get_nearby():
    lat = float(request.args.get('latitude'))
    lng = float(request.args.get('longitude'))
    rad = float(request.args.get('radius'))
    nearby = places.get_nearby_places(lat, lng, rad)
    pprint(nearby)
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
    for store in stores:

        # @app.route('/stores')
        # def get_nearby():
        #     lat = request.args.get('latitude')
        #     lng = request.args.get('longitude')
        #     rad = request.args.get('radius')
        #     return {'stores': places.get_nearby_places(lat, lng, rad)}

        # @app.route('/region_speed')
        # def get_region_speed():
        #     lat = request.args.get('latitude')
        #     lng = request.args.get('longitude')
        #     # 0.75 mile radius
        #     return {'region_speed': tt.get_region_speed(lat, lng, 0.75)}

        # @app.route('/flow_segment_data')
        # def get_flow_segment_data():
        #     lat = request.args.get('latitude')
        #     lng = request.args.get('longitude')
        #     # data as a dictionary includes frc (road classification), currentSpeed, freeFlowSpeed, confidence, and roadClosure
        #     return {'flow_segment_data': tt.get_flow_segment_data(lat, lng)}

        # @app.route('/currentSpeed')
        # # parameters latitude, longitude is a coordinate close to the road segment calculated using EPSG4326 projection
        # def getCurrentSpeed():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'currentSpeed': tt.getCurrentSpeed(latitude, longitude)}

        # @app.route('/freeFlowSpeed')
        # def getFreeFlowSpeed():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'freeFlowSpeed': tt.getFreeFlowSpeed(latitude, longitude)}

        # @app.route('/currentTravelTime')
        # def getCurrentTravelTime():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'currentTravelTime': tt.getCurrentTravelTime(latitude, longitude)}

        # @app.route('/freeFlowTravelTime')
        # def getFreeFlowTravelTime():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'freeFlowTravelTime': tt.getFreeFlowTravelTime(latitude, longitude)}

        # @app.route('/confidence')
        # def getConfidence():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'confidence': tt.getConfidence(latitude, longitude)}
        # @app.route('/roadClosure')
        # def getRoadClosure():
        #     latitude = request.args.get('latitude')
        #     longitude = request.args.get('longitude')
        #     return {'roadClosure': tt.getRoadClosure(latitude, longitude)}
