# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
from scrapy.conf import settings
from tweet_scraper.items import TweetItem

#将爬取的数据直接存入mongodb
class SaveToMongoPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.tweetCollection = db[settings['MONGODB_TWEET_COLLECTION']]
        self.tweetCollection.ensure_index([('ID', pymongo.ASCENDING)], unique=True, dropDups=True)

    def process_item(self, item, spider):        
        if isinstance(item, TweetItem):
            pass
        return item


class SaveToFilePipeline(object):
    
    def process_item(self, item, spider):
        if isinstance(item, TweetItem):
            with open("test_pipe", "a") as f:
                try:
                    json_str = json.dumps(dict(item)) + "\n"
                    f.write(json_str)
                except Exception as ex:
                    print(ex)
                    
                

