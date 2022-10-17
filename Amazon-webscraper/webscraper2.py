from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigatableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

	except AttributeError:

		try:
			# If there is some deal price
			price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

		except:		
			price = ""	

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = "Not Available"	

	return available	

if __name__ == '__main__':
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

    URL = "https://www.amazon.com/Crocs-Unisex-Classic-Black-Women/dp/B0014C2NBC/ref=zg-bs_fashion_sccl_1/139-9092933-9616351?pd_rd_w=sXjxF&content-id=amzn1.sym.1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_p=1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_r=RT1GWXG8RKF5YFZXV52G&pd_rd_wg=t5H6C&pd_rd_r=fd11ada1-e5a2-4df6-814f-2b96363256d8&pd_rd_i=B0014C2NBC&psc=1"

    webpage = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(webpage.content, "lxml")

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    links_list = []



if __name__ == '__main__':

	# Headers for request
	# HEADERS = ({'User-Agent':
	#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	#             'Accept-Language': 'en-US'})
    # HEADERS = {
        # 'authority': 'www.amazon.com',
        # 'pragma': 'no-cache',
        # 'cache-control': 'no-cache, no-transform',
        # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        # 'sec-fetch-site': 'none',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-dest': 'document',
        # 'referer': ,
        # 'accept-language': 

    # }
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
	# URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    URL = "https://www.amazon.com/Crocs-Unisex-Classic-Black-Women/dp/B0014C2NBC/ref=zg-bs_fashion_sccl_1/139-9092933-9616351?pd_rd_w=sXjxF&content-id=amzn1.sym.1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_p=1e7b1982-fb44-47aa-b1ce-d356a8609d66&pf_rd_r=RT1GWXG8RKF5YFZXV52G&pd_rd_wg=t5H6C&pd_rd_r=fd11ada1-e5a2-4df6-814f-2b96363256d8&pd_rd_i=B0014C2NBC&psc=1"
	
	# HTTP Request
    # 
    webpage = requests.get(URL, headers=HEADERS)

	# Soup Object containing all data
    # 
    soup = BeautifulSoup(webpage.content, "lxml")

	# Fetch links as List of Tag Objects
	
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

	# Store the links
    links_list = []

	# Loop for extracting links from Tag Objects
    for link in links:
	    links_list.append(link.get('href'))


	# Loop for extracting product details from each link 
for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "lxml")
        
        # Function calls to display all necessary product information
        print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        print("Product Rating =", get_rating(new_soup))
        print("Number of Product Reviews =", get_review_count(new_soup))
        print("Availability =", get_availability(new_soup))
        print()
        print()