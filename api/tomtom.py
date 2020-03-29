import requests
import json
import math

TOMTOM_API_KEY = "sADNyfxrS8ipzYVjHOllyXsYsggGp7Ag"
TOMTOM_BASE_URL = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point="
# style=absolute, zoom = 10, format = json
# parameters latitude, longitude is a coordinate close to the road segment calculated using EPSG4326 projection


def get_region_speed(latitude, longitude, radius):
    # 1 degree latitude = 69 miles, 1 degree longitude = 54.6 miles
    sum = 0
    x = radius/54.6
    y = radius/69
    for i in range(16):
        theta = i*math.pi/8
        for j in range(4):
            newlat = latitude+j/4*y*math.cos(theta)
            newlng = longitude+j/4*x*math.sin(theta)
            sum += get_current_speed(newlat, newlng) / \
                get_free_flow_speed(newlat, newlng)
    return sum/(16*4)


def get_flow_segment_data(latitude, longitude):
    url = TOMTOM_BASE_URL + latitude + "%2C" + \
        longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
    r = requests.get(url)
    data = json.loads(r.json())
    del data["-xmlns"]
    del data["-version"]
    del data["currentTravelTime"]
    del data["freeFlowTravelTime"]
    del data["coordinates"]
    return data


def get_current_speed(latitude, longitude):
    url = TOMTOM_BASE_URL + latitude + "%2C" + \
        longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
    r = requests.get(url)
    data = json.loads(r.json())
    return data["flowSegmentData"]["currentSpeed"]


def get_free_flow_speed(latitude, longitude):
    url = TOMTOM_BASE_URL + latitude + "%2C" + \
        longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
    r = requests.get(url)
    data = json.loads(r.json())
    return data["flowSegmentData"]["freeFlowSpeed"]


# def getCurrentTravelTime(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["currentTravelTime"]


# def getFreeFlowTravelTime(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["freeFlowTravelTime"]


# def getConfidence(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["confidence"]


# def getRoadClosure(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["roadClosure"]
