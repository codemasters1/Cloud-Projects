from bs4 import BeautifulSoup
import requests
import pandas as pd
import boto3
from io import StringIO

headers = {
    'authority': 'finviz.com',
    'pragma': 'no-cache',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://finviz.com/screener.ashx?v=340&s=ta_topgainers',
    'accept-language': 'en-US,en;q=0.8'
}


def main():
    url = 'https://finviz.com/screener.ashx?v=110&s=ta_topgainers'
    response = requests.get(url, headers=headers)
    print(response.content)
    #######################################
    DATA_BUCKET = "proxy-test1-html"
    s3 = boto3.resource("s3")
    #######################################
    filename = 'proxy-test1-html'
    #######################################
    s3.Object(DATA_BUCKET, filename).put( Body=response.content )

if __name__ == "__main__":
    main()