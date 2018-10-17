#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/17/18

__author__ = 'MiracleYoung'

from group_notice import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
