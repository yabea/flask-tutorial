# coding:utf-8

from flask import Flask
from sqlalchemy.engine.url import make_url
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError, ProgrammingError

from user import user
from views import views


def create_app(config='app.config.Config'):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config)

        from models import db, Users
        url = make_url(app.config['SQLALCHEMY_DATABASE_URI'])
        db.init_app(app)
        try:
            if not database_exists(url):
                create_database(url)
            db.create_all()
        except OperationalError:
            db.create_all()
        except ProgrammingError:
            pass
        else:
            db.create_all()
        app.db = db

    app.register_blueprint(views)
    app.register_blueprint(user)
    return app
