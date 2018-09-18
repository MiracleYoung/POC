#!/usr/bin/env python
# encoding: utf-8
# @Time    : 9/18/18

__author__ = 'MiracleYoung'

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from threading import Thread, Event, RLock
import random
import datetime


class Client(Thread):
    def __init__(self, count, is_new):
        super(Client, self).__init__()
        self._is_new = is_new
        self._count = count
        self._event = Event()
        self._rlock = RLock()
        self._pre_url = 'http://localhost:5000'
        self._noticeold_url = f'{self._pre_url}/notice/old'
        self._noticenew_url = f'{self._pre_url}/notice/new'
        self._url = self._noticenew_url if self._is_new else self._noticeold_url
        self._session = requests.Session()
        self._retry = Retry(connect=3, backoff_factor=10)
        self._adapter = HTTPAdapter(max_retries=self._retry)

        self._session.mount('http://', self._adapter)

    def run(self):
        for _ in range(self._count):
            payload = {
                'sid': random.randint(1, 21),
                'gid': random.randint(1, 51),
                'cid': random.randint(1, 21),
                'nid': 1,
            }
            self._session.request(method='PUT', url=self._url, json=payload)


if __name__ == '__main__':
    clients = [Client(10, True) for _ in range(200)]
    st = datetime.datetime.now()
    for c in clients:
        c.start()

    for c in clients:
        c.join()

    print(f'cost time: {(datetime.datetime.now() - st).seconds} seconds.')
