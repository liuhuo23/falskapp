#coding:utf-8

# __init__.py 一来表示这个文件夹是个包，而来作为工厂函数

from ntpath import join
import os
import sqlite3
from flask import Flask

def create_app(test_config=None):
    # 创建并初始化一个app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY ='dev',
        DATABASE = os.path.join(app.instance_path, 'flask.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "hello"

    from . import db
    db.init_app(app)
    return app
