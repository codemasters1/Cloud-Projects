import env
import requests
import json
import boto3
from datetime import datetime3
import time
 
URL = 'https://finviz.com/screener.ashx?v=110&s=ta_topgainers'
 
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
    quantity = 0
    attempt = 0
 
    while (quantity < 1):
        response = requests.get(URL, headers=headers)
        response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))
 
        quantity = response_formatted['availabilities'][0]['shipping']['quantityRemaining']
 
        if (quantity < 1):
            #Out Of stock
            print('Time=' + str(datetime.now()) + "- Attempt=" + str(attempt))
            attempt += 1
            time.sleep(5)
        else:
            print('Hey its in stock! Quantity=' + str(quantity))
            publish(quantity)
 
 
def publish(quantity):
    arn = 'arn:aws:sns:us-east-1:398447858632:InStockTopic'
    sns_client = boto3.client(
        'sns',
        aws_access_key_id=env.accessKey,
        aws_secret_access_key=env.secretKey,
        region_name='us-east-1'
    )
 
    response = sns_client.publish(TopicArn=arn, Message='Its in stock! Quantity=' + str(quantity))
    print(response)
 
main()
