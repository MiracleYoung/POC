#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/3/25 1:59 PM

__author__ = 'Miracle'

import tushare as ts

df = ts.get_hist_data('000651', ktype='5') #获取5分钟k线数据
df.to_csv('./data/格力电器_000651_20190322.csv')

df = ts.get_hist_data('601318', ktype='5') #获取5分钟k线数据
df.to_csv('./data/中国平安_601318_20190322.csv')