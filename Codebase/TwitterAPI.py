import tweepy
import time

import tweepy.cursor


consumer_key = '' # Empty to not share API keys
comsumer_secret = '' # Empty to not share API keys

access_token = '' # Empty to not share API keys
access_token_secret = '' # Empty to not share API keys

auth = tweepy.OAuthHandler(consumer_key, comsumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# Follow bot
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Ajdeasmith':
        follower.follow()
        break

# Other bot

search_string = 'My name' # If they contain my name I will retweet it.
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search(search_string)).items(numberOfTweets):
    try:
        tweepy.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break