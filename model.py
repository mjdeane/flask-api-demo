from dao import Dao

class Model:
    data_access = Dao()

    def __init__(self, params):
        self.name = params['name']
        self.function = params['function']
        self._id = str(params['_id'])

    @classmethod
    def update(cls, _id, params):
        if params['name'] == None:
            del params['name']
        if params['function'] == None:
            del params['function']
        print(params)
        response = cls.data_access.update(_id, params)
        print(response)
        return response

    @classmethod
    def save(cls, payload):
       _id = cls.data_access.add(payload)
       return {'_id' : _id}

    @classmethod
    def get_by_id(cls, _id):
        thing = cls.data_access.find(_id)
        return cls(thing)

    @classmethod
    def get_by_params(cls, params):
        thing_list = cls.data_access.find_by_params(params)
        thing_list = list(map(cls, thing_list))
        return thing_list

    @classmethod
    def delete(cls, _id):
        response = cls.data_access.delete(_id)
        return response