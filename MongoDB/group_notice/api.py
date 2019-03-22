#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/17/18

__author__ = 'MiracleYoung'

import random

from mongoengine import *
from flask import request, jsonify, Blueprint

from MongoDB.group_notice.models import GroupNotcieOld, db

notice = Blueprint('notice', __name__, url_prefix='/notice')


@notice.route('/old', methods=['PUT', ])
def read_notice_old():
    sid = request.json.get('sid', 0)
    gid = request.json.get('gid', 0)
    cid = request.json.get('cid', 0)
    nid = request.json.get('nid', 0)
    uid = ((sid - 1) * 50 * 20 * 50) + ((gid - 1) * 20 * 50) + ((cid - 1) * 50) + random.randint(0, 50)
    db['GroupNoticeOld'].update_one(
        {'_id': nid},
        {'$pull': {f'unrecieved.{sid}.{gid}.{cid}': uid}, '$push': {f'hasrecieved.{sid}.{gid}.{cid}': uid}}
    )
    return jsonify({'code': 200, 'msg': 'success', 'error': []})


@notice.route('/new', methods=['PUT', ])
def read_notice_new():
    sid = request.json.get('sid', 0)
    gid = request.json.get('gid', 0)
    cid = request.json.get('cid', 0)
    nid = request.json.get('nid', 0)
    uid = ((sid - 1) * 50 * 20 * 50) + ((gid - 1) * 20 * 50) + ((cid - 1) * 50) + random.randint(0, 50)
    db['GroupNoticeNew'].update_one(
        {'notice_id': nid, 'school_id': sid, 'group_id': gid, 'class_id': cid},
        {'$pull': {f'unrecieved': uid}, '$push': {f'hasrecieved': uid}}
    )
    return jsonify({'code': 200, 'msg': 'success', 'error': []})


if __name__ == '__main__':
    connect(db='test', alias='test')
    gn = GroupNotcieOld.objects().first()
    sid = random.randint(1, 21)
    gid = random.randint(1, 51)
    cid = random.randint(1, 21)

    uid = gn.unrecieved[str(sid)][str(gid)][str(cid)].pop()
    gn.hasrecieved[str(sid)][str(gid)][str(cid)].append(uid)
