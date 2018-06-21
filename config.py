# -*- coding:utf-8 -*-
# 配置
import redis


class Config(object):
    """配置参数"""
    DEBUG = True

    # 秘钥
    SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI+90o0O4CaJsFGjzRsYiya9SEgUDytXvzFsIaR'
    # 配置mysql数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_03'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 指定存储session数据的数据库类型为redis
    SESSION_TYPE = 'redis'
    # 指定session数据存储到的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session数据的签名、混淆
    SESSION_USE_SIGNER = True
    # 设置session有效期：这⾥指的是session的扩展操作session时设置的有效期
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # ⼀天