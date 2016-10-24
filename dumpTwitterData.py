#! /usr/bin/python
''' The script is used to pull data from twitter using twython and dumping the data into elasticsearch'''
import config as Config #Using config file to read the config settings from a separate config file.
from twython import Twython
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import *

es = Elasticsearch([Config.ES])
TWITTER_APP_KEY = Config.TWITTER_APP_KEY
TWITTER_APP_KEY_SECRET = Config.TWITTER_APP_KEY_SECRET
TWITTER_ACCESS_TOKEN = Config.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = Config.TWITTER_ACCESS_TOKEN_SECRET

twitterauth = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def pull_tweets(keyword):
    search = twitterauth.search(q=keyword,count=100)
    tweets = []
    tweets = search['statuses']
    for tweet in tweets:
        if tweet['user']['location'] is not None:
            doc = {
                'text': tweet['text'],
                'location': tweet['user']['location'],
                'timestamp': datetime.now()
            }
            res = es.index(index="twitter-index",doc_type='tweetData', body=doc)
            #print(res['created'])



def twittmap():
    try:
        for i in range(1,6):
            pull_tweets('java')
            pull_tweets('love')
            pull_tweets('trump')
            pull_tweets('clinton')
            pull_tweets('ruby')
            pull_tweets('columbia')
            pull_tweets('india')
            pull_tweets('diwali')
            pull_tweets('movie')
            pull_tweets('music')
    except:
        return

twittmap()
pull_tweets