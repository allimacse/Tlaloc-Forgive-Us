import tweepy
import json

class TweetTlaloc:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

consumer_key = "4OP4VrZQHAzkggYfo6nqpQ6Bv"
consumer_secret = "11zhrKgYFqXvRJKiSve4KbR7RU3OKfCr5Su82lYBW9QFadFjW0"

access_token="90939479-isS2wKlmaxOKMgJ3zkbohCGJKY6b1KpLVM7QtaXn3"
access_token_secret="FkosMEIa9vLLi2FUiSML3UR2ydxQD6hJwRyoZLjxyIX2b"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

tweetCount = 20
# The search term you want to find
query = ["Inundacion", "Zaragoza", "CDMX"]

# Language code (follows ISO 639-1 standards)
language = "es"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language, count=tweetCount)

#Create file tweetTlaloc.json
f= open("tweetTlaloc.json","w+")
#Count
contador = 1
# foreach through all tweets pulled
f.write('[\n')
for tweet in results:
   # printing the text stored inside the tweet object
  print(tweet.text)
  f.write('\n {')
  f.write('"id" : "{}",\n "nombre" : "{}", \n "ubicacion" : "{}", \n "hora" : "{}"'.format(tweet.id ,tweet.user.screen_name, tweet.user.location,tweet.created_at))
  f.write('}')
  if contador < 20 :
    f.write(',')
  contador += 1 
  
f.write('\n]')
f.close() 