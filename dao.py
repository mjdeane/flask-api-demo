from pymongo import MongoClient

class Dao:
#    _mongo = PyMongo(app)

    def __init__(self):
#        app.config['MONGO_DBNAME'] = 'thing_list'
#        app.config['MONGO_URI'] = 'mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
#        app.config['MONGO_URI'] = 'mongodb+srv://admin:iadmin@cluster0-bwkql.mongodb.net/test'
#        client = MongoClient('mongodb://admin:admin@cluster0-shard-00-00-bwkql.mongodb.net:27017,cluster0-shard-00-01-bwkql.mongodb.net:27017,cluster0-shard-00-02-bwkql.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
        client = MongoClient()
        self.db = client['thing_list']

    def add(self, item):
        self.db['things'].insert_one(item)

    def find(self, selector):
        item = self.db['things'].find_one(selector)
        if not item:
            return None
        else:
            return item

    def delete(self, name):
        item = self.db['things'].find_one_and_delete({'name':name})
        return item

    def find_all(self):
        item_list = self.db['things'].find()
        return item_list
