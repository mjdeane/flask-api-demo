from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

DB_URI = 'mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
DB_NAME = 'thing_list'
COLLECTION = 'things'

class Dao:
    def __init__(self):
        client = MongoClient(DB_URI)
        self.db = client[DB_NAME][COLLECTION]

    def add(self, item):
        self.db.insert_one(item)

    def find(self, _id):
        item = self.db.find_one({'_id':ObjectId(_id)})
        return item or None

    def delete(self, _id):
        response = self.db.delete_one({'_id': ObjectId(_id)})
        return json_util.dumps(response.raw_result)

    def find_by_params(self,params):
        item_list = self.db.find(params)
        return item_list

    def update(self, _id, updates):
        response = self.db.update_one({'_id':ObjectId(_id)}, {'$set':updates})
        return json_util.dumps(response.raw_result)