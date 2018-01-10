from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

class Dao:
    def __init__(self):
        client = MongoClient('mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
        self.db = client['thing_list']

    def add(self, item):
        self.db['things'].insert_one(item)

    def find(self, _id):
        item = self.db['things'].find_one({'_id':ObjectId(_id)})
        return item or None

    def delete(self, _id):
        response = self.db['things'].delete_one({'_id': ObjectId(_id)})
        return json_util.dumps(response.raw_result)

    def find_by_params(self,params):
        item_list = self.db['things'].find(params)
        return item_list

    def update(self, _id, updates):
        response = self.db['things'].update_one({'_id':ObjectId(_id)}, {'$set':updates})
        return json_util.dumps(response.raw_result)