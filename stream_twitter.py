import json
import tweepy

import credentials_var as cred

# User credentials to access Twitter API
ACCESS_TOKEN = "94752564-BvP4ZNJawmbcBbZfl9V9fVxCMqBEw3C3XfspEZFbZ"
ACCESS_TOKEN_SECRET = "tXyHXu7vJt6k3YlnPNm5JI8gBbfqIfQzOVWhlKzH1GNMS"
CONSUMER_KEY = "VDUHKifMgzsf0z98tEeaqgBkU"
CONSUMER_SECRET = "ukVf6fqYeqUeZ10WeMjv0a35DfZw79INqgzEM8Rat9y2pxncr5"

# Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def stream(keyword, limit):
    class CustomStreamListener(tweepy.StreamListener):

        def __init__(self, api):
            self.api = api
            super(tweepy.StreamListener, self).__init__()
            self.db = cred.TwitterDB
            self.counter = 1
            self.limit = limit

        def on_data(self, tweet):
            if self.counter <= self.limit:
                full_data = json.loads(tweet)
                if not full_data['retweeted'] and 'RT @' not in full_data['text']:
                    full_data['keyword'] = keyword[0]
                    full_data['processed'] = False
                    print(self.counter, full_data)
                    cred.tweets.insert_one(full_data)

                    self.counter += 1
                    return True
            else:
                tweet_stream.disconnect()

        def on_error(self, status_code):
            print(status_code)
            if status_code == 420:
                # returning False in on_data disconnects the stream
                return False

        def on_timeout(self):
            return True

    tweet_stream = tweepy.Stream(auth, CustomStreamListener(api))

    # Start streaming tweets
    tweet_stream.filter(track=keyword)
