import bs4
import urllib3
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import urlencode


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

    for i in range(min(len(textbox), 15)):
        nums = i.index("/upc/")+5
        upcdict[i[i.index("<p>")+3:i.index("</p>")]] = i[nums:nums+12]

    print(textbox[0])
    # <div class="rImage"><a href="/upc/696226194496" title="UPC 696226194496 product info">696226194496</a><p>Charmin Toilet Paper 2 Ply, 142 Sheets Charmin Ultra Soft Bathroom Tissue 4</p></div>

    return upcdict
