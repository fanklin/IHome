# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

class Config(object):
    """配置参数"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_03'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

app = Flask(__name__)

@app.route('/')
def hello_world():
    redis_store.set('xx', 'yy')
    return 'Hello World!'

# 加载配置参数
app.config.from_getobject(Config)
# 创建链接到数据库的对象
db = SQLAlchemy(app)
# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

if __name__ == '__main__':
    app.run()
