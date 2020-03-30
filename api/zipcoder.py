import requests

access_token = "aecce98e3c7f42"


def get_zipcode(lat, lng):
    url = "https://us1.locationiq.com/v1/reverse.php"
    data = {"key": access_token,
            "lat": lat,
            "lon": lng,
            "format": "json"}
    r = requests.get(url, params=data)
    data = r.json()
    if 'postcode' in data:
        return data['postcode']
    else:
        return data['address']['postcode']


def get_location(address):
    # address = (street, city, state, postalcode)
    street = address[0]
    city = address[1]
    state = address[2]
    zipcode = address[3]
    url = "https://us1.locationiq.com/v1/search.php"
    data = {
        'key': access_token,
        'street': street,
        'city': city,
        'state': state,
        'postalcode': str(zipcode),
        'countrycodes': 'us',
        'format': 'json'
    }
    r = requests.get(url, params=data)
    data = r.json()
    return (data['lat'], data['lon'])

# get_zipcode(38.9241603, -77.3996736)
