from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

DB_URI = 'mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
DB_NAME = 'thing_list'
COLLECTION = 'things'
client = MongoClient(DB_URI)
db = client[DB_NAME][COLLECTION]

class Dao:        

    def add(self, item):
        db.insert_one(item)

    def find(self, _id):
        item = db.find_one({'_id':ObjectId(_id)})
        return item or None

    def delete(self, _id):
        response = db.delete_one({'_id': ObjectId(_id)})
        return json_util.dumps(response.raw_result)

    def find_by_params(self,params):
        item_list = db.find(params)
        return item_list

    def update(self, _id, updates):
        response = db.update_one({'_id':ObjectId(_id)}, {'$set':updates})
        return json_util.dumps(response.raw_result)