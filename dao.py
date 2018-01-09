from pymongo import MongoClient

class Dao:
    def __init__(self):
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
