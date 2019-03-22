#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/2/26 11:07 AM

__author__ = 'Miracle'

import time

import pymongo
from faker import Faker

from MongoDB.fake_data import EduProvider
from MongoDB.fake_data import get_priority

conn = pymongo.MongoClient('mongodb://tapdata-server:27019')
db = conn['edu']
coll = db['students']

fake = Faker('zh_CN')
fake.seed(time.time())
fake.add_provider(EduProvider)

# 模拟10,000条学生数据
for i in range(10000):
    student = {
        'name': fake.name(),
        'school': fake.school(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'grade': fake.grade(),
        'create_time': fake.date_time_between(start_date="-180d", end_date="now", tzinfo=None),
        'prize': fake.prize(),
        'loc':fake.local_latlng(country_code="CN", coords_only=True)
    }
    coll_id = coll.insert_one(student).inserted_id
    obj = coll.find_one({'_id': coll_id})
    priority = get_priority(obj['school']['name'])
    grade = {
        'chinese': fake.fail_score() if i % (6 * priority) == 0 else fake.pass_score(),
        'math': fake.fail_score() if i % (5 * priority) == 0 else fake.pass_score(),
        'english': fake.fail_score() if i % (4 * priority) == 0 else fake.pass_score(),
        'physics': fake.fail_score() if i % (3 * priority) == 0 else fake.pass_score(),
        'chemitry': fake.fail_score() if i % (7 * priority) == 0 else fake.pass_score(),
        'history': fake.fail_score() if i % (2 * priority) == 0 else fake.pass_score(),
        'geography': fake.fail_score() if i % (8 * priority) == 0 else fake.pass_score(),
    }

    coll.update_one({'_id': coll_id}, {'$set': grade})


# 给某个学生增加历史成绩
# student = coll.find_one({})
# for i in range(10):
#     random.seed(time.time())
#     student.update({
#         'chinese': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'math': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'english': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'physics': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'chemitry': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'history': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#         'geography': fake.fail_score() if i % 3 == 0 else fake.pass_score(),
#     })
#     student.pop('_id')
#     new_obj = coll.insert_one(student).inserted_id

