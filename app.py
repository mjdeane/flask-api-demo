from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from model import Model
from dao import Dao

app = Flask(__name__)
api = Api(app)
dao = Dao(app)


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('function')


class Thing(Resource):
    def get(self, name):
        # TODO: do not interact with the DAO from the APP, the APP will communicate with the MODEL to handle all business logic
        thing = dao.find(name)
        
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
            
        return thing.serialize()

    def delete(self, name):
        # TODO: do not interact with the DAO from the APP, the APP will communicate with the MODEL to handle all business logic
        dao.delete(name)
        
        return name, 204

    def put(self, name):
        args = parser.parse_args()
        thing = dao.delete(name)
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        
        # TODO: do not interact with the DAO from the APP, the APP will communicate with the MODEL to handle all business logic
        dao.add(Model.from_dict({'name':name, 'function':args['function']}))

        return name, 201


class ThingList(Resource):
    def get(self):
        thing_list = list(dao.find_all())
        thing_dict = {}
        for i in range(0,len(thing_list)):

            # TODO: debugging, if i is not within thing_list you will get an error below with [i]['name'] ?
            print(thing_list[i])

            thing_dict[str(i)] = {'name':thing_list[i]['name'],'function':thing_list[i]['function']}
        return thing_dict

    def post(self):
        args = parser.parse_args()
        thing = Model.from_dict({'name':args['name'], 'function':args['function']})
        
        # TODO: DAO should not be accessed from the app, the APP will interact with the MODEL to handle all business logic
        dao.add(thing)

        return thing.serialize(), 201


api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<name>')

# TODO: what is this for?
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
