import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

#REMOTE_DB_URI = 'mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
DB_NAME = 'thing_list'
COLLECTION = 'things'
#client = MongoClient(REMOTE_DB_URI)
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client[DB_NAME][COLLECTION]

class Dao:        

    def add(self, item):
        return str(db.insert_one(item).inserted_id)

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