import requests
import pandas as pd
import boto3
from io import StringIO

cbCoins = []
url = 'https://api.pro.coinbase.com/currencies'
response = requests.get(url).json()

for i in range(len(response)):
    if response[i]['details']['type'] == 'crypto':
        cbCoins.append(response[i]['id'])

cbCoins = pd.DataFrame(cbCoins)


def main():
    #######################################
    DATA_BUCKET = "coinbase"
    s3 = boto3.resource("s3")
    #######################################
    filename = 'coinbase_coins_list'
    filename_buffer = StringIO()
    df.to_csv(filename_buffer)
    #######################################
    s3.Object(DATA_BUCKET, filename).put( Body=filename_buffer.getvalue() )


print(cbCoins)