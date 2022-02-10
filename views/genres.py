from flask_restx import Resource, Namespace
from flask import make_response, jsonify
from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return make_response(jsonify(genres_schema.dump(all_genres)), 200)


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id: int):
        genre = genre_service.get_one(id)
        return make_response(jsonify(genre_schema.dump(genre)), 200)
