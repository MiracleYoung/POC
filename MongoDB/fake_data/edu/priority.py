#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/2/26 11:52 AM

__author__ = 'Miracle'


def get_priority(school_name):
    school_priority = {
        '南京市中华中学': 10,
        '南京市第二十七高级中学': 9,
        '南京市文枢中学': 8,
        '南京市第十八中学': 7,
        '南京市第四十三中学': 6,
        '南京秦淮外国语学校（民办）': 5
    }
    return school_priority[school_name]
