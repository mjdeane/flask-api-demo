from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from model import Model

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('function')


class Thing(Resource):
    def get(self, name):
        thing = Model.get_by_name(name)
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        return vars(thing)

    def delete(self, name):
        thing = Model.delete(name)
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        return vars(thing), 204

    def put(self, name):
        args = parser.parse_args()
        thing = Model.update(name, args['function'])
        if not thing:
            abort(404, message='Thing {} not found'.format(name))
        return vars(thing), 201


class ThingList(Resource):
    def get(self):
        thing_list = list(Model.find_all())
        thing_dict = {}
        for i in range(0,len(thing_list)):
            thing_dict[str(i)] = {'name':thing_list[i]['name'],'function':thing_list[i]['function']}
        return thing_dict

    def post(self):
        args = parser.parse_args()
        thing = Model.save(args['name'],args['function'])
        
        return vars(thing), 201


api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<name>')

app.run(debug=True,host='0.0.0.0', port=80)
