from flask_restx import Resource, Namespace
from flask import make_response, jsonify

from dao.model.movie import MovieSchema
from implemented import movie_service

films_ns = Namespace('films')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@films_ns.route('/')
class FilmsView(Resource):
    def get(self):

        all_movies = movie_service.get_all()
        return make_response(jsonify(movies_schema.dump(all_movies)), 200)

    def post(self):

        movie_service.create()

        return f"Done", 201


@films_ns.route('/<int:id>')
class FilmView(Resource):
    def get(self, id: int):

        movie = movie_service.get_one(id)
        return make_response(jsonify(movie_schema.dump(movie)), 200)

    def put(self, id: int):
        movie_service.update(id)
        return "Done", 204

    def delete(self, id: int):
        movie_service.delete(id)
        return "Done", 204



