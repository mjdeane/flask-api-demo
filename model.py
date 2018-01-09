from dao import Dao

class Model:
    data_access = Dao()

    def __init__(self, name, function, _id):
        self.name = name
        self.function = function
        self._id = _id
    @classmethod
    def update(cls, name, function):
        thing = cls.data_access.delete(name)
        if not thing:
            return None
        updated_thing = {'name':name, 'function':function}
        cls.data_access.add(updated_thing)
        return cls.from_dict(updated_thing)
        
    @classmethod
    def save(cls, name, function):
       thing = {'name':name, 'function':function}
       cls.data_access.add(thing)
       return cls.from_dict(thing)

    @classmethod
    def get_by_id(cls, _id):
        thing = cls.data_access.find({'_id':_id})
        return cls.from_dict(thing)

    @classmethod
    def get_by_name(cls, name):
        thing = cls.data_access.find({'name':name})
        return cls.from_dict(thing)

    @classmethod
    def get_by_function(cls, function):
        thing = cls.data_access.find({'function':function})
        return cls.from_dict(thing)

    @classmethod
    def delete(cls, name):
        thing = cls.data_access.delete(name)
        return cls.from_dict(thing)

    @classmethod
    def find_all(cls):
        return cls.data_access.find_all()

    @classmethod
    def from_dict(cls, thing_dict):
        name = thing_dict['name']
        function = thing_dict['function']
        _id = str(thing_dict['_id'])
        return cls(name, function, _id)


