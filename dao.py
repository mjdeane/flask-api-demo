from flask_pymongo import PyMongo
from model import Model

class Dao:
    def __init__(self, app):
        app.config['MONGO_DBNAME'] = 'thing_list'
        
        # TODO: clusert configuration is good here, but this will connect to a local mongo docker container once you build out
        # your docker-compose file
        app.config['MONGO_URI'] = 'mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
        
        self.mongo = PyMongo(app)


    def add(self, item):
        self.mongo.db['things'].insert_one(item.serialize())

    def find(self, name):
        item = self.mongo.db['things'].find_one({'name':name})
        if not item:
            return None
        else:
            return Model.from_dict(item)

    def delete(self, name):
        item = self.mongo.db['things'].find_one_and_delete({'name':name})
        
        # TODO: debugging ?
        print(item)
        return item

    def find_all(self):
        item_list = self.mongo.db['things'].find()
        return item_list
