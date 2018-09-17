#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/17/18

__author__ = 'MiracleYoung'

from flask import Flask, Blueprint

notice = Blueprint('notice', __name__, url_prefix='/notice')