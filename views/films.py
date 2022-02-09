from flask_restx import Resource, Namespace

films_ns = Namespace('films')

@films_ns.route('/')
class FilmsView(Resource):
    def get(self):
        return "ololo", 200


@films_ns.route('/')
class FilmView(Resource):
    def get(self):
        return "ololo", 200

    def post(self):
        return "", 201

    def put(self):
        return "", 204

    def delete(self):
        return "", 204



