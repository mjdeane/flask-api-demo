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
        thing = dao.find(name)
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        return thing.serialize()

    def delete(self, name):
        dao.delete(name)
        return name, 204

    def put(self, name):
        args = parser.parse_args()
        thing = dao.delete(name)
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        dao.add(Model.from_dict({'name':name, 'function':args['function']}))
        return name, 201


class ThingList(Resource):
    def get(self):
        thing_list = list(dao.find_all())
        thing_dict = {}
        for i in range(0,len(thing_list)):
            print(thing_list[i])
            thing_dict[str(i)] = {'name':thing_list[i]['name'],'function':thing_list[i]['function']}
        return thing_dict

    def post(self):
        args = parser.parse_args()
        thing = Model.from_dict({'name':args['name'], 'function':args['function']})
        dao.add(thing)
        return thing.serialize(), 201


api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<name>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
