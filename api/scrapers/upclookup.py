import bs4
import urllib3
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup


def get_upc_url(item_string):
    url = "https://www.upcitemdb.com/query?"
    values = {"s": item_string,
              "type": 2}
    suffix = urlencode(values)
    url = url + suffix
    return url


def get_upc(item):
    url = get_upc_url(item)
    upcdict = dict()

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    textbox = soup.findAll('div', attrs={'class': 'rImage'})

    for i in textbox:
        i = str(i)
        if "UPC" in i:
            upcdict[i[i.index("/upc/")+5:i.index("\" title")].zfill(12)
                    ] = i[i.index("<p>")+3:i.index("</p>")]
        if len(upcdict) > 15:
            break

    return upcdict
