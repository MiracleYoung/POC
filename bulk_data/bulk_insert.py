#!/usr/bin/env python
# encoding: utf-8
# @Time    : 12/6/18

__author__ = 'MiracleYoung'

import datetime
from decimal import Decimal

import pymongo

MONGO_HOST = '192.168.56.3'
MONGO_PORT = 27017

client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT, maxPoolSize=100)
db = client['mydb']

data = {
    'job': 'Water quality scientist', 'company': 'GB51UBHB8644630682056 GB51UBHB8644630682056', 'ssn': '709-11-3334',
    'residence': 'GB51UBHB8644630682056\nGB51UBHB8644630682056, GB51UBHB8644630682056 GB51UBHB8644630682056',
    'current_location': (26.3211165, 39.854754), 'blood_group': 'B+',
    'website': ['https://www.GB51UBHB8644630682056/', 'http://GB51UBHB8644630682056/', 'http://GB51UBHB8644630682056/'],
    'username': 'cgb51ubhb8644630682056', 'name': 'GB51UBHB8644630682056 GB51UBHB8644630682056', 'sex': 'F',
    'address': 'GB51UBHB8644630682056\nGB51UBHB8644630682056, GB51UBHB8644630682056 GB51UBHB8644630682056',
    'mail': 'gb51ubhb8644630682056gb51ubhb8644630682056@hotmail.com', 'birthdate': datetime.datetime.now(),
    'text': "'Grow while such bag guy. Nation offer power month deal. South single make.\nFull member until assume lay. Clearly central address. Believe road chair pull much certain here.\nNumber performance answer really remember talk year. You maintain way pick crime. Traditional significant economic what experience ground.\nSo born write son develop time car. Picture guess yet nor cause radio.\nBest course star financial. Condition thought protect trip.\nCan race sea their that light police. Talk above camera every page fact. Above join already down think.\nRelationship again after mission away case. Follow wish you indicate throughout.\nReady manager actually collection word. Interesting church car full our.\nTwo process person hair choose. Work space a phone address dog commercial ever.\nTonight day turn little laugh rate politics recent. Nature enough consider lose hand recognize push energy.'",

}


def bulk_insert(count):
    for i in range(1, count + 1):
        data.update({'_id': i, 'role_id': i})
        db['user'].insert(data)


if __name__ == '__main__':
    bulk_insert(100)
