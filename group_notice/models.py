#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/9/17 上午5:58
# @Author  : MiracleYoung
# @File    : models.py


from datetime import datetime

from mongoengine import *
from pymongo import MongoClient

_client = MongoClient(host='127.0.0.1', port=27017, maxPoolSize=100)
db = _client['test']


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


def gen_notice_old():
    '''
    unrecieved: [
        '2': { # group_id
            '3': [ # class_id
                1, 2, 3, ... # uid
            ]
        }
    ]
    '''
    db['GroupNoticeOld'].drop()
    db['mongoengine.counters'].remove({'_id': 'GroupNoticeOld._id'})
    lst50 = list(range(1, 51))
    unrecieved = {}
    hasrecieved = {}
    for sid in range(1, 21):
        unrecieved[str(sid)] = {}
        hasrecieved[str(sid)] = {}
        for gid in range(1, 51):
            unrecieved[str(sid)][str(gid)] = {}
            hasrecieved[str(sid)][str(gid)] = {}
            for cid in range(1, 21):
                unrecieved[str(sid)][str(gid)][str(cid)] = lst50
                hasrecieved[str(sid)][str(gid)][str(cid)] = []
                lst50 = list(map(lambda x: x + 50, lst50))
    gn = GroupNotcieOld(title='全站', author='Miracle', type=1, unrecieved=unrecieved, hasrecieved=hasrecieved,
                        content='全站通知全站通知全站通知全站通知全站通知全站通知全站通知全站通知')
    gn.save()


def gen_notice_new():
    db['GroupNoticeNew'].drop()
    db['Notice'].drop()
    db['mongoengine.counters'].remove({'_id': 'Notice._id'})

    notice = Notice(title='全站', author='Miracle', type=1,
                    content='全站通知全站通知全站通知全站通知全站通知全站通知全站通知全站通知')
    notice.save()
    unrecieved = list(range(1, 51))
    hasrecieved = []
    for sid in range(1, 21):
        for gid in range(1, 51):
            for cid in range(1, 21):
                db['GroupNoticeNew'].insert({
                    'notice_id': 1, 'school_id': sid, 'group_id': gid, 'class_id': cid,
                    'unrecieved': unrecieved, 'hasrecieved': hasrecieved,
                })
                unrecieved = list(map(lambda x: x + 50, unrecieved))


if __name__ == '__main__':
    pass
