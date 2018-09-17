#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/17/18

__author__ = 'MiracleYoung'

import random

from mongoengine import *
from flask import request, jsonify

from group_notice.models import GroupNotcieOld, GroupNotcieNew, Notice
from group_notice.url import notice


@notice.route('/old', methods=('PUT'))
def read_notice_old():
    sid = request.data.get('sid', 0)
    gid = request.data.get('gid', 0)
    cid = request.data.get('cid', 0)
    uid = request.data.get('uid', 0)
    nid = request.data.get('nid', 0)
    gn = GroupNotcieOld.objects(_id=nid).first()
    uid = gn.unrecieved[str(sid)][str(gid)][str(cid)].remove(uid)
    gn.hasrecieved[str(sid)][str(gid)][str(cid)].append(uid)
    return jsonify({'code': 200, 'msg': 'success', 'error': []})


connect(db='test', alias='test')
gn = GroupNotcieOld.objects().first()
sid = random.randint(1, 21)
gid = random.randint(1, 51)
cid = random.randint(1, 21)

uid = gn.unrecieved[str(sid)][str(gid)][str(cid)].pop()
gn.hasrecieved[str(sid)][str(gid)][str(cid)].append(uid)
