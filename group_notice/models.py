#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/9/17 上午5:58
# @Author  : MiracleYoung
# @File    : models.py

import random
from datetime import datetime

from mongoengine import *


class User(DynamicEmbeddedDocument):
    _id = SequenceField(primary_key=True)
    uname = StringField()

    meta = {
        'collection': 'User',
        'db_alias': 'test'
    }


class Class(DynamicEmbeddedDocument):
    _id = SequenceField(primary_key=True)
    user = EmbeddedDocumentListField(User)

    meta = {
        'collection': 'Class',
        'db_alias': 'test'
    }


class Group(Document):
    _id = SequenceField(primary_key=True)
    cls = EmbeddedDocumentListField(Class)

    meta = {
        'collection': 'Group',
        'db_alias': 'test'
    }


class GroupNotcieOld(Document):
    TYPE = (
        (1, '全站通知'),
        (2, '系统通知'),
        (3, '学校通知'),
        (4, '学院通知'),
    )

    _id = SequenceField()
    title = StringField()
    content = StringField()
    ctime = DateTimeField(default=datetime.utcnow())
    author = StringField()
    type = IntField(choices=TYPE)
    unrecieved = DictField()
    hasrecieved = DictField()

    meta = {
        'collection': 'GroupNoticeOld',
        'db_alias': 'test',
    }


class Notice(Document):
    TYPE = (
        (1, '全站通知'),
        (2, '系统通知'),
        (3, '学校通知'),
        (4, '学院通知'),
    )
    _id = SequenceField()
    title = StringField()
    content = StringField()
    ctime = DateTimeField(default=datetime.utcnow())
    author = StringField()
    type = IntField(choices=TYPE)

    meta = {
        'collection': 'Notice',
        'db_alias': 'test'
    }


class GroupNotcieNew(Document):
    _id = SequenceField()
    notice_id = ReferenceField(Notice)
    school_id = IntField()
    group_id = IntField()
    class_id = IntField()
    unrecieved = DictField()
    hasrecieved = DictField()

    meta = {
        'collection': 'GroupNoticeNew',
        'db_alias': 'test',
    }


if __name__ == '__main__':
    u1 = User(uname='a')
    u1.save()
    u2 = User(uname='b')
    u2.save()
    c1 = Class(user=[u1, ])
    c1.save()
    c2 = Class(user=[u1, u2])
    c2.save()
    # g1 = Group(cls=[c1, c2], gid=1)
    # g1.save()

    g2 = Group(cls=[c1, c2])
    g2.save()

    u1 = User(uname='a')
    u2 = User(uname='b')
    c1 = Class(user=[u1, ])
    c2 = Class(user=[u1, u2])
    g2 = Group(cls=[c1, c2])
    g2.save()

    lst50 = list(range(1, 51))
    unrecieved = {}
    hasrecieved = {}
    for sid in range(1, 20):
        unrecieved[str(sid)] = {}
        hasrecieved[str(sid)] = {}
        for gid in range(1, 50):
            unrecieved[str(sid)][str(gid)] = {}
            hasrecieved[str(sid)][str(gid)] = {}
            for cid in range(1, 20):
                unrecieved[str(sid)][str(gid)][str(cid)] = lst50
                hasrecieved[str(sid)][str(gid)][str(cid)] = []
                lst50 = list(map(lambda x: x + 50, lst50))

    '''
    unrecieved: [
        '2': { # group_id
            '3': [ # class_id
                1, 2, 3, ... # uid
            ]
        }
    ]
    '''

    gn = GroupNotcieOld(title='全站', author='Miracle', type=1, unrecieved=unrecieved, hasrecieved=hasrecieved,
                        content='全站通知全站通知全站通知全站通知全站通知全站通知全站通知全站通知')
    gn.save()
