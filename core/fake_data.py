#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/22 4:13 PM

__author__ = 'Miracle'

import time
import random


def random_datetime(start=(1976, 1, 1, 0, 0, 0, 0, 0, 0), end=(2050, 12, 31, 23, 59, 59, 0, 0, 0),
                    fmt="%Y-%m-%d %H:%M:%S"):
    '''
    随机生成时间
    :param start:
    :param end:
    :return:
    '''
    start = time.mktime(start)  # 生成开始时间戳
    end = time.mktime(end)  # 生成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    dt_tuple = time.localtime(t)  # 将时间戳生成时间元组
    dt = time.strftime(fmt, dt_tuple)  # 将时间元组转成格式化字符串（1976-05-21）
    return dt
