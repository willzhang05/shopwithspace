import time
from flask import Flask
from flask import request
import tomtom as tt
import places

app = Flask(__name__)
api_key = "sADNyfxrS8ipzYVjHOllyXsYsggGp7Ag"


@app.route('/nearby')
def get_nearby():
    lat = request.args.get('latitude')
    lng = request.args.get('longitude')
    rad = request.args.get('radius')
    return {'stores': places.get_nearby_places(lat, lng, rad)}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/regionSpeed')
def getRegionSpeed():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    # 1.5 mile radius
    return {'regionSpeed': tt.getRegionSpeed(latitude, longitude, 1.5)}


@app.route('/flowSegmentData')
def getFlowSegmentData():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    # data as a dictionary includes frc (road classification), currentSpeed, freeFlowSpeed, confidence, and roadClosure
    return {'flowSegmentData': tt.getFlowSegmentData(latitude, longitude)}


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
