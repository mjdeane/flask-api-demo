from dao import Dao

class Model:
    data_access = Dao()

    def __init__(self, name, function, _id):
        self.name = name
        self.function = function
        self._id = _id
    @classmethod
    def update(cls, _id, name, function):
        updates = {}
        if name:
            updates['name'] = name
        if function:
            updates['function'] = function
        response = cls.data_access.update(_id, updates)
        print(response)
        return response

    @classmethod
    def save(cls, payload):
       cls.data_access.add(payload)
       return cls.from_dict(payload)

    @classmethod
    def get_by_id(cls, _id):
        thing = cls.data_access.find(_id)
        return cls.from_dict(thing)

    @classmethod
    def get_by_params(cls, params):
        thing_list = cls.data_access.find_by_params(params)
        thing_list = list(map(cls.from_dict, thing_list))
        return thing_list

    @classmethod
    def delete(cls, _id):
        response = cls.data_access.delete(_id)
        return response

    @classmethod
    def from_dict(cls, thing_dict):
        name = thing_dict['name']
        function = thing_dict['function']
        _id = str(thing_dict['_id'])
        return cls(name, function, _id)