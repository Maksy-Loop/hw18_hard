from flask_restx import Resource, Namespace
from flask import make_response, jsonify
from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return make_response(jsonify(directors_schema.dump(all_directors)), 200)


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id: int):
        director = director_service.get_one(id)
        return make_response(jsonify(director_schema.dump(director)), 200)
