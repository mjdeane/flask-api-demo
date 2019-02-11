from dao import Dao

class Model:
    data_access = Dao()

    def __init__(self, params):
        self.name = params['name'] if 'name' in params else None
        self.function = params['function'] if 'function' in params else None
        self._id = str(params['_id']) if '_id' in params else None

    @classmethod
    def update(cls, _id, params):
        response = cls.data_access.update(_id, params)
        thing = cls.data_access.find(_id)
        return cls(thing)

    @classmethod
    def save(cls, payload):
        _id = cls.data_access.add(payload)
        payload['_id'] = _id
        return cls(payload)

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