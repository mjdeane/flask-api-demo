from flask import Flask, jsonify
from flask_restful import reqparse, abort, Resource, Api
from model import Model

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('function')

class Thing(Resource):
    def get(self, _id):
        thing = Model.get_by_id(_id)
        if not thing:
            abort(404, message='Thing {} not found'.format(_id))
        return jsonify(vars(thing))

    def delete(self, _id):
        response = Model.delete(_id)
        if not response:
            abort(404, message='Thing {} not found'.format(_id))
        return jsonify(response)

    def put(self, _id):
        args = parser.parse_args()
        response = Model.update(_id, args['name'], args['function'])
        if not response:
            abort(404, message='Thing {} not found'.format(_id))
        return jsonify(response)

class ThingList(Resource):
    def get(self):
        args = parser.parse_args()
        params = {}
        if args['name']:
            params['name'] = args['name']
        if args['function']:
            params['funtion'] = args['function']
        thing_list = Model.get_by_params(params)

        thing_dict = dict(map(lambda t: (t._id, {'name':t.name, 'function': t.function}),
                              thing_list))
        return jsonify(thing_dict)

    def post(self):
        args = parser.parse_args()
        thing = Model.save({'name':args['name'],'function':args['function']})
        return jsonify(vars(thing))

api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<_id>')

app.run(debug=True,host='0.0.0.0', port=5000)