from bs4 import BeautifulSoup
import requests

# if __name__ == '__main__':

HEADERS = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2',
    'accept-language': 'en-US,en;q=0.7'
}

# The webpage URL
URL = "https://www.amazon.com/Crocs-Unisex-Classic-Black-Women/dp/B0014C2NBC/ref=zg-bs_fashion_sccl_1/139-9092933-9616351?pd_rd_w=sXjxF&content-id=amzn1.sym.1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_p=1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_r=RT1GWXG8RKF5YFZXV52G&pd_rd_wg=t5H6C&pd_rd_r=fd11ada1-e5a2-4df6-814f-2b96363256d8&pd_rd_i=B0014C2NBC&psc=1"

# HTTP Request
webpage = requests.get(URL, headers=HEADERS)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

soup2 = BeautifulSoup(soup.prettify(), "html.parser")

print("SOUP2!!!!!!:")
print(soup2)
