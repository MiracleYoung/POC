#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/17/18

__author__ = 'MiracleYoung'

from flask import Blueprint, Flask, request, jsonify

test = Blueprint('test', __name__)


@test.route('/test', methods=['GET', ])
def t():
    print(request.url_rule)
    p = request.data.get('sid')
    return jsonify({'code': 200})


app = Flask(__name__)
app.register_blueprint(test, url_prefix='/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
