#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/9/17 上午5:57
# @Author  : MiracleYoung
# @File    : __init__.py.py

from flask import Flask

from . import url


def create_app():
    app = Flask(__name__)
    app.register_blueprint(url.notice)
    return app

