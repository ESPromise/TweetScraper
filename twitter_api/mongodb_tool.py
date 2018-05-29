import pymongo
import settings
import json

class MongodbTool:
    
    def __init__(self):
        self.server = settings.MONGODB_SERVER
        self.port = settings.MONGODB_PORT
        self.db_name = settings.MONGODB_DB
        self.collection_name = settings.MONGODB_TWEET_COLLECTION
        #connect to collection.
        self.client = pymongo.MongoClient(self.server, self.port)
        self.database = self.client[self.db_name]
        self.collection = self.database[self.collection_name]

    def get_client(self):
        return self.client

    def get_database(self):
        return self.database

    def get_collection(self):
        return self.collection

    def insert_one(doc_dict):
        doc_id = self.collection.insert_one(doc_dict).inserted_id
        return doc_id

