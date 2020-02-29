# coding:utf-8
import os


class Config():
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = "mysql://root:123456@localhost/learn_flask?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session相关
    SESSION_KEY = os.urandom(24) # 这里方便起见就随便输入个字符串，可以随机生成保存
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = 'session'

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
