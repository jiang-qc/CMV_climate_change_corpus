from tweepy.streaming import StreamListener #tweepy version 3.10.0
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import cursor
import json
import re
from datetime import datetime
from dateutil import tz
#import pymongo
import sys, os
import time

import api_cred

## Handle the twitter api authentication for all functions
class twitterauthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(api_cred.consumer_key, api_cred.consumer_secret)
        auth.set_access_token(api_cred.access_token, api_cred.access_token_secret)
        return auth
        

## main Twitter streaming function
class TwitterStreamer():

    def __init__(self):
        self.twitter_auth = twitterauthenticator()

    def stream_tweets(self, hash_tag_list):

        listener = tweetListner(hash_tag_list)
        auth = self.twitter_auth.authenticate_twitter_app()
        stream = Stream(auth, listener, tweet_mode='extended')
        stream.filter(languages=["en"], track = hash_tag_list)

## The callback function of stream
class tweetListner(StreamListener):
    #get current time, used for timing file update
    tstamp1 = time.time()

    ## define blank array for batch storing
    tweetobj = []
    userobj = []
    

    ## get filename here
    def __init__(self, hash_tag_list):
        self.hash_tag_list = hash_tag_list

    
    #print(tstamp1)
    def on_data(self,data):
        try:
            ## save tweet data into tweet table
            dic = {}
            
            parsed = json.loads(data)
            
            #check if the tweet is retweeted. if true, store both the original tweet and the retweeted text
            if "retweeted_status" in parsed:
                if "extended_tweet" in parsed['retweeted_status']:
                    dic["og_tweet_txt"] = parsed["retweeted_status"]["extended_tweet"]["full_text"]    
                else:
                    dic["og_tweet_txt"] = parsed["retweeted_status"]["text"]
                # print(dic['og_tweet_txt'])
            else:
                dic["og_tweet_txt"] = ''

            if "extended_tweet" in parsed:
                dic["tweet_txt"] = parsed["extended_tweet"]['full_text']
            else:
                dic["tweet_txt"] = parsed["text"]
                
            self.tweetobj.append(dic)

            #update output file every 60 seconds
            tstamp2 = time.time()
            if tstamp2 - self.tstamp1 > 60:
                #save the output json file with date as file name
                if dic:
                    print("appending to doc",datetime.today().strftime('%m-%d-%Y')+".json")
                    with open(datetime.today().strftime('%m-%d-%Y')+".json", 'a', encoding = 'utf-16') as tf:
                        for d in self.tweetobj:
                            json.dump(d, tf)
                            tf.write('\n')
                        # tf.write(json_obj)
                    self.tweetobj = []
                    self.tstamp1 = tstamp2

        except BaseException as e:
            ##Debugging on where the error row is:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return True
    
    def on_error(self, status):
        if status == 420:
            ## Return false in case rate limit happens
            return False
        print(status)

## init it
if __name__ == "__main__":
    hash_tag_list = ["cryptocurrency","bitcoin","coinbase"]
    twitter_streamer = TwitterStreamer()
    print('start')
    twitter_streamer.stream_tweets(hash_tag_list)