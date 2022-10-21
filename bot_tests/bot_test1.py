import os
from os.path import join, dirname
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent, FollowEvent, Gift, GiftEvent, ViewerCountUpdateEvent
# from dotenv import load_dotenv, find_dotenv

client: TikTokLiveClient = TikTokLiveClient(unique_id='charliesuit01')


@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")


# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run() 