import bs4
import urllib3
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup


def get_sku_url(item_string):
    url = "https://storesteals.com/walmart/search/"
    # vals = {"zipcode": zipcode}
    suffix = quote(item_string)  # + "?" + urlencode()
    url = url + suffix
    return url


def get_sku(item):
    url = get_sku_url(item)
    skudict = dict()

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')

    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        item_name = row.findAll('td')[2].contents
        sku = row.findAll('td')[3].contents
        skudict[sku[0]] = item_name[0].encode_contents().decode("utf-8")

    return skudict
