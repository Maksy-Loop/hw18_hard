from flask_restx import Resource, Namespace

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DerectorsView(Resource):
    def get(self):
        return "ololo", 200


@directors_ns.route('/')
class DerectorView(Resource):
    def get(self):
        return "ololo", 200

