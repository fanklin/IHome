# -*- coding:utf-8 -*-
# 项目立项
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect



class Config(object):
    """配置参数"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_03'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

app = Flask(__name__)

# 加载配置参数
app.config.from_object(Config)

# 创建链接到数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

#开启csrf保护
CSRFProtect(app)

# 创建本地脚本管理器对象
manger = Manager(app)

# 让迁移时候，app与db建立关联
Migrate(app, db)

# 将数据库迁移的脚本、命令添加到脚本管理器对象
manger.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    redis_store.set('xx', 'yy')
    return 'Hello World!'

if __name__ == '__main__':
    manger.run()
