# -*- coding: utf-8 -*-
__author__ = 'Wang Xueyang'
__email__ = 'wxy_snowy@163.com'

from datetime import datetime
from multiprocessing import Pool
from lock_example.seckilling import seckilling, init_redis


def run_without_lock(name):
    while True:
        if datetime.now().second % 5 == 0:
            seckilling()
            return


if __name__ == '__main__':
    init_redis()
    p = Pool(16)
    for i in range(16):
        p.apply_async(run_without_lock, args=(i,))
    print('now 16 processes are going to get lock!')
    p.close()
    p.join()
    print('All subprocesses done.')
