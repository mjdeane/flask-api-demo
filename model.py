class Model:

    def __init__(self, name, function):
        self.name = name
        self.function = function

    @classmethod
    def from_dict(_class, thing_dict):
        name = thing_dict['name']
        function = thing_dict['function']
        return Model(name, function)

    def serialize(self):
        return {'name':self.name,'function':self.function}
