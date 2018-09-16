#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/9/17 上午5:58
# @Author  : MiracleYoung
# @File    : models.py

from mongoengine import *
from datetime import datetime



class User(Document):
    uname = StringField()
    uid = IntField()



class GroupNotcie(Document):
    TYPE = (
        (1, '全站通知'),
        (2, '系统通知'),
        (3, '学校通知'),
        (4, '学院通知'),
    )

    title = StringField()
    content = StringField()
    ctime = DateTimeField(default=datetime.utcnow())
    author = StringField()
    type = IntField(choices=TYPE)
    group = EmbeddedDocumentListField




