#!/usr/bin/env python
# encoding: utf-8
# @Time    : 12/7/18

__author__ = 'MiracleYoung'

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pymongo
from flask import Flask, jsonify, render_template, request, session, make_response, redirect, url_for

app = Flask(__name__)
# base64.b64encode(os.urandom(16)).decode()
app.secret_key = 'zHEaXuLG16okosm7vy4Caw=='

MONGO_HOST = '192.168.56.3'
MONGO_PORT = 27017

client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT, maxPoolSize=100)
db = client['mydb']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        res = make_response(redirect(url_for('index')))
        res.set_cookie('username', request.form['username'])
        return res


@app.route('/index')
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
    session['username'] = []
