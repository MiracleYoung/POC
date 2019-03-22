#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/22 2:48 PM

__author__ = 'Miracle'


def make_dict_factory(cursor):
    '''
    将oracle数据返回dict
    '''
    columnNames = [d[0] for d in cursor.description]

    def createRow(*args):
        return dict(zip(columnNames, args))

    return createRow


def make_namedtuple_factory(cursor):
    '''
    将oracle数据返回tuple
    '''
    columnNames = [d[0].lower() for d in cursor.description]
    import collections
    Row = collections.namedtuple('Row', columnNames)
    return Row

