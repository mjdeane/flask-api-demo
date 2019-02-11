from voluptuous import Schema, All, Length, Match, Required, Invalid

params_schema = Schema({'name':str,'function':str})

req_params_schema = Schema({Required('name'):str,Required('function'):str})

id_schema = Schema(All(str,Length(min=24,max=24,),Match(r'^[0123456789abcdef]*$')))
