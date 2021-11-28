# funcao que realiza o post no twitter
# o mesmo pega os arquivos de configuração que servem para autenticar no perfil

import tweepy
import settings

from funcao_conselho import get_random_conselho
 
CONSUMER_KEY = "gPiZzk9nRg0YZABbk0lExWTlh"
CONSUMER_SECRET = "6yKSWYoJFDnmI2PqzvZEfKwFTojp7763hdbcYilxr7XQ7ZaCTY"

ACCESS_KEY = "1457323725305614337-C8EF4XYtxnu3QcZPsDUMicJrlTq7ve"
ACCESS_SECRET = "yiAEDNzl1AXh0uKKVip9rCM2wVgnVtr7bcvBYbYyHukFR"


#client = tweepy.Client(consumer_key= CONSUMER_KEY,consumer_secret= CONSUMER_SECRET,access_token= ACCESS_KEY,access_token_secret= ACCESS_SECRET)
    
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
#CONSUMER_KEY = settings.ENV['CONSUMER_KEY']
#CONSUMER_SECRET = settings.ENV['CONSUMER_SECRET']

#ACCESS_KEY = settings.ENV['ACCESS_KEY']
#ACCESS_SECRET = settings.ENV['ACCESS_SECRET']

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

#try:
   # api.verify_credentials()
   # print("Authentication Successful")
#except:
 #   print("Authentication Error").
    
api.update_status(get_random_conselho())