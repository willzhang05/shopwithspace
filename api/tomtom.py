import requests
import json
import math

api_key = "sADNyfxrS8ipzYVjHOllyXsYsggGp7Ag"
base_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point="
# style=absolute, zoom = 10, format = json
# parameters latitude, longitude is a coordinate close to the road segment calculated using EPSG4326 projection


def getRegionSpeed(latitude, longitude, radius):
    # 1 degree latitude = 69 miles, 1 degree longitude = 54.6 miles
    sum = 0
    x = radius/54.6
    y = radius/69
    for i in range(16):
        theta = i*math.pi/8
        for j in range(4):
            sum += getCurrentSpeed(latitude+j/4*y*math.cos(theta),
                                   longitude+j/4*x*math.sin(theta))
    return sum/(16*4)


def getFlowSegmentData(latitude, longitude):
    url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
    r = requests.get(url)
    data = json.loads(r.json())
    del data["-xmlns"]
    del data["-version"]
    del data["currentTravelTime"]
    del data["freeFlowTravelTime"]
    del data["coordinates"]
    return data


def getCurrentSpeed(latitude, longitude):
    url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
    r = requests.get(url)
    data = json.loads(r.json())
    return data["flowSegmentData"]["currentSpeed"]


# def getFreeFlowSpeed(latitude, longitude):
#     url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["freeFlowSpeed"]


# def getCurrentTravelTime(latitude, longitude):
#     url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["currentTravelTime"]


# def getFreeFlowTravelTime(latitude, longitude):
#     url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["freeFlowTravelTime"]


# def getConfidence(latitude, longitude):
#     url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["confidence"]


# def getRoadClosure(latitude, longitude):
#     url = base_url + latitude + "%2C" + longitude + "&unit=MPH&key=" + api_key
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["roadClosure"]
