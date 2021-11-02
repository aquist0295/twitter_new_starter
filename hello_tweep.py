import tweepy

print('looking at tweets')

CONSUMER_KEY = 'Please insert token/key here'
CONSUMER_SECRET = 'Please insert token/key here'
ACCESS_TOKEN = 'Please insert token/key here'
ACCESS_TOKEN_SECRET = 'Please insert token/key here'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
