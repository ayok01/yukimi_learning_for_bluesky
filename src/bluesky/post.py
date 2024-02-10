#!python3.8
from atproto import Client

client = Client()
user_name = "neruneru0419.bsky.social"
password = "XXXXXXXXXXXXX"
client.login(user_name, password)

client.send_post(text='APIからポスト')