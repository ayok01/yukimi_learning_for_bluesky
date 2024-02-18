#!python3.8
from atproto import Client
from yukimi_text import yukimi_text
import get_timeline
import json
import random

with open('../config.json', 'r') as json_file:
    config = json.load(json_file)

client = Client()
user_name = config["login_data"]["user_name"]
password = config["login_data"]["password"]
client.login(user_name, password)

timeline_text = random.choice(get_timeline.get_timeline()).post.record.text
post_text = yukimi_text.change_yukimi(timeline_text)
client.send_post(text=post_text)