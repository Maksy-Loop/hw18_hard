# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns

from views.films import films_ns

# функция создания основного объекта app
def create_app(config_object):
     application = Flask(__name__)
     application.config.from_object(config_object)
     application.app_context().push()
     return application



# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(application):
     db.init_app(application)
     api = Api(app)
     api.add_namespace(films_ns)
     api.add_namespace(directors_ns)
     api.add_namespace(genres_ns)

 #    create_data(app, db)


app_config = Config()
app = create_app(app_config)
configure_app(app)


#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
if __name__ == '__main__':
     app.run()

