from atproto import Client

client = Client()
user_name = "XXXXXXXXX"
password = "XXXXXXXX"
client.login(user_name, password)

def follow_back():
    followers = client.get_followers(user_name).followers

    for f in followers:
        did = f.did
        client.follow(did)
