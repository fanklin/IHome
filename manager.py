# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'


app.config.from_object(Config)

db = app()
if __name__ == '__main__':
    app.run()
