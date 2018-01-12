import sys
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Resource, Api
from model import Model
from validate import params_schema, req_params_schema, id_schema

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('function')


class Thing(Resource):
    def get(self, _id):
        try:
            id_schema(_id)
            thing = Model.get_by_id(_id)
        except Invalid as e:
            abort(400,message='invalid id') 
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        if not thing:
            abort(404, message='Thing {} not found'.format(_id))
        return jsonify(vars(thing))

    def delete(self, _id):
        try:
            id_schema(_id)
            response = Model.delete(_id)
        except Invalid as e:
            abort(400,message='invalid id')
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(response)
        response.status_code = 204
        return response

    def put(self, _id):
        args = parser.parse_args()
        params = {k:v for k,v in args.items() if v is not None}
        try:
            id_schema(_id)
            params_schema(params)
            response = Model.update(_id, params)
        except Invalid as e:
            abort(400,message='invalid parameter')
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(response)
        response.status_code = 201
        return response

class ThingList(Resource):
    def get(self):
        args = parser.parse_args()
        params = {k:v for k,v in args.items() if v is not None}
        try:
            params_schema(params)
            thing_list = Model.get_by_params(params)
        except Invalid as e:
            abort(400,message='invalid parameter')
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        thing_dict = list(map(vars, thing_list))
        return jsonify(thing_dict)

    def post(self):
        args = parser.parse_args()
        try:
            req_params_schema(args)
            thing = Model.save(args)
        except Invalid as e:
            abort(400,message='invalid parameter')
        except:
            abort(500, message='Unexpected Error '+str(sys.exc_info()[0]))
        response = jsonify(thing)
        response.status_code = 201
        return response

api.add_resource(ThingList, '/things')
api.add_resource(Thing, '/things/<_id>')

app.run(debug=True,host='0.0.0.0', port=5000)