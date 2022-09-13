import os
from os.path import join, dirname
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent, FollowEvent, Gift, GiftEvent, ViewerCountUpdateEvent
# from dotenv import load_dotenv, find_dotenv
import boto3
from io import StringIO
import pandas as pd
import datetime
from datetime import date
import pytz

client: TikTokLiveClient = TikTokLiveClient(unique_id='tv_asahi_news')

saved_list = []

@client.on("connect")
async def on_connect(_: ConnectEvent):
    # print("Connected to Room ID:", client.room_id)
    string_conversion = str(client.room_id)
    saved_list.append("Connected to Room ID: " + string_conversion)
    # print(saved_list)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    # print(f"{event.user.nickname} -> {event.comment}")
    saved_list.append(f"{event.user.nickname} -> {event.comment}")
    # print(saved_list)


# Define handling an event via "callback"
client.add_listener("comment", on_comment)



def main():
    #######################################
    DATA_BUCKET = "hc-tiktokbots"
    s3.boto3.resource("s3")
    #######################################    
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    today = utc_now.astimezone(pytz.timezone("America/Chicago"))
    new_today = today.strftime("%m-%d-%Y")
    filename = str(unique_id) + new_today + '.csv'
    #######################################
    df.pd.DataFrame(saved_list)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    #######################################
    s3.Object(DATA_BUCKET, filename).put( Body=csv_buffer.getvalue() )



if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run() 