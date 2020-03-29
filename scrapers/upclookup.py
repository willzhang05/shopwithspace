import bs4
from urllib import request
from urllib import parse
import requests
from bs4 import BeautifulSoup

# charmin%20toilet%20paper&type=2


def get_upc_url(item_string):
    url = "https://www.upcitemdb.com/query?"
    values = {"s": item_string,
              "type": 2}
    response = requests.post(url, data=values)
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc


def get_upc(item):
    url = get_upc_url(item)
    upclist = list()

    htmldata = bs4.get(url)

    return upclist
