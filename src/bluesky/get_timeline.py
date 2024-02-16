from atproto import Client
import json

with open('../config.json', 'r') as json_file:
    config = json.load(json_file)

client = Client()
user_name = config["login_data"]["user_name"]
password = config["login_data"]["password"]
client.login(user_name, password)

def get_timeline():
    get_timeline = client.get_timeline(limit=100).feed
    post_list = []
    for gt in get_timeline:
        text = gt.post.record.text
        handle = gt.post.author.handle
        is_ngword = judgement_sentence(text)
        if text and handle != user_name and is_ngword:
            post_list.append(gt)
    return post_list

