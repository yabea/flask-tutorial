# coding:utf-8


class Config():
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = "mysql://root:272825@localhost/learn_flask?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False