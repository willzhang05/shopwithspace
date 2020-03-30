import requests
import json
import math

TOMTOM_API_KEY = "sADNyfxrS8ipzYVjHOllyXsYsggGp7Ag"
TOMTOM_BASE_URL = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point="
# style=absolute, zoom = 10, format = json
# parameters latitude, longitude is a coordinate close to the road segment calculated using EPSG4326 projection


# def get_region_speed(latitude, longitude):
#     # 1 degree latitude = 69 miles, 1 degree longitude = 54.6 miles
#     # s = 0
#     # x = radius/54.6
#     # y = radius/69
#     # for i in range(4):
#     #     theta = i*math.pi/2
#     #     for j in range(1):
#     #         newlat = latitude+j/1*y*math.cos(theta)
#     #         newlng = longitude+j/1*x*math.sin(theta)
#     #         speeds = get_speeds(newlat, newlng)
#     #         s += speeds[0]/speeds[1]
#     # return s/(4*1)
#     speeds = get_speeds(latitude, longitude)
#     return speeds[0]/speeds[1]

# def get_flow_segment_data(latitude, longitude):
#     url = TOMTOM_BASE_URL + str(latitude) + "%2C" + \
#         str(longitude) + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     del data["-xmlns"]
#     del data["-version"]
#     del data["currentTravelTime"]
#     del data["freeFlowTravelTime"]
#     del data["coordinates"]
#     return data


def get_speeds(latitude, longitude):
    url = TOMTOM_BASE_URL + str(latitude) + "%2C" + \
        str(longitude) + "&unit=MPH&key=" + TOMTOM_API_KEY
    r = requests.get(url)
    data = r.json()
    # print(data)
    if "error" in data:
        return (4., 8.)  # default ratio to 3
    return (float(data["flowSegmentData"]["currentSpeed"]), float(data["flowSegmentData"]["freeFlowSpeed"]))


# def get_current_speed(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + \
#         longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["currentSpeed"]


# def get_free_flow_speed(latitude, longitude):
#     url = TOMTOM_BASE_URL + latitude + "%2C" + \
#         longitude + "&unit=MPH&key=" + TOMTOM_API_KEY
#     r = requests.get(url)
#     data = json.loads(r.json())
#     return data["flowSegmentData"]["freeFlowSpeed"]


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
