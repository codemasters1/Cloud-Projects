from bs4 import BeautifulSoup
import requests
import time
import datetime
import json

headers = {
    'authority': 'finviz.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.bestbuy.ca/en-ca/product/logitech-c920s-pro-1080p-hd-webcam/13444247',
    'accept-language': 'en-US,en;q=0.8'
}


def main():
    url = 'https://finviz.com/screener.ashx?v=110&s=ta_topgainers'
    response = requests.get(url, headers=headers)
    response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

    print(response_formatted)
