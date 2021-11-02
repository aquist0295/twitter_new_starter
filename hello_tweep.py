import tweepy

print('looking at tweets')

CONSUMER_KEY = 'Xhv7EGdZUVZWC8gvGkjFgdakQ'
CONSUMER_SECRET = 'Ogn6YGJBmCjIk2js3l5o9v2n8oHFtmoNiUNbdVhQLK3WBS2kDL'
ACCESS_TOKEN = '191992412-wvCA4wTU8tQv3gjUEIj3v2TyKgTo1y0dIHjLpKdQ'
ACCESS_TOKEN_SECRET = 'UmymnKUP4EJPs4rIPFcpmo7kV1XHps5p28NoYeYrPGw10'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
