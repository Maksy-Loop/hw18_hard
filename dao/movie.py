from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):

        return self.session.query(Movie).all()

    def filter_year(self, data):
        return self.session.query(Movie).filter(Movie.year == int(data)).all()

    def filter_director_id(self, data):
        return self.session.query(Movie).filter(Movie.director_id == int(data)).all()

    def filter_genre_id(self, data):
        return self.session.query(Movie).filter(Movie.genre_id == int(data)).all()

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def create(self, data):
        movie = Movie(**data)
        with self.session.begin():
            self.session.add(movie)

        return movie


    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie


    def update_partial(self, data):
        pass

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

        return movie
