
import tweepy
import json
import settings
import pymongo
import time 
import logging
import pprint
from mongodb_tool import MongodbTool

#验证twitter api
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

mongodb_tool = MongodbTool()
mongo_collection = mongodb_tool.get_collection()

def check_mongo_collection():
    for tp in mongo_collection.find():
        print(tp)

def run_tweepy():
    for author in settings.AUTHORS:
        print("CURRENT AUTHOR: " + author)
        status_objs = []
        try:
            status_objs=api.user_timeline(screen_name=author)
        except Exception as e:
            logging.warning(e)
         
        for status_obj in status_objs:
            json_str = status_obj._json
            json_str['_id'] = json_str['id']
            try: 
                tp_id = mongo_collection.insert_one(json_str).inserted_id
                print(tp_id)
            except pymongo.errors.DuplicateKeyError as dub_e:
                pass

if __name__ == "__main__":
    run_tweepy()
    #check_mongo_collection()
