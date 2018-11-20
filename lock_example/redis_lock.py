import os
from datetime import datetime
from multiprocessing import Pool
from redlock import Redlock
from seckilling import seckilling, init_redis

rlock = Redlock([{"host": "10.40.110.90", "port": 6379, "db": 1}])


def run_with_redis_lock(name):
    while True:
        lock = rlock.lock("pants", 60000)
        # 暂停下来在redis里能找到pants这个key
        pid = os.getpid()
        print(pid, 'pants', datetime.now())
        seckilling()
        rlock.unlock(lock)
        return


def run_with_redis_lock2(name):
    while True:
        lock = rlock.lock("stress", 60000)
        pid = os.getpid()
        print(pid, "stress", datetime.now())
        seckilling()
        rlock.unlock(lock)
        return


if __name__ == '__main__':
    init_redis()
    p = Pool(16)
    run_with_redis_lock(1)
    for i in range(16):
        p.apply_async(run_with_redis_lock, args=(i,))
        p.apply_async(run_with_redis_lock2, args=(i,))
    print('now 16 processes are going to get lock!')
    p.close()
    p.join()
    print('All subprocesses done.')
