# images  class = sc-n1kvju-0 sc-izl178-2 gLQhnz cPIapC
# text p class = sc-14r3l9n-0 sc-izl178-5 hIUTkK gLWPJQ
# coupon expiration date class = sc-izl178-7
# coupon limit div = sc-izl178-7
# coupon clip it button = sc-mr2fb9-1 Fwebn sc-1cul4go-0 FJSae sc-izl178-8 jwQPhH    
    # button type = button, variant = primary

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup
import requests
from time import sleep
import datetime
from datetime import date

def return_page(url, class_chosen):

    # print(url)
    # print(class_chosen)

    HEADERS = {
        'authority': 'www.heb.com',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.heb.com/digital-coupon/coupon-selection/all-coupons',
        'accept-language': 'en-US,en;q=0.6'
    }

    req = Request(url, headers=HEADERS)
    webpage = urlopen(req).read()
    html = soup(webpage, "html.parser")
    print(html)
    chosen_item = html.find_all(attrs= {'class': class_chosen})

    # print(chosen_item)

    return chosen_item


# def text(url):



# def main():
#     images{}

def main():
    items = []
    items = return_page("https://www.heb.com/digital-coupon/coupon-selection/all-coupons", 'sc-1ib3jjn-0 sc-1sdr7i2-0 eEZvBO hhPkZp')
    # print(items)
    

if __name__ == "__main__":
    main()