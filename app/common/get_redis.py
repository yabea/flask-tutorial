# coding:utf-8
"""
desc: 连接redis
"""
import redis
from app.config import Config


class RedisHandler(object):
    def __init__(self):
        self.__redis_host = Config.REDIS_HOST
        self.__redis_port = Config.REDIS_PORT

    def get_redis_instance(self):
        if not self.__redis_host and self.__redis_port:
            return None
        redis_pool = redis.ConnectionPool(host=self.__redis_host, port=self.__redis_port)
        return redis.Redis(connection_pool=redis_pool)
