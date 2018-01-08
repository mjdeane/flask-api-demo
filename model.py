class Model:

    def __init__(self, name, function):
        self.name = name
        self.function = function


    # TODO: methods within this class should handle all the business logic from the app to the databases
    # TODO: these methods should include get_by_id , get_by_params, update, save, delete


    @classmethod
    def from_dict(_class, thing_dict):
        name = thing_dict['name']
        function = thing_dict['function']
        return Model(name, function)

    def serialize(self):
        return {'name':self.name,'function':self.function}
