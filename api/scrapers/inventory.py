from skulookup import get_sku
import urllib3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import re

urls = ["https://brickseek.com/walmart-inventory-checker/", "https://brickseek.com/cvs-inventory-checker/",
        "https://brickseek.com/target-inventory-checker/", "https://brickseek.com/bjs-inventory-checker/"]


def remove_tags(htmltext):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('\n', htmltext)


def get_walmarts(item_name, zipcode):
    skudict = get_sku(item_name)
    sku = list(skudict.keys())[0]
    item = skudict[sku]
    #     data = {'sku': '805984709', 'sort': 'recommended', 'zip': '20152'}

    #     data = {'sku': '791305460', 'sort': 'recommended', 'zip': '20152'}
    data = {'sku': str(sku), 'sort': 'recommended', 'zip': str(zipcode)}
    r = requests.post(urls[0], params={'sku': data['sku']}, data=data)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find_all('div', attrs={'class': 'table__row'})
    # print(rows[1])
    stores = list()
    for r in rows[1:]:
        if (len(stores) > 10):
            break
        try:
            quantity = r.find_all('span', attrs={
                'class': 'table__cell-quantity'})[0].encode_contents().decode('utf-8')
        except:
            quantity = 0
        # availability = r.find_all('span', attrs={
        #     'availability-status-indicator__text'})[0].encode_contents().decode('utf-8')
        storeName = r.find_all('strong', attrs={
            'class': 'address-location-name'})[0].encode_contents().decode('utf-8')
        address = remove_tags(r.find_all('address')[
                              0].encode_contents().decode('utf-8')).strip()

        store = dict()
        store["item"] = item
        store["sku"] = sku
        if quantity == 0:
            store["available"] = False
        else:
            store["available"] = True
        store["storename"] = storeName.strip()
        tokens = address.split("\n")
        citystatezip = tokens[1].strip().split(" ")
        city = " ".join(citystatezip[:-1])
        store["zipcode"] = citystatezip[-1]
        store["address"] = tokens[0]
        store["city"] = city
        stores.append(store)
    return stores


for store in get_walmarts("toilet paper", 22032):
    print(store)

''' [
    {
        "available": true,
        "storename": "walmart #1284",
        "zipcode" : "20182",
        "address" : "1234 Street St.",
        "city" : "Germantown, MD"
    }

  ]'''
