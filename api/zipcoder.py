import requests


def get_zipcode(lat, lng):
    url = "https://us1.locationiq.com/v1/reverse.php"
    data = {"key": "aecce98e3c7f42",
            "lat": lat,
            "lon": lng,
            "format": "json"}
    r = requests.get(url, params=data)
    data = r.json()
    return data["postcode"]


# get_zipcode(38.9241603, -77.3996736)
