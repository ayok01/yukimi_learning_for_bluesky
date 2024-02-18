from atproto import Client
import json

with open('../config.json', 'r') as json_file:
    config = json.load(json_file)

client = Client()
user_name = config["login_data"]["user_name"]
password = config["login_data"]["password"]

client.login(user_name, password)

def follow_back():
    followers = client.get_followers(user_name).followers

    for f in followers:
        did = f.did
        client.follow(did)
