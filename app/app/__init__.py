# coding:utf-8

from flask import Flask
from views import views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)

    return app