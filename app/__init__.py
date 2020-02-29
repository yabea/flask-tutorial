# coding:utf-8

from flask import Flask
from flask_session import Session
from sqlalchemy.engine.url import make_url
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError, ProgrammingError

from app.user import user
from app.views import views
from app.common import RedisHandler
from models import db, Users, Role


def init_redis(app):
    """
    初始化redis
    :param app:
    :return:
    """
    redis_handler = RedisHandler()
    redis_instance = redis_handler.get_redis_instance()
    app.config['SESSION_REDIS'] = redis_instance


def init_mysql(app):
    """
    初始化Mysql
    :param app:
    :return:
    """
    url = make_url(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    db.app = app
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
    Role.init_role()


def create_app(config='app.config.Config'):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config)
        init_redis(app)
        init_mysql(app)
        app.db = db

    app.register_blueprint(views)
    app.register_blueprint(user)
    Session(app)
    return app
