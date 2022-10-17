from bs4 import BeautifulSoup
import requests, re
from requests import get

# enter URL that you want to scrape, a single item
# URL = 'https://www.amazon.com/Crocs-Unisex-Classic-Black-Women/dp/B0014C2NBC/ref=zg-bs_fashion_sccl_1/139-9092933-9616351?pd_rd_w=sXjxF&content-id=amzn1.sym.1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_p=1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_r=RT1GWXG8RKF5YFZXV52G&pd_rd_wg=t5H6C&pd_rd_r=fd11ada1-e5a2-4df6-814f-2b96363256d8&pd_rd_i=B0014C2NBC&psc=1'
URL = 'https://www.amazon.com/pet-shops-dogs-cats-hamsters-kittens/b/?ie=UTF8&node=2619533011&ref_=nav_cs_pets'

# cover our tracks:
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
headers={'User-Agent': 'Mozilla/5.0'}
# get webpage
page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

# make it look easier to read
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#testing grabs:
# title = soup2.find(id='productTitle').get_text()

# price = soup2.find('span', class_='a-price-whole').get_text()
# test = soup2.find("div", {"id": "glow-ingress-line2"})
# a_href= soup2.find("a",{"class":"a-link-normal"}).get("href")

# test = soup2.find("")
# class=a-link-normal
# id=bylineInfo
# test3 = soup2.findAll('a', href=re.compile('/stores/MizunoUSA/'))
# test3 = soup2.find_all("a", class_="a-link-normal")
# test3 = soup2.findAll("a")
# test4 = test3.find(id='bylineInfo')
# el = soup2.find(class_='a-link-normal', href=True)
el = soup2.find(class_='nav_a', href=True)


# testing: 
# print(title)
# print("Price:", price)
# print(price)
# print(a_href)
# print(test3)
test_el = el['href']
# print(el['href'])
print(test_el)


# https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup