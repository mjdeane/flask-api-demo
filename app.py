import sys
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Resource, Api
from model import Model
from voluptuous import Schema, All, Length, Match

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('function')

params_schema = Schema({'name':str,'function':str})
id_schema = Schema(All(str,Length(min=24,max=24,),Match(r'^[0123456789abcdef]*$')))

class Thing(Resource):
    def get(self, _id):
        try:
            id_schema(_id)
        except:
            abort(400,message='invalid id')
        try:
            thing = Model.get_by_id(_id)
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        if not thing:
            abort(404, message='Thing {} not found'.format(_id))
        return jsonify(vars(thing))

    def delete(self, _id):
        try:
            id_schema(_id)
        except:
            abort(400,message='invalid id')
        try:
            response = Model.delete(_id)
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(response)
        response.status_code = 204
        return response

    def put(self, _id):
        try:
            id_schema(_id)
        except:
            abort(400,message='invalid id')
        args = parser.parse_args()
        try:
            response = Model.update(_id, {'name':args['name'], 'function':args['function']})
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(response)
        response.status_code = 201
        return response

class ThingList(Resource):
    def get(self):
        args = parser.parse_args()
        params = {}
        if args['name']:
            params['name'] = args['name']
        if args['function']:
            params['funtion'] = args['function']
        try:
            params_schema(params)
        except:
            abort(400,message='invalid parameter')
        try:
            thing_list = Model.get_by_params(params)
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        thing_dict = dict(map(lambda t: (t._id, {'name':t.name, 'function': t.function}),
                              thing_list))
        return jsonify(thing_dict)

    def post(self):
        args = parser.parse_args()
        params = {'name':args['name'],'function':args['function']}
        try:
            params_schema(params)
        except:
            abort(400,message='invalid parameter')
        try:
            thing = Model.save(params)
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(thing)
        response.status_code = 201
        return response

api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<_id>')

app.run(debug=True,host='0.0.0.0', port=5000)