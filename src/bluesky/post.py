#!python3.8
from atproto import Client
import get_timeline

import json

with open('../config.json', 'r') as json_file:
    config = json.load(json_file)

client = Client()
user_name = config["login_data"]["user_name"]
password = config["login_data"]["password"]
client.login(user_name, password)

timeline = get_timeline.get_timeline()

client.send_post(text='APIからポスト')