#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/2/26 10:40 AM

__author__ = 'Miracle'

import random
import time

from faker.providers import BaseProvider


class EduProvider(BaseProvider):
    def school(self):
        school_list = [
            {
                'name': '南京市中华中学',
                'level': '高中',
                'zip_code': 210006,
                'address': '南京市中华路369号',
                'phone': '86626026'
            },
            {
                'name': '南京市第二十七高级中学',
                'level': '高中',
                'zip_code': 210001,
                'address': '南京市平江府路166号',
                'phone': '86623355'
            },
            {
                'name': '南京市文枢中学',
                'level': '高中',
                'zip_code': 210004,
                'address': '南京市秦淮区仙鹤街88号、南京市秦淮区钓鱼台19号',
                'phone': '86623014'
            },
            {
                'name': '南京市第十八中学',
                'level': '初中',
                'zip_code': 210022,
                'address': '南京市宏光路双桥新村1号',
                'phone': '68905885'
            },
            {
                'name': '南京市第四十三中学',
                'level': '初中',
                'zip_code': 210006,
                'address': '秦淮区花露北岗21号',
                'phone': '52230054'
            },
            {
                'name': '南京秦淮外国语学校（民办）',
                'level': '初中',
                'zip_code': 210006,
                'address': '南京市秦淮区剪子巷132号',
                'phone': '52416807'
            },
        ]
        return random.choice(school_list)

    def pass_score(self):
        return random.randint(60, 100)

    def fail_score(self):
        return random.randint(0, 60)

    def grade(self):
        g = ['六年级', '初一', '初二', '初三', '高一', '高二', '高三']
        return random.choice(g)

    def prize(self):
        p = ['全国青少年信息学奥林匹克竞赛', '新概念作文大赛', '全国中小学生创新作文大赛', '全国中学生英语能力竞赛',
             '中国青少年机器人竞赛', '青少年艺术大赛']
        return random.sample(p, random.randint(0, 5))

