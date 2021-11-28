# Authenticate to Twitter

import tweepy

#CONSUMER_KEY = "gPiZzk9nRg0YZABbk0lExWTlh"
#CONSUMER_SECRET = "6yKSWYoJFDnmI2PqzvZEfKwFTojp7763hdbcYilxr7XQ7ZaCTY"
#ACCESS_KEY = "1457323725305614337-C8EF4XYtxnu3QcZPsDUMicJrlTq7ve"
#ACCESS_SECRET = "yiAEDNzl1AXh0uKKVip9rCM2wVgnVtr7bcvBYbYyHukFR"

API_key = "gPiZzk9nRg0YZABbk0lExWTlh"
API_secret_key = "6yKSWYoJFDnmI2PqzvZEfKwFTojp7763hdbcYilxr7XQ7ZaCTY"
access_token = "1457323725305614337-C8EF4XYtxnu3QcZPsDUMicJrlTq7ve"
access_token_secret = "yiAEDNzl1AXh0uKKVip9rCM2wVgnVtr7bcvBYbYyHukFR"

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")