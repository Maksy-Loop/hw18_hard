# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from flask import request
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
         self.dao = dao

    def get_all(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        if year or director_id or genre_id is None:
            return self.dao.get_all()
        elif year:
            return self.dao.filter_year(year)
        elif director_id:
            return self.dao.filter_director_id(director_id)
        elif genre_id:
            return self.dao.filter_genre_id(genre_id)
        else:
            return None

    def get_one(self, id):
        return self.dao.get_one(id)

    def create(self):
        data = request.json

        return self.dao.create(data)



    def update(self, id):
        movie = self.dao.get_one(id)
        data = request.json
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        return self.dao.update(movie)


    def update_partial(self, data):
        pass

    def delete(self, id: int):
        movie = self.dao.get_one(id)

        return self.dao.delete(movie)