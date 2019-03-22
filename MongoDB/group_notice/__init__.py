#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/9/17 上午5:57
# @Author  : MiracleYoung
# @File    : __init__.py.py

from flask import Flask
from mongoengine import connect

from MongoDB.group_notice import notice


def create_app():
    app = Flask(__name__)
    register_bp(app)
    create_db()
    return app


def register_bp(app):
    app.register_blueprint(notice, url_prefix='/notice')


def create_db():
    connect(db='test', alias='test')
